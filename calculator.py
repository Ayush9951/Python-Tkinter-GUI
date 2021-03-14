from tkinter import *
calculator = Tk()
calculator.geometry('450x400')
calculator.resizable(0,0)

num1 = IntVar()
num2 = IntVar()
result = IntVar()

def calculate_sum():
    a = num1.get()
    b = num2.get()
    result.set(f'{a} + {b} = {a+b}')
    
def calculate_sub():
    a = num1.get()
    b = num2.get()
    result.set(f'{a} - {b} = {a-b}')

def calculate_mul():
    a = num1.get()
    b = num2.get()
    result.set(f'{a} * {b} = {a*b}')
    
def calculate_div():
    try:
        a = num1.get()
        b = num2.get()
        c = round(a/b,2)
        result.set(f'{a} / {b} = {c}')
    except:
        result.set('dividing by zero')
    

calculator_heading = Label(calculator,text = 'Calculator',font = 25)
calculator_heading.place(x = 160,y = 50)

number1 = Entry(calculator,textvariable = num1)
number1.place(x = 135,y = 100)

number2 = Entry(calculator,textvariable = num2)
number2.place(x = 135,y = 140)

output = Label(calculator,textvariable = result)
output.place(x = 150,y = 180)

add = Button(calculator,text = '+',width = 2,height = 1,font = 6,command = calculate_sum)
add.place(x = 280,y = 80)

sub = Button(calculator,text = '-',width = 2,height = 1,font = 6,command = calculate_sub)
sub.place(x = 280,y = 115)

mul = Button(calculator,text = '*',width = 2,height = 1,font = 6,command = calculate_mul)
mul.place(x = 280,y = 150)

div = Button(calculator,text = '/',width = 2,height = 1,font = 6,command = calculate_div)
div.place(x = 280,y = 185)




