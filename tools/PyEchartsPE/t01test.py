# 项目地址 https://github.com/pyecharts/pyecharts
# 效果展示 http://pyecharts.herokuapp.com/
# 中文文档 https://pyecharts.org/#/zh-cn/
# 英文文档 见项目地址

from snapshot_selenium import snapshot as driver
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from selenium.webdriver.common.service import Service
from selenium import webdriver

def buildHtml():
    # V1 版本开始支持链式调用
    # 链式调用写法1
    bar = Bar().add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])\
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])\
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])\
        .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))

    # 链式调用写法2
    bar = (
        Bar()
            .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
            .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    bar.render('./data/render.html')

    # 不习惯链式调用的开发者依旧可以单独调用方法
    bar = Bar()
    bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
    bar.render()

def bar_chart() -> Bar:
    c = (
        Bar()
            .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
            .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )

    # 需要安装 snapshot-selenium 或者 snapshot-phantomjs
    make_snapshot(driver, c.render(), "./data/bar.png")

if __name__ == '__main__':
    buildHtml()
    # bar_chart()