import tkinter as tk
import random

def roll_dice(sides):
    #Return a random number between 1 and given sides.
    return random.randint(1, sides)

def roll_button(event=None):

    try:
        sides = int(side_entry.get())
        count = int(dice_entry.get())

        if count <= 0 or sides <= 0:
            result_label.config(text='🔴Enter positive numbers only.🔴')
            return
        
        results = []
        for i in range(count):
            results.append(f'🎲 Dice {i+1}: {roll_dice(sides)}')

        result_label.config(text='\n'.join(results))

    except ValueError:
        result_label.config(text='🔴Invalid input!🔴') 

def clear_button():

    #Cleat the inputs
    dice_entry.delete(0, tk.END)
    side_entry.delete(0, tk.END)

    #Put the keyboard cursor inside the dice_entry input box
    dice_entry.focus()


root = tk.Tk()
root.title('Dice Simulator')
root.geometry('400x400')

tk.Label(root, 
         text='Number of Dice:',
         font=('Arial', 10)).pack()

#Getting inputs of how much dice roll
dice_entry = tk.Entry(root,
                      font=('Arial', 10))
dice_entry.pack()

tk.Label(root, 
         text='Number of Sides',
         font=('Arial', 10)).pack()

#Getting inputs of how many side each dice has
side_entry = tk.Entry(root,
                      font=('Arial', 10))
side_entry.pack()

#Show the output
tk.Button(root, 
          text='Roll Dice',
          command=roll_button,
          font=('Arial', 10)).pack(pady=10)

#Clear the input fields
tk.Button(root,
          text='Clear',
          font=('Arial', 10),
          justify='right',
          command=clear_button,
          fg='red').pack()

result_label = tk.Label(root, text='',
                        justify='left',
                        font=('Arial', 15))
result_label.pack(pady=5)

#Enter button also show the output
root.bind("<Return>", roll_button)

root.mainloop()

