# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 00:48:22 2020

@author: 16434
"""

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

def jisuan():
    global salary,cal_salary,get_salary
    if test(salary):
         salary2=salary.get()
         salary1=float(salary2)
         salary3 = salary1 - 5000
         
         if salary3 > 85000:
                cal_salary = salary3 * 0.45 - 15160
         elif salary3 > 60000:
                cal_salary = salary3 * 0.35 - 7160
         elif salary3 > 40000:
                cal_salary = salary3 * 0.3 - 4410
         elif salary3 > 30000:
                cal_salary = salary3 * 0.25 - 2660
         elif salary3 > 17000:
                cal_salary = salary3 * 0.2 - 1410
         elif salary3 > 8000:
                cal_salary = salary3 * 0.1 - 210
         else:
                cal_salary = salary3 * 0.03
                
    get_salary = salary1 - cal_salary
    output_dialog1="您需缴纳的税额为"+str(cal_salary)+"您的税后工资为"+str(get_salary)           

    mb.showinfo("right",output_dialog1)

def main():
    top = tkinter.Tk()
    l = tkinter.Label(top,text="个人所得税")
    l.pack()  
    #mb.showinfo("个人所得税计算","欢迎使用个人所得税计算")
    
    #提示框
    tishi1=tkinter.Label(top,text="工资")
    tishi1.pack()
    
    #工资框
    var_salary=StringVar()
    global salary
    salary=tkinter.Entry(top,textvariable=var_salary)
    salary.pack() 
    var_salary.set("这里输入工资")
    # salary.grid(row=3, column=0)
    
    # tishi3=tkinter.Label(top,text="M")
    # tishi3.pack()
 
    #测试按钮
    zhuanhuan=tkinter.Button(top,text="点点试试",command=jisuan)
    zhuanhuan.pack()
    #结果输出的地方
    var_jieguo=StringVar()
    global jieguo
    jieguo=tkinter.Entry(top,textvariable=var_jieguo)
     
    jieguo.pack()
    
    top.mainloop()
main()
