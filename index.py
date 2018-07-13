from tkinter import Tk, Label, Button

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Edgeminer")

        self.label = Label(master, text="Welcome to EdgeMiner")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Welcome to Edgeminer")

root = Tk()
my_gui = GUI(root)
root.mainloop()