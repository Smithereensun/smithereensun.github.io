{

  "title": "整合Minio - 实现文件切片极速上传",
  "has_date": true,
  "description": "概述 官网地址：https://min.io/ 文档地址：https://docs.min.io/ Minio是一款开源的对象存储服务器，它可以运行在多种操作系统上，包括Linux、Windows和MacOS等。它提供了一种简单、可扩展、高可用的对象存储解决方案，支持多种数据格式，包括对象、块和文件",
  "tags": [
    "框架",
    "Spring Boot"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/springboot/minio-springboot - 整合Minio - 实现文件切片极速上传.md",
  "date": "2026-02-28"

}

## [概述](#概述)

官网地址：[https://min.io/](https://min.io/)

文档地址：[https://docs.min.io/](https://docs.min.io/)

Minio是一款开源的对象存储服务器，它可以运行在多种操作系统上，包括Linux、Windows和MacOS等。它提供了一种简单、可扩展、高可用的对象存储解决方案，支持多种数据格式，包括对象、块和文件等。

以下是Minio的主要特点：

- 简单易用： Minio的安装和配置非常简单，只需要下载并运行相应的二进制文件即可。它提供了一个Web UI,可以通过界面管理存储桶和对象。

- 可扩展性： Minio可以轻松地扩展到多个节点，以提供高可用性和容错能力。它支持多种部署模式，包括单节点、主从复制和集群等。

- 高可用性： Minio提供了多种机制来保证数据的可靠性和可用性，包括冗余备份、数据复制和故障转移等。

- 安全性： Minio提供了多种安全机制来保护数据的机密性和完整性，包括SSL/TLS加密、访问控制和数据加密等。

- 多语言支持： Minio支持多种编程语言，包括Java、Python、Ruby和Go等。

- 社区支持： Minio是一个开源项目，拥有庞大的社区支持和贡献者。它的源代码可以在GitHub上获得，并且有一个活跃的邮件列表和论坛。

- 对象存储： Minio的核心功能是对象存储。它允许用户上传和下载任意数量和大小的对象，并提供了多种API和SDK来访问这些对象。

- 块存储： Minio还支持块存储，允许用户上传和下载大型文件(例如图像或视频)。块存储是一种快速、高效的方式来处理大型文件。

- 文件存储： Minio还支持文件存储，允许用户上传和下载单个文件。文件存储是一种简单、快速的方式来处理小型文件。

总之，Minio是一款强大、灵活、可扩展的对象存储服务器，适用于各种应用场景，包括云存储、大数据存储和物联网等。

## [应用场景](#应用场景)

MinIO是一种高性能、扩展性好的对象存储系统，它可以适用于许多应用场景，其中包括但不限于以下几种：

- 大规模数据存储： 由于MinIO使用分布式环境来存储数据，因此可以轻松扩展以满足需要管理大量数据的组织和企业的需求。

- 图像和媒体存储： 由于MinIO对原始二进制数据进行了优化，因此非常适合存储图像、音频和视频等媒体文件。它还支持WebP、JPEG和PNG等格式，可在多种设备和浏览器上工作。

- 云原生应用程序： MinIO是一个云原生的对象存储系统，可以与Kubernetes、Docker Swarm和Mesosphere等容器编排工具无缝集成，可以很好地满足基于云的应用程序的需求。

- 数据保护和灾难恢复： MinIO的多副本写入功能和内置的纠删码支持，使得数据备份和恢复变得简单而强大。

- 分布式计算和机器学习： MinIO提供STS（S3 Select）和HDFS接口，支持在数据仓库中直接运行SQL查询和MapReduce等并行处理框架。这使得它成为用于Big Data、AI和ML等分布式计算任务的理想选择。

需要注意的是，以上列出的应用场景并不是MinIO所有可适用的场景。具体取决于每个使用情况的细节和需求。

## [Minio实现分片上传的主要步骤](#minio实现分片上传的主要步骤)

使用SpringBoot和MinIO实现分片上传、秒传、续传主要包含以下几个步骤：

- 前端选择文件并对其进行切割： 可以使用JavaScript等前端技术将文件切成多个片段，并为每个片段生成唯一标识。

- 将每个分片上传到MinIO对象存储： 调用MinIO的Java SDK将每个分片上传到MinIO中，每个分片的KEY名称包含基础名称和片段ID。

- 将所有分片合并成最终文件： 在前端完成所有分片的上传之后，在后台开发一个接口，按照唯一标识将所有分片合并成最终文件。合并过程可以在应用服务器上完成，也可以使用MinIO Object Storage本身的合并功能完成。

- 实现秒传： 在前端上传分片之前，通过请求后台接口来根据文件名称和文件MD5值判断该文件是否已经存在，如果存在则可以直接返回文件URL，即可实现秒传。

- 实现续传： 在前端上传分片时出现了网络问题或客户端故障导致文件上传被中断，这时候只需记录已上传的分片序列号和状态标志，从下一个分片重新开始上传即可。

- 处理错误和异常： 在文件上传过程中可能会遇到各种问题，比如服务故障、网络中断、客户端处理超时等。因此需要加入错误和异常处理，保证整个上传过程顺利进行。

总体而言，使用SpringBoot和MinIO实现分片上传、秒传、续传的难度不算大，可以根据上述步骤进行开发和实现。

## [SpringBoot整合](#springboot整合)

### [引入依赖](#引入依赖)

### [创建容器桶](#创建容器桶)
![](/imported/markdown/2026-02-28-markdown-29d35f81-整合minio-实现文件切片极速上传/images/f960882b7125-202406301042156.webp)![](/imported/markdown/2026-02-28-markdown-29d35f81-整合minio-实现文件切片极速上传/images/609cc3c3b00b-202406301042182.webp)
### [获取API访问凭证](#获取api访问凭证)
![](/imported/markdown/2026-02-28-markdown-29d35f81-整合minio-实现文件切片极速上传/images/ba4c4b015d2f-202406301042197.webp)![](/imported/markdown/2026-02-28-markdown-29d35f81-整合minio-实现文件切片极速上传/images/ba119e72d6e7-202406301042149.webp)
### [编写配置文件](#编写配置文件)

首先是服务器的配置：

- 端口号为8080,用于监听请求。

- 使用了一个Servlet来处理`multipart/form-data`类型的请求。

- 在接收到`multipart/form-data`类型的请求时，会将上传的文件大小限制在10MB以内，并将请求大小限制在10MB以内。

接下来是minio的配置：

- `access-key`和`secret-key`是访问minio服务的凭证，需要根据实际情况进行填写。

- url是minio服务的地址，需要根据实际情况进行填写。

- `bucket-name`是存储文件的桶名，需要根据实际情况进行填写。

### [http请求状态](#http请求状态)

### [通用常量信息](#通用常量信息)

### [创建Minio的配置类](#创建minio的配置类)

这段代码是Java中的一个配置类，用于配置与MinIO(一个对象存储服务)相关的属性。具体来说：

- `@Configuration`注解表示这是一个配置类，用于将该类中定义的属性注入到其他组件中使用。

- `@ConfigurationProperties`注解表示该类使用了`spring.minio.*`前缀的属性来配置Minio相关的属性。

- `@Data`注解表示自动生成getter和setter方法，简化了代码编写。

- `accessKey`和`secretKey`属性分别表示访问密钥和密钥值，用于连接到MinIO服务。

- url属性表示MinIO服务的URL地址。

- `bucketName`属性表示存储桶名称。

- `@Bean`注解表示将`minioClient()`方法返回的对象注册为bean,以便在其他组件中使用。

- `minioClient()`方法返回了一个`MinioClient`对象，用于连接到MinIO服务并操作存储桶。其中，`endpoint()`方法用于设置MinIO服务的URL地址，`credentials()`方法用于设置访问密钥和密钥值。

### [创建Minio的工具类](#创建minio的工具类)

该代码是一个工具类，用于使用阿里云的对象存储服务(OSS)进行文件上传和下载。具体功能如下：

- `getPolicy(String fileName, ZonedDateTime time)`：根据文件名和时间戳获取上传临时签名。

- `getPolicyUrl(String objectName, Method method, int time, TimeUnit timeUnit)`：获取上传文件的url。

- `upload(MultipartFile file, String fileName)`：将文件上传到OSS中。

- `getUrl(String objectName, int time, TimeUnit timeUnit)`：获取文件的下载url。

代码中使用了枚举类型来定义不同的上传和下载方法。

使用了注解`@Autowired`来自动注入`MinioClient`对象。

该工具类没有提供异常处理机制，需要根据实际情况进行补充。

### [创建Ajax请求工具类](#创建ajax请求工具类)

### [创建Minio文件操作接口层](#创建minio文件操作接口层)
