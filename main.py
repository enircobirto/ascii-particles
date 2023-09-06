from src.RenderMatrix import RenderMatrix
from src.Vector2D import Vector2D

def main():
    matrix = RenderMatrix(Vector2D(5,5))
    matrix.place(1,Vector2D(1,1))
    matrix.print_grid()

if __name__ == '__main__':
    main()
