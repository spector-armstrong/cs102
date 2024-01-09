from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """

    way = ["up", "right"]
    i, j = coord[0], coord[1]
    route = random.choice(way)
    if route == "up":
        if i != 1:
            grid[i - 1][j] = " "
        elif j + 2 != len(grid[0]):
            grid[i][j + 1] = " "
    else:
        if j + 2 != len(grid[0]):
            grid[i][j + 1] = " "
        elif i != 1:
            grid[i - 1][j] = " "
    return grid


def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 != 0 and y % 2 != 0:
                grid[x][y] = " "
                empty_cells.append((x, y))

    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки

    for i in empty_cells:
        grid = remove_wall(grid, i)

    # генерация входа и выхода
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """

    :param grid:
    :return:
    """

    exits = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'X':
                exits.append((i, j))

    return exits

    pass


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """



    pass


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    pass


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """

    row, col = coord
    rows = len(grid)
    cols = len(grid[0])

    if (row == 0 and col == 0) or (row == 0 and col == cols - 1) or (row == rows - 1 and col == 0) or (
            row == rows - 1 and col == cols - 1):
        return True

    if row == 0 and (col > 0 and col < cols - 1):
        if grid[row][col - 1] == '#' and grid[row][col + 1] == '#' and grid[row + 1][col] != '#':
            return False
        else:
            return True
    elif row == rows - 1 and (col > 0 and col < cols - 1):
        if grid[row][col - 1] == '#' and grid[row][col + 1] == '#' and grid[row - 1][col] != '#':
            return False
        else:
            return True
    elif col == 0 and (row > 0 and row < rows - 1):
        if grid[row - 1][col] == '#' and grid[row + 1][col] == '#' and grid[row][col + 1] != '#':
            return False
        else:
            return True
    elif col == cols - 1 and (row > 0 and row < rows - 1):
        if grid[row - 1][col] == '#' and grid[row + 1][col] == '#' and grid[row][col - 1] != '#':
            return False
        else:
            return True

    return False

    pass


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """

    def count_exits(grid: List[List[Union[str, int]]]) -> int: count = 0

    for row in grid: count += row.count(1)
    return count

    def is_dead_end(grid: List[List[Union[str, int]]], x: int, y: int) -> bool: return (
                grid[x][y] != 1 and grid[x - 1][y] == "#" and grid[x + 1][y] == "#" and grid[x][y - 1] == "#" and
                grid[x][y + 1] == "#")

    def dijkstra(grid: List[List[Union[str, int]]], start: Tuple[int, int]) -> List[
        Tuple[int, int]]:  # Ваша реализация алгоритма Дейкстры

    def solve_maze(grid: List[List[Union[str, int]]], ) -> Tuple[List[List[Union[str, int]]], Optional[Union[
        Tuple[int, int], List[Tuple[int, int]]]]]:  # Шаг 1 exits = count_exits(grid) if exits < 2: return grid, None

        if is_dead_end(grid, start[0], start[1]):
            return None, None
        path = dijkstra(grid, start)
        return grid, path

    Пример
    использования
    функции
    grid = [["#", "#", "#", "#", "#"], ["#", 1, 0, 0, "#"], ["#", "#", "#", "#", "#"]]
    updated_grid, path = solve_maze(grid)
    print(updated_grid)
    print(path)
    pass


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
