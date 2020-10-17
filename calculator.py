# coding=gbk
from tkinter import *
from functools import partial
from calculate import *


# ���ɼ�����������
def buju(root):
    menu = Menu(root)  # �˵�
    submenu1 = Menu(menu, tearoff=0)  # �ִ���0Ϊ��ԭ����1Ϊ�����Ϊ��������
    menu.add_cascade(label='�༭', menu=submenu1)  # �����ѡ�label����Ϊ��ʾ���ݣ�
    submenu1.add_command(label='����', command=lambda: bianji(entry, 'copy'))  # �������
    submenu1.add_command(label='����', command=lambda: bianji(entry, 'cut'))
    submenu1.add_command(label='ճ��', command=lambda: bianji(entry, 'paste'))
    submenu2 = Menu(menu, tearoff=0)
    menu.add_cascade(label='�鿴', menu=submenu2)
    submenu2.add_command(label='����', command=lambda: chakan(entry, 'help'))
    submenu2.add_command(label='����', command=lambda: chakan(entry, 'author'))
    root.config(menu=menu)  # �������ã���Ӳ˵�

    label = Label(root, width=29, height=1, bd=5, bg='#FFFACD', anchor='se',
                  textvariable=label_text)  # ��ǩ��������ʾ���ֻ�ͼƬ
    label.grid(row=0, columnspan=5)  # ���������򴰿�ע�Ტ��ʾ�ؼ��� rowspan�����õ�Ԫ�������Խ������

    entry = Entry(root, width=23, bd=5, bg='#FFFACD', justify="right", font=('΢���ź�', 12))  # �ı��򣨵��У�
    entry.grid(row=1, column=0, columnspan=5, sticky=N + W + S + E, padx=5, pady=5)  # ���ÿؼ���Χx��y����հ���������С

    myButton = partial(Button, root, width=5, cursor='hand2', activebackground='#90EE90')  # ƫ���������й̶������ĺ���
    button_sin = myButton(text='sin', command=lambda: get_input(entry, 'sin('))  # ��ť
    button_arcsin = myButton(text='arcsin', command=lambda: get_input(entry, 'arcsin('))
    button_exp = myButton(text='e', command=lambda: get_input(entry, 'e'))
    button_ln = myButton(text='ln', command=lambda: get_input(entry, 'ln('))
    button_xy = myButton(text='x^y', command=lambda: get_input(entry, '^'))
    button_sin.grid(row=2, column=0)
    button_arcsin.grid(row=2, column=1)
    button_exp.grid(row=2, column=2)
    button_ln.grid(row=2, column=3)
    button_xy.grid(row=2, column=4)

    button_shanyige = myButton(text='��', command=lambda: backspace(entry))  # commandָ����ť��Ϣ�Ļص�����
    button_shanquanbu = myButton(text=' C ', command=lambda: clear(entry))
    button_zuokuohao = myButton(text='(', command=lambda: get_input(entry, '('))
    button_youkuohao = myButton(text=')', command=lambda: get_input(entry, ')'))
    button_genhao = myButton(text='��x', command=lambda: get_input(entry, '��('))
    button_shanyige.grid(row=3, column=0)
    button_shanquanbu.grid(row=3, column=1)
    button_zuokuohao.grid(row=3, column=2)
    button_youkuohao.grid(row=3, column=3)
    button_genhao.grid(row=3, column=4)

    button_7 = myButton(text=' 7 ', command=lambda: get_input(entry, '7'))
    button_8 = myButton(text=' 8 ', command=lambda: get_input(entry, '8'))
    button_9 = myButton(text=' 9 ', command=lambda: get_input(entry, '9'))
    button_chu = myButton(text=' / ', command=lambda: get_input(entry, '/'))
    button_yu = myButton(text='%', command=lambda: get_input(entry, '%'))
    button_7.grid(row=4, column=0)
    button_8.grid(row=4, column=1)
    button_9.grid(row=4, column=2)
    button_chu.grid(row=4, column=3)
    button_yu.grid(row=4, column=4)

    button_4 = myButton(text=' 4 ', command=lambda: get_input(entry, '4'))
    button_5 = myButton(text=' 5 ', command=lambda: get_input(entry, '5'))
    button_6 = myButton(text=' 6 ', command=lambda: get_input(entry, '6'))
    button_cheng = myButton(text=' * ', command=lambda: get_input(entry, '*'))
    button_jiecheng = myButton(text='������', command=lambda: jinzhi(entry))
    button_4.grid(row=5, column=0)
    button_5.grid(row=5, column=1)
    button_6.grid(row=5, column=2)
    button_cheng.grid(row=5, column=3)
    button_jiecheng.grid(row=5, column=4)

    button_1 = myButton(text=' 1 ', command=lambda: get_input(entry, '1'))
    button_2 = myButton(text=' 2 ', command=lambda: get_input(entry, '2'))
    button_3 = myButton(text=' 3 ', command=lambda: get_input(entry, '3'))
    button_jian = myButton(text=' - ', command=lambda: get_input(entry, '-'))
    button_dengyu = myButton(text=' \n = \n ', command=lambda: calculator(entry))
    button_1.grid(row=6, column=0)
    button_2.grid(row=6, column=1)
    button_3.grid(row=6, column=2)
    button_jian.grid(row=6, column=3)
    button_dengyu.grid(row=6, column=4, rowspan=2)  # rowspan�����õ�Ԫ������Խ������

    button_pai = myButton(text=' �� ', command=lambda: get_input(entry, '��'))
    button_0 = myButton(text=' 0 ', command=lambda: get_input(entry, '0'))
    button_xiaoshudian = myButton(text=' . ', command=lambda: get_input(entry, '.'))
    button_jia = myButton(text=' + ', command=lambda: get_input(entry, '+'))
    button_pai.grid(row=7, column=0)
    button_0.grid(row=7, column=1)
    button_xiaoshudian.grid(row=7, column=2)
    button_jia.grid(row=7, column=3)


