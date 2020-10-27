# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 00:45:53 2020

@author: 16434
"""


import copy
import tkinter
import tkinter.simpledialog as dl 
import tkinter.messagebox as mb
from tkinter import *
import re
import math
from functools import partial
import sys

records=['1','2'] 
def calculate(): 
    global  shuzhi
    #平均值
    shuzu1 = shuzhi.get()
     
    records = list(map(int, shuzu1.split()))
    value1=sum(records)
    value2=len(records)
    if value2!=0:
        average = value1/value2                
        #方差
        fangcha = sum([(x - average) ** 2 for x in records]) / len(records)     
                
        #标准差
        bzc = math.sqrt(fangcha) 
                
        #均方根值
        jfgz = math.sqrt(sum([x ** 2 for x in records]) / len(records))
                       
        output_dialog1="平均值:"+str(average) +"\n均方根值:"+str(jfgz) + "\n标准差:"+str(bzc)+"\n均方根值:"+str(jfgz)
        
        global t 
        t.delete( 1.0,END)
        t.insert('end',output_dialog1)

def main():
    top = tkinter.Tk()
    l = tkinter.Label(top,text="统计函数")
    l.pack()
    top.geometry('400x220')
        
    
    #提示框
    tishi1=tkinter.Label(top,text="数值")
    tishi1.pack()
    
    #数值框
    var_shuzhi=StringVar()
    global shuzhi
    shuzhi=tkinter.Entry(top,width = 40,textvariable=var_shuzhi)
    shuzhi.pack()
    
    
    #处理字符串为数组并提取数值
    
    
    #测试按钮
    zhuanhuan=tkinter.Button(top,width = 40,text="计算",command=calculate)
    zhuanhuan.pack()
    
    #结果输出的地方
    '''
    var_jieguo=StringVar()
    global jieguo
    jieguo=tkinter.Entry(top,textvariable=var_jieguo) 
    jieguo.pack()
    '''
    global t
    t = tkinter.Text(top) 
    t.pack()
    
    top.mainloop()