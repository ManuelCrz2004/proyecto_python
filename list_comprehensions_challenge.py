from setuptools import PEP420PackageFinder


def run():
    # Create a list with all multipliers of 4, and those are multipliers of 6 and 9
    # There is a maximun of 5 digits

    numbers_challenge = [i*4 for i in range(1, 1000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(numbers_challenge)


if __name__ == '__main__':
    run()