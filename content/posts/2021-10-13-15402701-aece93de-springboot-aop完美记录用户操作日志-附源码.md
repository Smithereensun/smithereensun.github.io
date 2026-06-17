{

  "title": "SpringBoot AOP完美记录用户操作日志，附源码",
  "date": "2021-10-13",
  "description": "记录内容 接口名称 浏览器名称 操作系统 请求ip 接口入参、出参 接口耗时 。。。。 表结构 sys_log.sql 添加依赖 自定义注解(一) 备注：被该注解修饰的方法，会被记录到日志中** 自定义注解(二) 备注：被该注解修饰的类，会记录从表的id值和从表的表名(用于记录某张表的一行记录，历史",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/aop.html"

}

# 记录内容

1. 接口名称
2. 浏览器名称
3. 操作系统
4. 请求ip
5. 接口入参、出参
6. 接口耗时
7. 。。。。

# 表结构

![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_001_514d64e572dd.png)

![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_002_8f900a89c634.gif)
![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_003_961ddebeb323.gif)

```text
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sys_log
-- ----------------------------
DROP TABLE IF EXISTS `sys_log`;
CREATE TABLE `sys_log` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `module_name` varchar(256) DEFAULT NULL COMMENT '模块名称',
  `browser_name` varchar(1024) DEFAULT NULL COMMENT '浏览器名称',
  `os_name` varchar(256) DEFAULT NULL COMMENT '操作系统名称',
  `ip_addr` varchar(256) DEFAULT NULL COMMENT '请求ip',
  `app_name` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '服务名称',
  `class_name` varchar(1024) DEFAULT NULL COMMENT '类名',
  `method_name` varchar(512) DEFAULT NULL COMMENT '方法',
  `request_url` varchar(1024) DEFAULT NULL COMMENT '请求url',
  `request_method` varchar(255) DEFAULT NULL COMMENT '请求方式，POST、GET',
  `request_param` text COMMENT '请求参数',
  `result_text` text CHARACTER SET utf8 COLLATE utf8_general_ci COMMENT '响应参数',
  `status` tinyint(1) DEFAULT NULL COMMENT '接口状态（0成功 1失败）',
  `error_text` text COMMENT '错误信息',
  `take_up_time` varchar(64) DEFAULT NULL COMMENT '耗时',
  `edit_table_id` bigint(20) DEFAULT NULL COMMENT '编辑的表主键，只有修改时才有值',
  `edit_table_name` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '编辑的表名称，只有修改时才有值',
  `create_time` datetime DEFAULT NULL COMMENT '操作时间',
  `create_user_id` bigint(20) DEFAULT NULL COMMENT '创建人id',
  `create_phone_number` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL COMMENT '创建人手机号',
  `create_user_name` varchar(64) DEFAULT NULL COMMENT '创建人姓名',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='系统操作日志';

SET FOREIGN_KEY_CHECKS = 1;
```

sys_log.sql

# 添加依赖 

```text
           <!-- AOP -->
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-aop</artifactId>
                <version>${spring.boot.version}</version>
            </dependency>
            <!-- 获取浏览器信息 -->
            <dependency>
                <groupId>eu.bitwalker</groupId>
                <artifactId>UserAgentUtils</artifactId>
                <version>1.21</version>
            </dependency>
```

# 自定义注解(一)

```text
import java.lang.annotation.*;

@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface Log {
}
```

**备注：被该注解修饰的方法，会被记录到日志中**

# 自定义注解(二)

```text
import java.lang.annotation.*;

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface LogPlus {
    /**
     * 编辑的表主键
     * @return
     */
    String editTableId() default "id";

    /**
     * 编辑的表名称
     * @return
     */
    String editTableName() default "未知";
}
```

**备注：被该注解修饰的类，会记录从表的id值和从表的表名(用于记录某张表的一行记录，历史修改信息，不需要可忽略)**

# 日志表实体类

