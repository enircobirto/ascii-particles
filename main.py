from src.RenderMatrix import RenderMatrix
from src.Particle import Particle
from src.Vector2D import Vector2D
from time import sleep

import curses
import keyboard

def main():
    screen = curses.initscr()
    curses.curs_set(0)
    curses.noecho()
    curses.cbreak()
    rows, cols = screen.getmaxyx()
    matrix = RenderMatrix(Vector2D(cols-1,rows-1),screen)
    p = Particle(Vector2D(5,2),matrix)
    p.velocity = Vector2D(0.5,0)
    p.acceleration = Vector2D(0,0.02)
    
    while True:
        screen.clear()
        p.update()
        p.pre_render(matrix)
        matrix.display()
        sleep(0.01)
        screen.refresh()

        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            break
        elif keyboard.is_pressed('w'):
            p.velocity += Vector2D(0,-0.04)
        elif keyboard.is_pressed('a'):
            p.velocity += Vector2D(-0.02,0)
        elif keyboard.is_pressed('d'):
            p.velocity += Vector2D(0.02,0)
        elif keyboard.is_pressed('p'):
            p.size += 1
        elif keyboard.is_pressed('o'):
            p.size -= 1


    curses.endwin()

if __name__ == '__main__':
    main()
