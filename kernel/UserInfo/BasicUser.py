import abc


# 这个是所有用户基类
class BasicUser(object):
    @abc.abstractmethod
    def __init__(self, user_name, user_id):
        self.name = user_name
        self.id = user_id
        pass
