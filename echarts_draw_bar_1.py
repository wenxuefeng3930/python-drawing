# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from pyecharts import Bar
from pyecharts_snapshot.main import make_a_snapshot
from PIL import Image
import os
import sys

attr = ['Cifs', 'DNS', 'FTP', 'RPC', 'SMB']

info =[10, 2, 2, 18, '']
low = [6, 5, 5, 1, 1]
medium = [7, 8, 1, '', 6]
high = [1, 8, 1, '', 2]
urgent = ['', 1, 2, '', '']
colors = ['#10ae50', '#37baf1', '#ffa92e', '#ff605a', '#df0000']

bar = Bar('')
bar.height=200
bar.width=400

# 全局配置项要在最后一个 add() 上设置，否则设置会被冲刷掉。

bar.add('信息', attr, info, is_label_show=True, label_pos='inside', is_stack=True)
bar.add('低危', attr, low, is_label_show=True, label_pos='inside', is_stack=True)
bar.add('中危', attr, medium, is_label_show=True, label_pos='inside', is_stack=True)
bar.add('高危', attr, high, is_label_show=True, label_pos='inside', is_stack=True)
bar.add('紧急', attr, urgent, is_stack=True,
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
        # yaxis_interval=0,
        # 是否显示y轴
        # is_yaxis_show=False,
        # y轴反向显示
        is_yaxis_inverse=True,
        # 不显示工具箱
        is_toolbox_show=False
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

img = Image.open('test.png')
w, h = img.size
img = img.resize((int(w*0.5), int(h*0.5)), Image.ANTIALIAS)
img.save('hhh.png')
os.remove('test.png')
