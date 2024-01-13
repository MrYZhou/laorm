import re
from typing import Dict, List, Union, TypeVar
from abc import ABCMeta


T = TypeVar('T', bound='LaModel')

class LaModel(metaclass=ABCMeta):

    @classmethod
    def dynamic(cls: type[T], dynamicSql: str,params: Union[Dict[str, any], tuple, list] = None):
        # 翻译dynamicSql
        print("get ---",dynamicSql, params)

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


User.dynamic('selectByAccountAndPassword',[1,2])    

def parseMethodToSql(dynamicSql: str):
    # 使用正则表达式找到所有大写字母的位置并进行分割
    parts = re.split('(?=[A-Z])', dynamicSql)
    # 去除可能出现的空字符串（例如：首位是大写字母的情况）
    parts = [part for part in parts if part]
    return parts

# 测试数据
combined_input = "selectByAccountAndPassword"
result = parseMethodToSql(combined_input)
print(result)