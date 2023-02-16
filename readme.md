

This is a maze generator and solver. It is a simple deskptop app that uses python and tkinter. Here is some documentation of the functions

## redraw() method

this will redraw all the graphics in the window. Tkinter is *not* a reactive framework like React or Vue - we need to tell the window when it render to visuals.

The `redraw()` method on the window class simply call the root widget's [`update_idletasks()` and `update()`](https://tkdocs.com/pyref/tk.html) methods. Each time this is called, the window will redraw itself.

# Cell draw_move() method
 It draws a line from the *center* of one cell to another. The method definition look something like this:

```python
def draw_move(self, to_cell, undo=False):
```

The `undo` flag is not set, the line to draw is `"red"`. Otherwise make it `"gray"`. This is so that when we go to draw the path, whenever we backtrack we can show that in a different color to better visualize what's happening.

Use the x/y coordinates of the 2 cells in question to decide how to draw the line connecting the two cells.
## _break_walls_r(self, i, j)

The recursive `break_walls_r` method is a breadth-first traversal through the cells, breaking down walls as it goes. I'll describe the algorithm I used, 

1. Mark the current cell as visited
2. In a loop:
   1. Create a new empty list which will hold the `i` and `j` values you need to visit
   2. Check the cells that are directly adjacent to the current cell. If one isn't visited, keep track of it as a "possible direction" that you can move in.
   3. If there are no directions you can go from the current cell, then draw the current cell and `return` to break out of the loop
   4. Otherwise, pick a [random](https://docs.python.org/3/library/random.html#random.randrange) direction.
   5. Knock down the walls between the current cell and the chosen cell.
   6. Move to the chosen cell by recursively calling `_break_walls_r`


# Solve the maze

## solve() method

The `solve()` method on the `Maze` class simply calls the `_solve_r` method starting at `i=0` and `j=0`. It return `True` if the maze was solved, `False` otherwise. This is the same return value as `_solve_r`.

## _solve_r method

This is a depth-first first solution to the maze. Here were my steps.

The `_solve_r` method returns `True` if the current cell is an end cell, OR if it leads to the end cell. It returns `False` if the current cell is a loser cell.

1. Call the `_animate` method.
2. Mark the current cell as visited
3. If you are at the "end" cell (the goal) then return `True`.
4. For each direction:
   1. If there is a cell in that direction, there is no wall blocking you, and that cell hasn't been visited:
      1. Draw a move between the current cell and that cell
      2. Call `_solve_r` recursively to move to that cell. If that cell returns `True`, then just return `True` and don't worry about the other directions.
      3. Otherwise, draw an "undo" move between the current cell and the next cell
5. If none of the directions worked out, return `False`.

## Update the main function

Call `maze.solve()` in the main function and watch your algorithm do its work!

This code is written by [Lane Wagner](https://github.com/wagslane) who gave permission to use it for this exercise. It was originally produced for [boot.dev](https://boot.dev/)