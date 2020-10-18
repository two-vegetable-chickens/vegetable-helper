# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 23:41:27 2020

@author: 16434
"""

import tkinter
import tkinter.simpledialog as dl 
import tkinter.messagebox as mb
from tkinter import *
import re
import math
from functools import partial
def test(entry):
    formula=entry.get()
    for char in formula:
        if '\u4e00' <= char <= '\u9fa5':
            entry.delete(0, END)
            entry.insert(END, '你好歹输入个数好吗')
            return False
    return True
    
def suanyixia():
    
    global shengao,tizhong
    
    if test(shengao) and test(tizhong):
        shengao_2=shengao.get()
        tizhong_2=tizhong.get()
        shengao_1=float(shengao_2)
        tizhong_1=float(tizhong_2)
        bmi1=tizhong_1/(shengao_1*shengao_1)
        if bmi1<=18.4:
            output_dialog1="您的体重偏瘦，多吃点长长肉~，bmi指数为："+str(bmi1)
            mb.showinfo("Right",output_dialog1)
        elif   bmi1<=23.9:
            output_dialog1="您的身材很匀称哦，继续保持~，bmi指数为："+str(bmi1)
            mb.showinfo("<",output_dialog1)
        elif   bmi1<=27.9:
            output_dialog1="您的体重有些过重了哦，该减肥啦！~，bmi指数为："+str(bmi1)
            mb.showinfo("过重",output_dialog1)
        elif bmi1>=28.0:
            output_dialog1="您的体重过于肥胖，称表示压力山大啊~，bmi指数为："+str(bmi1)
            mb.showinfo("肥胖",output_dialog1)
     
         
        
        
def main():
    top = tkinter.Tk()
    l = tkinter.Label(top,text="BMI")
    l.pack()  
    #mb.showinfo("bmi指数计算","欢迎使用bmi指数计算")
    
    #提示框
    tishi1=tkinter.Label(top,text="身高")
    tishi1.pack()
    
    #身高框
    var_shengao=StringVar()
    global shengao
    shengao=tkinter.Entry(top,textvariable=var_shengao)
    shengao.pack() 
    var_shengao.set("这里输入身高")
    #shengao.grid(row=3, column=0)
    
   # tishi3=tkinter.Label(top,text="M")
   # tishi3.pack()
 
    #提示框
    tishi2=tkinter.Label(top,text="体重")
    tishi2.pack()
    #体重框
    var_tizhong=StringVar()
    global tizhong
    tizhong=tkinter.Entry(top,textvariable=var_tizhong)
    tizhong.pack()
    var_tizhong.set("这里输入体重")
    #测试按钮
    zhuanhuan=tkinter.Button(top,text="点点试试",command=suanyixia)
    zhuanhuan.pack()
    #结果输出的地方
    var_jieguo=StringVar()
    global jieguo
    jieguo=tkinter.Entry(top,textvariable=var_jieguo)
     
    jieguo.pack()
    
    top.mainloop()
main()