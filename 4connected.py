import matplotlib.pyplot as plt
import numpy as np
import time  # Untuk memberikan jeda waktu antara langkah-langkah

def boundary_fill(x, y, fill_color, boundary_color, screen, colors, step_delay=0.5):
    if (x < 0 or x >= len(screen[0]) or y < 0 or y >= len(screen) or
        screen[y][x] == fill_color or screen[y][x] == boundary_color):
        return
    
    # Isi warna saat ini
    screen[y][x] = fill_color
    
    # Tampilkan layar setelah setiap langkah
    create_plot(screen, colors)
    time.sleep(step_delay)  # Berikan jeda waktu antar langkah
    
    # Panggilan rekursif untuk arah kanan, kiri, bawah, dan atas
    boundary_fill(x + 1, y, fill_color, boundary_color, screen, colors, step_delay)  # Right
    boundary_fill(x - 1, y, fill_color, boundary_color, screen, colors, step_delay)  # Left
    boundary_fill(x, y + 1, fill_color, boundary_color, screen, colors, step_delay)  # Down
    boundary_fill(x, y - 1, fill_color, boundary_color, screen, colors, step_delay)  # Up

def create_plot(screen, colors):
    height = len(screen)
    width = len(screen[0])
    data = np.zeros((height, width, 3), dtype=np.uint8)  # Buat array 3D untuk warna RGB
    
    # Iterasi grid dan konversi elemen menjadi warna RGB
    for y in range(height):
        for x in range(width):
            data[y, x] = colors[screen[y][x]]
    
    plt.imshow(data)  # Tampilkan array sebagai gambar
    plt.axis('off')  # Hilangkan axis/sumbu
    plt.show()  # Tampilkan plot

# Initialize the screen
width, height = 10, 8
screen = [['white' for x in range(width)] for y in range(height)]

# Define colors
colors = {
    'black': [0, 0, 0],    # Warna hitam (RGB)
    'blue': [0, 0, 255],   # Warna biru (RGB)
    'white': [255, 255, 255]  # Warna putih (RGB)
}

# Draw a rectangle
for i in range(width):
    screen[0][i] = 'black'  # Garis atas
    screen[height-1][i] = 'black'  # Garis bawah

for i in range(height):
    screen[i][0] = 'black'  # Garis kiri
    screen[i][width-1] = 'black'  # Garis kanan

# Apply the boundary fill algorithm with step-by-step visualization
boundary_fill(5, 4, 'blue', 'black', screen, colors, step_delay=0.5)