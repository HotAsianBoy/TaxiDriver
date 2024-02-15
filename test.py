import curses
import random
import time
import sys


def main(stdscr):
    curses.curs_set(0)
    stdscr.timeout(100)
    stdscr.keypad(True)
    height, width = stdscr.getmaxyx()

    player = {'x': width // 2, 'y': height - 2, 'char': '^'}
    obstacles = []

    score = 0

    while True:
        stdscr.clear()
        stdscr.addch(player['y'], player['x'], player['char'])

        for obstacle in obstacles:
            stdscr.addch(obstacle['y'], obstacle['x'], '*')
            obstacle['y'] += 1

            if (
                player['x'] == obstacle['x']
                and player['y'] == obstacle['y']
            ):
                game_over(stdscr, score)

            if obstacle['y'] >= height:
                score += 1
                obstacles.remove(obstacle)

        if random.randint(0, 100) < 5:
            obstacles.append({'x': random.randint(0, width - 1), 'y': 0})

        stdscr.addstr(0, 0, f"Score: {score}")

        key = stdscr.getch()

        if key == ord('q'):
            game_over(stdscr, score)

        if key == curses.KEY_LEFT and player['x'] > 0:
            player['x'] -= 1
        elif key == curses.KEY_RIGHT and player['x'] < width - 1:
            player['x'] += 1

        time.sleep(0.1)


def game_over(stdscr, final_score):
    stdscr.clear()
    stdscr.addstr(
        curses.LINES // 2,
        (curses.COLS - len("Game Over! Press 'q' to quit.")) // 2,
        "Game Over! Press 'q' to quit."
    )
    stdscr.addstr(
        curses.LINES // 2 + 1,
        (curses.COLS - len(f"Final Score: {final_score}")) // 2,
        f"Final Score: {final_score}"
    )
    stdscr.refresh()
    stdscr.getch()
    sys.exit()



