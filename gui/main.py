# Import necessary modules
from customtkinter import CTk, CTkLabel, CTkFont, CTkButton


class App(CTk):
    def __init__(self):
        # Inheriting constructor of super class
        super().__init__()
        # Giving apt title and window size
        self.title("Graphical User Interface")
        self.geometry("300x100")
        # font
        my_font = CTkFont(
            family="Helvetica",
            size=16,
        )
        # Creating label and packing it to the window.
        self.label = CTkButton(
            self, text="Test text", text_color=("yellow"), font=my_font
        )
        self.label.pack(padx=20, pady=20)


app = App()
app.mainloop()