# ���ı����е���ʽ��𰸽��и��ơ����л�ճ��
def bianji(entry, argu):
    """
    :param entry: �ı���
    :param argu: ��ť��Ӧ��ֵ
    """
    if argu == 'copy':
        entry.event_generate("<<Copy>>")
    elif argu == 'cut':
        entry.event_generate("<<Cut>>")
        clear(entry)
    elif argu == 'paste':
        entry.event_generate("<<Paste>>")


# �鿴ʹ�ð�����������Ϣ
def chakan(entry, argu):
    root = Tk()
    root.resizable(0, 0)
    text = Text(root, width=20, height=2, bd=5, bg='#FFFACD', font=('΢���ź�', 12))
    text.grid(padx=5, pady=5)
    if argu == 'help':
        root.title('����')
        text.insert(INSERT, '�����������򵥣�\n')
        text.insert(INSERT, '�ͱ����Ҫ�����ˣ�')
    elif argu == 'author':
        root.title('����')
        text.insert(INSERT, '�˼�����Ӣ����˳\n')
        text.insert(INSERT, 'Time��2020��')


# ɾ�����һ����������
def backspace(entry):
    entry.delete(len(entry.get()) - 1)  # ɾ���ı�������һ������ֵ


# ɾ�������������ݺ���ʾ����
def clear(entry):
    entry.delete(0, END)  # ɾ���ı������������
    label_text.set('')


# ������������밴ť�����ı������������
def get_input(entry, argu):
    formula = entry.get()
    for char in formula:
        if '\u4e00' <= char <= '\u9fa5':
            clear(entry)  # ɾ���ı����еĺ�����ʾ�������ֶ�ɾ������
    entry.insert(INSERT, argu)  # ʹ��ENDʱ����������Ͱ���������ϲ��������


# ʮ��������ת��Ϊ����������
def jinzhi(entry):
    try:
        formula = entry.get()
        if re.match('\d+$', formula):
            number = int(formula)
            cunchu = []  # ����ÿ�γ���2�������
            result = ''
            while number:
                cunchu.append(number % 2)
                number //= 2  # ��������,������
            while cunchu:
                result += str(cunchu.pop())  # �������������õõ����
            clear(entry)
            entry.insert(END, result)
            label_text.set(''.join(formula + '='))
        else:
            clear(entry)
            entry.insert(END, '������ʮ��������')
    except:
        clear(entry)
        entry.insert(END, '����')


# �����=������м���
def calculator(entry):
    try:
        formula = entry.get()
        # ��������ֻ�����ֻ�л�eʱ������ʾ������
        if re.match('-?[\d+,��,e]\.?\d*$', formula):
            label_text.set(''.join(formula + '='))
            return
        # ������������ʽʱ����ʾ�������
        result = final_calc(formula_format(formula))
        clear(entry)
        entry.insert(END, result)  # �����������ı�����
        label_text.set(''.join(formula + '='))
    except:
        clear(entry)
        entry.insert(END, '����')


def kexuejisuanqi():
    root = Tk()  # ���ɴ���
    root.title('�˼���ҵС����')  # ���ڵ�����
    root.resizable(0, 0)  # ���ڴ�С�ɵ��ԣ��ֱ��ʾx��y����Ŀɱ���
    global label_text  # ����ȫ�ֱ���
    label_text = StringVar()
    buju(root)
    root.mainloop()  # ������Ϣѭ����������������������ɵĴ���һ������
