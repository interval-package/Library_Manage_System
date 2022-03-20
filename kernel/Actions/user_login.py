import sys
import warnings

try:
    from DataLoader import DataBaseAct, sql
except ImportError:
    sys.path.append("../../")
    from DataLoader import DataBaseAct, sql


def User_Login(user_id: int, password) -> (bool, str):
    with sql.connect(DataBaseAct.data_path) as conn:
        try:
            cursor = conn.execute("""
                select password from User
                where User.UserID = %s
                """ % (str(user_id)))
        except sql.DatabaseError as e:
            return False, "User not find, please check your UserId"
    for line in cursor:
        if password in line:
            return True, "Success"
    return False, "Password error, please check your input"


def Get_User_Obj():
    pass
