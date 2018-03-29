# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from pyecharts import Pie
from pyecharts_snapshot.main import make_a_snapshot
from PIL import Image
import os
import sys

savety = [u'危险', u'比较危险', u'比较安全', u'安全']
savety_colors = [u'#df0000', u'#ff5f5a', u'#37baf1', u'#10ae50']
savety_x = [6, 1, 2, 3]

# 标题居中
pie = Pie()
pie.add(
    # title
    '',
    # label
    savety,
    # 数值，比例
    savety_x,
    # 显示label
    is_label_show=True,
    # 不显示颜色提示的意思
    is_legend_show=False,
    # 是否高亮显示标签
    is_label_emphasis=False,
    # label字体size
    label_text_size=25,
    # 随机颜色
    # is_random=True,
    # 自定义标签颜色
    label_color=savety_colors,
    # 右侧工具箱
    is_toolbox_show=False
)

# 将生成的图片保存为html
pie.render()
# 将标准输出的信息，重定向到文件中
current = sys.stdout
f = open('temp', 'w')
sys.stdout = f
# 将html保存为pdf或png
make_a_snapshot('render.html', 'test.png')
# 还原标准输出
sys.stdout = current
f.close()
os.remove('render.html')
os.remove('temp')

img = Image.open('test.png')
w, h = img.size
img = img.resize((int(w*0.3), int(h*0.3)), Image.ANTIALIAS)
img.save('hhh.png')
os.remove('test.png')