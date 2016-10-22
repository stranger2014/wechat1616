# -*- coding: utf-8 -*-
#



__author__ = "Epsirom"


class BaseError(Exception):

    def __init__(self, code, msg):
        super(BaseError, self).__init__(msg)
        self.code = code
        self.msg = msg

    def __repr__(self):
        return '[ERRCODE=%d] %s' % (self.code, self.msg)


class InputError(BaseError):    #参数错误

    def __init__(self, msg):
        super(InputError, self).__init__(1, msg)


class LogicError(BaseError):   #逻辑错误

    def __init__(self, msg):
        super(LogicError, self).__init__(2, msg)


class ValidateError(BaseError): #验证错误

    def __init__(self, msg):
        super(ValidateError, self).__init__(3, msg)

class LoginError(BaseError):   #登陆错误

    def __init__(self, msg):
        super(LoginError, self).__init__(4, msg)

class LogoutError(BaseError):   #登陆错误

    def __init__(self, msg):
        super(LogoutError, self).__init__(5, msg)

class ActivityDetailError(BaseError):   #活动获取错误

    def __init__(self, msg):
        super(ActivityDetailError, self).__init__(6, msg)

class ActivityDeleteError(BaseError):   #活动删除错误

    def __init__(self, msg):
        super(ActivityDeleteError, self).__init__(7, msg)

class ActivityCreateError(BaseError):   #活动创建错误

    def __init__(self, msg):
        super(ActivityCreateError, self).__init__(8, msg)

class ImageUploadError(BaseError):   #活动创建错误

    def __init__(self, msg):
        super(ImageUploadError, self).__init__(9, msg)