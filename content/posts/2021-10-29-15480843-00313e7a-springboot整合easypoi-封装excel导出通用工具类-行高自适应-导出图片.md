{

  "title": "SpringBoot整合EasyPoi 封装Excel导出通用工具类，行高自适应，导出图片",
  "date": "2021-10-29",
  "description": "导读 下午抽空封装一个通用导出Excel工具类。之前还写过一篇EasyPoi导入参数校验，批注导出，点我直达 添加依赖 注意依赖版本超过4.1.0导出图片时有问题哟** EasyPoi工具类 时间工具类 导出样式 导出工具类 根据url下载图片转字节数组 导出实体类vo dao查询sql语句 con",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/easypoiexcel.html"

}

# 导读

　　下午抽空封装一个通用导出Excel工具类。之前还写过一篇EasyPoi导入参数校验，批注导出，[点我直达](https://www.cnblogs.com/chenyanbin/p/easypoi.html)

# 添加依赖

```text
 <!-- easy poi -->
            <dependency>
                <groupId>cn.afterturn</groupId>
                <artifactId>easypoi-spring-boot-starter</artifactId>
                <version>4.1.0</version>
            </dependency>
```

**注意依赖版本超过4.1.0导出图片时有问题哟**

# EasyPoi工具类

## 时间工具类

```text
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.Date;

/**
 * 时间工具类
 *
 * @Author：chenyanbin
 */
public class TimeUtil {
    public static final String YYYY_MM_DD_HH_MM_SS = "yyyy-MM-dd HH:mm:ss";

    public static final String YYYY_MM_DD = "yyyy-MM-dd";

    public static final String YYMMDD = "yyMMdd";

    public static final String YYYYMMDD = "yyyyMMdd";

    /**
     * 格式化日期
     *
     * @param time 当前时间
     * @return
     */
    public static String format(Date time) {
        return format(time, YYYY_MM_DD_HH_MM_SS);
    }

    /**
     * 格式化日期
     *
     * @param time    当前时间
     * @param pattern 格式化规则
     * @return
     */
    public static String format(Date time, String pattern) {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern(pattern);
        ZoneId zoneId = ZoneId.systemDefault();
        return dtf.format(time.toInstant().atZone(zoneId));
    }

    /**
     * timestamp 转 字符串
     *
     * @param timestamp
     * @return
     */
    public static String dateToStr(long timestamp) {
        return dateToStr(timestamp, YYYY_MM_DD_HH_MM_SS);
    }

    /**
     * timestamp 转 字符串
     *
     * @param timestamp 时间戳
     * @param pattern   格式化规则
     * @return
     */
    public static String dateToStr(long timestamp, String pattern) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern(pattern);
        ZoneId zoneId = ZoneId.systemDefault();
        String timeStr = formatter.format(new Date(timestamp).toInstant().atZone(zoneId));
        return timeStr;
    }

    /**
     * 字符串 转 date
     *
     * @param time
     * @return
     */
    public static Date strToDate(String time) {
        return strToDate(time, YYYY_MM_DD_HH_MM_SS);
    }

    /**
     * 字符串 转 date
     *
     * @param time    当前时间
     * @param pattern 格式化规则
     * @return
     */
    public static Date strToDate(String time, String pattern) {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern(pattern);
        LocalDateTime localDateTime = LocalDateTime.parse(time, formatter);
        return Date.from(localDateTime.atZone(ZoneId.systemDefault()).toInstant());
    }

    /**
     * 当前时间格式化
     *
     * @return
     */
    public static String currentTimeFormat() {
        LocalDateTime nowDate = LocalDateTime.now();
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern(YYYY_MM_DD_HH_MM_SS);
        return dtf.format(nowDate);
    }

    /**
     * 当前时间格式化
     *
     * @param pattern 格式化规则
     * @return
     */
    public static String currentTimeFormat(String pattern) {
        LocalDateTime nowDate = LocalDateTime.now();
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern(pattern);
        return dtf.format(nowDate);
    }
}
```

## 导出样式

```text
import cn.afterturn.easypoi.excel.entity.params.ExcelExportEntity;
import cn.afterturn.easypoi.excel.entity.params.ExcelForEachParams;
import cn.afterturn.easypoi.excel.export.styler.IExcelExportStyler;
import org.apache.poi.ss.usermodel.*;

/**
 * Easy Poi 导出样式
 * @Author：chenyanbin
 */
public class EasyPoiExcelExportStylerUitl implements IExcelExportStyler {

    private static final short STRING_FORMAT = (short) BuiltinFormats.getBuiltinFormat("TEXT");
    private static final short FONT_SIZE_TEN = 10;
    private static final short FONT_SIZE_ELEVEN = 11;
    private static final short FONT_SIZE_TWELVE = 12;
    /**
     * 大标题样式
     */
    private CellStyle headerStyle;
    /**
     * 每列标题样式
     */
    private CellStyle titleStyle;
    /**
     * 数据行样式
     */
    private CellStyle styles;

    public EasyPoiExcelExportStylerUitl(Workbook workbook) {
        this.init(workbook);
    }

    /**
     * 初始化样式
     *
     * @param workbook
     */
    private void init(Workbook workbook) {
        this.headerStyle = initHeaderStyle(workbook);
        this.titleStyle = initTitleStyle(workbook);
        this.styles = initStyles(workbook);
    }

    /**
     * 大标题样式
     *
     * @param color
     * @return
     */
    @Override
    public CellStyle getHeaderStyle(short color) {
        return headerStyle;
    }

    /**
     * 每列标题样式
     *
     * @param color
     * @return
     */
    @Override
    public CellStyle getTitleStyle(short color) {
        return titleStyle;
    }

    /**
     * 数据行样式
     *
     * @param parity 可以用来表示奇偶行
     * @param entity 数据内容
     * @return 样式
     */
    @Override
    public CellStyle getStyles(boolean parity, ExcelExportEntity entity) {
        return styles;
    }

    /**
     * 获取样式方法
     *
     * @param dataRow 数据行
     * @param obj     对象
     * @param data    数据
     */
    @Override
    public CellStyle getStyles(Cell cell, int dataRow, ExcelExportEntity entity, Object obj, Object data) {
        return getStyles(true, entity);
    }

    /**
     * 模板使用的样式设置
     */
    @Override
    public CellStyle getTemplateStyles(boolean isSingle, ExcelForEachParams excelForEachParams) {
        return null;
    }

    /**
     * 初始化--大标题样式
     *
     * @param workbook
     * @return
     */
    private CellStyle initHeaderStyle(Workbook workbook) {
        CellStyle style = getBaseCellStyle(workbook);
        style.setFont(getFont(workbook, (short) 14, true));
        return style;
    }

    /**
     * 初始化--每列标题样式
     *
     * @param workbook
     * @return
     */
    private CellStyle initTitleStyle(Workbook workbook) {
        CellStyle style = getBaseCellStyle(workbook);
        style.setFont(getFont(workbook, FONT_SIZE_TWELVE, true));
        //背景色
//        style.setFillForegroundColor(IndexedColors.GREY_25_PERCENT.getIndex());
//        style.setFillPattern(FillPatternType.SOLID_FOREGROUND);
        style.setDataFormat(STRING_FORMAT);
        return style;
    }

    /**
     * 初始化--数据行样式
     *
     * @param workbook
     * @return
     */
    private CellStyle initStyles(Workbook workbook) {
        CellStyle style = getBaseCellStyle(workbook);
        style.setFont(getFont(workbook, FONT_SIZE_ELEVEN, false));
        //背景色
//        style.setFillForegroundColor(IndexedColors.RED.getIndex());
//        style.setFillPattern(FillPatternType.SOLID_FOREGROUND);
        style.setDataFormat(STRING_FORMAT);
        return style;
    }

    /**
     * 基础样式
     *
     * @return
     */
    private CellStyle getBaseCellStyle(Workbook workbook) {
        CellStyle style = workbook.createCellStyle();
        //下边框
        style.setBorderBottom(BorderStyle.THIN);
        //左边框
        style.setBorderLeft(BorderStyle.THIN);
        //上边框
        style.setBorderTop(BorderStyle.THIN);
        //右边框
        style.setBorderRight(BorderStyle.THIN);
        //水平居中
        style.setAlignment(HorizontalAlignment.CENTER);
        //上下居中
        style.setVerticalAlignment(VerticalAlignment.CENTER);
        //设置自动换行
        style.setWrapText(true);
        return style;
    }

    /**
     * 字体样式
     *
     * @param size   字体大小
     * @param isBold 是否加粗
     * @return
     */
    private Font getFont(Workbook workbook, short size, boolean isBold) {
        Font font = workbook.createFont();
        //字体样式
        font.setFontName("宋体");
        //是否加粗
        font.setBold(isBold);
        //字体大小
        font.setFontHeightInPoints(size);
        return font;
    }
}
```

## 导出工具类

```text
import cn.afterturn.easypoi.excel.ExcelExportUtil;
import cn.afterturn.easypoi.excel.entity.ExportParams;
import cn.afterturn.easypoi.excel.entity.enmus.ExcelType;
import lombok.extern.slf4j.Slf4j;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;

import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.net.URLEncoder;
import java.util.List;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.LinkedBlockingDeque;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicReference;

/**
 * EasyPoi 导出工具类
 *
 * @Author：chenyanbin
 */
@Slf4j
public class EasyPoiExportUtil {
    private static final Long KEEP_ALIVE_TIME = 60L;
    private static final int APS = Runtime.getRuntime().availableProcessors();
    private static final ThreadPoolExecutor THREAD_POOL_EXECUTOR = new ThreadPoolExecutor(APS * 2, APS * 4, KEEP_ALIVE_TIME, TimeUnit.SECONDS, new LinkedBlockingDeque<>());

    /**
     * 导出Excel 一对多关系
     *
     * @param list        Excel数据集合
     * @param title       Excel第一行标题，如果设置为null，默认不显示
     * @param sheetName   sheet名称
     * @param pojoClass   泛型List的对象
     * @param fileName    导出文件名
     * @param type        excel类型 HSSF || XSSF
     * @param isOneToMany 是否一对多
     * @param response    响应体
     */
    public static void exportOneToManyExcel(
            List<?> list,
            String title,
            String sheetName,
            Class<?> pojoClass,
            String fileName,
            ExcelType type,
            boolean isOneToMany,
            HttpServletResponse response
    ) {
        ExportParams exportParams = new ExportParams(title, sheetName, type);
        exportParams.setStyle(EasyPoiExcelExportStylerUitl.class);
        AtomicReference<Workbook> workbook = new AtomicReference<>();
        workbookHandler(workbook, exportParams, pojoClass, list);
        if (workbook.get() == null) {
            return;
        }
        //判断是否是一对多
        if (isOneToMany) {
            setRowHeight(workbook.get());
        }
        downLoadExcel(fileName, response, workbook.get());
    }

    /**
     * 导出excel
     *
     * @param list         Excel数据集合
     * @param title        Excel第一行标题，如果设置为null，默认不显示
     * @param sheetName    sheet名称
     * @param pojoClass    泛型List的对象
     * @param fileName     导出文件名
     * @param setRowHeight 是否行高自适应
     * @param response     响应体
     */
    public static void exportOneExcel(
            List<?> list,
            String title,
            String sheetName,
            Class<?> pojoClass,
            String fileName,
            boolean setRowHeight,
            HttpServletResponse response
    ) {
        ExportParams exportParams = new ExportParams(title, sheetName);
        exportParams.setStyle(EasyPoiExcelExportStylerUitl.class);
        AtomicReference<Workbook> workbook = new AtomicReference<>();
        workbookHandler(workbook, exportParams, pojoClass, list);
        if (workbook.get() == null) {
            return;
        }
        //判断是否根据内容自适应行高
        if (setRowHeight) {
            Sheet sheet = workbook.get().getSheetAt(0);
            for (int i = 0; i <= sheet.getLastRowNum(); i++) {
                Row row = sheet.getRow(i);
                setRowHeight(row);
            }
        }
        downLoadExcel(fileName, response, workbook.get());
    }

    /**
     * 下载Excel
     *
     * @param fileName
     * @param response
     * @param workbook
     */
    private static void downLoadExcel(String fileName, HttpServletResponse response, Workbook workbook) {
        ServletOutputStream outputStream = null;
        try {
            outputStream = response.getOutputStream();
            response.setCharacterEncoding("UTF-8");
            response.setHeader("content-Type", "application/vnd.ms-excel");
            response.setHeader("Pragma", "No-cache");
            response.setHeader("Content-Disposition",
                    "attachment;filename=" + URLEncoder.encode(fileName, "UTF-8"));
            workbook.write(outputStream);
            outputStream.flush();
        } catch (IOException e) {
            throw new RuntimeException(e.getMessage());
        } finally {
            if (outputStream != null) {
                try {
                    outputStream.close();
                } catch (IOException e) {
                    log.error("excel导出关闭输出流异常：{}", e.getMessage());
                }
            }
        }
    }

    /**
     * 一对多，设置行高
     */
    private static void setRowHeight(Workbook workbook) {
        Sheet sheet = workbook.getSheetAt(0);
        //设置第4列的列宽为60（下标从0开始），TestExportSub2Vo 不知道为什么设置了列宽但是不起作用，只能在这里单独设置
        sheet.setColumnWidth(3, 60 * 256);
        for (int i = 0; i <= sheet.getLastRowNum(); i++) {
            Row row = sheet.getRow(i);
            if (i == 0) {
                //设置第一行的行高（表格标题）
                row.setHeightInPoints(35);
            } else if (i == 1) {
                //设置第二行的行高（表格表头）
                row.setHeightInPoints(25);
            } else {
                //设置其他行的行高根据内容自适应
                setRowHeight(row);
            }
        }
    }

    private static void setRowHeight(Row row) {
        //根据内容长度设置行高
        int enterCnt = 0;
        for (int j = 0; j < row.getPhysicalNumberOfCells(); j++) {
            int rwsTemp = row.getCell(j).toString().length();
            //这里取每一行中的每一列字符长度最大的那一列的字符
            if (rwsTemp > enterCnt) {
                enterCnt = rwsTemp;
            }
        }
        //设置默认行高为35
        row.setHeightInPoints(35);
        //如果字符长度大于35，判断大了多少倍，根据倍数来设置相应的行高
        if (enterCnt > 35) {
            float d = enterCnt / 35;
            float f = 35 * d;
            /*if (d>2 && d<4){
                f = 35*2;
            }else if(d>=4 && d<6){
                f = 35*3;
            }else if (d>=6 && d<8){
                f = 35*4;
            }*/
            row.setHeightInPoints(f);
        }
    }

    private static void workbookHandler(AtomicReference<Workbook> workbook, ExportParams exportParams, Class<?> pojoClass, List<?> list) {
        CountDownLatch latch = new CountDownLatch(1);
        THREAD_POOL_EXECUTOR.execute(() -> {
            try {
                workbook.set(ExcelExportUtil.exportExcel(exportParams, pojoClass, list));
            } finally {
                latch.countDown();
            }
        });
        try {
            latch.await();
        } catch (InterruptedException e) {
            log.error("多线程导出等待异常：{}", e.getMessage());
        }
    }
}
```

## 根据url下载图片转字节数组

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

## 导出实体类vo

```text
import cn.afterturn.easypoi.excel.annotation.Excel;
import io.swagger.annotations.ApiModel;
import lombok.Data;

/**
 * @Author：chenyanbin
 */
@Data
@ApiModel(value = "ProductFilingExportExcelVo对象", description = "商品备案明细导出信息")
public class ProductFilingExportExcelVo {
    /**
     * 主键
     */
    private Long id;

    @Excel(name = "商品编码", width = 20)
    private String productCode;

    @Excel(name = "HS编码", width = 25)
    private String hsCode;

    @Excel(name = "商品名称", width = 40)
    private String productName;

    @Excel(name = "品牌")
    private String brandName;

    @Excel(name = "规格型号", width = 20)
    private String specificationModel;

    @Excel(name = "申报要素", width = 40)
    private String reportElements;

    @Excel(name = "产品成分", width = 50)
    private String productComposition;

    @Excel(name = "生产企业", width = 25)
    private String enterprise;

    @Excel(name = "生产国/地区", width = 20)
    private String country;

    @Excel(name = "适用标准", width = 20)
    private String standards;

    @Excel(name = "商品条码", width = 30)
    private String productBarCode;

    @Excel(name = "功能", width = 40)
    private String function;

    @Excel(name = "其他说明", width = 40)
    private String remark;

    @Excel(name = "商品正面", type = 2, imageType = 2)
    private byte[] productFrontPic;

    /**
     * 临时商品正面url
     */
    private String tempProductFrontUrl;

    @Excel(name = "商品背面", type = 2, imageType = 2)
    private byte[] productBackPic;

    /**
     * 临时商品背面url
     */
    private String tempProductBackUrl;

    @Excel(name = "商品其他面", width = 15, type = 2, imageType = 2)
    private byte[] productOtherPic;

    /**
     * 临时商品其他url
     */
    private String tempProductOtherUrl;
}
```

## dao查询sql语句

```text
    <resultMap id="exportExcelMap" type="ProductFilingExportExcelVo">
        <id column="id" property="id"/>
        <result column="product_code" property="productCode"/>
        <result column="hs_code" property="hsCode"/>
        <result column="product_name" property="productName"/>
        <result column="brand_name" property="brandName"/>
        <result column="specification_model" property="specificationModel"/>
        <result column="report_elements" property="reportElements"/>
        <result column="product_composition" property="productComposition"/>
        <result column="enterprise" property="enterprise"/>
        <result column="country" property="country"/>
        <result column="standards" property="standards"/>
        <result column="product_bar_code" property="productBarCode"/>
        <result column="function" property="function"/>
        <result column="remark" property="remark"/>
        <result column="temp_product_front_url" property="tempProductFrontUrl"/>
        <result column="temp_product_back_url" property="tempProductBackUrl"/>
        <result column="temp_product_other_url" property="tempProductOtherUrl"/>
    </resultMap>

    <!-- excel导出 -->
    <select id="exportExcel" resultMap="exportExcelMap">
        SELECT
            bpfd.id,
            bpfd.product_code,
            bpfd.hs_code,
            bpfd.product_name,
            bb.brand_name,
            bpfd.specification_model,
            bpfd.report_elements,
            bpfd.product_composition,
            bpfd.enterprise,
            bpfd.country,
            bpfd.standards,
            bpfd.product_bar_code,
            bpfd.`function`,
            bpfd.remark,
            bof.url_path temp_product_front_url,
            bob.url_path temp_product_back_url,
            boo.url_path temp_product_other_url
        FROM
            basic_product_filing_detail bpfd
            LEFT JOIN basic_brand bb ON bb.id = bpfd.brand_id
            LEFT JOIN basic_oss bof ON ( bof.id = bpfd.product_front_id AND bof.del_flag = 0 )
            LEFT JOIN basic_oss bob ON ( bob.id = bpfd.product_back_id AND bob.del_flag = 0 )
            LEFT JOIN basic_oss boo ON ( boo.id = bpfd.product_other_id AND boo.del_flag = 0 )
        WHERE
            bpfd.product_filing_id = #{filing_id}
        ORDER BY
            bpfd.id DESC
    </select>
```

## controller层

```text
    @ApiOperation("导出")
    @GetMapping("export_detail_excel")
    public void exportDetailExcel(
            HttpServletResponse response,
            @ApiParam(value = "主表主键id", required = true) @RequestParam(value = "id") Long id
    ) {
        cacheService.exportDetailExcel(response, id);
    }
```

## service层

```text
import javax.servlet.http.HttpServletResponse;

public interface ProductFilingCacheService {
    /**
     * 导出
     * @param response 响应体
     * @param id 主表主键id
     */
    void exportDetailExcel(HttpServletResponse response, Long id);
}
```

```text
    service实现类！！！！
    private static final Long KEEP_ALIVE_TIME = 60L;
    private static final int APS = Runtime.getRuntime().availableProcessors();
    private static final ThreadPoolExecutor THREAD_POOL_EXECUTOR = new ThreadPoolExecutor(APS * 2, APS * 4, KEEP_ALIVE_TIME, TimeUnit.SECONDS, new LinkedBlockingDeque<>());

    @Override
    public void exportDetailExcel(HttpServletResponse response, Long id) {
        List<ProductFilingExportExcelVo> excelList = filingDetailMapper.exportExcel(id);
        CountDownLatch latch = new CountDownLatch(excelList.size());
        //转换图片字节码
        excelList.forEach(obj -> {
            try {
                if (StringUtils.isNotBlank(obj.getTempProductFrontUrl())) {
                    obj.setProductFrontPic(HttpUtil.getNetImgByUrl(obj.getTempProductFrontUrl()));
                }
                if (StringUtils.isNotBlank(obj.getTempProductBackUrl())) {
                    obj.setProductBackPic(HttpUtil.getNetImgByUrl(obj.getTempProductBackUrl()));
                }
                if (StringUtils.isNotBlank(obj.getTempProductOtherUrl())) {
                    obj.setProductOtherPic(HttpUtil.getNetImgByUrl(obj.getTempProductOtherUrl()));
                }
            } finally {
                latch.countDown();
            }
        });
        try {
            latch.await();
        } catch (InterruptedException e) {
            log.error("导出Excel等待下载文件流异常:{}", e.getMessage());
        }
        //获取货主名称
        String cargoOwnerName = "";
        ProductFilingDO productFilingDO = filingMapper.selectById(id);
        if (productFilingDO != null) {
            Long createUserId = productFilingDO.getCreateUserId();
            JsonData<String> jsonData = userControllerFeign.getCargoOwnerNameById(createUserId);
            if (JsonData.isSuccess(jsonData)) {
                cargoOwnerName = jsonData.getData();
            }
        }
        String fileName = cargoOwnerName + "-" + TimeUtil.currentTimeFormat(TimeUtil.YYMMDD) + ".xls";
        //导出
        EasyPoiExportUtil.exportOneExcel(
                excelList,
                fileName.replace(".xls", ""),
                "商品备案明细",
                ProductFilingExportExcelVo.class,
                fileName,
                false,
                response
        );
    }
```

```text
如果需要设置导出行高自适应，使用如下导出!!!!! false改成true

//导出
        EasyPoiExportUtil.exportOneExcel(
                excelList,
                fileName.replace(".xls", ""),
                "商品备案明细",
                ProductFilingExportExcelVo.class,
                fileName,
                true,
                response
        );
```

## 演示

![](/imported/posts/2021-10-29-15480843-00313e7a-springboot整合easypoi-封装excel导出通用工具类-行高自适应-导出图片/images/img_001_c59bc6b82340.gif)
