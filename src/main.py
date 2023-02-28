import sys
from config import load_config, parse_args, update_config

from graphics import Window
from maze import Maze
import tkinter as tk
from screen import (
    calculate_cell_size,
    ensure_window_size_within_screen,
    get_max_screen_size,
)


def main():
    config = load_config()
    args = parse_args(config)

    max_screen_x, max_screen_y = get_max_screen_size()
    screen_x, screen_y = ensure_window_size_within_screen(
        args.screen_x,
        args.screen_y,
        args.cols,
        args.rows,
        args.margin,
        max_screen_x,
        max_screen_y,
    )

    if screen_x != args.screen_x or screen_y != args.screen_y:
        print(f"Warning: Window size adjusted to fit screen ({screen_x}x{screen_y})")
        args.screen_x, args.screen_y = screen_x, screen_y

    cell_size_x, cell_size_y = calculate_cell_size(
        args.screen_x, args.screen_y, args.cols, args.rows, args.margin
    )

    sys.setrecursionlimit(10000)
    win = Window(args.screen_x, args.screen_y)

    maze = Maze(
        args.margin,
        args.margin,
        args.rows,
        args.cols,
        cell_size_x,
        cell_size_y,
        win,
        args.seed,
    )

    print("Maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("Maze can not be solved!")
    else:
        print("Maze solved!")
    win.wait_for_close()

    update_config(args)


main()
