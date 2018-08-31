# 集成音乐播放器使用说明

* [集成音乐播放器简介](#集成音乐播放器简介)
* [使用说明](#使用说明)
  * [解压](#解压)
  * [运行](#运行)
  * [安装方法](#安装方法)
* [运行效果图展示](#运行效果图展示)
* [spider.py](#spiderpy)
  * [spider简介](#spider简介)
  * [初始化的成员](#初始化的成员)
  * [需要重载的方法](#需要重载的方法)
* [distspider.py](#distspiderpy)
  * [spider简介](#spider简介)
* [multiworker.py](#multiworkerpy)
  * [multiworker简介](#multiworker简介)
* [insertmysql.py](#insertmysqlpy)
  * [insertmysql简介](#insertmysql简介)
* [parser.py](#parserpy)
  * [parser简介](#parser简介)
* [download.py](#downloadpy)
  * [download简介](#download简介)
* [color.py](#colorpy)
  * [color简介](#color简介)
* [反馈与建议](#反馈与建议)

# 集成音乐播放器简介

```
 ___       _                       _           _ 
|_ _|_ __ | |_ ___  __ _ _ __ __ _| |_ ___  __| |
 | || '_ \| __/ _ \/ _` | '__/ _` | __/ _ \/ _` |
 | || | | | ||  __/ (_| | | | (_| | ||  __/ (_| |
|___|_| |_|\__\___|\__, |_|  \__,_|\__\___|\__,_|
                   |___/ 
                     _              _                       
 _ __ ___  _   _ ___(_) ___   _ __ | | __ _ _   _  ___ _ __ 
| '_ ` _ \| | | / __| |/ __| | '_ \| |/ _` | | | |/ _ \ '__|
| | | | | | |_| \__ \ | (__  | |_) | | (_| | |_| |  __/ |   
|_| |_| |_|\__,_|___/_|\___| | .__/|_|\__,_|\__, |\___|_|   
Author: doupeng              |_|            |___/                              
                                     
                                     
1.支持网易云，QQ，虾米，酷狗，百度五大音乐网站的音乐搜索，下载，和外链。
2.各大音乐榜单，在线播放界面清爽。
3.搭建本地服务，在局域网内手机，电脑均可使用。
```

# 使用说明

### 解压

* 解压到自己想要放在的**目录**下，推荐放在D盘目录下 `D:\phpwamp_Pack`
* 双击`PHPWAMP_Pack.exe`，在底部托盘中找到图标后右键选择启动服务。如果遇到360等软件的阻碍，请选择允许访问，启动成功后，再次右键，选择打开网站，即可使用了，如果你的电脑默认的浏览器是IE，建议复制链接，或直接打开谷歌浏览器，或360浏览器，输入`localhost:8066` 或 `127.0.0.1:8066`来使用。
* 如何使用手机访问此服务，双击目录下的`get_ip.bat`，你会看到下图所示，例如我的局域网的IP就是`172.18.2.164`，因此在手机浏览器中打开`http://172.18.2.164:8066`即可，期间电脑要处于开机状态。

### 运行

* **`redis`数据库 `windows`版**
 * [redis-64bit.zip](http://pan.baidu.com/s/1pLrVxN1)
 * [redis-32bit.zip](http://pan.baidu.com/s/1pL6O5Vt)
* **`mysql`数据库 `windows`版 点击[这里](http://dev.mysql.com/downloads/installer)进入官网下载**

#### 安装方法

```markdown
1.python setup.py install
2.pip install dpspider-x.x.x.tar.gz ( win | linux | macOS )
3.dpspider-x.x.x.win-amd64.exe ( windows可执行文件，双击安装) 
```

* `xxx.tar.gz` 最新版本
 * [dpspider-2.1.12.tar.gz](http://pan.baidu.com/s/1jI3CHCy)
* `xxx.exe` 最新版本
 * [dpspider-2.1.12.win-amd64.exe](http://pan.baidu.com/s/1qYyaMhm)
 
# 运行效果图展示

* 点击查看 [test](https://github.com/doupengs/dpspider/tree/master/test) `实例源码`

![](https://github.com/doupengs/dpspider/blob/master/image/master.gif)<br>
```markdown
1.master
```

![](https://github.com/doupengs/dpspider/blob/master/image/worker.gif)<br>
```markdown
2.worker
```

# spider.py

#### spider简介

```markdown
框架的主体，配置文件要继承的类
```
#### 初始化的成员

* **self.listGetUrls** : 最初的要爬取的列表页的所有GET链接
* **self.listPostUrl** : 最初需要爬取的列表页的POST链接
* **self.postPages** : 最初需要爬取的列表页的POST链接的所有页数
* **self.postPageName** : 最初需要爬取的列表页的POST链接的页数KEY的名字
* **self.encoding** : 网页的编码，两级可分别设置，默认均为UTF-8
* **self.threadNum** : 开启的线程数量，默认开启20个线程
* **self.logFile** : 如果有，将输出写入文件，没有就打印到控制台
* **self.color** : 打印是否带有颜色
* **self.debug** : 有四个等级，0 什么都不输出，1 只输出[Error],2 输出[Error]和[WARING],3 输出[Error]，[WARING]和[INFO],4 全输出
* **self.downloader** 下载器的参数设置:
 * **self.useProxyMaxNum** : 每个代理的连续使用的最大次数，当连续使用次数达到这个数字时，强制更换代理，防止代理被封，默认为10次
 * **self.proxyFilePath** :  代理文件的路径，默认为当前路径下的 proxyList.txt 文件
 * **self.method** : 请求方法，默认为 (GET,GET) 方法, 还有（POST,GET）
 * **self.proxyEnable** : 是否使用代理，默认为 False
 * **下面这些是请求时可能用到可选参数，相对常会用到的: data, headers, cookies, timeout**
 * **self.params** = None
 * **self.data** = None
 * **self.json** = None
 * **self.headers** = None
 * **self.cookies** = None
 * **self.files** = None
 * **self.auth** = None
 * **self.timeout** = None
 * **self.allowRedirects** = True
 * **self.verify** = None
 * **self.stream** = None
 * **self.cert** = None
* **self.IM** mysql数据库的参数设置 :
 * **self.mysqlHost** : 数据库的主机名，默认为本机 localhost
 * **self.mysqlUser** : 数据库的用户名
 * **self.mysqlPassword** : 数据库的密码
 * **self.mysqlDb** : 数据库的库名
 * **self.mysqlTableName** : 数据库库下的表名
 * **self.mysqlCharset** : 默认编码为 UTF-8
 * **self.isMysqlFLF** : 插入失败的sql语句日志，默认不生成insertMysqlFail.log文件
 * **self.isMysqlRLF** : 违反mysql主键唯一约束条件,没有插入数据库的sql语句，相当于去重，默认不生成insertMysqlRepeat.log文件
 * **self.isInsertMysql** : 是否连接数据库，测试抓取正常时启用，默认不连接数据库
* **self.RD** redis数据库的参数设置:
 * **self.isUseRedis** : 是否使用redis数据库进行去重, 默认为 False
 * **self.redisKey** : 如果使用redis去重，作为redis的一个key存储，value值为mysql的表名
 * **self.isRedisKeyUrl** : 如果redisKey是详情页的url，url作为去重依据，默认值为True，则这个详情页会在第一层过滤，不会再下载，节约资源
 * **self.redisHost** : 数据库的主机名，默认为本机 localhost
 * **self.redisPort** : 数据库的端口号，默认为6379
 * **self.redisDb** : redis数据库，默认为0
 * **self.redisPassword** : 数据库的密码，默认为 None

#### 需要重载的方法

* **parseList(**self,data,response**)**
```markdown
通过data(是一个Parser类，可以看parser.py来了解这个类下的方法)，response，解析的所有详情页的url添加到urls列表中
并返回列表urls
```

* **parsePage(**self,data,response**)**
```markdown
通过data(是一个Parser类，可以看parser.py来了解这个类下的方法)，response，解析的所有你想要的字段添加到jsonData字典中
并返回字典jsonData
{
colunm1:value1,
colunm2:value2,
...
}
```

# distspider.py

#### distspider简介

```markdown
spider.py使用的是多线程
distspider.py 是将下载任务交给 multiworker.py， 采用分布式多进程
所以就没有线程的设置 self.threadNum 多了下面三个成员
```

* **self.serverHost** : 服务器地址
* **self.serverPort** : 服务器端口号
* **self.serverAuthkey** : 密钥

# multiworker.py

#### multiworker简介

```markdown
distspider.py 的下载器，设置的参数如下(与 distspider 参数相对应)
processNum=4 进程数
serverHost='127.0.0.1' 服务器地址
serverAuthkey=''密钥 
serverPort=5000 服务器端口号
logFile=None
color=True
debug=4
```

# insertmysql.py

#### insertmysql简介

```markdown
数据写入模块
如果数据插入失败会生成 insertMysqlFail.log
可以选择是否生成违反主键唯一约束条件的插入语句，即 insertMysqlRepeat.log
```

# parser.py

#### parser简介

```markdown
选择 xpath 和 re 相结合的解析方法，方法很强大
```

点击了解[xpath](http://www.w3school.com.cn/xpath/)

# download.py

#### download简介

```markdown
可以选择是否使用代理下载
代理不能使用会自动更新下一个代理，还可以设置每个代理最大连续使用次数
```

# color.py

#### color简介

```markdown
可选是否带有颜色打印，或者设置输出的级别
```

# 反馈与建议

* 希望反馈您的宝贵意见、建议和使用中的BUG.
* GITHUP地址：[窦朋 | doupengs](https://github.com/doupengs)
* 微信公众号：[人生苦短遂学python](https://mp.weixin.qq.com/mp/homepage?__biz=MzI5MzI5NTQ4Mg==&hid=1&sn=fde1700cb5532eb84d227b1f6ded6838&uin=Njg4NTExNDQw&key=9ed31d4918c154c8f98e46aaf51029e25d006894bd336605c9ea269077414f400da2fd9110bf7810e535c7ca20c6c5b603eab7f647d52d77496e30ce9f13d357022d8408093b3456b3ce82c9a9069ceb&devicetype=Windows+10&version=62030053&lang=zh_CN&winzoom=1)
* 邮箱：<doupeng1993@sina.com>