# Доработать класс Project
# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.
import json
from User import User
from Exceptions import UserNotFoundError, LevelError, NotFoundError


class Project:

    def __init__(self, users_list):
        if users_list is None:
            self.users_list = []
        self.users_list = users_list
        self.u_admin = None

    @classmethod
    def load_js(cls):
        with open('task2.json', 'r', encoding='utf-8') as f:
            my_dict = json.load(f, object_hook=lambda d: {int(k) if k.isdigit() else k: v for k, v in d.items()})
        project_users = []
        for level, users in my_dict.items():
            for user_id, name in users.items():
                user = User(name, user_id, level)
                project_users.append(user)
        return Project(project_users)

    def enter(self, name, u_id):

        user = User(name, u_id)
        for proj_user in self.users_list:
            if user == proj_user:
                self.u_admin = proj_user
                break
        else:
            raise UserNotFoundError(name, u_id)

    def add_user(self, name, id_, level):

        if self.u_admin is None:
            raise NotFoundError
        if level > self.u_admin.level:
            raise LevelError(level, self.u_admin.level)
        self.users_list.append(User(name, id_, level))

    def remove_user(self, name, u_id, level):

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

        self.file = open(f'new_file.json', 'w', encoding='utf-8')
        temp = {k: {} for k in range(1, 8)}
        for user in self.users_list:
            temp[user.level].update({user.u_id: user.name})
        json.dump(temp, self.file, ensure_ascii=False)
        self.file.close()


with Project.load_js() as p:
    print(*p.users_list)
    p.enter("Roy", 5)
    print(p)
    p.add_user('Max', 5, 2)
    print(*p.users_list)
    p.remove_user("Bill", 2, 2)
    print(*p.users_list)

