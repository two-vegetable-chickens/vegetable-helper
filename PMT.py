# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:28:38 2020

@author: 16434
"""


from tkinter import *


def Calculator():
     
    window = Toplevel()  # 建立窗口
    window.title("房贷计算器")  # 命名窗口标题

    # 定义StringVar对象动态存储输入框的值
    global amountVar,rateVar,yearsVar,monthsVar,monthVar,total_1Var,totalInterest_1Var
    global totalRepayment_1Var,remain_1Var,monthRepayment_1Var,total_2Var
    global totalInterest_2Var,totalRepayment_2Var,remain_2Var,monthRepayment_2Var
    amountVar = StringVar()  # 贷款金额
    rateVar = StringVar()  # 年化利率
    yearsVar = StringVar()  # 贷款年限
    monthsVar = StringVar()  # 已还期数
    monthVar = StringVar()  # 第i月
    total_1Var = StringVar()  # 等额本息总还款额
    totalInterest_1Var = StringVar()  # 等额本息总利息
    totalRepayment_1Var = StringVar()  # 等额本息累计已还
    remain_1Var = StringVar()  # 等额本息待还金额
    monthRepayment_1Var = StringVar()  # 等额本息第i月应还
    total_2Var = StringVar()  # 等额本金总还款额
    totalInterest_2Var = StringVar()  # 等额本金总利息
    totalRepayment_2Var = StringVar()  # 等额本金累计已还
    remain_2Var = StringVar()  # 等额本金待还金额
    monthRepayment_2Var = StringVar()  # 等额本金第i月应还

    # 设置一些默认值
    monthsVar.set("0")
    monthVar.set('1')

    # 整体面板，设置总体的边距
    frame = Frame(window)
    frame.pack(padx=20, pady=20)


    label_1=Label(frame, text="贷款金额").grid(row=1, column=1, columnspan=3)
    label_2=Label(frame, text="年化利率").grid(row=2, column=1, columnspan=3)
    label_3=Label(frame, text="贷款年限").grid(row=3, column=1, columnspan=3)
    label_4=Label(frame, text="已还期数").grid(row=4, column=1, columnspan=3)
    label_5=Label(frame, text="总还款额").grid(row=7, column=1, columnspan=3)
    label_6=Label(frame, text="总利息额").grid(row=8, column=1, columnspan=3)
    label_7=Label(frame, text="累计已还").grid(row=9, column=1, columnspan=3)
    label_8=Label(frame, text="剩余待还").grid(row=10, column=1, columnspan=3)
    label_9=Label(frame, text="第").grid(row=11, column=1)
    label_10=Label(frame, text="月应还").grid(row=11, column=3)

        
    entry_1=Entry(frame, justify=RIGHT, textvariable=amountVar).grid(row=1, column=4)
    entry_2=Entry(frame, justify=RIGHT, textvariable=rateVar).grid(row=2, column=4)
    entry_3=Entry(frame, justify=RIGHT, textvariable=yearsVar).grid(row=3, column=4)
    entry_4=Entry(frame, justify=RIGHT, textvariable=monthsVar).grid(row=4, column=4)
    entry_5=Entry(frame, width=4, justify=CENTER, textvariable=monthVar).grid(row=11, column=2)
    label_10=Label(frame, textvariable=total_1Var).grid(row=7, column=4, sticky=E)
    label_11=Label(frame, textvariable=total_2Var).grid(row=7, column=6, sticky=E)
    label_12=Label(frame, textvariable=totalInterest_1Var).grid(row=8, column=4, sticky=E)
    label_13=Label(frame, textvariable=totalInterest_2Var).grid(row=8, column=6, sticky=E)
    label_14=Label(frame, textvariable=totalRepayment_1Var).grid(row=9, column=4, sticky=E)
    label_15=Label(frame, textvariable=totalRepayment_2Var).grid(row=9, column=6, sticky=E)
    label_16=Label(frame, textvariable=remain_1Var).grid(row=10, column=4, sticky=E)
    label_17=Label(frame, textvariable=remain_2Var).grid(row=10, column=6, sticky=E)
    label_18=Label(frame, textvariable=monthRepayment_1Var).grid(row=11, column=4, sticky=E)
    label_19=Label(frame, textvariable=monthRepayment_2Var).grid(row=11, column=6, sticky=E)

    # 添加Message存储单位
    message_1=Message(frame, text="元").grid(row=1, column=5)
    message_2=Message(frame, text="%").grid(row=2, column=5)
    message_3=Message(frame, text="年").grid(row=3, column=5)
    message_4=Message(frame, text="月").grid(row=4, column=5)
    message_5=Message(frame, text="元").grid(row=7, column=5)
    message_6=Message(frame, text="元").grid(row=7, column=7)
    message_7=Message(frame, text="元").grid(row=8, column=5)
    message_8=Message(frame, text="元").grid(row=8, column=7)
    message_9=Message(frame, text="元").grid(row=9, column=5)
    message_10=Message(frame, text="元").grid(row=9, column=7)
    message_11=Message(frame, text="元").grid(row=10, column=5)
    message_12=Message(frame, text="元").grid(row=10, column=7)
    message_13=Message(frame, text="元").grid(row=11, column=5)
    message_14=Message(frame, text="元").grid(row=11, column=7)

    # 空Frame以撑开空间
    Frame(frame, height=10).grid(row=5, column=4, columnspan=7)

    # 按钮，事件监听函数为calculate
    button_1=Button(frame, width=19, text="等额本息", command=calculate_1).grid(row=6, column=4, columnspan=1, pady=0)
    button_2=Button(frame, width=19, text="等额本金", command=calculate_2).grid(row=6, column=6, columnspan=1, pady=0)

    # 消息循环
    window.mainloop()

    # 按钮点击监听
def calculate_1():
         
        # 获取输入的参数
    global amountVar,rateVar,yearsVar,monthsVar,monthVar,total_1Var,totalInterest_1Var
    global totalRepayment_1Var,remain_1Var,monthRepayment_1Var,total_2Var
    global totalInterest_2Var,totalRepayment_2Var,remain_2Var,monthRepayment_2Var
    amount = eval(amountVar.get())
    rate = eval(rateVar.get()) / 100 / 12  # 将年化利率转为月利率，单位为1
    years = eval(yearsVar.get())
    months = eval(monthsVar.get())
    month = eval(monthVar.get())

    # 计算每月还款
    monthRepayment = amount * rate * ((1 + rate ) ** (years * 12)) / ((1 + rate ) ** (years * 12) - 1)

    # 将计算结果设置给控件
    total = monthRepayment * 12 * years  # 总还款金额
    total_1Var.set(format(total, ".3f"))

    totalInterest = total - amount  # 总利息
    totalInterest_1Var.set(format(totalInterest, '.3f'))

    if (months >= 0) and (months <= years * 12):  # 已还期数必须在贷款期数内
        totalRepayment = monthRepayment * months  # 已还金额
        remain = total - totalRepayment  # 剩余待还金额
        totalRepayment_1Var.set(format(totalRepayment, '.3f'))
        remain_1Var.set(format(remain, '.3f'))
    else:
        totalRepayment_1Var.set('已还期数输入有误!')
        remain_1Var.set('已还期数输入有误!')

    if (month >= 1) and (month <= years * 12):
        monthRepayment_1Var.set(format(monthRepayment, '.3f'))
    else:
        monthRepayment_1Var.set('第_月份输入有误!')

def calculate_2():
    """
    等额本金法计算函数
    """
    # 获取输入的参数
    global amountVar,rateVar,yearsVar,monthsVar,monthVar,total_1Var,totalInterest_1Var
    global totalRepayment_1Var,remain_1Var,monthRepayment_1Var,total_2Var
    global totalInterest_2Var,totalRepayment_2Var,remain_2Var,monthRepayment_2Var
    amount = eval(amountVar.get())
    rate = eval(rateVar.get()) / 100 / 12  # 将年化利率转为月利率，单位为1
    years = eval(yearsVar.get())
    months = eval(monthsVar.get())
    month = eval(monthVar.get())
    month_amount = amount / (years * 12)

    # 存储每月还款
    monthRepayment = []
    for i in range(1, (years * 12) + 1):
        monthpayment = month_amount + (amount - (i - 1) * month_amount) * rate
        monthRepayment.append(monthpayment)

    # 将计算结果设置给控件
    total = sum(monthRepayment)
    total_2Var.set(format(total, ".3f"))

    totalInterest = total - amount
    totalInterest_2Var.set(format(totalInterest, '.3f'))

    if (months >= 0) and (months <= years * 12):
        totalRepayment = sum(monthRepayment[:months])
        remain = total - totalRepayment
        totalRepayment_2Var.set(format(totalRepayment, '.3f'))
        remain_2Var.set(format(remain, '.3f'))
    else:
        totalRepayment_2Var.set('已还期数输入有误!')
        remain_2Var.set('已还期数输入有误!')

    if (month >= 1) and (month <= years * 12):
        monthRepayment_2Var.set(format(monthRepayment[month - 1], '.3f'))
    else:
        monthRepayment_2Var.set('第_月份输入有误!')


 
     