```text
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * <p>
 * 系统操作日志
 * </p>
 *
 * @author chenyanbin
 * @since 2021-10-13
 */
@Data
@TableName("sys_log")
@ApiModel(value = "SysLogDO对象", description = "系统操作日志")
public class LogDO implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "主键")
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;

    @ApiModelProperty(value = "模块名称")
    private String moduleName;

    @ApiModelProperty(value = "浏览器名称")
    private String browserName;

    @ApiModelProperty(value = "操作系统名称")
    private String osName;

    @ApiModelProperty(value = "请求ip")
    private String ipAddr;

    @ApiModelProperty(value = "服务名称")
    private String appName;

    @ApiModelProperty(value = "类名")
    private String className;

    @ApiModelProperty(value = "方法")
    private String methodName;

    @ApiModelProperty(value = "请求url")
    private String requestUrl;

    @ApiModelProperty(value = "请求方式，POST、GET")
    private String requestMethod;

    @ApiModelProperty(value = "请求参数")
    private String requestParam;

    @ApiModelProperty(value = "响应参数")
    private String resultText;

    @ApiModelProperty(value = "接口状态（0成功 1失败）")
    private Byte status;

    @ApiModelProperty(value = "错误信息")
    private String errorText;

    @ApiModelProperty(value = "耗时")
    private String takeUpTime;

    @ApiModelProperty(value = "编辑的表主键，只有修改时才有值")
    private Long editTableId;

    @ApiModelProperty(value = "编辑的表名称，只有修改时才有值")
    private String editTableName;

    @ApiModelProperty(value = "操作时间")
    private Date createTime;

    @ApiModelProperty(value = "创建人id")
    private Long createUserId;

    @ApiModelProperty(value = "创建人手机号")
    private String createPhoneNumber;

    @ApiModelProperty(value = "创建人姓名")
    private String createUserName;

}
```

# Mapper.java

```text
import com.baomidou.mybatisplus.core.mapper.BaseMapper;

public interface LogMapper extends BaseMapper<LogDO> {
}
```

# Aspect (AOP)

```text
import com.alibaba.fastjson.JSON;
import eu.bitwalker.useragentutils.Browser;
import eu.bitwalker.useragentutils.OperatingSystem;
import eu.bitwalker.useragentutils.UserAgent;
import io.swagger.annotations.ApiOperation;
import lombok.extern.slf4j.Slf4j;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.aspectj.lang.reflect.MethodSignature;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.context.request.RequestAttributes;
import org.springframework.web.context.request.RequestContextHolder;

import javax.servlet.http.HttpServletRequest;

/**
 * 操作日志处理
 *
 * @Author：chenyanbin
 */
@Slf4j
@Aspect
@Component
public class LogAspect {
    @Autowired
    LogMapper logMapper;
    @Value("${spring.application.name}")
    private String appNname;

    @Pointcut("@annotation(com.yida.annotation.Log)")
    public void logPoint() {
    }

    @Around("logPoint()")
    public Object around(ProceedingJoinPoint joinPoint) throws Throwable {
        Object result = null;
        LogDO logDO = new LogDO();
        try {
            RequestAttributes requestAttributes = RequestContextHolder.getRequestAttributes();
            HttpServletRequest request = (HttpServletRequest) requestAttributes
                    .resolveReference(RequestAttributes.REFERENCE_REQUEST);
            MethodSignature methodSignature = (MethodSignature) joinPoint.getSignature();
            UserAgent userAgent = UserAgent.parseUserAgentString(request.getHeader("User-Agent"));
            //浏览器对象
            Browser browser = userAgent.getBrowser();
            //操作系统对象
            OperatingSystem operatingSystem = userAgent.getOperatingSystem();
            logDO.setBrowserName(browser.getName());
            ApiOperation aon = methodSignature.getMethod().getAnnotation(ApiOperation.class);
            if (aon != null) {
                logDO.setModuleName(aon.value());
            }
            logDO.setOsName(operatingSystem.getName());
            logDO.setIpAddr(CommonUtil.getIpAddr(request));
            logDO.setAppName(appNname);
            logDO.setClassName(joinPoint.getTarget().getClass().getName());
            logDO.setMethodName(methodSignature.getMethod().getName());
            logDO.setRequestUrl(request.getRequestURI());
            logDO.setRequestMethod(request.getMethod());
            //获取请求参数
            CommonUtil.getRequestParam(joinPoint, methodSignature, logDO);
            logDO.setResultText(JSON.toJSONString(result));
            logDO.setStatus((byte) 0);
            logDO.setCreateTime(CommonUtil.getCurrentDate());
            logDO.setCreateUserId(CommonUtil.getCurrentUserId());
            logDO.setCreatePhoneNumber(CommonUtil.getCurrentPhoneNumber());
            logDO.setCreateUserName(CommonUtil.getCurrentUserName());
            long startTime = System.currentTimeMillis();
            result = joinPoint.proceed();
            long endTime = System.currentTimeMillis();
            logDO.setTakeUpTime(String.format("耗时：%s 毫秒", endTime - startTime));
            logDO.setResultText(result.toString());
        } catch (Exception e) {
            logDO.setStatus((byte) 1);
            if (e instanceof BizException) {
                BizException bizException = (BizException) e;
                result = JsonData.buildCodeAndMsg(bizException.getCode(), bizException.getMessage());
                logDO.setErrorText(result.toString());
            } else if (e instanceof RpvException) {
                RpvException ve = (RpvException) e;
                result = JsonData.buildCodeAndMsg(ve.getCode(), ve.getMessage());
                logDO.setErrorText(result.toString());
            } else {
                logDO.setErrorText(e.getMessage());
                result = e.getMessage();
            }
        } finally {
            logMapper.insert(logDO);
        }
        return result;
    }
}
```

