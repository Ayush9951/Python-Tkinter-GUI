from tkinter import *
playing_board = Tk()
playing_board.geometry('400x400')
playing_board.resizable(0,0)

turns = 0
result = StringVar()

def play(button):

    global turns
    
    if(turns % 2 == 0):
        if(button['text'] == ''):
            button['text'] = 'O'
    else:
         if(button['text'] == ''):
            button['text'] = 'X'

    turns = turns + 1
    
    if(b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O'):
        result.set('player 1 is winner')
        
    elif(b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O'):
        result.set('player 1 is winner')
        
    elif(b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O'):
        result.set('player 1 is winner')
        
    elif(b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X'):
        result.set('player 2 is winner')
        
    elif(b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X'):
        result.set('player 2 is winner')
        
    elif(b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X'):
        result.set('player 2 is winner')
        
    elif(b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O'):
        result.set('player 1 is winner')
        
    elif(b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O'):
        result.set('player 1 is winner')
        
    elif(b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
        result.set('player 1 is winner')
        
    elif(b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X'):
        result.set('player 2 is winner')
        
    elif(b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X'):
        result.set('player 2 is winner')
        
    elif(b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
        result.set('player 2 is winner')
        
    elif(turns == 9):
        result.set('Game Tied')

b1 = Button(playing_board,text = '',height = 5,width = 10,command = lambda : play(b1))
b1.grid(row = 0,column = 0)

b2 = Button(playing_board,text = '',height = 5,width = 10,command = lambda : play(b2))
b2.grid(row = 0,column = 1)

b3 = Button(playing_board,text = '',height = 5,width = 10,command = lambda : play(b3))
b3.grid(row = 0,column = 2)

b4 = Button(playing_board,text = '',height = 5,width = 10,command = lambda : play(b4))
b4.grid(row = 1,column = 0)

b5 = Button(playing_board,text = '',height = 5,width = 10,command = lambda : play(b5))
b5.grid(row = 1,column = 1)

b6 = Button(playing_board,text = '',height = 5,width = 10,command = lambda : play(b6))
b6.grid(row = 1,column = 2)

b7 = Button(playing_board,text = '',height = 5,width = 10,command = lambda : play(b7))
b7.grid(row = 2,column = 0)

b8 = Button(playing_board,text = '',height = 5,width = 10,command = lambda : play(b8))
b8.grid(row = 2,column = 1)

b9 = Button(playing_board,text = '',height = 5,width = 10,command = lambda : play(b9))
b9.grid(row = 2,column = 2)

match_result = Label(playing_board,textvariable = result)
match_result.place(x = 80,y = 300)


