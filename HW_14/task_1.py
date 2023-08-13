# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
import json
class User:
    def __init__(self, name, u_id, level=None):
        self.u_id = u_id
        self.name = name
        self.level = level

    def __str__(self):
        return f'\tID: {self.u_id}\t NAME: {self.name:<4}\t LEVEL: {self.level}\n'

    def __eq__(self, other):
        return self.u_id == other.u_id and self.name == other.name

class BasicException(Exception):
    pass


class NotFoundError(BasicException):
    def __str__(self):
        return "Admin not found! Access denied!"


class LevelError(BasicException):
    def __init__(self, user_level, admin_level):
        self.user_level = user_level
        self.admin_level = admin_level

    def __str__(self):
        return f"Access denied!!! Access level must be higher than({self.admin_level})"


class UserNotFoundError(BasicException):
    def __init__(self, name, u_id):
        self.name = name
        self.u_id = u_id

    def __str__(self):
        return f"User {self.name} {self.u_id} not found! Access denied!!!"

class Project:
    """Класс управления пользователями проекта"""

    def __init__(self, users_list):
        if users_list is None:
            self.users_list = []
        self.users_list = users_list
        self.u_admin = None

    @classmethod
    def load_js(cls, path):
        with open(path, 'r', encoding='utf-8') as f:
            my_dict = json.load(f, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})
        project_users = []
        for level, users in my_dict.items():
            for user_id, name in users.items():
                user = User(name, user_id, level)
                project_users.append(user)
        return Project(project_users)

    def enter(self, name, u_id):
        """
        Метод входа в систему.
        :param name: Имя пользователя
        :param u_id: Идентификатор пользователя
        :exception NotAllowedError: Срабатывает, если пользователя нет в списке.
        """
        user = User(name, u_id)
        for proj_user in self.users_list:
            if user == proj_user:
                self.u_admin = proj_user
                break
        else:
            raise UserNotFoundError(name, u_id)


    def add_user(self, name, u_id, level):
        """
        Метод добавления нового пользователя в проект.
        :param name: Имя пользователя
        :param id_: Идентификатор пользователя
        :param level: Уровень доступа пользователя
        :exception AdminNotFoundError: Срабатывает, если не установлен администратор.
        :exception LevelError: Срабатывает, если уровень пользователя больше, чем у администратора
        """
        if self.u_admin is None:
            raise NotFoundError
        if level > self.u_admin.level:
            raise LevelError(level, self.u_admin.level)
        self.users_list.append(User(name, u_id, level))

    def remove_user(self, name, u_id, level):
        """
        Метод удаления пользователя из проекта.
        :param name: Имя пользователя
        :param id_: Идентификатор пользователя
        :param level: Уровень доступа пользователя
        :exception AdminNotFoundError: Срабатывает, если не установлен администратор.
        :exception LevelError: Срабатывает, если уровень пользователя больше, чем у администратора
        :exception ValueError: Срабатывает, если пользователя с введёнными данными нет в проекте
        """
        if self.u_admin is None:
            raise NotFoundError
        if level > self.u_admin.level:
            raise LevelError(level, self.u_admin.level)
        try:
            self.users_list.remove(User(name, u_id, level))
        except ValueError:
            print(f"DeleteError!!!\n User {name} not found")

    def __str__(self):
        return f'Admin{self.u_admin}'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Метод выхода из контекстного менеджера
        При выходе, актуальный список пользователей сохраняется в файл.
        """
        self.file = open(f'new_file.json', 'w', encoding='utf-8')
        temp = {k: {} for k in range(1, 8)}
        for user in self.users_list:
            temp[user.level].update({user.u_id: user.name})
        json.dump(temp, self.file, ensure_ascii=False)
        self.file.close()


with Project.load_js('task2.json') as p:
    print(*p.users_list)
    p.enter("Roy", 3)
    print(p)
    p.add_user('Max', 5, 2)
    print(*p.users_list)
    p.remove_user("Bill", 2, 2)
    print(*p.users_list)

