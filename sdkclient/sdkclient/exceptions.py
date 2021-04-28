

class SDKBaseException(Exception):
    """
    Base class for SDK client exceptions.
    """
    default_detail = 'A SDK client error occurred.'
    default_code = 'ERR-000'

    def __init__(self, detail=None, code=None):
        if detail is None:
            self.detail = self.default_detail
        if code is None:
            self.code = self.default_code

    def __str__(self):
        return f"{self.code} {self.detail}"


class AuthenticationFailed(BaseException):
    default_detail = 'A SDK client authentication failed.'
    default_code = 'ERR-401'


class FatalError(BaseException):
    default_detail = 'A SDK client fatal error occured.'
    default_code = 'ERR-50X'
