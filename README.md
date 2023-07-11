# Scary

## 工作流

<img src="https://nunbey-bill.oss-cn-beijing.aliyuncs.com/2020-weekReport/image-20230710105134236.png" alt="image-20230710105134236" style="zoom:50%;" />

## 下载

```shell
scrapy startproject 项目名
```



### 生成爬虫

```shell
scrapy genspider 文件名 域名范围
```

## 运行相应的scrapy

```
cd 对应的爬虫
scrapy crawl 对应的爬虫
```

## 部署

```shel
scrapyd-deploy 部署名(配置文件中设置的名称) -p 项目名称
```

scrapyd-delop run -p movie
