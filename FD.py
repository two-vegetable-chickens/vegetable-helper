# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 22:28:38 2020

@author: 16434
"""


from tkinter import *


class Calculator:
    def __init__(self):
        window = Tk()  # 建立窗口
        window.title("房贷计算器")  # 命名窗口标题

        # 定义StringVar对象动态存储输入框的值
        self.amountVar = StringVar()  # 贷款金额
        self.rateVar = StringVar()  # 年化利率
        self.yearsVar = StringVar()  # 贷款年限
        self.monthsVar = StringVar()  # 已还期数
        self.monthVar = StringVar()  # 第i月
        self.total_1Var = StringVar()  # 等额本息总还款额
        self.totalInterest_1Var = StringVar()  # 等额本息总利息
        self.totalRepayment_1Var = StringVar()  # 等额本息累计已还
        self.remain_1Var = StringVar()  # 等额本息待还金额
        self.monthRepayment_1Var = StringVar()  # 等额本息第i月应还
        self.total_2Var = StringVar()  # 等额本金总还款额
        self.totalInterest_2Var = StringVar()  # 等额本金总利息
        self.totalRepayment_2Var = StringVar()  # 等额本金累计已还
        self.remain_2Var = StringVar()  # 等额本金待还金额
        self.monthRepayment_2Var = StringVar()  # 等额本金第i月应还

        # 设置一些默认值
        self.monthsVar.set("0")
        self.monthVar.set('1')

        # 整体面板，设置总体的边距
        frame = Frame(window)
        frame.pack(padx=20, pady=20)

        """
        添加标签
        .grid(row, column)设置标签位置
        """
        Label(frame, text="贷款金额").grid(row=1, column=1, columnspan=3)
        Label(frame, text="年化利率").grid(row=2, column=1, columnspan=3)
        Label(frame, text="贷款年限").grid(row=3, column=1, columnspan=3)
        Label(frame, text="已还期数").grid(row=4, column=1, columnspan=3)
        Label(frame, text="总还款额").grid(row=7, column=1, columnspan=3)
        Label(frame, text="总利息额").grid(row=8, column=1, columnspan=3)
        Label(frame, text="累计已还").grid(row=9, column=1, columnspan=3)
        Label(frame, text="剩余待还").grid(row=10, column=1, columnspan=3)
        Label(frame, text="第").grid(row=11, column=1)
        Label(frame, text="月应还").grid(row=11, column=3)

        """
        添加输入和输出框
        textvariable = self.amountVar 由相应的StringVar对象动态保存输入框中的文本
        justify=RIGHT 输入框中的文本右对齐
        sticky=E 控件在单元格中右对齐
        """
        Entry(frame, justify=RIGHT, textvariable=self.amountVar).grid(row=1, column=4)
        Entry(frame, justify=RIGHT, textvariable=self.rateVar).grid(row=2, column=4)
        Entry(frame, justify=RIGHT, textvariable=self.yearsVar).grid(row=3, column=4)
        Entry(frame, justify=RIGHT, textvariable=self.monthsVar).grid(row=4, column=4)
        Entry(frame, width=4, justify=CENTER, textvariable=self.monthVar).grid(row=11, column=2)
        Label(frame, textvariable=self.total_1Var).grid(row=7, column=4, sticky=E)
        Label(frame, textvariable=self.total_2Var).grid(row=7, column=6, sticky=E)
        Label(frame, textvariable=self.totalInterest_1Var).grid(row=8, column=4, sticky=E)
        Label(frame, textvariable=self.totalInterest_2Var).grid(row=8, column=6, sticky=E)
        Label(frame, textvariable=self.totalRepayment_1Var).grid(row=9, column=4, sticky=E)
        Label(frame, textvariable=self.totalRepayment_2Var).grid(row=9, column=6, sticky=E)
        Label(frame, textvariable=self.remain_1Var).grid(row=10, column=4, sticky=E)
        Label(frame, textvariable=self.remain_2Var).grid(row=10, column=6, sticky=E)
        Label(frame, textvariable=self.monthRepayment_1Var).grid(row=11, column=4, sticky=E)
        Label(frame, textvariable=self.monthRepayment_2Var).grid(row=11, column=6, sticky=E)

        # 添加Message存储单位
        Message(frame, text="元").grid(row=1, column=5)
        Message(frame, text="%").grid(row=2, column=5)
        Message(frame, text="年").grid(row=3, column=5)
        Message(frame, text="月").grid(row=4, column=5)
        Message(frame, text="元").grid(row=7, column=5)
        Message(frame, text="元").grid(row=7, column=7)
        Message(frame, text="元").grid(row=8, column=5)
        Message(frame, text="元").grid(row=8, column=7)
        Message(frame, text="元").grid(row=9, column=5)
        Message(frame, text="元").grid(row=9, column=7)
        Message(frame, text="元").grid(row=10, column=5)
        Message(frame, text="元").grid(row=10, column=7)
        Message(frame, text="元").grid(row=11, column=5)
        Message(frame, text="元").grid(row=11, column=7)

        # 空Frame以撑开空间
        Frame(frame, height=10).grid(row=5, column=4, columnspan=7)

        # 按钮，事件监听函数为calculate
        Button(frame, width=19, text="等额本息", command=self.calculate_1).grid(row=6, column=4, columnspan=1, pady=0)
        Button(frame, width=19, text="等额本金", command=self.calculate_2).grid(row=6, column=6, columnspan=1, pady=0)

        # 消息循环
        window.mainloop()

    # 按钮点击监听
    def calculate_1(self):
        """
        等额本息法计算函数
        """
        # 获取输入的参数
        amount = eval(self.amountVar.get())
        rate = eval(self.rateVar.get()) / 100 / 12  # 将年化利率转为月利率，单位为1
        years = eval(self.yearsVar.get())
        months = eval(self.monthsVar.get())
        month = eval(self.monthVar.get())

        # 计算每月还款
        monthRepayment = amount * rate * ((1 + rate ) ** (years * 12)) / ((1 + rate ) ** (years * 12) - 1)

        # 将计算结果设置给控件
        total = monthRepayment * 12 * years  # 总还款金额
        self.total_1Var.set(format(total, ".3f"))

        totalInterest = total - amount  # 总利息
        self.totalInterest_1Var.set(format(totalInterest, '.3f'))

        if (months >= 0) and (months <= years * 12):  # 已还期数必须在贷款期数内
            totalRepayment = monthRepayment * months  # 已还金额
            remain = total - totalRepayment  # 剩余待还金额
            self.totalRepayment_1Var.set(format(totalRepayment, '.3f'))
            self.remain_1Var.set(format(remain, '.3f'))
        else:
            self.totalRepayment_1Var.set('已还期数输入有误!')
            self.remain_1Var.set('已还期数输入有误!')

        if (month >= 1) and (month <= years * 12):
            self.monthRepayment_1Var.set(format(monthRepayment, '.3f'))
        else:
            self.monthRepayment_1Var.set('第_月份输入有误!')

    def calculate_2(self):
        """
        等额本金法计算函数
        """
        # 获取输入的参数
        amount = eval(self.amountVar.get())
        rate = eval(self.rateVar.get()) / 100 / 12  # 将年化利率转为月利率，单位为1
        years = eval(self.yearsVar.get())
        months = eval(self.monthsVar.get())
        month = eval(self.monthVar.get())
        month_amount = amount / (years * 12)

        # 存储每月还款
        monthRepayment = []
        for i in range(1, (years * 12) + 1):
            monthpayment = month_amount + (amount - (i - 1) * month_amount) * rate
            monthRepayment.append(monthpayment)

        # 将计算结果设置给控件
        total = sum(monthRepayment)
        self.total_2Var.set(format(total, ".3f"))

        totalInterest = total - amount
        self.totalInterest_2Var.set(format(totalInterest, '.3f'))

        if (months >= 0) and (months <= years * 12):
            totalRepayment = sum(monthRepayment[:months])
            remain = total - totalRepayment
            self.totalRepayment_2Var.set(format(totalRepayment, '.3f'))
            self.remain_2Var.set(format(remain, '.3f'))
        else:
            self.totalRepayment_2Var.set('已还期数输入有误!')
            self.remain_2Var.set('已还期数输入有误!')

        if (month >= 1) and (month <= years * 12):
            self.monthRepayment_2Var.set(format(monthRepayment[month - 1], '.3f'))
        else:
            self.monthRepayment_2Var.set('第_月份输入有误!')


if __name__ == '__main__':
    Calculator()
    pass