# coding=gbk
import re
from math import *
from decimal import Decimal
from decimal import getcontext

#���ַ��������ʽ��������Ż��Ǽ��ŵ�����
def formula_format(formula):
    """
    ��ʽ
    """
    formula=re.sub(' ','',formula)
    #ȥ���ո�
    formula_list=[i for i in re.split('(-[\d+,math.pi,e]\.?\d*)',formula)if i]#-[\d+,math.pi,e]\.?\d*���ֵ�������ʽ
    final_formula=[]
    for item in formula_list:
        #�����ʽ�Ժ�ܿ�ͷ�����һ������Ϊ���������Ϊ����
        if len(final_formula)==0 and re.match('-[\d+,math.pi,e]\.?\d*',item):
            final_formula.append(item)
            continue
        #������һ�������������ô���������
        if len(final_formula) > 0:
            if re.match('[\+\-\*\/\(\%\^]$', final_formula[-1]):
                final_formula.append(item)
                continue
        # ����������ָ
        item_split = [i for i in re.split('([\+\-\*\/\(\)\%\^\��])', item) if i]
        final_formula += item_split
    return final_formula


# �ж��Ƿ��������������Ƿ���True
def is_operator(e):
    """
    :param e: str
    :return: bool
    """
    opers = ['+', '-', '*', '/', '(', ')', '%', '^', '��', 'sin', 'arcsin', 'ln']
    return True if e in opers else False  # ��forѭ����Ƕ��ʹ��if��else���


# �Ƚ�����������������ж���ѹջ���ǵ�ջ
def decision(tail_op, now_op):
    """
    :param tail_op: �����ջ�����һ�������
    :param now_op: ����ʽ�б�ȡ���ĵ�ǰ�����
    :return: 1����ջ���㣬0�����������ջ���һ��Ԫ��'('��-1��ʾѹջ
    """
    # ����4�����������
    rate1 = ['+', '-']
    rate2 = ['*', '/', '%']
    rate3 = ['^', '��', 'sin', 'arcsin', 'ln']
    rate4 = ['(']
    rate5 = [')']

    if tail_op in rate1:
        if now_op in rate2 or now_op in rate3 or now_op in rate4:
            return -1  # ˵����ǰ��������ȼ����������ջ�����һ�����������Ҫѹջ
        else:
            return 1  # ˵����ǰ��������ȼ����������ջ�����һ�����������Ҫ��ջ����

    elif tail_op in rate2:
        if now_op in rate3 or now_op in rate4:
            return -1
        else:
            return 1

    elif tail_op in rate3:
        if now_op in rate4:
            return -1
        else:
            return 1

    elif tail_op in rate4:
        if now_op in rate5:
            return 0  # '('����')',��Ҫ����'('������')',�����������ڵ���ʽ�Ѽ�����ɲ������ѹ������ջ��
        else:
            return -1  # ֻҪջ��Ԫ��Ϊ'('�ҵ�ǰԪ�ز���')'����Ӧѹ��ջ��


# �����������֣�һ��������������������ͬ������Ӧ���
def calculate(   n11,   n21, operator):
    """
    :param n1: float
    :param n2: float
    :param operator: + - * / % ^
    :return: float
    """
    result = 0
    n1=Decimal(n11)
    n2=Decimal(n21)
    getcontext().prec=10
    if operator == '+':
        result = n1 + n2
    if operator == '-':
        result = n1 - n2
    if operator == '*':
        result = n1 * n2
    if operator == '/':
        result = n1 / n2
    if operator == '%':
        result = n1 % n2
    if operator == '^':
        result = n1 ** n2
     
    return result


# �����ڵ���ʽ����������󣬼����()��sin()��arcsin()
def gaojie(op_stack, num_stack):
    if op_stack[-1] == '��':
        op = op_stack.pop()
        num2 = Decimal(num_stack.pop())
        num_stack.append(sqrt(num2))
    elif op_stack[-1] == 'sin':
        op = op_stack.pop()
        num2 = Decimal(num_stack.pop())
        num_stack.append(sin(num2))
    elif op_stack[-1] == 'arcsin':
        op = op_stack.pop()
        num2 =Decimal(num_stack.pop())
        num_stack.append(asin(num2))
    elif op_stack[-1] == 'ln':
        op = op_stack.pop()
        num2 = Decimal(num_stack.pop())
        num_stack.append(log(num2))


# ���������ʽ�б��е��ַ�������ѹ������ջ�л�ѹ�������ջ�л�ջ����
def final_calc(formula_list):
    """
    :param formula_list: ��ʽ�б�
    :return: ������
    """
    num_stack = []  # ����ջ
    op_stack = []  # �����ջ
    for item in formula_list:
        operator = is_operator(item)
        # ѹ������ջ
        if not operator:
            # �к�eת���ɿ����ڼ����ֵ
            if item == '��':
                num_stack.append(pi)
            elif item == '-��':
                num_stack.append(-pi)
            elif item == 'e':
                num_stack.append(e)
            elif item == '-e':
                num_stack.append(-e)
            else:
                num_stack.append(float(item))  # �ַ���ת��Ϊ������
        # ����������
        else:
            while True:
                # ��������ջΪ�գ�����������ջ
                if len(op_stack) == 0:
                    op_stack.append(item)
                    break
                # ����ѹջ��ջ
                tag = decision(op_stack[-1], item)
                # �����-1����ѹ�������ջ��������һ��ѭ��
                if tag == -1:
                    op_stack.append(item)
                    break
                # �����0���򵯳������ջ�����һ��'('��������ǰ')'��������һ��ѭ��
                elif tag == 0:
                    op_stack.pop()
                    gaojie(op_stack, num_stack)  # '('ǰ��'��'��'sin'��'arcsin'ʱ������������ʽ�ļ���������Ӧ������
                    break
                # �����1���򵯳������ջ�����һ��Ԫ�غ�����ջ���������Ԫ��
                elif tag == 1:
                    if item in ['��', 'sin', 'arcsin']:
                        op_stack.append(item)
                        break
                    op = op_stack.pop()
                     
                    num2 = Decimal(num_stack.pop())
                    num1 = Decimal(num_stack.pop())
                    # ��������ѹ������ջ������ѭ����ֱ������break����ѭ��
                    num_stack.append(calculate(num1, num2, op))
    # ��ѭ������������ջ�������ջ�п��ܻ���Ԫ�ص����
    while len(op_stack) != 0:
        op = op_stack.pop()
        num2 = Decimal(num_stack.pop())
        num1 = Decimal(num_stack.pop())
        num_stack.append(calculate(num1, num2, op))
    result = str(num_stack[0])
    # ȥ����Ч��0��С���㣬����1.0ת��Ϊ1
    while True :
        if result[len(result) - 1] == '0' and '.' in result:
            result = result[0:-1]
        else:
            break
    return result


if __name__ == '__main__':
    # formula = "2 * ( 3 - 5 * ( - 6 + 3 * 2 / 2 ) )"
    formula = "1.25-1.24"
    formula_list = formula_format(formula)
    result = final_calc(formula_list)
    print("��ʽ��", formula)
    print("��������", result)  
        
    
        
