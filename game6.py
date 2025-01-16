import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Snake")

        # Ukuran layar game
        self.canvas_width = 400
        self.canvas_height = 400
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack()

        # Konfigurasi game
        self.snake_size = 20
        self.snake = [(100, 100), (80, 100), (60, 100)]  # Posisi awal ular
        self.snake_direction = "Right"
        self.food_position = self.create_food()

        # Membuat ular dan makanan di canvas
        self.snake_squares = [self.canvas.create_rectangle(x, y, x + self.snake_size, y + self.snake_size, fill="green") for x, y in self.snake]
        self.food_square = self.canvas.create_rectangle(*self.food_position, self.food_position[0] + self.snake_size, self.food_position[1] + self.snake_size, fill="red")

        # Kontrol gerakan ular
        self.root.bind("<Up>", lambda _: self.change_direction("Up"))
        self.root.bind("<Down>", lambda _: self.change_direction("Down"))
        self.root.bind("<Left>", lambda _: self.change_direction("Left"))
        self.root.bind("<Right>", lambda _: self.change_direction("Right"))

        # Skor
        self.score = 0
        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12), bg="black", fg="white")
        self.score_label.pack()

        # Memulai game
        self.update_snake()

    def create_food(self):
        """Membuat makanan di posisi acak"""
        x = random.randint(0, (self.canvas_width - self.snake_size) // self.snake_size) * self.snake_size
        y = random.randint(0, (self.canvas_height - self.snake_size) // self.snake_size) * self.snake_size
        return x, y

    def change_direction(self, new_direction):
        """Mengubah arah ular, tapi tidak boleh berbalik arah"""
        opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction != opposite_directions.get(self.snake_direction):
            self.snake_direction = new_direction

    def update_snake(self):
        """Mengupdate posisi ular dan logika game setiap frame"""
        x, y = self.snake[0]
        if self.snake_direction == "Up":
            y -= self.snake_size
        elif self.snake_direction == "Down":
            y += self.snake_size
        elif self.snake_direction == "Left":
            x -= self.snake_size
        elif self.snake_direction == "Right":
            x += self.snake_size

        # Cek jika ular menabrak dinding atau tubuhnya sendiri
        new_head = (x, y)
        if x < 0 or x >= self.canvas_width or y < 0 or y >= self.canvas_height or new_head in self.snake:
            self.game_over()
            return

        # Menambahkan kepala baru
        self.snake = [new_head] + self.snake

        # Cek jika ular memakan makanan
        if new_head == self.food_position:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.food_position = self.create_food()
            self.canvas.coords(self.food_square, *self.food_position, self.food_position[0] + self.snake_size, self.food_position[1] + self.snake_size)
        else:
            # Menghapus ekor jika tidak memakan makanan
            self.snake.pop()
        
        # Update posisi ular di layar
        for i, (x, y) in enumerate(self.snake):
            self.canvas.coords(self.snake_squares[i], x, y, x + self.snake_size, y + self.snake_size)
        
        # Tambah bagian tubuh jika ular memakan makanan
        if len(self.snake) > len(self.snake_squares):
            self.snake_squares.append(self.canvas.create_rectangle(x, y, x + self.snake_size, y + self.snake_size, fill="green"))

        # Mengatur ulang pembaruan
        self.root.after(100, self.update_snake)

    def game_over(self):
        """Menampilkan pesan Game Over"""
        self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2, text="Game Over", font=("Arial", 24), fill="white")
        self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2 + 30, text=f"Score: {self.score}", font=("Arial", 16), fill="white")

# Jalankan game
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
