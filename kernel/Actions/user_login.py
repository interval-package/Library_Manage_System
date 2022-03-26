import sys
import warnings

try:
    from DataLoader import DataBaseAct, sql
except ImportError:
    sys.path.append("../../")
    from DataLoader import DataBaseAct, sql


# 将过程抽象成对象
class LoginProcess(object):
    # 在构造的时候
    def __init__(self, conn):
        pass

    # 验证用户身份
    @staticmethod
    def User_Login_Certification(user_id: str, password) -> (bool, str):
        with sql.connect(DataBaseAct.data_path) as conn:
            try:
                cursor = conn.execute("""
                    select password from User
                    where User.UserID = %s
                    """ % (user_id))
            except sql.DatabaseError as e:
                return False, "User not find, please check your UserId"
        for line in cursor:
            if password in line:
                return True, "Success"
        return False, "Password error, please check your input"

    @staticmethod
    def Get_User_Obj():
        pass