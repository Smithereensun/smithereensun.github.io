{

  "title": "SpringBoot 整合EasyExcel 获取动态Excel列名",
  "date": "2021-04-28",
  "description": "导读 最近负责消息网关，里面有个短信模板导入功能，因为不同模板编号对应不同参数，导入后的数据定时发送，涉及到Excel中列名不固定问题，于是想根据列名+值，组合成一个大JSON，具体代码如下。 引入依赖 Excel监听器 控制器 注：已经组装好动态列名数组，具体业务逻辑，需自行实现 Excel模板 ",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/14715074.html"

}

# 导读

　　最近负责消息网关，里面有个短信模板导入功能，因为不同模板编号对应不同参数，导入后的数据定时发送，涉及到Excel中列名不固定问题，于是想根据列名+值，组合成一个大JSON，具体代码如下。

## 引入依赖

```text
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>easyexcel</artifactId>
            <version>2.2.6</version>
        </dependency>
        <!--fastjson-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.76</version>
        </dependency>
```

## Excel监听器

```text
import com.alibaba.excel.context.AnalysisContext;
import com.alibaba.excel.event.AnalysisEventListener;
import com.alibaba.fastjson.JSON;

import java.util.*;

/**
 * @Description：Excel监听器
 * @Author：chenyanbin
 * @Date：2021/4/28 下午3:36
 * @Versiion：1.0
 */

public class ExcelListener extends AnalysisEventListener<Map<Integer, String>> {
    //Excel数据
    private List<Map<Integer, Map<Integer, String>>> list;
    //Excel列名
    private Map<Integer, String> headTitleMap = new HashMap<>();

    public ExcelListener() {
        list = new ArrayList<>();
    }

    @Override
    public void invoke(Map<Integer, String> data, AnalysisContext context) {
        System.out.println("解析到一条数据：" + JSON.toJSONString(data));
        Map<Integer, Map<Integer, String>> map = new HashMap<>();
        map.put(context.readRowHolder().getRowIndex(), data);
        list.add(map);
    }

    @Override
    public void doAfterAllAnalysed(AnalysisContext context) {
        System.out.println("所有数据解析完成");
    }

    @Override
    public void invokeHeadMap(Map<Integer, String> headMap, AnalysisContext context) {
        headTitleMap = headMap;
    }

    public List<Map<Integer, Map<Integer, String>>> getList() {
        return list;
    }

    public void setList(List<Map<Integer, Map<Integer, String>>> list) {
        this.list = list;
    }

    public Map<Integer, String> getHeadTitleMap() {
        return headTitleMap;
    }

    public void setHeadTitleMap(Map<Integer, String> headTitleMap) {
        this.headTitleMap = headTitleMap;
    }
}
```

## 控制器

　　注：已经组装好动态列名数组，具体业务逻辑，需自行实现

```text
import com.alibaba.excel.EasyExcel;
import com.alibaba.fastjson.JSON;
import com.ybchen.springbooteasyexcel.listener.ExcelListener;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/4/28 下午3:36
 * @Versiion：1.0
 */
@RestController
public class DemoController {
    /**
     * 导入
     *
     * @param file
     * @throws IOException
     */
    @RequestMapping(value = "import")
    public List<Object> importStudentInfos(MultipartFile file) throws IOException {
        ExcelListener studentListener = new ExcelListener();
        EasyExcel.read(file.getInputStream(), studentListener).sheet().doRead();
        List<Map<Integer, Map<Integer, String>>> list = studentListener.getList();
        Map<Integer, String> headTitleMap = studentListener.getHeadTitleMap();
        List<Map<String, String>> mapList = new ArrayList<>();
        for (int i = 0; i < list.size(); i++) {
            Map<Integer, Map<Integer, String>> integerMapMap = list.get(i);
            integerMapMap.forEach((k, l) -> {
                Map<String, String> map = new HashMap<>();
                l.forEach((y, z) -> {
                    map.put(headTitleMap.get(y), z);
                });
                mapList.add(map);
            });
        }
        System.out.println(mapList);
        System.out.println("=============================");
        System.out.println(JSON.toJSONString(mapList));
        return null;
    }
}
```

## Excel模板

![](/imported/posts/2021-04-28-14715074-56528ead-springboot-整合easyexcel-获取动态excel列名/images/img_001_2b0e0701e586.png)

## 演示

![](/imported/posts/2021-04-28-14715074-56528ead-springboot-整合easyexcel-获取动态excel列名/images/img_002_afa8ba3ad2e8.png)
