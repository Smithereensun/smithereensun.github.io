{

  "title": "SpringBoot 整合Easy Poi 下载Excel(标题带批注)、导出Excel(带图片)、导入Excel(校验参数，批注导出)，附案例源码",
  "date": "2021-09-25",
  "description": "导读 日常开发过程中，经常遇到Excel导入、导出等功能，其中导入逻辑相对麻烦些，还涉及到参数的校验，然后将错误信息批注导出。之前写过EasyExcel导入(参数校验，带批注)(**点我直达1**、**点我直达2**)、导出等功能。今天遇到一个需求是，导入、导出还需要带上图片，EasyExcel目前",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/easypoi.html"

}

# 导读

　　日常开发过程中，经常遇到Excel导入、导出等功能，其中导入逻辑相对麻烦些，还涉及到参数的校验，然后将错误信息批注导出。之前写过EasyExcel导入(参数校验，带批注)(**[点我直达1](https://www.cnblogs.com/chenyanbin/p/13957503.html)**、**[点我直达2](https://www.cnblogs.com/chenyanbin/p/14366596.html)**)、导出等功能。今天遇到一个需求是，导入、导出还需要带上图片，EasyExcel目前还不支持Excel中带图片的。Easy Poi支持带图片导入、导出，批注等功能，好啦~废话不多说，下面开始叭~**EasyPoi官网**，[点我直达](http://easypoi.mydoc.io/#) [点我直达(新地址)](http://doc.wupaas.com/docs/easypoi/easypoi-1c2cp5rf3hnqv)

# 项目源码

## 添加依赖

```text
            <!-- easy poi -->
            <dependency>
                <groupId>cn.afterturn</groupId>
                <artifactId>easypoi-spring-boot-starter</artifactId>
                <version>4.1.0</version>
            </dependency>
            <!-- JSR 303 规范验证包 -->
            <dependency>
                <groupId>org.hibernate</groupId>
                <artifactId>hibernate-validator</artifactId>
                <version>5.2.4.Final</version>
            </dependency>
```

```text
            <!-- 阿里云OSS -->
            <dependency>
                <groupId>com.aliyun.oss</groupId>
                <artifactId>aliyun-sdk-oss</artifactId>
                <version>3.10.2</version>
            </dependency>
```

### 友情提示

-

### **Easy Poi依赖版本大于4.1.0时，导出图片显示异常！！！！！这个坑了我好久 呜呜呜呜**

- **Easy Poi导入时，支持hibernate的注解，校验参数**

## 实体类

导入实体类

```text
import cn.afterturn.easypoi.excel.annotation.Excel;
import lombok.Data;

import javax.validation.constraints.NotNull;
import javax.validation.constraints.Pattern;
import java.io.Serializable;
import java.util.Date;

/**
 * 人员信息Excel导出实体类
 *
 * @Author：chenyanbin
 */
@Data
public class PersonImportExcelDomain implements Serializable {
    /**
     * 姓名
     */
    @Excel(name = "姓名", height = 20, width = 30)
    @EasyPoiCellAnnotation(cellIndex = 0)
    @NotNull(message = "姓名不能为空")
    private String userNick;

    /**
     * 性别
     * replace：替换枚举值，1->男；2->女
     * suffix：为每个值后，添加后缀
     */
    @Excel(name = "性别", replace = {"1_男", "2_女"}, suffix = "生")
    @EasyPoiCellAnnotation(cellIndex = 1)
    @Pattern(regexp = "男|女", message = "性别不能为空 1->男|2->女")
    private String sex;

    /**
     * 出生日期
     */
    @Excel(name = "出生日期", databaseFormat = "yyyyMMddHHmmss", importFormat = "yyyy-MM-dd HH:mm:ss", format = "yyyy-MM-dd HH:mm:ss", width = 25)
    @EasyPoiCellAnnotation(cellIndex = 2)
    private Date birthday;

    /**
     * 头像
     */
    @Excel(name = "头像", type = 2, savePath = "/Users/chenyanbin/upload")
    @EasyPoiCellAnnotation(cellIndex = 3)
    @NotNull(message = "头像不能为空")
    private String pic;

    /**
     * 临时头像字节
     */
    private String tempPicUrl;
}
```

**注意**：导入时，Easy Poi会将Excel和图片，下载到宿主机中，此时该实体类中的pic为当前宿主机图片的绝对路径，需要将图片上传至阿里云Oss上，并将图片url赋值到tempPicUrl

导出实体类

```text
package com.yida.excel.domain;

import cn.afterturn.easypoi.excel.annotation.Excel;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * 人员信息Excel导出实体类
 * @Author：chenyanbin
 */
@Data
public class PersonExportExcelDomain implements Serializable {
    /**
     * 姓名
     */
    @Excel(name = "姓名", height = 20, width = 30)
    private String userNick;

    /**
     * 性别
     * replace：替换枚举值，1->男；2->女
     * suffix：为每个值后，添加后缀
     */
    @Excel(name = "性别", replace = {"男_1", "女_2"}, suffix = "生")
    private int sex;

    /**
     * 出生日期
     */
    @Excel(name = "出生日期", databaseFormat = "yyyyMMddHHmmss", importFormat = "yyyy-MM-dd HH:mm:ss", format = "yyyy-MM-dd HH:mm:ss",width = 25)
    private Date birthday;

    /**
     * 头像
     */
    @Excel(name = "头像", type = 2, width = 10, height = 10, imageType = 2)
    private byte[] pic;

    /**
     * 临时头像地址
     */
    private String tempPicUrl;
}
```

**注意**：导出图片时，需要将网络图片转换成字节数组！做法：将tempPicUrl调用http工具类，转换成字节数组，赋值到pic

导入校验参数批注实体类

```text
import lombok.Data;

/**
 * Excel 错误批注信息vo
 * @Author：chenyanbin
 */
@Data
public class ExcelErrorInfoVo {
    /**
     * 行索引，从0开始
     */
    private int rowIndex;
    /**
     * 列索引，从0开始
     */
    private int cellIndex;

    /**
     * 错误原因
     */
    private String reasonText;
}
```

## 工具类

Http工具类

```text
import lombok.extern.slf4j.Slf4j;

import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

/**
 * Http工具类
 *
 * @Author：chenyanbin
 */
@Slf4j
public class HttpUtil {

    /**
     * 获取网络图片转成字节流
     *
     * @param strUrl 完整图片地址
     * @return 图片资源数组
     */
    public static byte[] getNetImgByUrl(String strUrl) {
        try {
            URL url = new URL(strUrl);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setConnectTimeout(2 * 1000);
            // 通过输入流获取图片数据
            InputStream inStream = conn.getInputStream();
            // 得到图片的二进制数据
            byte[] btImg = readInputStream(inStream);
            return btImg;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    /**
     * 从输入流中获取字节流数据
     *
     * @param inStream 输入流
     * @return 图片流
     */
    private static byte[] readInputStream(InputStream inStream) throws Exception {
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        // 设置每次读取缓存区大小
        byte[] buffer = new byte[1024 * 10];
        int len = 0;
        while ((len = inStream.read(buffer)) != -1) {
            outStream.write(buffer, 0, len);
        }
        inStream.close();
        return outStream.toByteArray();
    }
}
```

添加批注工具类

```text
import org.apache.commons.lang3.StringUtils;
import org.apache.poi.hssf.usermodel.HSSFClientAnchor;
import org.apache.poi.hssf.usermodel.HSSFRichTextString;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.*;
import org.apache.poi.xssf.usermodel.XSSFClientAnchor;
import org.apache.poi.xssf.usermodel.XSSFRichTextString;

import javax.validation.ConstraintViolation;
import javax.validation.Validation;
import javax.validation.Validator;
import java.lang.reflect.Field;
import java.util.*;

/**
 * Easy Poi Excel工具类
 *
 * @Author：chenyanbin
 */
public class EasyPoiExcelUtil {
    private static Validator validator = Validation.buildDefaultValidatorFactory().getValidator();

    /**
     * 添加批注
     *
     * @param workbook       工作簿
     * @param titleRowsIndex 标题的行索引，从0计数
     * @param commentStr     批注格式： 0#姓名不能为空__1#学生性别 1:男 2:女__2#出生日期：yyyy-MM-dd__3#图片不能为空
     */
    public static void buildComment(Workbook workbook, int titleRowsIndex, String commentStr) {
        Sheet sheet = workbook.getSheetAt(0);
        //创建一个图画工具
        Drawing<?> drawing = sheet.createDrawingPatriarch();
        Row row = sheet.getRow(titleRowsIndex);
        if (StringUtils.isNotBlank(commentStr)) {
            //解析批注，并传换成map
            Map<Integer, String> commentMap = getCommentMap(commentStr);
            for (Map.Entry<Integer, String> entry : commentMap.entrySet()) {
                Cell cell = row.getCell(entry.getKey());
                //创建批注
                Comment comment = drawing.createCellComment(newClientAnchor(workbook));
                //输入批注信息
                comment.setString(newRichTextString(workbook, entry.getValue()));
                //将批注添加到单元格对象中
                cell.setCellComment(comment);

//                //设置单元格背景颜色
//                CellStyle cellStyle = workbook.createCellStyle();
//                //设置颜色
//                cellStyle.setFillForegroundColor(IndexedColors.BLACK1.getIndex());
//                //设置实心填充
//                cellStyle.setFillPattern(FillPatternType.SOLID_FOREGROUND);
//                cell.setCellStyle(cellStyle);
            }
        }
    }

    /**
     * 添加批注
     *
     * @param workbook      工作簿
     * @param errorInfoList 批注错误集合
     */
    public static void buildComment(Workbook workbook, List<ExcelErrorInfoVo> errorInfoList) {
        Sheet sheet = workbook.getSheetAt(0);
        //创建一个图画工具
        Drawing<?> drawing = sheet.createDrawingPatriarch();
        for (ExcelErrorInfoVo vo : errorInfoList) {
            Row row = sheet.getRow(vo.getRowIndex());
            if (StringUtils.isNotBlank(vo.getReasonText())) {
                Cell cell = row.getCell(vo.getCellIndex());
                //创建批注
                Comment comment = drawing.createCellComment(newClientAnchor(workbook));
                //输入批注信息
                comment.setString(newRichTextString(workbook, vo.getReasonText()));
                //将批注添加到单元格对象中
                cell.setCellComment(comment);

//                //设置单元格背景颜色
//                CellStyle cellStyle = workbook.createCellStyle();
//                //设置颜色
//                cellStyle.setFillForegroundColor(IndexedColors.BLACK1.getIndex());
//                //设置实心填充
//                cellStyle.setFillPattern(FillPatternType.SOLID_FOREGROUND);
//                cell.setCellStyle(cellStyle);
            }
        }
    }

    /**
     * 校验Excel数据
     *
     * @param obj      Excel中当前行的数据对象
     * @param clz      Excel中当前行的数据对象的类
     * @param rowIndex 该条记录对应的行索引
     * @return
     */
    public static <T> List<ExcelErrorInfoVo> checkExcelData(T obj, Class<?> clz, int rowIndex) {
        List<ExcelErrorInfoVo> errorInfoList = new ArrayList<>();
        Set<ConstraintViolation<T>> cvSet = validator.validate(obj);
        Field f = null;
        for (ConstraintViolation<T> cv : cvSet) {
            try {
                f = clz.getDeclaredField(cv.getPropertyPath().toString());
                f.setAccessible(true);
                EasyPoiCellAnnotation annotation = f.getAnnotation(EasyPoiCellAnnotation.class);
                if (annotation == null) {
                    continue;
                }
                int cellIndex = annotation.cellIndex();
                ExcelErrorInfoVo vo = new ExcelErrorInfoVo();
                vo.setRowIndex(rowIndex);
                vo.setCellIndex(cellIndex);
                vo.setReasonText(cv.getMessage());
                errorInfoList.add(vo);
            } catch (NoSuchFieldException e) {
            } finally {
                if (f != null) {
                    f.setAccessible(false);
                }
            }
        }
        return errorInfoList;
    }

    /**
     * 批注信息，默认解析：批注#列索引，比如用户名不允许重复#0。可覆盖此方法，解析自定义的批注格式
     *
     * @param commentStr 当前行的所有批注信息
     * @return key：列索引，value：对应列的所有批注信息
     */
    protected static Map<Integer, String> getCommentMap(String commentStr) {
        //每行的所有单元格的批注都在commentStr里，并用”__”分隔
        String[] split = commentStr.split("__");
        Map<Integer, String> commentMap = new HashMap<>();
        for (String msg : split) {
            String[] cellMsg = msg.split("#");
            //如果当前列没有批注，会将该列的索引作为key存到map里；已有批注，以“,“分隔继续拼接
            int cellIndex = Integer.parseInt(cellMsg[0]);
            if (commentMap.get(cellIndex) == null) {
                commentMap.put(cellIndex, cellMsg[1]);
            } else {
                commentMap.replace(cellIndex, commentMap.get(cellIndex) + "," + cellMsg[1]);
            }
        }
        return commentMap;
    }

    private static ClientAnchor newClientAnchor(Workbook workbook) {
        //xls
        if (workbook instanceof HSSFWorkbook) {
            return new HSSFClientAnchor(0, 0, 0, 0, (short) 3, 3, (short) 5, 6);
        }
        //xlsx
        else {
            return new XSSFClientAnchor(0, 0, 0, 0, (short) 3, 3, (short) 5, 6);
        }
    }

    private static RichTextString newRichTextString(Workbook workbook, String msg) {
        //xls
        if (workbook instanceof HSSFWorkbook) {
            return new HSSFRichTextString(msg);
        }
        //xlsx
        else {
            return new XSSFRichTextString(msg);
        }
    }
}
```

## 自定义注解

```text
import java.lang.annotation.*;

@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
public @interface EasyPoiCellAnnotation {
    /**
     * 字段索引位置，从0开始计数
     * @return
     */
    int cellIndex();
}
```

## 阿里云Oss文件上传

```text
import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

/**
 * 阿里云oss配置文件
 * @Author：chenyanbin
 */
@Data
@Configuration
@ConfigurationProperties(prefix = "aliyun.oss")
public class OssConfig {

    private String endpoint;

    private String accessKeyId;

    private String accessSecret;

    private String bucketName;
}
```

```text
import org.springframework.web.multipart.MultipartFile;

import java.io.File;

/**
 * 阿里云oss文件上传service
 * @Author：chenyanbin
 */
public interface OssFileService {
    /**
     * 上传文件
     * @param file
     * @return
     */
    String uploadFile(MultipartFile file);

    /**
     * 上传客户端本地文件
     * @param file
     * @return
     */
    String uploadClientFile(File file);
}
```

```text
import com.aliyun.oss.OSS;
import com.aliyun.oss.OSSClientBuilder;
import com.aliyun.oss.model.ObjectMetadata;
import com.aliyun.oss.model.PutObjectResult;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

/**
 * @Author：chenyanbin
 */
@Service
@Slf4j
public class OssFileServiceImpl implements OssFileService {
    @Autowired
    private OssConfig ossConfig;

    @Override
    public String uploadFile(MultipartFile file) {
        //获取相关配置
        String bucketName = ossConfig.getBucketName();
        String endpoint = ossConfig.getEndpoint();
        String accessKeyId = ossConfig.getAccessKeyId();
        String accessSecret = ossConfig.getAccessSecret();
        //创建OSS对象
        OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessSecret);
        //原始文件名称  xxx.jpg
        String originalFileName = file.getOriginalFilename();
        //JDK8 日期格式化
        LocalDateTime ldt = LocalDateTime.now();
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd");
        //文件路径
        String folder = dtf.format(ldt);
        //拼装路径，oss上存储的路径 2021/05/16/xxx.jpg
        String fileName = CommonUtil.generateUUID();
        //扩展名
        String extension = originalFileName.substring(originalFileName.lastIndexOf("."));
        String newFileName = "user/" + folder + "/" + fileName + extension;
        //推送到oss
        try {
            PutObjectResult putObjectResult = ossClient.putObject(bucketName, newFileName, file.getInputStream());
            //拼装返回路径
            if (putObjectResult != null) {
                String imgUrl = "https://" + bucketName + "." + endpoint + "/" + newFileName;
                return imgUrl;
            }
        } catch (IOException e) {
            log.error("oss文件上传失败：{}", e);
        } finally {
            //oss关闭
            ossClient.shutdown();
        }
        return null;
    }

    @Override
    public String uploadClientFile(File file) {
        try {
            //获取相关配置
            String bucketName = ossConfig.getBucketName();
            String endpoint = ossConfig.getEndpoint();
            String accessKeyId = ossConfig.getAccessKeyId();
            String accessSecret = ossConfig.getAccessSecret();
            //创建OSS对象
            OSS ossClient = new OSSClientBuilder().build(endpoint, accessKeyId, accessSecret);
            //以输入流的形式上传文件
            InputStream is = new FileInputStream(file);
            //文件名
            String fileName = file.getName();
            //文件大小
            Long fileSize = file.length();
            //创建上传Object的Metadata
            ObjectMetadata metadata = new ObjectMetadata();
            //上传的文件的长度
            metadata.setContentLength(is.available());
            //指定该Object被下载时的网页的缓存行为
            metadata.setCacheControl("no-cache");
            //指定该Object下设置Header
            metadata.setHeader("Pragma", "no-cache");
            //指定该Object被下载时的内容编码格式
            metadata.setContentEncoding("utf-8");
            //文件的MIME，定义文件的类型及网页编码，决定浏览器将以什么形式、什么编码读取文件。如果用户没有指定则根据Key或文件名的扩展名生成，
            //如果没有扩展名则填默认值application/octet-stream
            metadata.setContentType(getContentType(fileName));
            //指定该Object被下载时的名称（指示MINME用户代理如何显示附加的文件，打开或下载，及文件名称）
            metadata.setContentDisposition("filename/filesize=" + fileName + "/" + fileSize + "Byte.");
            //JDK8 日期格式化
            LocalDateTime ldt = LocalDateTime.now();
            DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd");
            //文件路径
            String folder = dtf.format(ldt);
            String newFileName = "user/" + folder + "/" + fileName;
            //上传文件   (上传文件流的形式)
            PutObjectResult putResult = ossClient.putObject(bucketName, newFileName, is, metadata);
            String imgUrl = "https://" + bucketName + "." + endpoint + "/" + newFileName;
            return imgUrl;
        } catch (Exception e) {
        }
        return null;
    }

    /**
     * 通过文件名判断并获取OSS服务文件上传时文件的contentType
     *
     * @param fileName 文件名
     * @return 文件的contentType
     */
    private String getContentType(String fileName) {
        //文件的后缀名
        String fileExtension = fileName.substring(fileName.lastIndexOf("."));
        if (".bmp".equalsIgnoreCase(fileExtension)) {
            return "image/bmp";
        }
        if (".gif".equalsIgnoreCase(fileExtension)) {
            return "image/gif";
        }
        if (".jpeg".equalsIgnoreCase(fileExtension) || ".jpg".equalsIgnoreCase(fileExtension) || ".png".equalsIgnoreCase(fileExtension)) {
            return "image/jpeg";
        }
        if (".html".equalsIgnoreCase(fileExtension)) {
            return "text/html";
        }
        if (".txt".equalsIgnoreCase(fileExtension)) {
            return "text/plain";
        }
        if (".vsd".equalsIgnoreCase(fileExtension)) {
            return "application/vnd.visio";
        }
        if (".ppt".equalsIgnoreCase(fileExtension) || "pptx".equalsIgnoreCase(fileExtension)) {
            return "application/vnd.ms-powerpoint";
        }
        if (".doc".equalsIgnoreCase(fileExtension) || "docx".equalsIgnoreCase(fileExtension)) {
            return "application/msword";
        }
        if (".xml".equalsIgnoreCase(fileExtension)) {
            return "text/xml";
        }
        //默认返回类型
        return "image/jpeg";
    }
}
```

```text
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.extern.slf4j.Slf4j;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.security.MessageDigest;
import java.util.Random;
import java.util.UUID;

/**
 * 公共工具类
 *
 * @Author：chenyanbin
 */
@Slf4j
public class CommonUtil {
    /**
     * 生成uuid
     *
     * @return
     */
    public static String generateUUID() {
        return UUID.randomUUID().toString().replaceAll("-", "").substring(0, 32);
    }

}
```

## 控制层

```text
import cn.afterturn.easypoi.excel.ExcelExportUtil;
import cn.afterturn.easypoi.excel.ExcelImportUtil;
import cn.afterturn.easypoi.excel.entity.ExportParams;
import cn.afterturn.easypoi.excel.entity.ImportParams;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.apache.commons.lang3.StringUtils;
import org.apache.poi.ss.usermodel.Workbook;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletResponse;
import java.io.File;
import java.io.IOException;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 * @Author：chenyanbin
 */
@RestController
@RequestMapping("/api/excel/v1")
@Api(tags = "Easy Poi API测试")
public class ExcelController {
    @Autowired
    OssFileService ossFileService;

    @ApiOperation("下单Excel模板")
    @GetMapping("downloadExcelTemplate")
    public void downloadExcelTemplate(HttpServletResponse response) {
        //1、数据库查询数据，此处模拟数据
        List<PersonExportExcelDomain> personExcelList = new ArrayList<>();
        String fileName = "学生信息表.xls";
        Workbook workbook = ExcelExportUtil.exportExcel(new ExportParams("xxx班学生信息", "学生信息"), PersonExportExcelDomain.class, personExcelList);
        //标题加批注
        EasyPoiExcelUtil.buildComment(workbook, 1, "0#姓名不能为空__1#学生性别 1:男 2:女__2#出生日期：yyyy-MM-dd__3#图片不能为空");
        ServletOutputStream outputStream = null;
        try {
            outputStream = response.getOutputStream();
            response.setCharacterEncoding("UTF-8");
            response.setContentType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"); //mime类型
            response.setHeader("Pragma", "No-cache");//设置不要缓存
            response.setHeader("Content-Disposition", "attachment;filename=" + URLEncoder.encode(fileName, "UTF-8"));
            workbook.write(outputStream);
            outputStream.flush();
        } catch (IOException e) {
            throw new RuntimeException(e);
        } finally {
            if (outputStream != null) {
                try {
                    outputStream.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    @ApiOperation("导出Excel数据")
    @GetMapping("exportExcelTemplate")
    public void exportExcelTemplate(HttpServletResponse response) {
        //1、数据库查询数据，此处模拟数据
        List<PersonExportExcelDomain> personExcelList = new ArrayList<>();
        //学生：张三
        PersonExportExcelDomain person_1 = new PersonExportExcelDomain();
        person_1.setUserNick("张三");
        person_1.setSex(1);
        person_1.setBirthday(new Date());
        person_1.setTempPicUrl("https://images.cnblogs.com/cnblogs_com/chenyanbin/1560326/o_qianxun.jpg");
        personExcelList.add(person_1);
        //学生：李四
        PersonExportExcelDomain person_2 = new PersonExportExcelDomain();
        person_2.setUserNick("李四");
        person_2.setSex(2);
        person_2.setBirthday(new Date());
        person_2.setTempPicUrl("https://pic.cnblogs.com/face/1988848/20200625143435.png");
        personExcelList.add(person_2);
        //学生：王五
        PersonExportExcelDomain person_3 = new PersonExportExcelDomain();
        person_3.setUserNick("王五");
        person_3.setSex(2);
        person_3.setBirthday(new Date());
        personExcelList.add(person_3);
        //处理导出Excel图片
        for (PersonExportExcelDomain domain : personExcelList) {
            if (StringUtils.isNotBlank(domain.getTempPicUrl())) {
                //将网络图片，转换成文件流
                domain.setPic(HttpUtil.getNetImgByUrl(domain.getTempPicUrl()));
            }
        }
        String fileName = "xxx公司人员信息表.xls";
        Workbook workbook = ExcelExportUtil.exportExcel(new ExportParams("xxx部门人员表", "部门"), PersonExportExcelDomain.class, personExcelList);
        //标题加批注
        EasyPoiExcelUtil.buildComment(workbook, 1, "0#姓名不能为空__1#性别 1:男 2:女__2#出生日期：yyyy-MM-dd__3#头像不能为空");
        ServletOutputStream outputStream = null;
        try {
            outputStream = response.getOutputStream();
            response.setCharacterEncoding("UTF-8");
            response.setContentType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
            response.setHeader("Pragma", "No-cache");
            response.setHeader("Content-Disposition", "attachment;filename=" + URLEncoder.encode(fileName, "UTF-8"));
            workbook.write(outputStream);
            outputStream.flush();
        } catch (IOException e) {
        } finally {
            if (outputStream != null) {
                try {
                    outputStream.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    /**
     * 导入Excel
     *
     * @param file
     * @param response
     */
    @PostMapping("importExcel")
    @ApiOperation("导入Excel")
    public void importExcel(
            @ApiParam(value = "文件上传", required = true) @RequestPart("file") MultipartFile file,
            HttpServletResponse response
    ) throws Exception {
        //1、导入参数配置
        ImportParams params = new ImportParams();
        params.setNeedSave(true);
        params.setTitleRows(1);
        params.setSaveUrl("/Users/chenyanbin/upload");
        //2、获取Excel数据(Excel中单元格中若存在图片，EasyPoi会将图片上传到本机)
        List<PersonImportExcelDomain> personList = ExcelImportUtil.importExcel(file.getInputStream(), PersonImportExcelDomain.class, params);
        //3、处理上传图片，转换至字节流
        List<ExcelErrorInfoVo> errorList = new ArrayList<>();
        for (int i = 0; i < personList.size(); i++) {
            //图片不为空
            if (StringUtils.isNotBlank(personList.get(i).getPic())) {
                String fileUrl = ossFileService.uploadClientFile(new File(personList.get(i).getPic()));
                personList.get(i).setTempPicUrl(fileUrl);
            }
            PersonImportExcelDomain domain = personList.get(i);
            //4、将校验失败的Excel添加至集合中
            errorList.addAll(EasyPoiExcelUtil.checkExcelData(domain, PersonImportExcelDomain.class, i + 2));
        }
        //5、Excel数据是否正确
        if (errorList.size() == 0) {
            //数据正确
            //TODO 导入数据库
            personList.stream().forEach(System.err::println);
        } else {
            String fileName = "学生信息表导入-校验错误.xls";
            //数据格式不正确，添加批注导出
            Workbook workbook = ExcelExportUtil.exportExcel(new ExportParams("xxx班学生信息", "学生信息"), PersonImportExcelDomain.class, personList);
            //标题加批注
            EasyPoiExcelUtil.buildComment(workbook, errorList);
            ServletOutputStream outputStream = null;
            try {
                outputStream = response.getOutputStream();
                response.setCharacterEncoding("UTF-8");
                response.setContentType("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"); //mime类型
                response.setHeader("Pragma", "No-cache");//设置不要缓存
                response.setHeader("Content-Disposition", "attachment;filename=" + URLEncoder.encode(fileName, "UTF-8"));
                workbook.write(outputStream);
                outputStream.flush();
            } catch (IOException e) {
                throw new RuntimeException(e);
            } finally {
                if (outputStream != null) {
                    try {
                        outputStream.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
}
```

## 演示

### 下载Excel模块

　　标题带批注

![](./images/images/img_001_eb26c85e66a2.gif)

### 带图片导出Excel

![](./images/images/img_002_e41f14a17a3b.gif)

### 导入Excel

　　参数校验，带批注导出

![](./images/images/img_003_d42bfc920e6f.gif)

# 尾声

　　如果贴的代码不全，请联系我微信~
