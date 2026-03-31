class Menu:
    options = ["Manage Students","Manage Classes","Manage Professors"]
    def __init__(self):
        self.display()


    #displays all available options
    def display(self):
        for selection in self.options:
            print (selection)
