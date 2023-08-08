class User:
    def __init__(self, name, u_id, level=None):
        self.u_id = u_id
        self.name = name
        self.level = level

    def __str__(self):
        return f'\tID: {self.u_id}\t NAME: {self.name:<4}\t LEVEL: {self.level}\n'

    def __eq__(self, other):
        return self.u_id == other.u_id and self.name == other.name