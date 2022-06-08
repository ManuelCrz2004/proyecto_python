import numpy as np

def run():
    squares = []
    squares_divided = []
    for i in range(1, 101):
        squares.append(i**2)

    for i in range(1, 101):
        squares_divided.append(squares/3)

    
    print(squares_divided)
    


if __name__ == '__main__':
    run()