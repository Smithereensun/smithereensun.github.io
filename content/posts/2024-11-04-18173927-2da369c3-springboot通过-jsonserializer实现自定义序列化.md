{

  "title": "SpringBoot通过 JsonSerializer实现自定义序列化",
  "date": "2024-11-04",
  "description": "介绍 是 Jackson 库中的一个类，用于自定义 Java 对象到 JSON 字符串的序列化过程。在使用 Jackson 进行对象序列化时，有时候需要对某些特定类型的字段进行定制化的序列化处理，这时就可以使用 来实现自定义的序列化逻辑。 使用 继承JsonSerializer VO上添加注解：**",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/18173927"

}

# 介绍

`　　JsonSerializer` 是 Jackson 库中的一个类，用于自定义 Java 对象到 JSON 字符串的序列化过程。在使用 Jackson 进行对象序列化时，有时候需要对某些特定类型的字段进行定制化的序列化处理，这时就可以使用 `JsonSerializer` 来实现自定义的序列化逻辑。

# 使用

继承JsonSerializer<T>

```text
package com.ybchen.seria;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.databind.JsonSerializer;
import com.fasterxml.jackson.databind.SerializerProvider;
import org.apache.commons.lang3.StringUtils;

import java.io.IOException;

/**
 * @description: 图片序列化
 * @author: alex
 * @create: 2024-05-05 21:10
 */
public class PictureJsonSerializer extends JsonSerializer<String> {
    @Override
    public void serialize(String str, JsonGenerator gen, SerializerProvider serializerProvider) throws IOException {
        if (StringUtils.isNotEmpty(str)){
            //转换图片加签
            gen.writeString(str+"xxx.jpg");
        }
    }
}
```

VO上添加注解：**@JsonSerialize(using = PictureJsonSerializer.class)**

```text
package com.ybchen.vo;

import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.ybchen.seria.PictureJsonSerializer;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.ArrayList;
import java.util.List;

/**
 * @description:
 * @author: alex
 * @create: 2024-05-05 21:15
 */
@Data
public class ImageVO {
    @ApiModelProperty("主键id")
    private Integer id;

    @ApiModelProperty("图片")
    @JsonSerialize(using = PictureJsonSerializer.class)
    private String image;

    @ApiModelProperty("图片列表")
    private List<String> imageList=new ArrayList<>();
}
```

# 处理非空的情况，也进入JsonSerializer

```text
 @JsonSerialize(using = xxxx.class,nullsUsing=xxxx.class)
    private String image;
```
