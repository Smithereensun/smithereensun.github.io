{

  "title": "SpringBoot 校验post请求参数",
  "date": "2020-11-17",
  "description": "导读 前后端分离项目中，前端往后端传值时，后端都要做参数格式校验，比如校验数字最大值、最小值、是否允许为空、日期格式等等。 添加依赖 自定义日期注解 作用 校验日期格式，自定义校验规格 DateTime.java 约束自定义注解校验器 作用 校验自定义注解验证格式 DateTimeValidator",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13993403.html"

}

# 导读

　　前后端分离项目中，前端往后端传值时，后端都要做参数格式校验，比如校验数字最大值、最小值、是否允许为空、日期格式等等。

# 添加依赖

```text
        <!-- 参数校验 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-validation</artifactId>
        </dependency>
```

# 自定义日期注解

## 作用

　　校验日期格式，自定义校验规格

DateTime.java

```text
package net.ybclass.online_ybclass.utils;

import javax.validation.Constraint;
import javax.validation.Payload;
import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Target({ElementType.FIELD, ElementType.PARAMETER})
@Retention(RetentionPolicy.RUNTIME)
@Constraint(validatedBy = DateTimeValidator.class)
public @interface DateTime {
    String message() default "日期格式错误";

    String format() default "yyyyMM";

    Class<?>[] groups() default {};

    Class<? extends Payload>[] payload() default {};
}
```

# 约束自定义注解校验器

## 作用

　　校验自定义注解验证格式

DateTimeValidator.java

```text
package net.ybclass.online_ybclass.utils;

import javax.validation.ConstraintValidator;
import javax.validation.ConstraintValidatorContext;
import java.text.SimpleDateFormat;

/**
 * @ClassName：DateTimeValidator
 * @Description：日期校验器
 * @Author：chenyb
 * @Date：2020/11/17 10:13 上午
 * @Versiion：1.0
 */
public class DateTimeValidator implements ConstraintValidator<DateTime, String> {
    private DateTime dateTime;

    /**
     * 初始化
     * @param dateTime
     */
    @Override
    public void initialize(DateTime dateTime) {
        this.dateTime = dateTime;
    }

    /**
     * 验证参数
     * @param value
     * @param context
     * @return
     */
    @Override
    public boolean isValid(String value, ConstraintValidatorContext context) {
        // 如果 value 为空则不进行格式验证，为空验证可以使用 @NotBlank @NotNull @NotEmpty 等注解来进行控制，职责分离
        if (value == null) {
            return true;
        }
        String format = dateTime.format();

        if (value.length() != format.length()) {
            return false;
        }

        SimpleDateFormat simpleDateFormat = new SimpleDateFormat(format);

        try {
            simpleDateFormat.parse(value);
        } catch (Exception e) {
            return false;
        }
        return true;
    }
}
```

# 常用校验注解标签

- @AssertFalse 所注解的元素必须是Boolean类型，且值为false
- @AssertTrue 所注解的元素必须是Boolean类型，且值为true
- @DecimalMax 所注解的元素必须是数字，且值小于等于给定的值
- @DecimalMin 所注解的元素必须是数字，且值大于等于给定的值
- @Digits 所注解的元素必须是数字，且值必须是指定的位数
- @Future 所注解的元素必须是将来某个日期
- **@Max** 所注解的元素必须是数字，且值小于等于给定的值
- **@Min** 所注解的元素必须是数字，且值小于等于给定的值
- @Range 所注解的元素需在指定范围区间内
- **@NotNull** 所注解的元素值不能为null
- **@NotBlank** 所注解的元素值有内容
- **@Null** 所注解的元素值为null
- @Past 所注解的元素必须是某个过去的日期
- @PastOrPresent 所注解的元素必须是过去某个或现在日期
- **@Pattern** 所注解的元素必须满足给定的正则表达式
- @Size 所注解的元素必须是String、集合或数组，且长度大小需保证在给定范围之内
- @Email 所注解的元素需满足Email格式

# demo

## 请求参数实体类

