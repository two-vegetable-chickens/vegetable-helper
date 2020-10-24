
from calculator import *
import tkinter as tk
  
from time import time
import BMI 
from tkinter import messagebox
from PIL import ImageTk, Image
import huilv
import daxie
import grsds
from PMT import *
import wucha
from tuodanceshi import *
def get_image(filename,width,height):
    im=(Image.open(filename).resize((width,height)))
    return ImageTk.PhotoImage(im)
    
btime=ctime=0    
hold=True
onetime=0
paused=True 




def gettime():
    global dao
    global btime,ctime
    global hold
    global onetime
    global paused
    global entryhour,entrymin,entrysec
    try:
        hour=entryhour.get()
        hour=int(hour)
    except:
        hour=0
    
    try:
        min=entrymin.get()
        min=int(min)
    except:
        min=0
    try:
        sec=entrysec.get()
        sec=int(sec)
    except:
        sec=0
        
    minsec=3600*hour+60*min+sec
    return minsec
    
def run_timer():
    global btime,ctime
    global hold
    global onetime
    global paused    
    global oldtime,minsec
    global dao
    if not paused:
        if  btime and  ctime:
            delta=time()-ctime+btime-oldtime
            btime=ctime=0
        elif btime:
            delta=btime-oldtime
        else:
            delta=time()-oldtime
            
        delta1=minsec-delta-10*onetime
        (e,f)=divmod(delta1,60)
        (g,e)=divmod(e,60)
            #时分秒分别为 g,e,f
            #正计时时分秒分别为d,a,c
            ##(a,c)=divmod(self.delta,60)
            #(d,a)=divmod(a,60)
        if delta1>0:
            deltastr='{:.0f}:{:.0f}:{:.3f}'.format(g,e,f)
            dao.display.config(text=deltastr)
            dao.display.after(1,run_timer)
        else:
            deltastr='00:00:00'
            tk.messagebox.showinfo('提示！','时间到!!!')
                
            
    #开始按钮
def start():
    global btime,ctime
    global hold
    global onetime
    global paused
    global dao
    if  paused==True :
        global minsec
        minsec=gettime()
        global oldtime
        oldtime=time()
        paused=False
        run_timer()
    #重置按钮
def reset_time():
    global btime,ctime
    global hold
    global onetime
    global paused,minsec
    global dao,varhour,varmin,varsec
    global entryhour,entrymin,entrysec
    if hold:
        paused=True
        dao.display.config(text='00:00:00')
        onetime=0
        varhour.set('0')
        entryhour=tk.Entry(dao,textvariable=varhour)
        varmin.set('0')
        entrymin=tk.Entry(dao,textvariable=varmin)
        varsec.set('0')
        entrysec=tk.Entry(dao,textvariable=varsec)
        minsec=gettime()
    else:
        tk.messagebox.showinfo("error1,你不能这样干呀")
    
    #暂停按钮
def stop_time():
    global btime,ctime
    global hold
    global onetime
    global paused
    global dao,button_stop
    if not paused:
        if  hold:
            hold=False
            button_stop.config(text="继续")
            btime=time()
        else:
            ctime=time()
            hold=True
            button_stop.config(text="暂停")
        
        
    #减少10秒按钮    
def reduce_time():
    
    global dao
    global onetime
   
    onetime+=1
        
    #获取时间函数    

    #时间运行点

def  Timecounter():
    global dao
    dao=tk.Tk()
    dao.title("菜鸡倒计时")
    dao.geometry('200x400+200+200')
    dao.display=tk.Label(dao,text="00:00:00",font=(50),bg="red")
    dao.display.pack(pady=5)
        
        #类里面创建开始按钮
    button_start=tk.Button(dao,text='开始',command=start)
    button_start.pack(pady=5)
        
        #类里面创建减少10秒按钮
    button_reduce=tk.Button(dao,text='减少10秒',command=reduce_time)
    button_reduce.pack(pady=5)
        
        #创建重置按钮
    button_reset=tk.Button(dao,text='重置',command=reset_time)
    button_reset.pack(pady=5)
        
        #创建暂停按钮
    global button_stop
    button_stop=tk.Button(dao,text='暂停',command=stop_time)
    button_stop.pack(pady=5)
    
    hour=tk.Label(dao,text="小时")
    hour.pack(pady=5)
        #记录下小时
    global entryhour,varhour
    
    varhour=tk.StringVar()
    entryhour=tk.Entry(dao,textvariable=varhour)
    entryhour.pack(pady=5)
        
        
    min=tk.Label(dao,text="分钟")
    min.pack(pady=5)
        #记录下分钟
    global entrymin,varmin
    varmin=tk.StringVar()
    entrymin=tk.Entry(dao,textvariable=varmin)
    entrymin.pack(pady=5)
        
        
    sec=tk.Label(dao,text="秒钟")
    sec.pack(pady=5)
        #记录下秒钟
    global entrysec,varsec
    varsec=tk.StringVar()
    entrysec=tk.Entry(dao,textvariable=varsec)
    entrysec.pack(pady=5)
    
    
       
    
    dao.mainloop()


