from  tkinter import *
import os
    from tkinter.scrolledtext import ScrolledText
root = Tk()
now = os.getcwd()
root.geometry("220x170")
root.title("@ljc")
title = Label(root,text='表白墙搜索器',font=("微软雅黑",18)).place(x=30,y=20)
shuru = Entry(root)
shuru.insert(0,'输入关键词')
label = Label(root,text='      数据时间:2016.5.1-2018.5.10 \nauthor:ljc').place(x=0,y=120)
shuru.place(x=25,y=80)
def content(i,j):
  bb =[]
  c = 0
  try:
    txt = now+'\content\\{}.{}.txt'.format(i,j)
    with open(txt,'rb') as f:
        BB = ''
        for line in f.readlines():
            if line == '\n' or len(line) == 0 or len(line) == 1:
                continue
            this = line.decode('utf-8')
            if c == 0:
                time = this
                c +=1
            elif c == 1:
                title = this
                c += 1
            else:
                if this == '[表白]\n':
                    if len(BB) != 0:
                        aa = BB.strip()
                        cc = aa.strip('\n')
                        bb.append(cc)
                        BB = ''
                else:
                    BB+=this
    return (time,bb)
  except:
      pass
def clear(x):
    y=''
    for i in range(len(x)):
        if str.isalpha(x[i]):
            y+=x[i]
    return y
def searchx():
  x = shuru.get()
  outcome = Toplevel()
  outcome.geometry("380x300")
  outcome.title("结果显示")
  sum = 0
  a = ''
  for i in range(65):
    for j in range(1,10):
        this = content(i,j)
        if this!= None:
            context = this[1]
            for item in context:
                if x in item:
                    a+=this[0]+clear(item)
                    sum += 1
                    a+='\n\n'

  count = Label(outcome,text = "上墙次数"+str(sum),font=("微软雅黑",10)).place(x=10,y=20)
  jieguo = ScrolledText(outcome,height = 16,width =50)
  jieguo.insert('0.0',a)
  jieguo.place(x=10,y=60)
  outcome.mainloop()
sousuo = Button(root,text='搜索',command = searchx).place(x=170,y=78)
root.mainloop()
