from math import log
from os import name
from typing import Union, TypeVar
from abc import ABCMeta

from sqlalchemy import false, true

T = TypeVar('T', bound='Model')

class Model(metaclass=ABCMeta):

    @classmethod
    def get(cls: type[T], id: Union[int, str]):
        print("get one", id)

    @classmethod
    def delete(cls: type[T], id: Union[int, str]):
        print(f"delete one{str(id)}")


# 自定义生成sql
def sql(cls):
    pass

class FieldDescriptor:
    
    def __init__(self, primary=False):
        self.primary = primary
        

    # def __get__(self, instance, owner):
    #     return instance.__dict__.get(self.name)

    # def __set__(self, instance, value):
    #     print(instance, value)
    #     instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        # 在描述符绑定到类时自动记录属性名和注解信息
        # print(self, owner, name)
        # 获取owner的类名user
        # print(owner.__name__,name,self.primary,owner.dictMap)
        owner.dictMap[name] = {}
        owner.dictMap[name]['primary'] = self.primary
        # owner.dictMap = {**owner.dictMap,name:self.primary}
        # self.name = name
        # if hasattr(self, '_field_annotations'):
        #     self._field_annotations[name] = {'primary': self.primary}
        # else:
        #     self._field_annotations = {name: {'primary': self.primary}}


# 元类装饰器实现
def table(name:str):
    def wrapper(cls):
        class DecoratedModel(Model, cls):
            _table_name = name  # 将表名存储到类属性中
            
            # 如果需要执行其他初始化操作，可以在 __init_subclass__ 中添加
            @classmethod
            def __init_subclass__(cls, **kwargs):
                super().__init_subclass__(**kwargs)
                cls._table_name = name

        return DecoratedModel
    return wrapper

@table('user')
class User:
    dictMap:dict = {}
    id:str = FieldDescriptor(primary=True)
    name:str = FieldDescriptor()
    # @sql
    # def selectByAccountAndPassword(a:str,b:str):pass
      


# 现在 User 类已经有了 get 和 delete 方法
# User.get(1)
# User.delete(1)


# User.selectByAccountAndPassword("123","123")
    
print(User._table_name,User.dictMap)