```text
String agent=request.getHeader("User-Agent");
//解析agent字符串
UserAgent userAgent = UserAgent.parseUserAgentString(agent);
//获取浏览器对象
Browser browser = userAgent.getBrowser();
//获取操作系统对象
OperatingSystem operatingSystem = userAgent.getOperatingSystem();

System.out.println("浏览器名:"+browser.getName());
System.out.println("浏览器类型:"+browser.getBrowserType());
System.out.println("浏览器家族:"+browser.getGroup());
System.out.println("浏览器生产厂商:"+browser.getManufacturer());
System.out.println("浏览器使用的渲染引擎:"+browser.getRenderingEngine());
System.out.println("浏览器版本:"+userAgent.getBrowserVersion());

System.out.println("操作系统名:"+operatingSystem.getName());
System.out.println("访问设备类型:"+operatingSystem.getDeviceType());
System.out.println("操作系统家族:"+operatingSystem.getGroup());
System.out.println("操作系统生产厂商:"+operatingSystem.getManufacturer());
```

## 其他类

![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_002_8f900a89c634.gif)
![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_003_961ddebeb323.gif)

```text
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.extern.slf4j.Slf4j;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.reflect.MethodSignature;
import org.springframework.core.DefaultParameterNameDiscoverer;
import org.springframework.core.ParameterNameDiscoverer;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.validation.ConstraintViolation;
import javax.validation.Validation;
import javax.validation.Validator;
import java.io.IOException;
import java.io.PrintWriter;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.security.MessageDigest;
import java.util.*;

/**
 * 公共工具类
 *
 * @Author：chenyanbin
 */
@Slf4j
public class CommonUtil {
    private static Validator validator = Validation.buildDefaultValidatorFactory().getValidator();

    /**
     * 获取ip
     *
     * @param request
     * @return
     */
    public static String getIpAddr(HttpServletRequest request) {
        String ipAddress = null;
        try {
            ipAddress = request.getHeader("x-forwarded-for");
            if (ipAddress == null || ipAddress.length() == 0 || "unknown".equalsIgnoreCase(ipAddress)) {
                ipAddress = request.getHeader("Proxy-Client-IP");
            }
            if (ipAddress == null || ipAddress.length() == 0 || "unknown".equalsIgnoreCase(ipAddress)) {
                ipAddress = request.getHeader("WL-Proxy-Client-IP");
            }
            if (ipAddress == null || ipAddress.length() == 0 || "unknown".equalsIgnoreCase(ipAddress)) {
                ipAddress = request.getRemoteAddr();
                if (ipAddress.equals("127.0.0.1")) {
                    // 根据网卡取本机配置的IP
                    InetAddress inet = null;
                    try {
                        inet = InetAddress.getLocalHost();
                    } catch (UnknownHostException e) {
                        e.printStackTrace();
                    }
                    ipAddress = inet.getHostAddress();
                }
            }
            // 对于通过多个代理的情况，第一个IP为客户端真实IP,多个IP按照','分割
            if (ipAddress != null && ipAddress.length() > 15) {
                // "***.***.***.***".length()
                // = 15
                if (ipAddress.indexOf(",") > 0) {
                    ipAddress = ipAddress.substring(0, ipAddress.indexOf(","));
                }
            }
        } catch (Exception e) {
            ipAddress = "";
        }
        return ipAddress;
    }

    /**
     * 获取当前时间戳
     *
     * @return
     */
    public static long getCurrentTimestamp() {
        return System.currentTimeMillis();
    }

    /**
     * 获取当前日期
     *
     * @return
     */
    public static Date getCurrentDate() {
        return new Date();
    }

    /**
     * 获取当前操作用户的主键id
     *
     * @return
     */
    public static Long getCurrentUserId() {
        LoginUser loginUser = getLoginUser();
        if (loginUser == null) {
            return null;
        }
        return loginUser.getId();
    }

    private static LoginUser getLoginUser() {
        return JwtFilter.threadLocal.get();
    }

    /**
     * 获取当前操作用户的手机号
     *
     * @return
     */
    public static String getCurrentPhoneNumber() {
        LoginUser loginUser = getLoginUser();
        if (loginUser == null) {
            return null;
        }
        return loginUser.getPhoneNumber();
    }

    /**
     * 获取当前操作用户的名称
     *
     * @return
     */
    public static String getCurrentUserName() {
        LoginUser loginUser = getLoginUser();
        if (loginUser == null) {
            return null;
        }
        return loginUser.getUserName();
    }

    /**
     * 判断当前用户是否管理员
     */
    public static boolean isAdmin() {
        return getCurrentUserId() == 1;
    }

    /**
     * 获取请求参数
     *
     * @param joinPoint 切入点
     * @param signature 方法签名
     * @param logDO     日志对象
     */
    public static void getRequestParam(ProceedingJoinPoint joinPoint, MethodSignature signature, LogDO logDO) {
        // 参数值
        Object[] args = joinPoint.getArgs();
        ParameterNameDiscoverer pnd = new DefaultParameterNameDiscoverer();
        Method method = signature.getMethod();
        String[] parameterNames = pnd.getParameterNames(method);
        Map<String, Object> paramMap = new HashMap<>(32);
        for (int i = 0; i < parameterNames.length; i++) {
            paramMap.put(parameterNames[i], args[i]);
            if (args[i] != null) {
                //反射获取具体的值
                LogPlus logPlus = args[i].getClass().getAnnotation(LogPlus.class);
                if (logPlus != null) {
                    Field f = null;
                    try {
                        f = args[i].getClass().getDeclaredField(logPlus.editTableId());
                        f.setAccessible(true);
                        Object obj = f.get(args[i]);
                        logDO.setEditTableId(Long.valueOf(obj + ""));
                        logDO.setEditTableName(logPlus.editTableName());
                    } catch (Exception e) {
                        log.error("反射获取编辑的表主键异常：{}", e.getMessage());
                    } finally {
                        if (f != null) {
                            f.setAccessible(false);
                        }
                    }
                }
            }
        }
        logDO.setRequestParam(paramMap.toString());
    }
}
```

