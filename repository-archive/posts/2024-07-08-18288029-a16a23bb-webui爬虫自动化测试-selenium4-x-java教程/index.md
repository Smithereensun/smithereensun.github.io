{

  "title": "WebUi爬虫自动化测试 Selenium4.X+Java教程",
  "date": "2024-07-08",
  "description": "为什么要学习Selenium 自动化测试 Selenium是最受欢迎的Web应用程序自动化测试工具之一。 通过学习Selenium，可以编写自动化测试脚本，用于自动执行各种任务，例如验证功能、测试用户界面、模拟用户交互 大大提高测试效率，减少手动测试的工作量。 网络爬虫 Selenium可以用于构建",
  "tags": [
    "Java"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/18288029/selenium"

}

# 为什么要学习Selenium

-

自动化测试

  -

Selenium是最受欢迎的Web应用程序自动化测试工具之一。

  -

通过学习Selenium，可以编写自动化测试脚本，用于自动执行各种任务，例如验证功能、测试用户界面、模拟用户交互

  -

大大提高测试效率，减少手动测试的工作量。

-

网络爬虫

  -

Selenium可以用于构建网络爬虫，从网页上提取数据。通过模拟用户的交互行为，如点击按钮、填写表单等

  -

Selenium能够获取页面上动态生成的内容，而且可以处理JavaScript渲染的网页。

  -

这对于需要爬取动态内容的网站很有帮助。

-

自动化操作

  -

Selenium可以用于自动化各种Web应用程序的操作，例如批量提交表单、自动化下载文件、自动化填写信息等。

  -

可以减少重复性的任务，并提高工作效率。

-

官网：[https://www.selenium.dev](https://www.selenium.dev/)

# 环境安装

## 谷歌浏览器版本

![](./images/images/img_001_2e5680b54df5.png)

## 安装驱动

　　注意：大版本号要保持一致，否则可能出现兼容性问题（若找不到响应版本，降浏览器版本号） 

-

[https://registry.npmmirror.com/binary.html?path=chromedriver](https://registry.npmmirror.com/binary.html?path=chromedriver)

-

[https://googlechromelabs.github.io/chrome-for-testing/#stable](https://googlechromelabs.github.io/chrome-for-testing/#stable)

## 下载驱动

![](./images/images/img_002_aedae81b6452.png)

## 创建java工程

![](./images/images/img_003_52d270c7a1fa.gif)

```text
        <!-- Selenium -->
        <dependency>
            <groupId>org.seleniumhq.selenium</groupId>
            <artifactId>selenium-java</artifactId>
            <version>4.10.0</version>
        </dependency>
```

## 编写你的第一个demo

　　需要修改你的驱动路径

```text
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class Main {
    public static void main(String[] args) {

        //指定驱动路径
        System.setProperty("webdriver.chrome.driver","/Users/alex/Desktop/chromedriver-mac-x64/chromedriver");
        // 谷歌驱动
        ChromeOptions options = new ChromeOptions();
        // 允许所有请求
        options.addArguments("--remote-allow-origins=*");

        WebDriver webDriver = new ChromeDriver(options);
        // 启动需要打开的网页
        webDriver.get("https://www.cnblogs.com/chenyanbin");

    }
}
```

![](./images/images/img_004_7cc4d7fe7f59.gif)

# html元素定位实战

## Selenium常见的元素定位方式概述

-

比较常用的是id选择器和xpath选择器

<table> <thead> <tr><th>定位方法</th><th>Java语言实现实例</th></tr> </thead> <tbody> <tr> <td>id 定位</td> <td>driver.findElement(By.id(“id的值”))；</td> </tr> <tr> <td>name定位</td> <td>driver.findElement(By.name(“name的值”))；</td> </tr> <tr> <td>链接的全部文字定位</td> <td>driver.findElement(By.linkText(“链接里面的的全部文字”))；</td> </tr> <tr> <td>链接的部分文字定位</td> <td>driver.findElement(By.partialLinkText(“链接里面的部分文字”))；</td> </tr> <tr> <td>css 方式定位</td> <td>driver.findElement(By.cssSelector(“css表达式”))；</td> </tr> <tr> <td>xpath 方式定位</td> <td>driver.findElement(By.xpath(“xpath表达式”))；</td> </tr> <tr> <td>Class 名称定位</td> <td>driver.findElement(By.className(“class属性”))；</td> </tr> <tr> <td>TagName 标签名称定位</td> <td>driver.findElement(By.tagName(“标签名称”))；</td> </tr> </tbody> </table>

### 拷贝元素的xpath路径

![](./images/images/img_005_b618b0154246.gif)

![](./images/images/img_006_157628901488.png)

## 通过id定位元素

　　案例：搜索当前北京时间

![](./images/images/img_007_b3ca3a17e982.gif)

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

import java.util.concurrent.TimeUnit;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        //指定驱动路径
        System.setProperty("webdriver.chrome.driver","/Users/alex/Desktop/chromedriver-mac-x64/chromedriver");
        // 谷歌驱动
        ChromeOptions options = new ChromeOptions();
        // 允许所有请求
        options.addArguments("--remote-allow-origins=*");

        WebDriver webDriver = new ChromeDriver(options);
        // 启动需要打开的网页
        webDriver.get("https://www.baidu.com/");
        //测试id定位
        idTest(webDriver);

    }

    /**
     * 测试id定位元素
     * @param webDriver
     */
    public static void idTest(WebDriver webDriver) throws InterruptedException {
        //睡眠2秒，让网站元素先加载完成
        TimeUnit.SECONDS.sleep(2);
        //利用ID定位到百度搜索的输入框
        WebElement inputElement = webDriver.findElement(By.id("kw"));
        //输入文字
        inputElement.sendKeys("北京时间");
        //睡眠一会
        TimeUnit.MILLISECONDS.sleep(500);
        //点击搜索功能
        WebElement searchElement = webDriver.findElement(By.id("su"));
        searchElement.click();
    }
}
```

案例代码

## 通过xpath定位

-

XPath（XML Path Language）是一种在XML文档中查找信息的语言，也可以用于HTML

-

XPath提供了非常强大的定位能力，可以定位到几乎任何元素。

-

语法案例（更多语法搜索博文资料 [https://www.w3school.com.cn/xpath/index.asp](https://www.w3school.com.cn/xpath/index.asp)）

<table> <thead> <tr><th>表达式</th><th>描述</th><th>实例</th><th>案例说明</th></tr> </thead> <tbody> <tr> <td>nodename</td> <td>选取nodename节点的所有子节点</td> <td>xpath(‘//div’)</td> <td>选取了div节点的所有子节点</td> </tr> <tr> <td>/</td> <td>从根节点选取</td> <td>xpath(‘/div’)</td> <td>从根节点上选取div节点</td> </tr> <tr> <td>//</td> <td>选取所有的当前节点，不考虑他们的位置</td> <td>xpath(‘//div’)</td> <td>选取所有的div节点</td> </tr> <tr> <td>.</td> <td>选取当前节点</td> <td>xpath(‘./div’)</td> <td>选取当前节点下的div节点</td> </tr> <tr> <td>..</td> <td>选取当前节点的父节点</td> <td>xpath(‘..’)</td> <td>回到上一个节点</td> </tr> <tr> <td>@</td> <td>选取属性</td> <td>xpath（’//@class’）</td> <td>选取所有的class属性</td> </tr> </tbody> </table>

-

HTML文档本身就是一个标准的XML页面，可以使用Xpath 的用法来定位页面元素

-

有两种路径定位方式

  -

绝对路径

    -

以 "/" 开头， 让xpath 从文档的根节点开始解析

    -

如果页面结构发生改变，改路径也随之失效，必须重新配置

  -

相对路径

    -

以"//" 开头， 让xpath 从文档的任何元素节点开始解析

    -

推荐采用这个方式，结合适合的元素，则通用性更好

-

**注意事项**

  -

webdriver会将整个页面的元素扫描定位所需要的元素，如果大量使用xpath做元素定位的话， 脚本的执行速度可能会稍慢

![](./images/images/img_010_d29eefb8b23f.gif)

```text
    public static void main(String[] args) throws InterruptedException {
        //指定驱动路径
        System.setProperty("webdriver.chrome.driver","/Users/alex/Desktop/chromedriver-mac-x64/chromedriver");
        // 谷歌驱动
        ChromeOptions options = new ChromeOptions();
        // 允许所有请求
        options.addArguments("--remote-allow-origins=*");

        WebDriver webDriver = new ChromeDriver(options);
        // 启动需要打开的网页
        webDriver.get("https://www.baidu.com/");
        //测试id定位
//        idTest(webDriver);

        xpathTest(webDriver);

    }

    /**
     * 通过xpath定位元素
     * @param webDriver
     * @throws InterruptedException
     */
    public static void xpathTest(WebDriver webDriver) throws InterruptedException {
        //睡眠2秒，让网站元素先加载完成
        TimeUnit.SECONDS.sleep(2);
        //利用ID定位到百度搜索的输入框
        WebElement inputElement = webDriver.findElement(By.xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input"));
        //输入文字
        inputElement.sendKeys("北京时间");
        //睡眠一会
        TimeUnit.MILLISECONDS.sleep(500);
        //点击搜索功能
        WebElement searchElement = webDriver.findElement(By.xpath("/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input"));
        searchElement.click();
    }
```

# 基础知识

## **什么是WebDriver**

-

Selenium WebDriver是一个浏览器自动化框架，允许执行Web应用程序上的操作，就如同一个真实用户一样。

-

在Selenium 4.x版本中，WebDriver API提供了一系列与浏览器进行交互的方法，常见API如下

<table> <thead> <tr><th>方法</th><th>描述</th></tr> </thead> <tbody> <tr> <td>get(String url）</td> <td>访问目标 url 地址，打开网页</td> </tr> <tr> <td>getCurrentUrl()</td> <td>获取当前页面 url 地址</td> </tr> <tr> <td>getTitle()</td> <td>获取页面标题</td> </tr> <tr> <td>getPageSource()</td> <td>获取页面源代码</td> </tr> <tr> <td>close()</td> <td>关闭浏览器当前打开的窗口</td> </tr> <tr> <td>quit()</td> <td>关闭浏览器所有的窗口</td> </tr> <tr> <td>findElement(by)</td> <td>查找单个元素</td> </tr> <tr> <td>findElements(by)</td> <td>查到元素列表，返回一个集合</td> </tr> <tr> <td>getWindowHandle()</td> <td>获取当前窗口句柄</td> </tr> <tr> <td>getWindowHandles()</td> <td>获取所有窗口的句柄</td> </tr> </tbody> </table>

```text
    public static void main(String[] args) throws InterruptedException {
        //指定驱动路径
        System.setProperty("webdriver.chrome.driver","/Users/alex/Desktop/chromedriver-mac-x64/chromedriver");
        // 谷歌驱动
        ChromeOptions options = new ChromeOptions();
        // 允许所有请求
        options.addArguments("--remote-allow-origins=*");

        WebDriver webDriver = new ChromeDriver(options);
        // 启动需要打开的网页
//        webDriver.get("https://www.baidu.com/");
        //测试id定位
//        idTest(webDriver);

//        xpathTest(webDriver);

        webdriverTest(webDriver);
    }

    public static void webdriverTest(WebDriver webDriver) throws InterruptedException{
        //访问目标 url 地址，打开网页
        webDriver.get("https://www.baidu.com/");
        //getCurrentUrl() 方法获取当前页面的 url 地址
        String currentUrl = webDriver.getCurrentUrl();
        System.out.println("当前页面的 url 地址是：" + currentUrl);

        //getTitle() 方法获取当前页面的标题
        String title = webDriver.getTitle();
        System.out.println("当前页面的标题是：" + title);

        //getPageSource() 方法获取当前页面的源码
        String pageSource = webDriver.getPageSource();
        System.out.println("当前页面的源码是：" + pageSource);

        //通过 id 定位元素，并输入搜索关键词
        webDriver.findElement(By.id("kw")).sendKeys("北京时间");

        //findElements() 方法返回所有匹配的元素
//        webDriver.findElements(By.id("kw")).get(0).sendKeys("北京时间");

        String windowHandle = webDriver.getWindowHandle();
        System.out.println("当前窗口句柄是：" + windowHandle);
        Set<String> windowHandles = webDriver.getWindowHandles();
        for (String wh : windowHandles) {
            System.out.println("当前窗口句柄是：" + wh);
        }

        TimeUnit.SECONDS.sleep(5);
        //close() 方法关闭当前页面
        webDriver.close();

        //quit() 方法关闭所有浏览器
//        webDriver.quit();
    }
```

## 什么是WebElement对象

-

`WebElement` 是 Selenium WebDriver API 中的一个核心接口，

-

代表了DOM（Document Object Model）树中的一个HTML元素。

-

通过 `WebElement` 对象，可以与页面上的元素进行交互，例如点击按钮、输入文本、选择选项、检查元素的属性或状态等。

-

通常会通过 WebDriver 的 `find_element_by_*` 或 `find_elements_by_*` 方法来定位页面上的元素，获取 `WebElement` 对象。

-

这些方法会返回一个或多个 `WebElement` 对象，对象代表了与给定选择器匹配的DOM元素。

<table> <thead> <tr><th>方法</th><th>说明</th></tr> </thead> <tbody> <tr> <td>click</td> <td>点击对象</td> </tr> <tr> <td>sendKeys</td> <td>在对象上模拟按键输入</td> </tr> <tr> <td>clear</td> <td>清除对象输入的文本内容</td> </tr> <tr> <td>submit</td> <td>提交,比如表单对象</td> </tr> <tr> <td>getAttribute</td> <td>获取元素的指定属性</td> </tr> <tr> <td>getText</td> <td>用于获取元素的文本信息</td> </tr> </tbody> </table>

```text
    public static void main(String[] args) throws InterruptedException {
        //指定驱动路径
        System.setProperty("webdriver.chrome.driver","/Users/alex/Desktop/chromedriver-mac-x64/chromedriver");
        // 谷歌驱动
        ChromeOptions options = new ChromeOptions();
        // 允许所有请求
        options.addArguments("--remote-allow-origins=*");

        WebDriver webDriver = new ChromeDriver(options);
        // 启动需要打开的网页
//        webDriver.get("https://www.baidu.com/");
        //测试id定位
//        idTest(webDriver);

//        xpathTest(webDriver);

//        webdriverTest(webDriver);

        webEleTest(webDriver);
    }

    public static void webEleTest(WebDriver webDriver)throws InterruptedException {
        //启动需要打开的网页
        webDriver.get("https://www.baidu.com");
        String title = webDriver.getTitle();
        String currentUrl = webDriver.getCurrentUrl();
        System.out.println("title="+title+",currentUrl="+currentUrl);

        TimeUnit.SECONDS.sleep(2);

        //输入元素 sendKey
        webDriver.findElement(By.id("kw")).sendKeys("华为手机");
        TimeUnit.SECONDS.sleep(2);

        //清除元素  clear
        webDriver.findElement(By.id("kw")).clear();

        TimeUnit.SECONDS.sleep(2);
        webDriver.findElement(By.id("kw")).sendKeys("苹果手机");

        //点击元素  click
        webDriver.findElement(By.id("su")).click();
        TimeUnit.SECONDS.sleep(2);

        webDriver.findElement(By.id("kw")).clear();
        webDriver.findElement(By.id("kw")).sendKeys("苹果手机最新款");
        //提交元素  submit
        webDriver.findElement(By.id("su")).submit();
        String text = webDriver.findElement(By.id("su")).getAttribute("value");
        System.out.println("text======"+text);
    }
```

## **自动化操作里面的浏览器API案例实战**

-

需求

  -

浏览器操作网页，有前进、后退，不同网页直接切换，窗口最大化、刷新等

  -

通过Selenium的api完成上述的操作案例

<table> <thead> <tr><th>方法</th><th>说明</th></tr> </thead> <tbody> <tr> <td>back</td> <td>模拟浏览器后退按钮</td> </tr> <tr> <td>forward</td> <td>模拟浏览器前进按钮</td> </tr> <tr> <td>refresh</td> <td>刷新页面（F5）</td> </tr> <tr> <td>maximize</td> <td>浏览器最大化</td> </tr> <tr> <td>setSize</td> <td>浏览器宽高</td> </tr> <tr> <td>manage( ).window( ).setSize( )</td> <td>设置浏览器的大小</td> </tr> </tbody> </table>

```text
    public static void main(String[] args) throws InterruptedException {
        //指定驱动路径
        System.setProperty("webdriver.chrome.driver","/Users/alex/Desktop/chromedriver-mac-x64/chromedriver");
        // 谷歌驱动
        ChromeOptions options = new ChromeOptions();
        // 允许所有请求
        options.addArguments("--remote-allow-origins=*");

        WebDriver webDriver = new ChromeDriver(options);
        // 启动需要打开的网页
//        webDriver.get("https://www.baidu.com/");
        //测试id定位
//        idTest(webDriver);

//        xpathTest(webDriver);

//        webdriverTest(webDriver);

//        webEleTest(webDriver);

        browserTest(webDriver);
    }

    public static void browserTest(WebDriver webDriver)throws InterruptedException {
        //启动需要打开的网页
        webDriver.get("https://www.baidu.com");
        TimeUnit.SECONDS.sleep(2);
        //输入
        webDriver.findElement(By.id("kw")).sendKeys("北京时间");
        TimeUnit.SECONDS.sleep(2);
        //点击搜索
        webDriver.findElement(By.id("su")).click();
        //浏览器刷新
        TimeUnit.SECONDS.sleep(2);
        webDriver.navigate().refresh();
        //浏览器后退一步
        TimeUnit.SECONDS.sleep(2);
        //加个休眠时间
        webDriver.navigate().back();

        //浏览器前进
        TimeUnit.SECONDS.sleep(2);
        webDriver.navigate().forward();
        TimeUnit.SECONDS.sleep(2);

        //浏览器窗口按照指定大小来显示
        webDriver.manage().window().setSize(new Dimension(300,300));
        TimeUnit.SECONDS.sleep(2);
        //浏览器全屏
        webDriver.manage().window().fullscreen();
    }
```

## Selenium的鼠标事件

-

鼠标操作主要是通过`Actions`类来实现的，该类提供了一系列模拟鼠标操作的方法

-

包括有 右击、双击、悬停、拖动等

<table> <thead> <tr><th>方法</th><th>说明</th></tr> </thead> <tbody> <tr> <td>contextClick( )</td> <td>右击</td> </tr> <tr> <td>clickAndHold( )</td> <td>鼠标点击并控制</td> </tr> <tr> <td>doubleClick( )</td> <td>双击</td> </tr> <tr> <td>dragAndDrop( )</td> <td>拖动</td> </tr> <tr> <td>release( )</td> <td>释放鼠标</td> </tr> <tr> <td>perform( )</td> <td>执行所有Actions中存储的行为</td> </tr> </tbody> </table>

-

单击操作

```text
WebElement element = driver.findElement(By.id("element_id")); // 替换为你要单击的元素的ID
element.click(); // 或者使用 Actions 实现单击

// 使用 ActionChains
Actions actions = new Actions(driver);
actions.click(element).perform();
```

-

双击操作

```text
WebElement element = driver.findElement(By.id("element_id")); // 替换为你要双击的元素的ID
new Actions(driver).doubleClick(element).perform();
```

-

右键操作

```text
WebElement element = driver.findElement(By.id("element_id")); // 替换为你要右击的元素的ID
new Actions(driver).contextClick(element).perform();
```

-

悬停操作

```text
WebElement element = driver.findElement(By.id("element_id")); // 替换为你要悬停的元素的ID
new Actions(driver).moveToElement(element).perform();
```

-

拖拽操作

```text
WebElement sourceElement = driver.findElement(By.id("source_id")); // 源元素ID
WebElement targetElement = driver.findElement(By.id("target_id")); // 目标元素ID
new Actions(driver).dragAndDrop(sourceElement, targetElement).perform();
```

```text
    public static void main(String[] args) throws InterruptedException {
        //指定驱动路径
        System.setProperty("webdriver.chrome.driver", "/Users/alex/Desktop/chromedriver-mac-x64/chromedriver");
        // 谷歌驱动
        ChromeOptions options = new ChromeOptions();
        // 允许所有请求
        options.addArguments("--remote-allow-origins=*");

        WebDriver webDriver = new ChromeDriver(options);
        // 启动需要打开的网页
//        webDriver.get("https://www.baidu.com/");
        //测试id定位
//        idTest(webDriver);

//        xpathTest(webDriver);

//        webdriverTest(webDriver);

//        webEleTest(webDriver);

//        browserTest(webDriver);

        mouseTest(webDriver);
    }

    public static void mouseTest(WebDriver webDriver) throws InterruptedException {
        //启动需要打开的网页
        webDriver.get("https://www.baidu.com");
        TimeUnit.SECONDS.sleep(2);
        //输入
        webDriver.findElement(By.id("kw")).sendKeys("北京时间");
        TimeUnit.SECONDS.sleep(2);
        //点击搜索
        webDriver.findElement(By.id("su")).click();
        TimeUnit.SECONDS.sleep(3);
        //右键操作
        WebElement element = webDriver.findElement(By.cssSelector("#s_tab > div > a.s-tab-item.s-tab-item_1CwH-.s-tab-wenku_GwhrW.s-tab-wenku"));
        new Actions(webDriver).contextClick(element).perform();
    }
```

## **模拟键盘操作**

-

利用`Actions`和`Keys`类来模拟键盘操作，包括文本输入、按键和组合键序列，增强自动化脚本的用户交互能力

-

`Keys`枚举提供了方便的表示键盘上按键的方法，而`Actions`类则用于构建复杂的交互序列。

-

这两者结合，允许在Web自动测试中模拟几乎任何类型的键盘操作。

-

键盘操作示例

  -

发送普通文本

    -

可以使用`WebElement`的`sendKeys()`方法来向页面元素发送普通文本。

    -

例如，向一个输入框发送文本“Hello, Selenium!”：

```text
WebElement inputBox = driver.findElement(By.id("inputBoxId"));
inputBox.sendKeys("Hello, Selenium!");
```

-

  - 发送特殊字符

    -

sendKeys 使用`Keys`类中的常量，可以发送特殊字符或按键事件，sendKeys接收可变参数　　　　

```text
sendKeys(Keys.BACK_SPACE) 回格键（BackSpace）、sendKeys(Keys.SPACE) 空格键 (Space)
sendKeys(Keys.TAB) 制表键 (Tab)、sendKeys(Keys.ESCAPE) 回退键（Esc）
sendKeys(Keys.ENTER) 回车键（Enter）、sendKeys(Keys.F1) 键盘 F1
sendKeys(Keys.CONTROL,'a') 全选（Ctrl+A）、sendKeys(Keys.CONTROL,'c') 复制（Ctrl+C）
sendKeys(Keys.CONTROL,'x') 剪切（Ctrl+X）、sendKeys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
```

-

  -

例如，发送回车键：

```text
WebElement button = driver.findElement(By.id("buttonId"));
button.sendKeys(Keys.ENTER);
```

-

  - 模拟组合键操作　　

    -

Selenium还支持模拟组合键操作，如Ctrl+C、Alt+F4等。　　　　

    -

这需要使用`Actions`类来构建一系列动作，并通过`perform()`方法执行。　　　　

```text
Actions action = new Actions(driver);
action.keyDown(Keys.CONTROL);  //按下 Ctrl 键
action.keyUp(Keys.CONTROL);  //释放 Ctrl 键
```

-

  -

    -

使用快捷键Ctrl+Alt+a，可以通过下面语句来实现：　　　　

```text
Actions action = new Actions(driver);
action.keyDown(Keys.CONTROL).keyDown(Keys.ALT)
.sendKeys(“a”).keyUp(Keys.CONTROL).keyUp(Keys.ALT).perform();
```

-

  -

    -

keyDown(Key)方法的调用，如没有接着调用keyUp(Key)或者sendKeys(Keys.NULL) 来释放，按键将一样保持按住状态

```text
    public static void main(String[] args) throws InterruptedException {
        //指定驱动路径
        System.setProperty("webdriver.chrome.driver", "/Users/alex/Desktop/chromedriver-mac-x64/chromedriver");
        // 谷歌驱动
        ChromeOptions options = new ChromeOptions();
        // 允许所有请求
        options.addArguments("--remote-allow-origins=*");

        WebDriver webDriver = new ChromeDriver(options);
        // 启动需要打开的网页
//        webDriver.get("https://www.baidu.com/");
        //测试id定位
//        idTest(webDriver);

//        xpathTest(webDriver);

//        webdriverTest(webDriver);

//        webEleTest(webDriver);

//        browserTest(webDriver);

//        mouseTest(webDriver);

        keyboardTest(webDriver);
    }

    public static void keyboardTest(WebDriver webDriver) throws InterruptedException {
        //启动需要打开的网页
        webDriver.get("https://www.baidu.com");
        TimeUnit.SECONDS.sleep(2);
        //输入
        WebElement kw = webDriver.findElement(By.id("kw"));
        kw.sendKeys("北京时间");
        TimeUnit.SECONDS.sleep(2);
        //删除一个字符
        kw.sendKeys(Keys.BACK_SPACE);
        kw.sendKeys(Keys.BACK_SPACE);
        TimeUnit.SECONDS.sleep(2);
        kw.sendKeys("故宫");
        //点击搜索
        webDriver.findElement(By.id("su")).click();
        TimeUnit.SECONDS.sleep(3);
    }
```

-

注意事项

  -

在发送键盘操作之前，请确保目标元素是可交互的（即可见且可点击）。

  -

如果元素在发送键盘操作之前处于隐藏或不可交互状态，可能会导致测试失败。

  -

在使用组合键时，请注意按键的顺序和释放的顺序，如果顺序不正确，可能会导致测试行为不符合预期。

- 不同操作系统的键盘说明

```text
windows:
send_keys(Keys.CONTROL, ‘a’) 方法用于全选文本，
send_keys(Keys.CONTROL, ‘c’) 方法用于复制文本，
send_keys(Keys.CONTROL, ‘x’) 方法用于剪切文本，
send_keys(Keys.CONTROL, ‘v’) 方法用于粘贴文本。
mac:
send_keys(Keys.COMMAND, ‘a’) 方法用于全选文本，
send_keys(Keys.COMMAND, ‘c’) 方法用于复制文本，
send_keys(Keys.COMMAND, ‘x’) 方法用于剪切文本，
send_keys(Keys.COMMAND, ‘v’) 方法用于粘贴文本。
```

## 显示等待和隐式等待

-

Web应用通常通过异步加载（如Ajax）来动态更新页面内容，页面元素可能不是立即可用的。

-

当自动化测试脚本尝试访问或操作这些元素时，如果没有等待机制，可能会遇到定位失败、元素状态不正确等异常

-

Selenium4等待主要解决以下问题：

  -

**元素加载延迟**

    -

当页面上的某些元素是通过异步请求（如Ajax）加载的，这些元素可能不会立即出现在DOM中。

    -

网络波动或服务器响应延迟，页面上的某些内容可能需要一些时间才能加载。

    -

如果没有等待机制，测试脚本可能会在元素实际可用之前访问它，导致定位失败。

  -

**依赖关系**：

    -

测试脚本中的操作可能依赖于前一步的结果或内容。

    -

例如，一个表单提交后，可能需要等待新页面加载完成才能继续执行后续操作。

  -

**页面更新**：

    -

JavaScript可能会动态更改页面内容，如添加、删除或修改元素。

    -

如果没有等待，测试脚本可能会错过这些变化，导致测试失败。

-

Selenium 等待元素出现的方式有以下三种

  -

**强制等待**

    -

即线程休眠，在代码中强制当前正在执行的线程休眠（暂停执行）不管元素有没出现都固定时间

    -

前面案例操作中已经多次使用 `TimeUnit.SECONDS.sleep(2);`

  -

**显式等待(Explicit Wait)**

    -

通俗说就是死等，不灵活的等待，在指定的时间内一定要等到某个元素的出现或可操作的状态

    -

如果等不到,就一直等,直到在规定的时间之内都要操作的元素仍没找到,就抛出异常

    -

可以针对特定的元素或一组元素进行等待，提供了更灵活的等待机制，可以等待复杂的条件。

  -

**隐式等待 (Implicit Wait)**

    -

设置**全局等待时间，全部查找都会生效**，驱动初始化后就可以配置，在指定时间内轮询DOM，直到找到元素或超时。

    -

一旦设置，在整个WebDriver对象实例的生命周期内都有效。

    -

适用于等待整个页面加载完毕。

```text
    public static void main(String[] args) throws InterruptedException {
        //指定驱动路径
        System.setProperty("webdriver.chrome.driver", "/Users/alex/Desktop/chromedriver-mac-x64/chromedriver");
        // 谷歌驱动
        ChromeOptions options = new ChromeOptions();
        // 允许所有请求
        options.addArguments("--remote-allow-origins=*");

        WebDriver webDriver = new ChromeDriver(options);
        // 启动需要打开的网页
//        webDriver.get("https://www.baidu.com/");
        //测试id定位
//        idTest(webDriver);

//        xpathTest(webDriver);

//        webdriverTest(webDriver);

//        webEleTest(webDriver);

//        browserTest(webDriver);

//        mouseTest(webDriver);

//        keyboardTest(webDriver);

        waitTest(webDriver);
    }

    public static void waitTest(WebDriver webDriver)throws InterruptedException {
        //启动需要打开的网页
        webDriver.get("https://www.baidu.com");

        // >>>>>>>方式一
//        // 创建显式等待对象，设置最大等待时间为10秒
//        WebDriverWait wait = new WebDriverWait(webDriver, Duration.ofSeconds(5));
//        // 使用ExpectedConditions定义等待条件，例如元素可见性
//        wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("kw")));

        // >>>>>>>方式二
        //隐式等待,可以用一个不存在的元素位置进行测试
        webDriver.manage().timeouts().implicitlyWait(Duration.ofSeconds(5));

        //输入元素 sendKey
        webDriver.findElement(By.id("kw")).sendKeys("北京时间");

        //提交元素  submit
        webDriver.findElement(By.id("su")).submit();
        String text = webDriver.findElement(By.id("su")).getAttribute("value");
        System.out.println("text======"+text);
    }
```

# 谷歌插件【重要】

　　实际工作中，可以使用谷歌一款录屏插件，直接稍微修改下代码即可使用自动化操作

　　插件名称：**Selenium IDE**

![](./images/images/img_011_f72f1a024585.png)

## 示例 

### 录制脚本

![](./images/images/img_012_3cbc1906bb28.gif)

### 导出java自动化脚本

![](./images/images/img_013_fae60e76832b.gif)

```text
// 指定驱动

    //指定驱动路径
    System.setProperty("webdriver.chrome.driver", "/Users/alex/Desktop/chromedriver-mac-x64/chromedriver");
    // 谷歌驱动
    ChromeOptions options = new ChromeOptions();
    // 允许所有请求
    options.addArguments("--remote-allow-origins=*");

    driver = new ChromeDriver(options);
```
