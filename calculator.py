from tkinter import *
calculator = Tk()
calculator.geometry('450x400')
calculator.resizable(0,0)

x=IntVar()
y=IntVar()
z=IntVar()

def calculate_sum():
    a=x.get()
    b=y.get()
    c=a+b
    z.set(f'{a} + {b} = {a+b}')
    
def calculate_sub():
    a=x.get()
    b=y.get()
    c=a+b
    z.set(f'{a} - {b} = {a-b}')

def calculate_mul():
    a=x.get()
    b=y.get()
    c=a*b
    z.set(f'{a} * {b} = {a*b}')
    
def calculate_div():
    try:
        a=x.get()
        b=y.get()
        c=round(a/b,2)
        z.set(f'{a} / {b} = {c}')
    except:
        z.set('dividing by zero')
    

calculator_heading=Label(calculator,text='Calculator',font=25)
calculator_heading.place(x=160,y=50)

number1= Entry(calculator,text='number 1',textvariable=x)
number1.place(x=135,y=100)

number2= Entry(calculator,text='number 2',textvariable=y)
number2.place(x=135,y=140)

output = Label(calculator,textvariable=z)
output.place(x=150,y=180)

add = Button(calculator,text='+',width=2,height=1,font=(6),command=calculate_sum)
add.place(x=280,y=80)

sub = Button(calculator,text='-',width=2,height=1,font=(6),command=calculate_sub)
sub.place(x=280,y=115)

mul = Button(calculator,text='*',width=2,height=1,font=(6),command=calculate_mul)
mul.place(x=280,y=150)

div = Button(calculator,text='/',width=2,height=1,font=(6),command=calculate_div)
div.place(x=280,y=185)




