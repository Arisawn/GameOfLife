from django.shortcuts import render
from .models import Cell
import random

def initialize_grid(rows, cols):
    for row in range(rows):
        for col in range(cols):
            state = random.choice([0, 1])
            Cell.objects.create(row=row, col=col, state=state)

def update_grid(rows, cols):
    for row in range(rows):
        for col in range(cols):
            cell = Cell.objects.get(row=row, col=col)
            live_neighbors = Cell.objects.filter(
                row__in=[row-1, row, row+1],
                col__in=[col-1, col, col+1],
                state=True
            ).exclude(row=row, col=col).count()

            # Update cell state based on the rules
            if cell.state == 1 and (live_neighbors < 2 or live_neighbors > 3):
                cell.state = 0
            elif cell.state == 0 and live_neighbors == 3:
                cell.state = 1

            cell.save()

def game_of_life(request):
    rows, cols = 50, 50

    # Check if the grid is initialized, if not, initialize it
    if not Cell.objects.exists():
        initialize_grid(rows, cols)

    # Update the grid based on the rules
    update_grid(rows, cols)

    # Retrieve the current state of the grid
    grid = [[Cell.objects.get(row=row, col=col).state for col in range(cols)] for row in range(rows)]

    return render(request, 'gameoflife/grid.html', {'grid': grid})
