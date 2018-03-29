# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from pyecharts import Bar
from pyecharts_snapshot.main import make_a_snapshot
from PIL import Image
import sys
import os

attr = ['test']

info =[10]
low = [2]
medium = [2]
high = [18]
urgent = ['']
colors = ['#10ae50', '#37baf1', '#ffa92e', '#ff605a', '#df0000']

bar = Bar('')

# bar.width=400
# bar.height=200

# 全局配置项要在最后一个 add() 上设置，否则设置会被冲刷掉。

bar.add('', attr, info, is_label_show=True, label_pos='inside', is_stack=True)
bar.add('', attr, low, is_label_show=True, label_pos='inside', is_stack=True)
bar.add('', attr, medium, is_label_show=True, label_pos='inside', is_stack=True)
bar.add('', attr, high, is_label_show=True, label_pos='inside', is_stack=True)
bar.add('', attr, urgent, is_stack=True,
        # 网格线
        is_splitline_show=False,
        label_pos='inside',
        # 是否高亮显示标签
        # is_label_emphasis=False,
        # 高亮标签字体颜色
        # label_emphasis_textcolor='red',
        # 高亮标签的位置
        label_emphasis_pos='inside',
        # 标签数据
        is_label_show=True,
        # 标签颜色自定义
        label_color=colors,
        # 标签字体颜色
        label_text_color='#000',
        # 标签字体大小
        label_text_size=15,
        # x/y交换
        is_convert=True,
        # y轴刻度标签
        yaxis_interval=0,
        # 是否显示y轴
        is_yaxis_show=False,
        is_xaxis_show=False,
        # y轴反向显示
        is_yaxis_inverse=True,
        # 不显示工具箱
        is_toolbox_show=False,
        yaxis_max=10
        )
bar.render()

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

# 裁切图片
img = Image.open('test.png')

width, height = img.size

width_left = 0
width_right = 0
height_top = 0
height_buttom = 0

color = (255, 255, 255, 255)

# 裁切图片
for h in range(0, height - 1):
    for w in range(0, width - 1):
        try:
            pixel = img.getpixel((w, h))
        except:
            continue
        # 如果像素点为白色，跳过
        if pixel == color:
            continue
        # 高度是否为0, 第一次找到不为白色的像素点时, 修改裁切的宽度0点, 高度0点值
        if not height_top:
            height_top = h
            width_left = w
        # 如果当前宽度像素点的下一个像素点为白色,说明当前的像素点为应该裁切的最后一个宽度点
        if img.getpixel((w + 1, h)) == color:
            if not width_right:
                width_right = w
        # # 如果当前高度像素点的下一个像素点为白色,说明当前的像素点为应该裁切的最后一个高度点
        if img.getpixel((w, h + 1)) == color:
            if not height_buttom:
                height_buttom = h

# img.crop((宽度起始点, 高度起始点, 要裁切的宽度, 要裁切的高度))
img = img.crop((width_left, height_top, width_right, height_buttom))
# 如果文件过小, 会报错
img.save('hhh.png')
os.remove('test.png')
