### 实现思路
主要用到selenium这个模块，我的对requests模块的理解是模拟浏览器进行访问，需要自行追加所需要的信息；
而selenium这个模块是去调用一个真正的浏览器去访问（会启动浏览器页面），你要做的是编写在浏览器页面的处理逻辑，点击、拖动等等

目前“市面上”常见的实现方式是获取无缺口图，获取有缺口图，
对比两张图像素，某个像素位差距大于某个限定值（threshold）就认定这是缺失位置
在刚进入页面时，验证图片为完整图片，点击滑块按钮，图片变成有缺口图片

有一种验证图片是以图片碎片的形式给出的，还需要通过程序将碎片拼接成完整的图片再进行操作\
一篇登录b站参考：https://blog.csdn.net/Jeeson_Z/article/details/82047685\
又一篇登录b站的参考：https://cloud.tencent.com/developer/article/1423528

目前的好像是一种更难的方式是，不给出原图，直接出现的就是带缺口的图，这种的可能要借助图像识别领域的算法来实现
然后我就找到这么一个https://blog.csdn.net/weixin_41624982/article/details/87927331
在京东上测试准确率很高

### 我的测试环境
|项目|内容|
|---|---|
|时间|20200316|
|python|3.7|
|谷歌浏览器驱动程序|80.0.3987.106|
|selenium|3.141.0|
|beautifulsoup4|4.6.0|
|opencv（就是程序中的cv2）|4.1.2.30|
|Windows|Win10|
|Pycharm|


### 问题记录

- webdriver.Chrome()需要传入一个浏览器的驱动程序文件，而不是浏览器的执行程序文件
  
  参见https://blog.csdn.net/weixin_43746433/article/details/95237254，并没有64位的驱动，下载32位的后可用
- 京东的滑块验证图片的显示尺寸跟图片的实际不一样！！！
  
  在F12查看网页源码时，定位到验证图片的源码处，就能看到显示图片尺寸


### 参考文献
>滑动轨迹参考
>https://www.aneasystone.com/archives/2018/03/python-selenium-geetest-crack.html
>
>一个还能划过头再回来一点儿的轨迹（未测试）
>https://blog.csdn.net/qq_39802740/article/details/83584980
>
>一篇登录b站参考
>https://blog.csdn.net/Jeeson_Z/article/details/82047685
>
>又一篇登录b站的参考
>https://cloud.tencent.com/developer/article/1423528
>
>[python PIL/cv2/base64相互转换](https://blog.csdn.net/haveanybody/article/details/86494063)
>
>抢购 https://cloud.tencent.com/developer/article/1565598
>
>抢购 https://www.hotbak.net/key/python%E4%BA%AC%E4%B8%9C%E7%A7%92%E6%9D%80%E8%84%9A%E6%9C%AC.html


