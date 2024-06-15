import tkinter as tk
import random
import copy

class Sudoku:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku")
        self.board = [[0]*9 for _ in range(9)]
        self.tiles = [[None]*9 for _ in range(9)]
        self.ans = [[0]*9 for _ in range(9)]
        self.create_widgets() 
        self.logic()
        self.ans = self.answer()
        self.update_board()
        self.master.bind("<Key>", self.handle_keypress)
        self.empty_tiles = empty_cells(self.board)
        self.selected = self.empty_tiles[0]

    def create_widgets(self):
        self.frame = tk.Frame(self.master, bg="light slate gray")
        self.frame.grid(sticky=tk.NSEW, padx=10, pady=10)
        self.frame.pack(fill="both",expand=True, padx=10, pady=10)
        
        for i in range(9):
            for j in range(9):
                tile = tk.Label(self.frame, text="", font=("Helvetica", 26, 'bold'), width=4, height=2, bg="mint cream",fg="black", borderwidth=3, relief="solid")
                
                tile.grid(row=i, column=j, padx=2, pady=2)

                if i == 3 or i == 6:
                    tile.grid(row=i, column=j, padx=2, pady=(10,2))

                if j == 3 or j == 6:
                    tile.grid(row=i, column=j, padx=(10,2), pady=2)

                if (i == 3 and j == 3) or (i == 3 and j == 6) or (i == 6 and j == 3) or (i == 6 and j == 6):
                    tile.grid(row=i, column=j, padx=(10,2), pady=(10,2))

                self.tiles[i][j] = tile

    def logic(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    nums = list(range(1, 10))
                    random.shuffle(nums)

                    for num in nums:
                        if is_valid(self.board, num, i, j):
                            self.board[i][j] = num
                            if self.logic():
                                return True
                            self.board[i][j] = 0
                    return False
        return True
    
    def handle_keypress(self, event):
        print(f"Key pressed: {event.keysym}") 
        self.select(event.keysym)

        if is_game_over(self.board, self.ans):
            self.win()

    def select(self, key):
        if key in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if is_valid(self.board, int(key), self.selected[0], self.selected[1]):
                self.board[self.selected[0]][self.selected[1]] = int(key)
                self.tiles[self.selected[0]][self.selected[1]].config(text=str(key), fg='black')
            else:
                self.tiles[self.selected[0]][self.selected[1]].config(text=str(key), fg='red')

        if key == 'BackSpace':
            self.board[self.selected[0]][self.selected[1]] = 0
            self.tiles[self.selected[0]][self.selected[1]].config(text="")


        if key == 'Up':
            if self.selected[0] != 0:
                self.tiles[self.selected[0]][self.selected[1]].config(bg='mint cream')

                for i in range(len(self.empty_tiles)):
                    if self.empty_tiles[len(self.empty_tiles)-i-1][0] < self.selected[0]:
                        self.selected = self.empty_tiles[len(self.empty_tiles)-i-1]
                        break
                    

                self.tiles[self.selected[0]][self.selected[1]].config(bg='pale green')

        elif key == 'Down':
            if self.selected[0] != 8:
                self.tiles[self.selected[0]][self.selected[1]].config(bg='mint cream')

                for i in range(len(self.empty_tiles)):
                    if self.empty_tiles[i][0] > self.selected[0]:
                        self.selected = self.empty_tiles[i]
                        break

                
                self.tiles[self.selected[0]][self.selected[1]].config(bg='pale green')


        elif key == 'Left':
            self.tiles[self.selected[0]][self.selected[1]].config(bg='mint cream')

            for i in range(len(self.empty_tiles)):
                if self.empty_tiles[len(self.empty_tiles)-i-1][0] == self.selected[0]:
                    if self.empty_tiles[len(self.empty_tiles)-i-1][1] < self.selected[1]:
                        self.selected = self.empty_tiles[len(self.empty_tiles)-i-1]
                        break
            
            self.tiles[self.selected[0]][self.selected[1]].config(bg='pale green')
        
        elif key == 'Right':
            self.tiles[self.selected[0]][self.selected[1]].config(bg='mint cream')
            
            for i in range(len(self.empty_tiles)):
                if self.empty_tiles[i][0] == self.selected[0]:
                    if self.empty_tiles[i][1] > self.selected[1]:
                        self.selected = self.empty_tiles[i]
                        break
            
            self.tiles[self.selected[0]][self.selected[1]].config(bg='pale green')


    def answer(self):
        ans = copy.deepcopy(self.board)

        for _ in range(40):
            i = random.randint(0, 8)
            j = random.randint(0, 8)

            self.board[i][j] = 0
        
        return ans

    def update_board(self):
        for i in range(9):
            for j in range(9):
                print(self.board[i][j], end=" ")
                if self.board[i][j] != 0:
                    value = self.board[i][j]
                    self.tiles[i][j].config(text=str(value) if value else "", bg='pale turquoise')
            
            print()

    def win(self):
        win = tk.Frame(self.frame, borderwidth=5)
        win.place(relx=0.5, rely=0.5, anchor='center')
        tk.Label(win, text="You Win!", font=('Helvetica', 48, 'bold'), bg='blanched almond', fg='steel blue').pack()

def main():
    root = tk.Tk()
    game = Sudoku(root)
    root.mainloop()

def is_valid(board, num, row, col):
        for i in range(9):
            if board[row][i] == num:
                return False
        
        for i in range(9):
            if board[i][col] == num:
                return False
        
        start_row, start_col = 3*(row//3), 3*(col//3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
                
        return True

def empty_cells(board):
        empty_tiles = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    empty_tiles.append([i, j])
        
        return empty_tiles

def is_game_over(board, ans):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ans[i][j]:
                    continue
                else:
                    return False
        
        return True
    
if __name__ == "__main__":
	main()