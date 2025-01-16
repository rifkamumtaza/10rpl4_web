import tkinter as tk
import random

class CatchTheBallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Ball Game")
        
        # Ukuran layar game
        self.canvas_width = 500
        self.canvas_height = 400
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="lightblue")
        self.canvas.pack()
        
        # Membuat pemain
        self.player_width = 50
        self.player_height = 20
        self.player_x = self.canvas_width // 2 - self.player_width // 2
        self.player_y = self.canvas_height - self.player_height - 10
        self.player = self.canvas.create_rectangle(self.player_x, self.player_y, self.player_x + self.player_width, self.player_y + self.player_height, fill="blue")
        
        # Membuat bola
        self.ball_size = 20
        self.ball_x = random.randint(0, self.canvas_width - self.ball_size)
        self.ball_y = 0
        self.ball = self.canvas.create_oval(self.ball_x, self.ball_y, self.ball_x + self.ball_size, self.ball_y + self.ball_size, fill="red")
        
        # Skor
        self.score = 0
        self.score_text = self.canvas.create_text(10, 10, anchor="nw", font=("Arial", 14), text="Score: 0")
        
        # Kecepatan bola
        self.ball_speed = 3
        
        # Kontrol gerakan pemain
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        
        # Jalankan game
        self.update_ball()

    def move_left(self, event):
        if self.player_x > 0:
            self.player_x -= 20
            self.canvas.move(self.player, -20, 0)

    def move_right(self, event):
        if self.player_x < self.canvas_width - self.player_width:
            self.player_x += 20
            self.canvas.move(self.player, 20, 0)

    def update_ball(self):
        # Update posisi bola
        self.ball_y += self.ball_speed
        self.canvas.move(self.ball, 0, self.ball_speed)
        
        # Jika bola menyentuh bagian bawah
        if self.ball_y >= self.canvas_height:
            self.reset_ball()
        
        # Deteksi jika pemain menangkap bola
        if self.player_y < self.ball_y + self.ball_size and self.player_x < self.ball_x < self.player_x + self.player_width:
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.reset_ball()
        
        # Lanjutkan update bola
        self.root.after(20, self.update_ball)

    def reset_ball(self):
        self.ball_x = random.randint(0, self.canvas_width - self.ball_size)
        self.ball_y = 0
        self.canvas.coords(self.ball, self.ball_x, self.ball_y, self.ball_x + self.ball_size, self.ball_y + self.ball_size)

# Jalankan game
root = tk.Tk()
game = CatchTheBallGame(root)
root.mainloop()
