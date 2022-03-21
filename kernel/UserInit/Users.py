import abc


# 这个是所有用户基类
class BasicUser(object):
    @abc.abstractmethod
    def __init__(self, user_name, user_id):
        pass


class SuperUser(BasicUser):
    def __init__(self, user_name, user_id):
        pass
    

class Student(BasicUser):
    def __init__(self, user_name, user_id):
        pass


class Teacher(BasicUser):
    def __init__(self, user_name, user_id):
        pass