```text
package net.ybclass.online_ybclass.model.request;

import net.ybclass.online_ybclass.utils.DateTime;

import javax.validation.constraints.*;

public class ParamValidRequest {
    @Max(value = 100, message = "id=最大值不能超过100")
    @Min(value = 1, message = "id=最小不能小于1")
    private int id;
    @NotNull(message = "userName======》@NotNull")
    private String userName;
    @NotBlank(message = "salary======》@NotBlank")
    private String salary;
    @NotBlank
    @Pattern(regexp = "1234567890",message = "phone=手机号支持正则表达式，手机号必须：1234567890")
    private String phone;
    //删除时间，当输入的时间为2020-08-26或2020/08/26 11:22:33,时间格式不符合"yyyy-MM-dd HH:mm:ss"
    //@Pattern(regexp = "^((([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8]))))|((([0-9]{2})(0[48]|[2468][048]|[13579][26])|((0[48]|[2468][048]|[3579][26])00))-02-29))\\s+([0-1]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$")
    @NotNull
    @DateTime(format = "yyyy-MM-dd",message = "createDate=日期格式不正确，正确格式：yyyy-MM-dd")
    private String createDate;
    @AssertTrue(message = "flag=必须为true")
    private Boolean flag;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getSalary() {
        return salary;
    }

    public void setSalary(String salary) {
        this.salary = salary;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getCreateDate() {
        return createDate;
    }

    public void setCreateDate(String createDate) {
        this.createDate = createDate;
    }

    public Boolean getFlag() {
        return flag;
    }

    public void setFlag(Boolean flag) {
        this.flag = flag;
    }

    @Override
    public String toString() {
        return "TestRequest{" +
                "id=" + id +
                ", userName='" + userName + '\'' +
                ", salary='" + salary + '\'' +
                ", phone='" + phone + '\'' +
                ", createDate=" + createDate +
                ", flag=" + flag +
                '}';
    }
}
```

## 控制器

```text
package net.ybclass.online_ybclass.controller;

import net.ybclass.online_ybclass.model.request.ParamValidRequest;
import net.ybclass.online_ybclass.utils.JsonData;
import org.springframework.validation.BindingResult;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ParamController {
    @PostMapping("param")
    public JsonData param(@Validated @RequestBody ParamValidRequest request, BindingResult br) {
        //判断参数是否校验失败，若校验失败，直接返回错误信息
        if (br.hasErrors()) {
            return JsonData.buildError(br.getFieldError().getDefaultMessage());
        }
        System.out.println(request);
        return JsonData.buildSuccess("ok");
    }
}
```

## 验证

![](/imported/posts/2020-11-17-13993403-eca1fc1d-springboot-校验post请求参数/images/img_001_506fae4b2393.gif)

# 补充

　　我之前一家公司的，用这种方法不行，然后自己手动写了个工具类，通过工具类校验请求参数格式，如下

```text
package com.zcsoft.rc.bms.utils;

import java.util.Set;
import javax.validation.ConstraintViolation;
import javax.validation.Validation;
import javax.validation.Validator;

import com.sharingif.cube.core.exception.validation.ValidationCubeException;
import org.hibernate.validator.HibernateValidator;
/**
 * @ClassName：ValidationUtils
 * @Description：请求参数验证工具类
 * @Author：chenyb
 * @Date：2020/8/14 9:50 上午
 * @Versiion：1.0
 */
public class ValidationUtils{
    /**
     * 使用hibernate的注解来进行验证
     *
     */
    private static Validator validator = Validation
            .byProvider(HibernateValidator.class).configure().failFast(true).buildValidatorFactory().getValidator();

    /**
     * 功能描述: <br>
     * 〈注解验证参数〉
     *
     * @param obj
     * @see [相关类/方法](可选)
     * @since [产品/模块版本](可选)
     */
    public static  <T> void validate(T obj) {
        Set<ConstraintViolation<T>> constraintViolations = validator.validate(obj);
        // 抛出检验异常
        if (constraintViolations.size() > 0) {
            throw new ValidationCubeException(String.format("参数校验失败:%s", constraintViolations.iterator().next().getMessage()));
        }
    }
}
```

控制层

```text
    @RequestMapping(value = "add", method= RequestMethod.POST)
    public SecurityRiskLibaryAddRsp add(SecurityRiskLibaryAddReq req){
        ValidationUtils.validate(req);
        return securityRiskLibaryService.add(req);
    }
```
