import tkinter as tk
 
from time import time
  
from tkinter import messagebox
from PIL import ImageTk, Image
value_1=0
value_2=0
value_3=0
value_4=0
def get_image(filename,width,height):
    im=(Image.open(filename).resize((width,height)))
    return ImageTk.PhotoImage(im)
def get_1():
    global value_1
    if value_1==0:
        value_1=18
     
def get_2():
    global value_1
    if value_1==0:
        value_1=24 
     
def get_3():
    global value_1
    if value_1==0:
        value_1=12
def get_4():
    global value_2
    if value_2==0:
        value_2=12
def get_5():
    global value_2
    if value_2==0:
        value_2=18
def get_6():
    global value_2
    if value_2==0:
        value_2=20
def get_7():
    global value_3
    if value_3==0:
        value_3=18
def get_8():
    global value_3
    if value_3==0:
        value_3=12
def get_9():
    global value_3
    if value_3==0:
        value_3=20
def get_10():
    global value_4
    if value_4==0:
        value_4=20
def get_11():
    global value_4
    if value_4==0:
        value_4=36
def get_12():
    global value_4
    if value_4==0:
        value_4=28
def jiesuan():
    global value_1,value_2,value_3,value_4
    value=value_1+value_2+value_3+value_4
    if value<=100 and value>80:
        output_diyige="您的得分是"+str(value)+"，您好像很有经验的样子哦，是个情场老手了吧"
    elif value>60:
        output_diyige="您的得分是"+str(value)+"，你能猜出对方的大概意思，但如果迟迟不出手，脱单的机会也是会溜走的哟~"
    elif value>40:
        output_diyige="您的得分是"+str(value)+"，您可以多和朋友们出去玩玩，找找话题，找找朋友哦"
    else:
        output_diyige="您的得分是"+str(value)+"，怎么说呢，不能脱单不是你的错，你缺一个懂你的人"
    tk.messagebox.showinfo("结果",output_diyige)
def reset():
    global value_1,value_2,value_3,value_4
    value_1=0
    value_2=0
    value_3=0
    value_4=0
def tuodan():
    #创建窗口
    tuo=tk.Toplevel()
     
    tuo.title("脱单小助手")
    tuo.geometry("800x600+30+40")
   # canvas_root_1=tk.Canvas(tuo,width=400,height=300) 
    im_root_2=get_image('first.jpg',200,150)
    im_root_3=get_image('second.jpg',200,150)
    #canvas_root_1.create_image(200,150,image=im_root_2) 
    #canvas_root_1.pack()
    label_1=tk.Label(tuo,text="看下面的图片，你看到了什么？", anchor='n',compound = "bottom",image=im_root_2).grid(column=1,row=1)
    button_1=tk.Button(tuo,text="想睡",width=30,command=get_1 ).grid(column=0,row=2)
    button_2=tk.Button(tuo,text="昏迷" ,width=30,command=get_2).grid(column=1,row=2)
    button_3=tk.Button(tuo,text="旋转",width=30,command=get_3).grid(column=2,row=2)
    label_2=tk.Label(tuo,text="男生想要和女生感情更进一步，带女生去看哪种类型的电影效果更好？" ).grid(row=3,column=1)
    button_4=tk.Button(tuo,text="喜剧片",width=30,command=get_4 ).grid(column=0,row=4)
    button_5=tk.Button(tuo,text="文艺片" ,width=30,command=get_5).grid(column=1,row=4)
    button_6=tk.Button(tuo,text="纪录片",width=30,command=get_6).grid(column=2,row=4)
    label_3=tk.Label(tuo,text="这组“密码”出现在了某封告白信里，请问它代表什么意思？", anchor='n',compound = "bottom",image=im_root_3).grid(column=1,row=5)
    button_7=tk.Button(tuo,text="喜欢你",width=30,command=get_7 ).grid(column=0,row=6)
    button_8=tk.Button(tuo,text="我想你" ,width=30,command=get_8).grid(column=1,row=6)
    button_9=tk.Button(tuo,text="我爱你",width=30,command=get_9).grid(column=2,row=6)
    label_4=tk.Label(tuo,text="程序猿说：10011110101110110100010请问这代表什么意思？" ).grid(row=7,column=1)
    button_11=tk.Button(tuo,text="今天你要嫁给我",width=30,command=get_10 ).grid(column=0,row=8)
    button_12=tk.Button(tuo,text="我爱你一生一世" ,width=30,command=get_11).grid(column=1,row=8)
    button_13=tk.Button(tuo,text="你就是我的唯一",width=30,command=get_12).grid(column=2,row=8)
    button_14=tk.Button(tuo,text="提交",command=jiesuan).grid(column=1,row=9)
    button_15=tk.Button(tuo,text="重置",command=reset).grid(column=2,row=9)
    tuo.mainloop()


 


 
