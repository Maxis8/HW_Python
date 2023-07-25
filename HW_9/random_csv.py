from random import randint
import csv


def csv_rand(rows, start_pos, end):
    num_count = 3
    for _ in range(rows):
        lst = [str(randint(start_pos, end)) for _ in range(num_count)]
        with open(f'{csv_rand.__name__}.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(lst)

