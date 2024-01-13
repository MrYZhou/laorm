from typing import List, Union, TypeVar
from abc import ABCMeta


T = TypeVar('T', bound='LaModel')

class LaModel(metaclass=ABCMeta):

    @classmethod
    def get(cls: type[T], id: Union[int, str]):
        print("get one", id)

    @classmethod
    def delete(cls: type[T], id: Union[int, str]):
        print(f"delete one{str(id)}")

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
        class DecoratedModel(LaModel, cls):
            tablename = _table_name  # 将表名存储到类属性中
        return DecoratedModel
    return wrapper


@table('user')
class User:
    id:str = FieldDescriptor(primary=True)
    name:str = FieldDescriptor()


# 1.现在 User 类已经有了 get 和 delete 方法，说明可以通过元类装饰器实现类的增强。添加我们想给类添加的常见
# sql方法。元装饰器 @table('user')
# User.get(1)
# User.delete(1)

#2. FieldDescriptor属性赋值方法，可以对字段进行收集，为后续的功能打下环境基础
# print(User.tablename,User.dictMap)


