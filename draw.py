# -*- coding: utf-8 -*-
from matplotlib import mlab, font_manager as fm
from matplotlib import pyplot as plt


savety = [u'危险', u'比较危险', u'比较安全', u'安全']
savety_colors = [u'#df0000', u'#ff5f5a', u'#37baf1', u'#10ae50']
labels = [u'信息', u'低风险', u'中风险', u'高风险', u'紧急']
savety_x = [6, 1, 1, 1]

# matplotlib显示中文的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
# 显示负号
plt.rcParams['axes.unicode_minus'] = False
# 设置为圆形，不设置就是椭圆的
plt.axis('equal')
# 画饼图（数据，数据对应的标签，百分数保留两位小数点）
# patches是饼图的返回值，texts是饼外的文本，autotexts是饼内的文本
pathches, texts, autotexts = plt.pie(savety_x,
                                     # 饼图的颜色
                                     colors=savety_colors,
                                     # 标签名
                                     labels=savety,
                                     # 小数
                                     autopct='%1.1f%%',
                                     # 角度
                                     startangle=90,
                                     )

# 颜色提示, loc设置legend的位置，包括'upper right', 'upper left', 'lower right', 'lower left'
# bbox_to_anchor: 表示legend距离图形之间的距离，当出现图形与legend重叠时，可使用bbox_to_anchor进行调整legend的位置
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))
# 一定要放在plt.show()之前
plt.savefig("PieChart.jpg")
plt.show()
plt.close()
