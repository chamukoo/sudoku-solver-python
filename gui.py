from tkinter import *


window = Tk()
window.title("Sudoku Solver")
window.geometry("370x480")


label = Label(window, text="Welcome to Sudoku Generator and Solver!",
              font=("Helvetica", 12), fg="black", pady = 10)
label.grid(row=0, column=1,columnspan=10)

# For unsolvavble sudoku puzzle
errorLabel = Label(window, text="", fg="red", font=("Arial", 16))
errorLabel.grid(row=20, column=1, columnspan=10, pady=20)

# For solvable sudoku puzzle
solvedLable = Label(window, text="", fg="green", font=("Arial", 16))
solvedLable.grid(row=20, column=1, columnspan=10, pady=20)

cells = {}


# Checking the validity of numbers
def isValid(P):
    out = (P.isdigit() or P=="") and len(P) < 2
    return out

reg = window.register(isValid)


# Drawing the 3x3 Grid
def draw3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            userInput = Entry(window, width=5, bg=bgcolor, fg='black', 
                              font=('Arial', 10, 'bold'), justify='center', cursor="plus", 
                              validate='key', validatecommand=(reg, '%P'))
            userInput.grid(row=row+i+1, column=column+j+1, sticky='nsew', 
                           padx=1, pady=1, ipady=5)
            cells[(row+i+1, column+j+1)] = userInput


# Drawing a 9x9 Grid 
def draw9x9Grid():
    color = "light yellow"
    for row in range(1, 10, 3):
        for col in range(0, 9 , 3):
            draw3x3Grid(row, col, color)
            if color == "light yellow":
                color = "light cyan"
            else:
                color = "light yellow"


# Call Sudoku solver def (called by solve button)
def getValues():
    board= []
    errorLabel.configure(text="")
    solvedLable.configure(text="")

    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))

        board.append(rows)
 

# Main Loop
draw9x9Grid()
window.mainloop()