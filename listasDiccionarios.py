def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Manuel", "lastname": "Cruz"}

    super_list = [
        {"firstname": "Manuel", "lastname": "Cruz"},
        {"firstname": "Jeadran", "lastname": "Malagón"},
        {"firstname": "Carolina", "lastname": "Garrote"},
        {"firstname": "Victoria", "lastname": "Malagón"},
        {"firstname": "Dali", "lastname": "De La Cruz"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5], 
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    
    for values in super_list:
        for key, value in values.items():
            print(f'{key} - {value}')

if __name__ == '__main__':
    run()