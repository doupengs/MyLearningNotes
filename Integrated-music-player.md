# 集成音乐播放器使用说明

* [简介](#简介)
* [解压-开启服务-访问服务](#解压-开启服务-访问服务)
  * [解压](#解压)
  * [开启服务](#开启服务)
  * [访问服务](#访问服务)
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

# 简介

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

# 解压-开启服务-访问服务

### 解压

* 解压到自己想要放在的**目录**下，推荐放在D盘目录下 `D:\phpwamp_Pack`<br>
![](https://github.com/doupengs/MyLearningNotes/blob/master/img/jieya.png)<br>
* 解压后<br>
![](https://github.com/doupengs/MyLearningNotes/blob/master/img/jieyahou.png)<br>

### 开启服务

* 双击`PHPWAMP_Pack.exe`。
* 在底部托盘中找到图标后右键选择启动服务。如果遇到360等软件的阻碍，请选择允许访问。

### 访问服务

* 启动成功后，再次右键，选择打开网站，即可使用了。
  * 如果你的电脑默认的浏览器是IE，建议复制链接，或直接打开谷歌浏览器或360浏览器，输入`localhost:8066` 或 `127.0.0.1:8066`来使用。
* 如何使用手机访问此服务，双击目录下的`get_ip.bat`，你会看到下图所示，例如我的局域网的IP就是`172.18.2.164`，因此在手机浏览器中打开`172.18.2.164:8066`即可，期间电脑要处于开机状态，当然这个同样适用于电脑。
* 也就是说电脑可以通过三种方式访问:
  * `localhost:8066`
  * `127.0.0.1:8066`
  * `172.18.2.164:8066`
* 手机只可以通过一种方式访问:
  * `172.18.2.164:8066`






 
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
