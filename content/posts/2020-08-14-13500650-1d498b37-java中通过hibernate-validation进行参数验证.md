{

  "title": "JAVA中通过Hibernate-Validation进行参数验证",
  "date": "2020-08-14",
  "description": "导读 在开发JAVA服务器端代码时，我们会遇到对外部传来的参数合法性进行验证，而hibernate-validator提供了一些常用的参数校验注解，我们可以拿来使用。 引入maven依赖 在Model中定义要校验的字段：** 定义Validation工具类** 在代码中调用工具类进行参数校验：** ",
  "tags": [
    "Java"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13500650.html"

}

# 导读

在开发JAVA服务器端代码时，我们会遇到对外部传来的参数合法性进行验证，而hibernate-validator提供了一些常用的参数校验注解，我们可以拿来使用。

## 引入maven依赖

```text
<dependency>
    <groupId>org.hibernate</groupId>
    <artifactId>hibernate-validator</artifactId>
    <version>4.3.1.Final</version>
</dependency>
```

## **在Model中定义要校验的字段：**

```text
import javax.validation.constraints.Pattern;
import javax.validation.constraints.Size;
import org.hibernate.validator.constraints.NotEmpty;

public class PayRequestDto {

    /**
     * 支付完成时间
     **/
    @NotEmpty(message="支付完成时间不能空")
    @Size(max=14,message="支付完成时间长度不能超过{max}位")
    private String payTime;

    /**
     * 状态
     **/
    @Pattern(regexp = "0[0123]", message = "状态只能为00或01或02或03")
    private String status;

    public String getPayTime() {
        return payTime;
    }

    public void setPayTime(String payTime) {
        this.payTime = payTime;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
```

## **定义Validation工具类**

```text
import java.util.Set;
import javax.validation.ConstraintViolation;
import javax.validation.Validation;
import javax.validation.Validator;
import org.hibernate.validator.HibernateValidator;
import com.atai.framework.lang.AppException;

public class ValidationUtils {

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
    public static <T> void validate(T obj) {
        Set<ConstraintViolation<T>> constraintViolations = validator.validate(obj);
        // 抛出检验异常
        if (constraintViolations.size() > 0) {
            throw new AppException("0001", String.format("参数校验失败:%s", constraintViolations.iterator().next().getMessage()));
        }
    }
}
```

## **在代码中调用工具类进行参数校验：**

```text
    /**
     * 添加
     * @param req
     * @return
     */
    @RequestMapping(value = "add", method= RequestMethod.POST)
    public SecurityRiskLibaryAddRsp add(SecurityRiskLibaryAddReq req){
        ValidationUtils.validate(req);
        return securityRiskLibaryService.add(req);
    }
```

### **以下是对hibernate-validator中部分注解进行描述：**

<table border="0"> <tbody> <tr> <td>@AssertTrue</td> <td>用于boolean字段，该字段只能为true  </td> </tr> <tr> <td>@AssertFalse</td> <td>该字段的值只能为false</td> </tr> <tr> <td>@CreditCardNumber</td> <td>对信用卡号进行一个大致的验证</td> </tr> <tr> <td>@DecimalMax</td> <td>只能小于或等于该值</td> </tr> <tr> <td>@DecimalMin</td> <td>只能大于或等于该值</td> </tr> <tr> <td>@Digits(integer=,fraction=)</td> <td>检查是否是一种数字的整数、分数,小数位数的数字</td> </tr> <tr> <td>@Email</td> <td>检查是否是一个有效的email地址</td> </tr> <tr> <td>@Future</td> <td>检查该字段的日期是否是属于将来的日期</td> </tr> <tr> <td>@Length(min=,max=)</td> <td>检查所属的字段的长度是否在min和max之间,只能用于字符串</td> </tr> <tr> <td>@Max</td> <td>该字段的值只能小于或等于该值</td> </tr> <tr> <td>@Min</td> <td>该字段的值只能大于或等于该值</td> </tr> <tr> <td>@NotNull</td> <td>不能为null</td> </tr> <tr> <td>@NotBlank</td> <td>不能为空，检查时会将空格忽略</td> </tr> <tr> <td>@NotEmpty</td> <td>不能为空，这里的空是指空字符串</td> </tr> <tr> <td>@Null</td> <td>检查该字段为空</td> </tr> <tr> <td>@Past</td> <td>检查该字段的日期是在过去</td> </tr> <tr> <td>@Pattern(regex=,flag=)</td> <td>被注释的元素必须符合指定的正则表达式</td> </tr> <tr> <td>@Range(min=,max=,message=)</td> <td>被注释的元素必须在合适的范围内</td> </tr> <tr> <td>@Size(min=, max=)</td> <td>检查该字段的size是否在min和max之间，可以是字符串、数组、集合、Map等</td> </tr> <tr> <td>@URL(protocol=,host,port)</td> <td>检查是否是一个有效的URL，如果提供了protocol，host等，则该URL还需满足提供的条件</td> </tr> <tr> <td>@Valid</td> <td>该注解主要用于字段为一个包含其他对象的集合或map或数组的字段，或该字段直接为一个其他对象的引用，这样在检查当前对象的同时也会检查该字段所引用的对象</td> </tr> </tbody> </table>

## 验证

![](/imported/posts/2020-08-14-13500650-1d498b37-java中通过hibernate-validation进行参数验证/images/img_001_2b77a41198db.png)
