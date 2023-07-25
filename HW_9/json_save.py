import os
import json


def save_params(func):
    func_name = func.__name__
    if os.path.exists(f'{func_name}.json'):
        with open(f'{func_name}.json', 'r', encoding='utf-8') as f:
            lst = json.load(f)
    else:
        lst = []

    def wrapper(*args, **kwargs):
        func_res = func(*args, **kwargs)
        result = {'args': args,
                  'kwargs': kwargs,
                  'result': func_res}
        lst.append(result)
        with open(f'{func_name}.json', 'w', encoding='utf-8') as f1:
            json.dump(lst, f1, indent=2)
        return lst

    return wrapper