#主界面代码    

dian=False
def dianzhewan():
     
    global dian
    if dian==False :
        dian=True
        tk.messagebox.showinfo('菜鸡','跟你说了不能点了，是不是傻')
    else:
        dian=False
        
    
    
    
a=2    
huanse=True     
 #背景颜色变换
def colorchange():
    global im_root,canvas_root,huanse,a
    if huanse:
        b=str(a)
        value=b+'.jpg'
        im_root=get_image(value,400,400)
        canvas_root.create_image(200,150,image=im_root)
        
        if a<=6:
            a=a+1
        else:
            a=1
    #else:
     #   im_root=get_image('1.jpg',400,300)
      #  canvas_root.create_image(200,150,image=im_root)
         
def kaishi():    
    win=Tk()
    win.geometry('400x300+300+150')
    win.resizable(False,False)
    #这个时候窗口一闪而过，需要使用消息循环让它停留即mainloop()
    #窗口的名字
    #添加label
    label_12=Label(win,text="我们是菜鸡")
    label_12.pack()
    global canvas_root
    canvas_root=tk.Canvas(win,width=400,height=400)
    im_root=get_image('1.jpg',400,400)
    im_root_1=get_image('1.jpg',40,20)
    canvas_root.create_image(200,150,image=im_root)
    canvas_root.pack()
    win.title("菜鸡助手指南")
    #窗口的大小
    win.geometry("300x400+200+200")
    
     
     
    #bg是背景色
    #显示label，用label.pack()
     
    #接下来做按钮控件！！！不是模块，用Button()
    
    #未设置功能
    canvas_root.create_window(260, 320, window=Button(win,  width=10,height=1,text="BMI",compound=tk.CENTER, bg="white",command=BMI.main))
    canvas_root.create_window(260, 360, window=Button(win, width=10,height=1,text="汇率",compound=tk.CENTER, bg="white",command=huilv.moneychange))
    canvas_root.create_window(40,360, window=Button(win, width=10,height=1,text="大小写",compound=tk.CENTER, bg="white",command=daxie.main))
    canvas_root.create_window(150, 360, window=Button(win, width=10,height=1,text="脱单测试",compound=tk.CENTER, bg="white",command=tuodan))
    
    #计算器
    canvas_root.create_window(150,320,window=Button(win,text="科学计算器",width=10,height=1,compound=tk.CENTER, bg="white",command=kexuejisuanqi))
     
    #玩的按钮
    canvas_root.create_window(40,320,window=Button(win,text="你不能点我",width=10,height=1,compound=tk.LEFT, bg="white",command=dianzhewan))
    
    #倒计时按钮
    canvas_root.create_window(150,280,window=Button(win,text="倒计时器",width=10,height=1,compound=tk.CENTER, bg="white" ,command=Timecounter))
     
    #个税
    canvas_root.create_window(40,280,window=Button(win,text="个人所得税",width=10,height=1,compound=tk.CENTER, bg="white" ,command=grsds.main)) 
    #canvas.create_window(100, 50, width=100, height=20

                                            
    #背景颜色按钮
    canvas_root.create_window(40,320,window=Button(win,text="背景颜色变化",width=10,height=1,compound=tk.CENTER, bg="white",command=colorchange))
     
    canvas_root.create_window(260, 280, window=Button(win, width=10,height=1,text="PMT",compound=tk.CENTER, bg="white",command=Calculator)) 
    win.mainloop()

if __name__=='__main__':
    kaishi()
