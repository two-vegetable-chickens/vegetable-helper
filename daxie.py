# -*- coding: utf-8 -*-  n  
"""
Created on Tue Oct 13 00:02:32 2020

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

def test(entry):
    formula=entry.get()
    for char in formula:
        if '\u4e00' <= char <= '\u9fa5':
            entry.delete(0, END)
            entry.insert(END, '输个数啊喂')
            return False
    return True

def money_transfer():
    
    global money_en
    if test(money_en):
         money_en2=money_en.get()
         money_en1=float(money_en2)
         
    num_list = [{'0': '整', '1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖'},
                '拾', '佰', '仟', '万']

    decimal_list = ['角','分']

    def func(b):
        ns = ''
        for x in range(1, len(b)):
            num = num_list[0][b[x]]
            word = num + (num_list[x] if b[x]!='0' else '')
            ns = word + ns

        return ns + (num_list[0][b[0]] if b[0] != '0' else '')

    NUM_LINE = 10000
    money_cn = ''
    if money_en1 == 0:
        return '零圆'

    aa = copy.copy(int(money_en1))
    unit = '圆'
    while aa % NUM_LINE:
        b = str(aa % NUM_LINE)[::-1]
        if len(str(aa)) > 4 and len(str(b)) != 4:
            b = b + '0'
        money_cn = func(b) + unit + money_cn
        aa = aa // NUM_LINE
        unit = '万' if aa else '圆'


    if isinstance(money_en1,float):
        ab = round(money_en1,2)
        ab = str(ab).split('.')[1]
        for x in range(0, len(ab)):
            num = num_list[0][ab[x]]
            word = num + (decimal_list[x] if ab[x] != '0' else '')
            money_cn += word
            
    output_dialog1="财务大写为"+str(money_cn)           
    mb.showinfo("right",output_dialog1)
    
def main():
    top = tkinter.Tk()
    l = tkinter.Label(top,text="财务大写")
    l.pack()  
    #mb.showinfo("财务大写转换","欢迎使用财务大写转换")
    
    #提示框
    tishi1=tkinter.Label(top,text="数值")
    tishi1.pack()
    
    #财务大写框
    var_money_en=StringVar()
    global money_en
    money_en=tkinter.Entry(top,textvariable=var_money_en)
    money_en.pack() 
    var_money_en.set("这里输入数值")
    # money_cn.grid(row=3, column=0)
    
    # tishi3=tkinter.Label(top,text="M")
    # tishi3.pack()
 
    #测试按钮
    zhuanhuan=tkinter.Button(top,text="点点试试",command=money_transfer)
    zhuanhuan.pack()
    #结果输出的地方
    var_jieguo=StringVar()
    global jieguo
    jieguo=tkinter.Entry(top,textvariable=var_jieguo)
     
    jieguo.pack()
    
    top.mainloop()
main()