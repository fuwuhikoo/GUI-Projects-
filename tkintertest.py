from tkinter import *

top = Tk()
playlistList = []
myRolls = []
rollTimes = 0
dieType = 0 

def results():
    print(playlistList)

def addToList():
    newItem = E1.get()
    playlistList.append(newItem)
    E1.delete(0, END)

def exportList():
    with open('test.text', 'w') as f:
        for item in playlistList:
            f.write("%s/n" % item)

def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUIs")
    LMain.grid(column = 2, row = 1) 

    B1Main = Button(text = "Week 1", bg = "white", command = week1)
    B1Main.grid(column = 2, row = 2)
    
    B2Main = Button(text ="Week 2", bg = "white")
    B2Main.grid(column = 2, row = 3)
    
    B3Main = Button(text = "Week 3", bg = "white")
    B3Main.grid(column = 2, row = 4)


def week1():
    clearWindow()
    #This is a Label widget 
    L1 = Label(top, text="Playlist Maker")
    L1.grid(column= 0, row = 1)

    LMain = Label(top, text = "Block 1 GUIs")
    LMain.grid(column= 0, row = 2) 

    #This is a Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column = 0, row = 2)

    #This is a Button widget
    B1 = Button(text =  "    print playlist    ", bg = "#c6edee", command = results )
    B1.grid(column= 0, row = 3) 

    B2 = Button(text = " add song ", bg = "#feebe5", command = addToList)
    B2.grid(column = 1, row = 2)

    B3 = Button(text = "export list", bg = "#ceb0af", command= exportList)
    B3.grid(column = 0, row = 4)

    """
    Bclear = Button(text = "Clear Window", bg = "white", command = clearWIndow)
    Blear.grid(column = 3, row = 1)
    """

def week2():
    def rollDice():
        #update variable data
        dieType = E1W2.get()
        rollTimes = E2W2.get()
        #Clear window AFTER pulling entry data
        clearWindow()
        #roll the dice
        for x in range(0, int(rollTimes)):
            myRolls.append(random.randint(1, int(dieType)))
            
        #build the results window
        L4W2 = Label(top, text= "Here are your rolls!")
        L4W2.grid(column= 0, row= 1)
        #this one will use a .format() statement 
        L5W2 = Label(top, text = "{}".format(myRolls))
        L5W2.grid(column = 0, row = 2)
        
        B2W2 = Button(text= "Main Menu", bg= "black", command = mainMenu)
        B2W2.grid(column= 0, row = 3)
            
    clearWindow()
    B1Week2 = Button(text="Roll em!", bg="yellow", command = rollDice)
    B1Week2.grid(column = 2, row= 4)

    L1Week2 = Label(top, text= "Dice Roller App")
    L1Week2.grid(column= 2, row= 1) 
    
    clearWindow()
    L1W2 = Label(top, text="Dice Roller Program")
    L1W2.grid(column = 0, row = 1)

    L2W2 = Label(top, text = "How many sides?")
    L2W2.grid(column = 0, row = 2)

    L3W2 = Label(top, text = "How many rolls?") 
    L3W2.grid(column= 2, row= 2)

    E1W2 = Entry(top, bd = 5)
    EE1W2.grid(column = 0, row = 3)

    E2W2 = Entry(top, bd = 5)
    E2W2.grid(column= 2, row=4)

    #to add: roll function and exit button

if __name__ == "__main__":
    mainMenu()
top.mainloop()
