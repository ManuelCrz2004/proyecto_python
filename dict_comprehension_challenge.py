import math

def run():
    dict_challenge = {i: math.sqrt(i) for i in range(1, 1001)}
    print(dict_challenge)


if __name__ == '__main__':
    run()