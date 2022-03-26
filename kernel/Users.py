import abc


# 这个是所有用户基类
from kernel.Quary_Info import Query_UserRentingHis


class BasicUser(object):
    def __init__(self, user_id, user_name, role, password):
        self.id = user_id
        self.name = user_name
        self.role = role
        self.password = password

        self.RentHis = Query_UserRentingHis(self.id)
        pass


def UserGet(pack) -> BasicUser:
    Uid, name, role, password = pack
    res = BasicUser(Uid, name, role, password)
    return res
