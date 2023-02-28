import tkinter as tk


def get_max_screen_size():
    root = tk.Tk()
    max_screen_x = root.winfo_screenwidth()
    max_screen_y = root.winfo_screenheight()
    root.destroy()
    return max_screen_x, max_screen_y


def ensure_window_size_within_screen(
    screen_x, screen_y, cols, rows, cell_size_x, cell_size_y, margin
):
    max_screen_x, max_screen_y = get_max_screen_size()
    screen_x = min(cols * cell_size_x + margin, max_screen_x, screen_x)
    screen_y = min(rows * cell_size_y + margin, max_screen_y, screen_y)
    return screen_x, screen_y


def calculate_cell_size(screen_x, screen_y, num_cols, num_rows, margin):
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    return cell_size_x, cell_size_y