CommonUtil.java

![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_002_8f900a89c634.gif)
![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_003_961ddebeb323.gif)

```text
import com.fasterxml.jackson.annotation.JsonProperty;
import lombok.Data;

/**
 * 登录用户
 * @Author：chenyanbin
 */
@Data
public class LoginUser {
    /**
     * 主键
     */
    private Long id;

    /**
     * 手机号
     */
    @JsonProperty("phone_number")
    private String phoneNumber;

    /**
     * 用户昵称
     */
    @JsonProperty("user_name")
    private String userName;

    /**
     * 是否货主(0是 1否)
     */
    @JsonProperty("cargo_master")
    private byte cargoMaster;

    /**
     * 管理员 (0是 1否)
     */
    private byte admin;
}
```

LoginUser.java

![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_002_8f900a89c634.gif)
![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_003_961ddebeb323.gif)

```text
import lombok.Data;

/**
 * 业务异常类
 * @Author：chenyanbin
 */
@Data
public class BizException extends RuntimeException {
    private int code;
    private String message;

    public BizException(int code, String message) {
        super(message);
        this.code = code;
        this.message = message;
    }

    public BizException(BizCodeEnum bizCodeEnum) {
        super(bizCodeEnum.getMessage());
        this.code = bizCodeEnum.getCode();
        this.message = bizCodeEnum.getMessage();
    }
}
```

BizException.java

![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_002_8f900a89c634.gif)
![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_003_961ddebeb323.gif)

```text
import lombok.Data;

/**
 * Request Param Value：请求参数异常
 * @Author：chenyanbin
 */
@Data
public class RpvException extends RuntimeException {
    private int code;
    private String message;

    public RpvException(int code, String message) {
        this.code = code;
        this.message = message;
    }
}
```

RpvException.java

![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_002_8f900a89c634.gif)
![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_003_961ddebeb323.gif)

