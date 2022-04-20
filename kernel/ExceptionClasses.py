
class DefinedQueryException(Exception):
    def __init__(self, msg=None):
        super(DefinedQueryException, self).__init__(msg)
        pass


class RentRefuse(DefinedQueryException):
    def __init__(self, msg=None):
        super(RentRefuse, self).__init__("Rent Refused"+msg)
        pass
