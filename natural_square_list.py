import numpy as np

def run():
    natural_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    multiplication_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = np.multiply(natural_list, multiplication_list)

    
    print("Esta es una lista con los primeros numeros naturales elevados al cuadrado")
    print(natural_list)
    print("Lista elevanda al cuadrado:")
    print(result)


if __name__ == '__main__':
    run()
