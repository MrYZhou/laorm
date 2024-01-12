from typing import List, Union, TypeVar
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
        
    def __set_name__(self, owner, name):
        if not hasattr(owner, 'dictMap'):
            owner.dictMap = {}
        owner.dictMap[name] = {}
        owner.dictMap[name]['primary'] = self.primary


# 元类装饰器实现
def table(_table_name:str):
    def wrapper(cls):
        class DecoratedModel(Model, cls):
            tablename = _table_name  # 将表名存储到类属性中
            
            # 如果需要执行其他初始化操作，可以在 __init_subclass__ 中添加
            # @classmethod
            # def __init_subclass__(cls, **kwargs):
            #     super().__init_subclass__(**kwargs)
            #     cls.tablename = name

        return DecoratedModel
    return wrapper

@table('user')
class User:
    id:str = FieldDescriptor(primary=True)
    name:str = FieldDescriptor()
    @sql
    def selectByAccountAndPassword(a:str,b:str):List[User]

    @sql
    def selectByAccountAndPassword(a:str,b:str):User


# 现在 User 类已经有了 get 和 delete 方法
# User.get(1)
# User.delete(1)


User.selectByAccountAndPassword("123","123")
    
print(User.tablename,User.dictMap)