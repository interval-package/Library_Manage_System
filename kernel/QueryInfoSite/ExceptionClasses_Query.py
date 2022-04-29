
class DefinedQueryException(Exception):
    def __init__(self, msg=None):
        super(DefinedQueryException, self).__init__(msg)
        pass


class RentRefuse(DefinedQueryException):
    def __init__(self, msg=''):
        super(RentRefuse, self).__init__("Rent Refused"+msg)
        pass


class ReturnRefuse(DefinedQueryException):
    def __init__(self, msg='return refused'):
        super(ReturnRefuse, self).__init__(msg)
        pass
