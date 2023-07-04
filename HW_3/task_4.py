# 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. * Верните все возможные варианты комплектации рюкзака.
# hike = {'палатка': 5, 'котелок': 2, 'веревка': 4, 'еда': 3, 'одежда': 2, 'спальник': 3}

backpack = {'flashlight': 1, 'water': 2, 'tent': 10, 'food': 3, 'spinning': 3}


def backpack_unpacking(weight: int, things: dict) -> list[str]:
    packaging_option = []
    summary = []
    for key, value in things.items():
        if value <= weight:
            weight -= value
            packaging_option.append(key)
    return packaging_option


print(backpack_unpacking(9, backpack))

