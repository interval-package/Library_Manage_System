# 这个是所有用户基类
from kernel.QueryInfoSite.QueryInfo import Query_UserRentingHis


class BasicUser(object):
    def __init__(self, user_id, user_name, role, password):
        self.id = user_id
        self.name = user_name
        self.role = role
        self.password = password

        self.RentHis = Query_UserRentingHis(self.id)
        pass

    def updateRentHis(self):
        self.RentHis = Query_UserRentingHis(self.id)


def UserGet(pack) -> BasicUser:
    Uid, name, role, password = pack
    res = BasicUser(Uid, name, role, password)
    return res
