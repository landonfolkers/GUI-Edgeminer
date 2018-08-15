import Tkinter


class Menu():
    def __init__(self, master):
        self.master = master
        
        menu = Tkinter.Menu(self.master)
        self.master.config(menu=menu)

        account = Tkinter.Menu(menu)
        account.add_command(label="Login", command=self.client_exit)
        account.add_command(label="Logout", command=self.client_exit)
        account.add_command(label="Account Info", command=self.client_exit)
        menu.add_cascade(label="Account", menu=account)

        mine = Tkinter.Menu(menu)
        mine.add_command(label="Choose Currency", command=self.client_exit)
        mine.add_command(label="Rigs", command=self.client_exit)
        menu.add_cascade(label="Mine", menu=mine)

        pool = Tkinter.Menu(menu)
        pool.add_command(label="Choose Pool", command=self.client_exit)
        pool.add_command(label="Pools List", command=self.client_exit)
        menu.add_cascade(label="Pool", menu=pool)

        root.config(menu=menu)

    def client_exit(self):
        exit()


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Edgeminer")

        self.label = Tkinter.Label(master, text="Welcome to EdgeMiner")
        self.label.pack()

        self.greet_button = Tkinter.Button(
            master, text="Greet", command=self.greet, width=20)
        self.greet_button.pack()

        self.close_button = Tkinter.Button(
            master, text="Close", command=master.quit, width=20)
        self.close_button.pack()

    def greet(self):
        print("Welcome to Edgeminer")


root = Tkinter.Tk()
root.geometry('700x500')
menubar = Menu(root)
my_gui = GUI(root)
root.mainloop()
