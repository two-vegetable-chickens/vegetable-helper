
from tkinter import *
from time import time
  
from tkinter import messagebox
from PIL import ImageTk, Image



from tkinter import ttk

from tkinter import scrolledtext

from tkinter import Menu

from tkinter import Spinbox

def get_image(filename,width,height):
    im=(Image.open(filename).resize((width,height)))
    return ImageTk.PhotoImage(im)

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
    messagebox.showinfo("结果",output_diyige)
    
value_1=12
value_2=12
value_3=18
value_4=20
def v_1get():
    global v_1
    global value_1
    value_1=int(v_1.get())

def v_2get():
    global v_2
    global value_2
    value_2=int(v_2.get())
    
def v_3get():
    global v_3
    global value_3
    value_3=int(v_3.get())
def v_4get():
    global v_4
    global value_4
    value_4=int(v_4.get())
def tuodan():
    tuo = Toplevel()
    #设置窗口
    tuo.title("脱单小助手")
    tuo.geometry("600x600+30+40")
   # canvas_root_1=tk.Canvas(tuo,width=400,height=300) 
    im_root_2=get_image('first.jpg',200,150)
    im_root_3=get_image('second.jpg',200,150)

    label_1=Label(tuo,text="看下面的图片，你看到了什么？", anchor='n',compound = "bottom",image=im_root_2).grid(column=1,row=1)
    global v_1,v_2,v_3,v_4
    v_1 = IntVar()
    v_2=IntVar()
    v_3=IntVar()
    v_4=IntVar()
    
    v_1.set(12)
    v_2.set(12)
    v_3.set(18)
    v_4.set(20)
    
    label_1=Label(tuo,text="观察下面的图片，你看到了什么？", anchor='n',compound = "bottom",image=im_root_2).grid(column=1,row=1)
    #第一题的选择
    Radiobutton(tuo,text='晃动',variable=v_1,value=12,command=v_1get).grid(column=0,row=2)

    Radiobutton(tuo,text='静止',variable=v_1,value=24,command=v_1get).grid(column=1,row=2)

    Radiobutton(tuo,text='旋转',variable=v_1,value=18,command=v_1get).grid(column=2,row=2)
    
    label_2=Label(tuo,text="男生想要和女生感情更进一步，带女生去看哪种类型的电影效果更好？" ).grid(row=3,column=1)
    #第二题的选择
    Radiobutton(tuo,text='喜剧片',variable=v_2,value=12,command=v_2get).grid(column=0,row=4)

    Radiobutton(tuo,text='恐怖片',variable=v_2,value=18,command=v_2get).grid(column=1,row=4)

    Radiobutton(tuo,text='爱情片',variable=v_2,value=20,command=v_2get).grid(column=2,row=4)
    label_3=Label(tuo,text="这组“密码”出现在了某封告白信里，请问它代表什么意思？", anchor='n',compound = "bottom",image=im_root_3).grid(column=1,row=5)
    #第三题的选择
    Radiobutton(tuo,text='喜欢你',variable=v_3,value=18,command=v_3get).grid(column=0,row=6)

    Radiobutton(tuo,text='我想你',variable=v_3,value=12,command=v_3get).grid(column=1,row=6)

    Radiobutton(tuo,text='我爱你',variable=v_3,value=20,command=v_3get).grid(column=2,row=6)
    label_4=Label(tuo,text="程序猿说：10011110101110110100010请问这代表什么意思？" ).grid(row=7,column=1)
    #第四题的选择
    Radiobutton(tuo,text='今天你要嫁给我',variable=v_4,value=20,command=v_4get).grid(column=0,row=8)

    Radiobutton(tuo,text='我爱你一生一世',variable=v_4,value=36,command=v_4get).grid(column=1,row=8)

    Radiobutton(tuo,text='你就是我的唯一',variable=v_4,value=28,command=v_4get).grid(column=2,row=8)
    #提交按钮
    button_14=Button(tuo,text="提交",command=jiesuan).grid(column=1,row=9)
    
    mainloop()

