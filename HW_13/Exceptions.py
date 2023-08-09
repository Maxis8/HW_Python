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

