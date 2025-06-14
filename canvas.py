import tkinter as tk
from tkinter import colorchooser, filedialog
import random
from PIL import Image, ImageColor

# App window
window = tk.Tk()
window.title("ArtCell")
window.geometry("650x750")
window.config(bg="#f0f0f0")

# Set pixel size and grid size
pixel_size = 20
grid_rows = 10
grid_cols = 10

# Default color
current_color = "#FF6232"
rainbow_mode = False
eraser_mode = False

# Function to choose color
def choose_color():
    global current_color, rainbow_mode, eraser_mode
    rainbow_mode = False
    eraser_mode = False
    color = colorchooser.askcolor(title="Pick a color")
    if color[1]:
        current_color = color[1]

# Function to paint a pixel
def paint_pixel(event):
    global rainbow_mode, eraser_mode
    if rainbow_mode:
        r_color = f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}"
        event.widget.config(bg=r_color)
    elif eraser_mode:
        event.widget.config(bg="white")
    else:
        event.widget.config(bg=current_color)

# Function to clear the canvas
def clear_canvas():
    for pixel in pixels:
        pixel.config(bg="white")

# Enable rainbow mode
def activate_rainbow_mode():
    global rainbow_mode, eraser_mode
    rainbow_mode = True
    eraser_mode = False

# Enable eraser mode
def activate_eraser():
    global eraser_mode, rainbow_mode
    eraser_mode = True
    rainbow_mode = False

# Function to save canvas as image
def save_canvas():
    image = Image.new("RGB", (grid_cols, grid_rows), "white")
    for i in range(grid_rows):
        for j in range(grid_cols):
            color = canvas_grid[i][j].cget("bg")
            image.putpixel((j, i), ImageColor.getrgb(color))
    image = image.resize((grid_cols * pixel_size, grid_rows * pixel_size), Image.NEAREST)
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        image.save(file_path)
        print(f"Canvas saved as {file_path}👍")

# Function to load image into canvas
def load_canvas():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        loaded_image = Image.open(file_path).resize((grid_cols, grid_rows), Image.NEAREST)
        for i in range(grid_rows):
            for j in range(grid_cols):
                r, g, b = loaded_image.getpixel((j, i))
                hex_color = f"#{r:02x}{g:02x}{b:02x}"
                canvas_grid[i][j].config(bg=hex_color)
        print(f"Loaded image from {file_path}👍")

# Color pick button
color_button = tk.Button(window, text="🎨 Choose Color✌️", command=choose_color, font=("Arial", 14), bg="#4CAF50", fg="white")
color_button.pack(pady=6)

# Rainbow mode button
rainbow_button = tk.Button(window, text="🌈 Rainbow Mode", command=activate_rainbow_mode, font=("Arial", 14), bg="#673AB7", fg="white")
rainbow_button.pack(pady=6)

# Eraser button
eraser_button = tk.Button(window, text="✏️ Eraser", command=activate_eraser, font=("Arial", 14), bg="#9E9E9E", fg="white")
eraser_button.pack(pady=6)

# Clear button
clear_button = tk.Button(window, text="🗑️ Clear Canvas", command=clear_canvas, font=("Arial", 14), bg="#f44336", fg="white")
clear_button.pack(pady=6)

# Save button
save_button = tk.Button(window, text="💾 Save Image", command=save_canvas, font=("Arial", 14), bg="#2196F3", fg="white")
save_button.pack(pady=6)

# Load button
load_button = tk.Button(window, text="📖 Load Image", command=load_canvas, font=("Arial", 14), bg="#FF9800", fg="white")
load_button.pack(pady=6)

# Frame for pixels
canvas_frame = tk.Frame(window, bg="#000000")
canvas_frame.pack(pady=20)

# List to store pixel labels
pixels = []
canvas_grid = []

# Create pixel grid
for i in range(grid_rows):
    row = []
    for j in range(grid_cols):
        pixel = tk.Label(canvas_frame, bg="white", width=2, height=1, borderwidth=1, relief="solid")
        pixel.grid(row=i, column=j)
        pixel.bind("<Button-1>", paint_pixel)
        pixels.append(pixel)
        row.append(pixel)
    canvas_grid.append(row)

# Run the app
footer = tk.Label(window, text="ArtCell with ❤️ By Sheetal Bajaj😊", font=("Arial", 12), bg="#f0f0f0", fg="#555555")
footer.pack(side="bottom", pady=10)
window.mainloop()

