from tkinter import *
from tkinter import messagebox
from raina_bethea_hw3 import *

# start game command for button that intiliazes game and text component
i = 1

def game():
   elimination_game(int(n.get()),int(k.get())) 
   gameLog.insert(END, f"Round {i+1}: {str(eliminated.data)} eliminated!")

def initialize(num):
    global n, k, node1
    current=node1
    node1=None
    previous=None
    for i in range(1, num+1):
        new_node=CaterpillarListNode(f"Player{i}")
        if not node1:
            node1=new_node
        else:
            previous.nxt=new_node
        previous= new_node
    current= node1
    for i in range(num):
        Label(root,text=str(current.data),relief='solid', bd=2).grid(row=i, column=2)
        current = current.nxt
    # create elimination button
    elimination = Button(root, text="Elimate", width=15,command=game)
    elimination.grid(row=num+2, column=2)

        
def startGame():
    global n, k
    nValue = int(n.get())
    kValue = int(k.get())
    if (((nValue >12) and (nValue <= 1)) or (kValue<=1)):
        messagebox.showinfo(message='Allowed Valuse: \n 1<N<12\n K>=1 ')
    else:
        gameLog.insert(END, f"Game Started! N={nValue} K={kValue}\n")
        initialize(nValue)
        
root = Tk()
root.geometry("1000x900")
root.title('Very Hungry Caterpillar Game')

# input area for player n and k values
Label(root, text='N').grid(row=0)
Label(root, text='K').grid(row=1)
n = Entry(root)
k = Entry(root)
n.grid(row=0, column=1)
k.grid(row=1, column=1)

# text widget to show log of what is happening in game
gameLog = Text(master=root, height=30,width=100,)
gameLog.grid(row=20, column=1)

# button to start the game
button = Button(root,text='Start Game', width=25, command=startGame)
button.grid(row=3, column =0, columnspan=2 )


root.mainloop()



