#Q1. Try out 'Canvas' widget from tkinter
#Q.2 'Tic-toc-toe' game code


# tic-toc-toe game

from tkinter import *
from tkinter import messagebox

# creating window
root1 = Tk()
root1.title("(EXP:5.2 TicTacToe Game")

clicked = True
count = 0

# button clicked function
def clicked_b(b):
    global clicked , count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked= False
        count = count +1
        XorO()
    elif b["text"] == " " and clicked == False :
        b["text"] = "O"
        clicked=True
        count = count +1
        XorO()
    else :
        messagebox.showerror("Tile already selected")

# to disable all tiles once game is over
def disable_tiles():
    b1.config(state = DISABLED)
    b2.config(state = DISABLED)
    b3.config(state = DISABLED)
    b4.config(state = DISABLED)
    b5.config(state = DISABLED)
    b6.config(state = DISABLED)
    b7.config(state = DISABLED)
    b8.config(state = DISABLED)
    b9.config(state = DISABLED)

# to check who won
def XorO() :
    global winner
    winner = False
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg = "light blue")
        b2.config(bg = "light blue")
        b3.config(bg = "light blue")
        winner = True
        messagebox.showinfo("X WON !!!")
        disable_tiles()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg = "light blue")
        b5.config(bg = "light blue")
        b6.config(bg = "light blue")
        winner = True
        messagebox.showinfo("X WON !!!")
        disable_tiles()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg = "light blue")
        b8.config(bg = "light blue")
        b9.config(bg = "light blue")
        winner = True
        messagebox.showinfo("X WON !!!")
        disable_tiles()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg = "light blue")
        b5.config(bg = "light blue")
        b9.config(bg = "light blue")
        winner = True
        messagebox.showinfo("X WON !!!")
        disable_tiles()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg = "light blue")
        b5.config(bg = "light blue")
        b7.config(bg = "light blue")
        winner = True
        messagebox.showinfo("X WON !!!")
        disable_tiles()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg = "light blue")
        b4.config(bg = "light blue")
        b7.config(bg = "light blue")
        winner = True
        messagebox.showinfo("X WON !!!")
        disable_tiles()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg = "light blue")
        b5.config(bg = "light blue")
        b8.config(bg = "light blue")
        winner = True
        messagebox.showinfo("X WON !!!")
        disable_tiles()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg = "light blue")
        b6.config(bg = "light blue")
        b9.config(bg = "light blue")
        winner = True
        messagebox.showinfo("X WON !!!")
        disable_tiles()

    # to check for O
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg = "light blue")
        b2.config(bg = "light blue")
        b3.config(bg = "light blue")
        winner = True
        messagebox.showinfo("O WON !!!")
        disable_tiles()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg = "light blue")
        b5.config(bg = "light blue")
        b6.config(bg = "light blue")
        winner = True
        messagebox.showinfo("O WON !!!")
        disable_tiles()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg = "light blue")
        b8.config(bg = "light blue")
        b9.config(bg = "light blue")
        winner = True
        messagebox.showinfo("O WON !!!")
        disable_tiles()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg = "light blue")
        b5.config(bg = "light blue")
        b9.config(bg = "light blue")
        winner = True
        messagebox.showinfo("O WON !!!")
        disable_tiles()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg = "light blue")
        b5.config(bg = "light blue")
        b7.config(bg = "light blue")
        winner = True
        messagebox.showinfo("O WON !!!")
        disable_tiles()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg = "light blue")
        b4.config(bg = "light blue")
        b7.config(bg = "light blue")
        winner = True
        messagebox.showinfo("O WON !!!")
        disable_tiles()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg = "light blue")
        b5.config(bg = "light blue")
        b8.config(bg = "light blue")
        winner = True
        messagebox.showinfo("O WON !!!")
        disable_tiles()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg = "light blue")
        b6.config(bg = "light blue")
        b9.config(bg = "light blue")
        winner = True
        messagebox.showinfo("O WON !!!")
        disable_tiles()

# creating game tiles uding button
b1 = Button(root1,text = " ",font = 30,height = 10, width =20,bg = "SystemButtonFace", command = lambda:clicked_b(b1))
b2 = Button(root1,text = " ",font = 30,height = 10, width =20,bg = "SystemButtonFace", command = lambda:clicked_b(b2))
b3 = Button(root1,text = " ",font = 30,height = 10, width =20,bg = "SystemButtonFace", command = lambda:clicked_b(b3))

b4 = Button(root1,text = " ",font = 30,height = 10, width =20,bg = "SystemButtonFace", command = lambda:clicked_b(b4))
b5 = Button(root1,text = " ",font = 30,height = 10, width =20,bg = "SystemButtonFace", command = lambda:clicked_b(b5))
b6 = Button(root1,text = " ",font = 30,height = 10, width =20,bg = "SystemButtonFace", command = lambda:clicked_b(b6))

b7 = Button(root1,text = " ",font = 30,height = 10, width =20,bg = "SystemButtonFace", command = lambda:clicked_b(b7))
b8 = Button(root1,text = " ",font = 30,height = 10, width =20,bg = "SystemButtonFace", command = lambda:clicked_b(b8))
b9 = Button(root1,text = " ",font = 30,height = 10, width =20,bg = "SystemButtonFace", command = lambda:clicked_b(b9))

# gridding the tiles
b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)

b4.grid(row=1,column=0)
b5.grid(row=1,column=1)
b6.grid(row=1,column=2)

b7.grid(row=2,column=0)
b8.grid(row=2,column=1)
b9.grid(row=2,column=2)


root1.mainloop()
