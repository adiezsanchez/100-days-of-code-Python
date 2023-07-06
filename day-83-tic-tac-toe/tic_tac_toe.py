import tkinter as tk
from tkinter import font

class TicTacToeBoard(tk.Tk): # TicTacToeBoard class inherits from Tk, making it a fully fledged GUI window (superclass)
    def __init__(self):
        super().__init__() # Call the superclass init method to initialize the parent class using the super() function
        self.title("Tic-Tac-Toe Game")
        self._cells = {} # Dictionary mapping the buttons/cells to their corresponding row and column coordinates
        # Call the methods below from the class initializer
        self.create_board_display()
        self._create_board_grid()

    def create_board_display(self):
        display_frame = tk.Frame(master=self) # Create a Frame object to hold the game display, master argument (game's window will be frame's parent)
        display_frame.pack(fill=tk.X) # Geometry manager, place the frame on window top border, tk.X frame fills the entire width
        self.display = tk.Label( # Label object living within the Frame object
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack() # Packs the display inside the frame using the pack() geometry manager

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=50)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=5,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
# ---------------------------- UI SETUP ------------------------------- #

window = TicTacToeBoard()
print(window._cells)
window.mainloop()