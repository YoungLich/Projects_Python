import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.buttons = [tk.Button(root, text='', font='normal 20 bold', width=5, height=2,
                                  command=lambda i=i: self.click(i)) for i in range(9)]
        self.create_board()

    def create_board(self):
        for i, button in enumerate(self.buttons):
            row = i // 3
            col = i % 3
            button.grid(row=row, column=col)

    def click(self, index):
        if self.board[index] == '' and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.current_player} venceu!")
                self.reset_game()
            elif '' not in self.board:
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]              # Diagonais
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '':
                return True
        return False

    def reset_game(self):
        self.board = ['' for _ in range(9)]
        for button in self.buttons:
            button.config(text='')
        self.current_player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()