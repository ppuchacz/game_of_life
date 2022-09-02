import pygame
import numpy as np

pygame.init()

COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_RED = (255, 0, 0)
COLOR_GREEN = (0, 255, 0)
COLOR_WHITE = (255, 255, 255)

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_BG_COLOR = COLOR_BLACK

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
board = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
])

BOARD_HEIGHT = WINDOW_HEIGHT
BOARD_WIDTH = WINDOW_WIDTH
BOARD_POS_X = 0
BOARD_POS_Y = 0
BOARD_CELL_ACTIVE_COLOR = COLOR_WHITE
BOARD_CELL_INACTIVE_COLOR = COLOR_BLACK
BOARD_CELL_BG_COLOR = COLOR_BLACK
BOARD_CELL_PADDING = 1

CELL_STATUS_DEAD = 0
CELL_STATUS_ALIVE = 1

CA_STEP_DELAY_MS = 50


def get_cell_width(columns: int) -> float:
    return BOARD_WIDTH / columns


def get_cell_height(rows: int) -> float:
    return BOARD_HEIGHT / rows


def get_cell_pos_x(column_no: int, cell_width: float) -> float:
    return BOARD_POS_X + cell_width * column_no


def get_cell_pos_y(row_no: int, cell_height: float) -> float:
    return BOARD_POS_Y + cell_height * row_no


def board_display():
    board_row_count = len(board)
    for row in range(0, board_row_count):
        board_column_count = len(board[row])
        for column in range(0, board_column_count):
            cell_width = get_cell_width(board_column_count)
            cell_height = get_cell_height(board_row_count)
            pos_x = get_cell_pos_x(column, cell_width)
            pos_y = get_cell_pos_y(row, cell_height)
            inner_rect = (
                pos_x + BOARD_CELL_PADDING,
                pos_y + BOARD_CELL_PADDING,
                cell_height - 2 * BOARD_CELL_PADDING,
                cell_width - 2 * BOARD_CELL_PADDING
            )
            outer_rect = (
                pos_x,
                pos_y,
                cell_height,
                cell_width
            )
            color = BOARD_CELL_INACTIVE_COLOR if board[row][column] == 0 else BOARD_CELL_ACTIVE_COLOR
            pygame.draw.rect(screen, BOARD_CELL_BG_COLOR, outer_rect)
            pygame.draw.rect(screen, color, inner_rect)


def screen_display():
    screen.fill(WINDOW_BG_COLOR)
    board_display()

    pygame.display.flip()


def cell_exists(row: int, column: int) -> bool:
    row_exists = row < len(board) and row >= 0
    col_exists = column < len(board[0]) and column >= 0
    return row_exists and col_exists


def count_alive_neighbours(row: int, column: int):
    tl = int(cell_exists(row-1, column-1) and board[row-1][column-1])
    tm = int(cell_exists(row-1, column) and board[row-1][column])
    tr = int(cell_exists(row-1, column+1) and board[row-1][column+1])
    ml = int(cell_exists(row, column-1) and board[row][column-1])
    mr = int(cell_exists(row, column+1) and board[row][column+1])
    bl = int(cell_exists(row+1, column-1) and board[row+1][column-1])
    bm = int(cell_exists(row+1, column) and board[row+1][column])
    br = int(cell_exists(row+1, column+1) and board[row+1][column+1])
    return sum([tl, tm, tr, ml, mr, bl, bm, br])


def gol_get_next_step(board):
    new_board = board.copy()
    board_row_count = len(board)
    for row in range(0, board_row_count):
        board_column_count = len(board[row])
        for column in range(0, board_column_count):
            cell_status = board[row][column]
            alive_around = count_alive_neighbours(row, column)
            if cell_status == CELL_STATUS_ALIVE and alive_around in [2, 3]:
                continue
            if cell_status == CELL_STATUS_DEAD and alive_around == 3:
                new_board[row][column] = CELL_STATUS_ALIVE
                continue
            new_board[row][column] = CELL_STATUS_DEAD
    return new_board


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.wait(CA_STEP_DELAY_MS)
    board = gol_get_next_step(board)
    screen_display()

pygame.quit()
