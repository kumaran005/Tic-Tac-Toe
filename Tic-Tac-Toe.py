from tkinter import *
from tkinter import messagebox

root =Tk()
root.title("Tic Tac Toe")

#players
player_a = StringVar()
player_b = StringVar()

p1 = StringVar()
p2 = StringVar()

root.configure(bg="#cb464e")

player1_name =Entry(root,textvariable=p1,bd=5,bg="#fcfcec",width=40)
player1_name.grid(row=1,column=1,columnspan=8)

player2_name = Entry(root,textvariable=p2,bd=5,bg="#fcfcec",width=40)
player2_name.grid(row=2,column=1,columnspan=8)

bclick = True
flag = 0

def disableButton():
    button1.configure(state = DISABLED)
    button2.configure(state = DISABLED)
    button3.configure(state = DISABLED)
    button4.configure(state = DISABLED)
    button5.configure(state = DISABLED)
    button6.configure(state = DISABLED)
    button7.configure(state = DISABLED)
    button8.configure(state = DISABLED)
    button9.configure(state = DISABLED)

def btnClick(buttons):
    global bclick,flag,player2_name,player1_name,player_b,player_a

    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        player_b = p2.get()+"Wins!"
        player_a = p1.get()+"Wins!"
        checkForWin()
        flag += 1
    
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    
    else:
        messagebox.showinfo("Ti-Tac-Toe","Button already clicked!")

def checkForWin():
    if(button1["text"] == 'X' and 
       button2["text"] == 'X' and
       button3["text"] == 'X' or 
       button4["text"] == 'X' and 
       button5["text"] == 'X' and
       button6["text"] == 'X' or 
       button7["text"] == 'X' and 
       button8["text"] == 'X' and
       button9["text"] == 'X' or 
       button1["text"] == 'X' and 
       button5["text"] == 'X' and
       button9["text"] == 'X' or 
       button3["text"] == 'X' and 
       button5["text"] == 'X' and
       button7["text"] == 'X' or 
       button1["text"] == 'X' and 
       button4["text"] == 'X' and
       button7["text"] == 'X' or 
       button2["text"] == 'X' and 
       button5["text"] == 'X' and
       button8["text"] == 'X' or 
       button3["text"] == 'X' and 
       button6["text"] == 'X' and
       button9["text"] == 'X'):
        disableButton()
        messagebox.showinfo("Tic-Tac-Toe",player_a)
    
    elif(flag == 8):
        messagebox.showinfo("Tic-Toc-Toe","It is a Tie")
    
    elif(button1["text"] =='O' and 
        button2["text"] == 'O' and
        button3["text"] == 'O' or 
        button4["text"] == 'O' and 
        button5["text"] == 'O' and
        button6["text"] == 'O' or 
        button7["text"] == 'O' and 
        button8["text"] == 'O' and
        button9["text"] == 'O' or 
        button1["text"] == 'O' and 
        button5["text"] == 'O' and
        button9["text"] == 'O' or 
        button3["text"] == 'O' and
        button5["text"] == 'O' and
        button7["text"] == 'O' or 
        button1["text"] == 'O' and 
        button4["text"] == 'O' and
        button7["text"] == 'O' or 
        button2["text"] == 'O' and 
        button5["text"] == 'O' and
        button8["text"] == 'O' or 
        button3["text"] == 'O' and 
        button6["text"] == 'O' and
        button9["text"] == 'O'):    
        disableButton()
        messagebox.showinfo("Tic-Tac-Toe",player_b)

buttons = StringVar()

label = Label(root,text="Player 1:",font="Times 20 bold",
bg="#cb464e",fg="#fcfcec",height=1,width=8)
label.grid(row=1,column=0)

label = Label(root,text="Player 2:",font="Times 20 bold",
bg="#cb464e",fg="#fcfcec",height=1,width=8)
label.grid(row=2,column=0)

button1 = Button(root,text=' ',font='Times 20 bold',
bg="#4b7fa4",fg="#fcfcec",height=4,width=8,
command=lambda:btnClick(button1))
button1.grid(row=3,column=0)

button2 = Button(root,text=' ',font='Times 20 bold',
bg="#4b7fa4",fg="#fcfcec",height=4,width=8,
command=lambda:btnClick(button2))
button2.grid(row=3,column=1)

button3 = Button(root,text=' ',font='Times 20 bold',
bg="#4b7fa4",fg="#fcfcec",height=4,width=8,
command=lambda:btnClick(button3))
button3.grid(row=3,column=2)

button4 = Button(root,text=' ',font='Times 20 bold',
bg="#4b7fa4",fg="#fcfcec",height=4,width=8,
command=lambda:btnClick(button4))
button4.grid(row=4,column=0)

button5 = Button(root,text=' ',font='Times 20 bold',
bg="#4b7fa4",fg="#fcfcec",height=4,width=8,
command=lambda:btnClick(button5))
button5.grid(row=4,column=1)

button6 = Button(root,text=' ',font='Times 20 bold',
bg="#4b7fa4",fg="#fcfcec",height=4,width=8,
command=lambda:btnClick(button6))
button6.grid(row=4,column=2)

button7 = Button(root,text=' ',font='Times 20 bold',
bg="#4b7fa4",fg="#fcfcec",height=4,width=8,
command=lambda:btnClick(button7))
button7.grid(row=5,column=0)

button8 = Button(root,text=' ',font='Times 20 bold',
bg="#4b7fa4",fg="#fcfcec",height=4,width=8,
command=lambda:btnClick(button8))
button8.grid(row=5,column=1)

button9 = Button(root,text=' ',font='Times 20 bold',
bg="#4b7fa4",fg="#fcfcec",height=4,width=8,
command=lambda:btnClick(button9))
button9.grid(row=5,column=2)

root.mainloop()