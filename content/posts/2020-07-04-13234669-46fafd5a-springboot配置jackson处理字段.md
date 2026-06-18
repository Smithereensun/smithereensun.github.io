{

  "title": "SpringBoot配置Jackson处理字段",
  "date": "2020-07-04",
  "description": "常用框架 阿里fastjson，谷歌gson等 JavaBean序列化为json 性能：Jackson>FastJson>Gson>lib 同个结构 Jackson、Fastjson、Gson等库各有优缺点，各有自己的专长 空间换时间，时间换空间 Jackson处理相关自动 指定字段不返回：@Jso",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13234669.html"

}

常用框架 阿里fastjson，谷歌gson等

JavaBean序列化为json

- 性能：Jackson>FastJson>Gson>lib 同个结构
- Jackson、Fastjson、Gson等库各有优缺点，各有自己的专长
- 空间换时间，时间换空间

Jackson处理相关自动

- 指定字段不返回：@JsonIgnore
- 指定日期格式：@JsonFormat(pattern="yyyy-MM-dd hh:mm:ss",locale="zh",timezone="GMT+8")
- 空字段不返回：@JsonInclude(JsonInclude.Include.NON_NULL)
- 指定别名：@JsonProperty("TITLE")

```text
package net.cyb.demo.domain;

import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.io.Serializable;
import java.util.Date;
import java.util.List;

public class Video implements Serializable {
    private int id;
    //设置别名
    @JsonProperty("TITLE")
    private String title;
    private String summary;
    //指定字段不返回
    @JsonIgnore
    private int pricce;
    //空字段不返回
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private String converImg;
    //指定日期格式
    @JsonFormat(pattern="yyyy-MM-dd hh:mm:ss",locale="zh",timezone="GMT+8")
    private Date createTime;
    private List<Chapter> chapterList;

    public List<Chapter> getChapterList() {
        return chapterList;
    }

    public void setChapterList(List<Chapter> chapterList) {
        this.chapterList = chapterList;
    }

    public Video() {
    }

    public Video(int id, String title) {
        this.id = id;
        this.title = title;
        this.createTime = new Date();
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getSummary() {
        return summary;
    }

    public void setSummary(String summary) {
        this.summary = summary;
    }

    public int getPricce() {
        return pricce;
    }

    public void setPricce(int pricce) {
        this.pricce = pricce;
    }

    public String getConverImg() {
        return converImg;
    }

    public void setConverImg(String converImg) {
        this.converImg = converImg;
    }

    public Date getCreateTime() {
        return createTime;
    }

    public void setCreateTime(Date createTime) {
        this.createTime = createTime;
    }

    @Override
    public String toString() {
        return "Video{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", summary='" + summary + '\'' +
                ", pricce=" + pricce +
                ", converImg='" + converImg + '\'' +
                ", createTime=" + createTime +
                ", chapterList=" + chapterList +
                '}';
    }
}
```

序列化操作

```text
    public JsonData list() throws JsonProcessingException {
        List<Video> list=videoService.listVideo();
        ObjectMapper objectMapper=new ObjectMapper();
        String jsonStr=objectMapper.writeValueAsString(list);
        System.out.println(jsonStr);
        return JsonData.buildSuccess(list);
    }
```

反序列化

```text
    public JsonData list() throws JsonProcessingException {
        List<Video> list=videoService.listVideo();
        ObjectMapper objectMapper=new ObjectMapper();
        String jsonStr=objectMapper.writeValueAsString(list);
        System.out.println(jsonStr);
        List<Video> list1 = objectMapper.readValue(jsonStr, List.class);
        System.out.println(list1);
        return JsonData.buildSuccess(list);
    }
```
