#coding:utf-8
import sys
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from scipy.misc import imread
from datetime import datetime

novel='all.txt' #'assz.txt'
imgmask='background.png' #'assz.jpg'
t=datetime.now()
resimg="word_"+novel.split('.')[0]+"_"+str(t.month)+str(t.day)+str(t.hour)+str(t.minute)+str(t.second)+".jpg"

novletext=open(novel,'rb').read().decode('utf-8')
hmseg=jieba.cut(novletext)
seg_space=' '.join(hmseg)
alice_color=imread(imgmask)
20#wordcloud默认不支持中文，这里的font_path需要指向中文字体，不然得到的词云全是乱码
fwc=WordCloud(font_path='msyh.ttc',max_words=150,background_color='white',mask=alice_color,max_font_size=200,font_step=1).generate(seg_space)
imagecolor=ImageColorGenerator(alice_color)
plt.imshow(fwc.recolor(color_func=imagecolor))
plt.axis("off")
plt.show()
fwc.to_file(resimg)