```text
package com.yida.utils;

import com.yida.enums.BizCodeEnum;

import java.io.Serializable;

/**
 * @Description：统一协议JsonData工具类
 * @Author：chenyanbin
 * @Date：2021/5/9 下午8:09
 * @Versiion：1.0
 */
public class JsonData<T> implements Serializable {
    /**
     * 状态码 0 表示成功，1表示处理中，-1表示失败
     */
    private Integer code;
    /**
     * 数据
     */
    private T data;
    /**
     * 描述
     */
    private String msg;

    private JsonData() {
    }

    private static <T> JsonData<T> build(Integer code, T data, String msg) {
        JsonData json = new JsonData();
        json.setCode(code);
        json.setData(data);
        json.setMsg(msg);
        return json;
    }

    /**
     * 成功，传⼊数据
     *
     * @return
     */
    public static <T> JsonData<T> buildSuccess() {
        return build(0, (T) "", "");
    }

    /**
     * 默认添加成功
     *
     * @return
     */
    public static <T> JsonData<T> buildAddSuccess() {
        return build(0, (T) "添加成功", "");
    }

    /**
     * 默认修改成功
     *
     * @return
     */
    public static <T> JsonData<T> buildEditSuccess() {
        return build(0, (T) "修改成功", "");
    }

    /**
     * 默认删除成功
     *
     * @return
     */
    public static <T> JsonData<T> buildRemoveSuccess() {
        return build(0, (T) "删除成功", "");
    }

    /**
     * 成功，传⼊数据
     *
     * @param data
     * @return
     */
    public static <T> JsonData<T> buildSuccess(T data) {
        return build(0, data, "");
    }

    /**
     * 失败，传⼊描述信息
     *
     * @param msg
     * @return
     */
    public static <T> JsonData<T> buildError(String msg) {
        return build(-1, (T) "", msg);
    }

    /**
     * ⾃定义状态码和错误信息
     *
     * @param code
     * @param msg
     * @return
     */
    public static <T> JsonData<T> buildCodeAndMsg(int code, String msg) {
        return build(code, null, msg);
    }

    /**
     * 传⼊枚举，返回信息
     *
     * @param codeEnum
     * @return
     */
    public static <T> JsonData<T> buildResult(BizCodeEnum codeEnum) {
        return buildCodeAndMsg(codeEnum.getCode(), codeEnum.getMessage());
    }

    /**
     * 判断接口响应是否成功，只是判断状态码是否等于：0
     *
     * @param data
     * @return
     */
    public static boolean isSuccess(JsonData data) {
        return data.getCode() == 0;
    }

    /**
     * 判断接口响应是否失败，状态码除了0以外的，默认调用失败
     *
     * @param data
     * @return
     */
    public static boolean isFailure(JsonData data) {
        return !isSuccess(data);
    }

    public Integer getCode() {
        return code;
    }

    public void setCode(Integer code) {
        this.code = code;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }

    @Override
    public String toString() {
        return "JsonData{" +
                "code=" + code +
                ", data=" + data +
                ", msg='" + msg + '\'' +
                '}';
    }
}
```

JsonData.java

# 控制器添加@Log注解

```text
    @ApiOperation("用户登录")
    @PostMapping("login")
    @Log
    public JsonData login(
            @ApiParam("用户登录对象") @RequestBody UserLoginRequest userLoginRequest
    ) {
        return userService.login(userLoginRequest);
    }
```

修改接口，json对象添加@LogPlus

```text
@Data
@ApiModel(value = "角色编辑对象", description = "用户编辑请求对象")
@LogPlus(editTableId = "id", editTableName = "sys_role")
public class RoleEditRequest {
    @ApiModelProperty(value = "主键id", example = "-1")
    @DecimalMin(value = "1", message = "角色id最小为1")
    private Long id;

    @ApiModelProperty(value = "角色名称", example = "货主")
    @JsonProperty("role_name")
    @NotBlank(message = "角色名称不能为空")
    private String roleName;

    @ApiModelProperty(value = "角色状态（0正常 1停用）", example = "0")
    @Min(value = 0, message = "角色状态（0正常 1停用）")
    @Max(value = 1, message = "角色状态（0正常 1停用）")
    private byte status;

    @ApiModelProperty(value = "备注", example = "货主角色")
    private String remark;

    @ApiModelProperty(value = "菜单id列表", example = "[1,2,3,4]")
    private List<Long> menuIds;
}
```

# 效果演示

![](/imported/posts/2021-10-13-15402701-aece93de-springboot-aop完美记录用户操作日志-附源码/images/img_004_56f138927ca6.gif)
