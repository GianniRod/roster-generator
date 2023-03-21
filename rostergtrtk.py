import tkinter as tk
import pyperclip
from faker import Faker

root = tk.Tk()
root.title("Roster Generator")
root.geometry("500x960")

faker = Faker()

class RosterGenerator:
    
    rostergtr = tk.Label(root, text="ROSTER GENERATOR", font=("Arial", 30))
    rostergtr.pack()
    
    def __init__(self):
        self.positions = {'PG': 2, 'SG': 2, 'SF': 3, 'PF': 3, 'C': 2}
        self.setup_ui()
    
    def setup_ui(self):
        for position, count in self.positions.items():
            for i in range(1, count+1):
                new_first_name = faker.first_name_male()
                new_last_name = faker.last_name_male()
                player_name = f"{new_first_name} {new_last_name} ({position})"
                setattr(self, f'nombrep{position}{i}', new_first_name)
                setattr(self, f'apellidop{position}{i}', new_last_name)
                frame = tk.Frame(root, bd=2, relief="groove", borderwidth=2, pady=10)
                frame.pack(fill="x")
                lbl = tk.Label(frame, text=player_name, font=("Arial", 15))
                lbl.pack(side="left", padx=10)
                setattr(self, f'lblp{position}{i}', lbl)
                btn_copy = tk.Button(frame, text="COPIAR", font=("Arial", 15), command=lambda text=player_name: self.copy_to_clipboard(text))
                btn_copy.pack(side="right", padx=10)
        btn_reset = tk.Button(root, text="RESET", font=("Arial", 20), command=self.reset_players)
        btn_reset.pack(pady=20)
    
    def copy_to_clipboard(self, text):
        pyperclip.copy(text)
    
    def reset_players(self):
        for position, count in self.positions.items():
            for i in range(1, count+1):
                new_first_name = faker.first_name_male()
                new_last_name = faker.last_name_male()
                player_name = f"{new_first_name} {new_last_name} ({position})"
                setattr(self, f'nombrep{position}{i}', new_first_name)
                setattr(self, f'apellidop{position}{i}', new_last_name)
                getattr(self, f'lblp{position}{i}').config(text=player_name)

app = RosterGenerator()
root.mainloop()
