import tkinter as tk
import time

class ReactionTimeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste de Reação")

        self.label = tk.Label(root, text="Se concentre", font=("Helvetica", 24))
        self.label.pack(pady=50)

        self.start_game_button = tk.Button(root, text="Iniciar Teste", command=self.start_game)
        self.start_game_button.pack()

        self.root.bind("<Button-1>", self.handle_click)

    def start_game(self):
        self.label.config(text="Se concentre", bg="blue")
        self.start_game_button.config(state=tk.DISABLED)  # Desativa o botão durante o teste
        self.root.after(3000, self.change_color)

    def change_color(self):
        self.label.config(text="Clique agora!", bg="green")
        self.start_time = time.time()

    def handle_click(self, event):
        if self.label.cget("bg") == "green":
            self.end_time = time.time()
            reaction_time_ms = round((self.end_time - self.start_time) * 1000, 1)
            self.label.config(text=f"Tempo de reação: {reaction_time_ms} ms", bg="black", fg="white")
            self.start_game_button.config(state=tk.NORMAL)  # Ativa o botão após o teste

if __name__ == "__main__":
    root = tk.Tk()
    app = ReactionTimeApp(root)
    root.mainloop()
