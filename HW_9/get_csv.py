from random_csv import csv_rand
import csv


def get_num_csv(func):
    lst = []
    csv_rand(100, 1, 100)

    def wrapper(*args, **kwargs):
        with open(f'{csv_rand.__name__}.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for i in reader:
                args = map(int, i)
                lst.append(func(*args, **kwargs))
            return lst

    return wrapper

