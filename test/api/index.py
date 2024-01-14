from typing import List, Union, TypeVar
from abc import ABCMeta
class SqlStateMachine:
    def __init__(self):
        self.states = ['INITIAL', 'SELECT', 'FROM', 'WHERE', 'GROUP_BY', 'HAVING', 'ORDER_BY', 'FINAL']
        self.current_state = 'INITIAL'
        self.keyword = ['SELECT', 'FROM', 'WHERE', 'GROUP BY', 'HAVING', 'ORDER BY']
        self.sql_parts = {
            'select': [],
            'from': '',
            'where': [],
            'group_by': [],
            'having': [],
            'order_by': []
        }
    def process_keyword(self, keyword, value=None):
        keyword = keyword.upper()
        print( self.sql_parts)
        # 异常返回
        if self.current_state == 'SELECT' and  keyword!='BY':
            return
        if keyword == 'SELECT':
            self.sql_parts['select'].append(value)
            self.current_state = 'SELECT'
        elif keyword == 'FROM':
            self.sql_parts['from'] = value
            self.current_state = 'FROM'
        elif keyword == 'WHERE':
            self.sql_parts['where'].append(value)
            self.current_state = 'WHERE'
        elif keyword == 'GROUP_BY':
            self.sql_parts['group_by'].append(value)
            self.current_state = 'GROUP_BY'
        elif keyword == 'HAVING':
            self.sql_parts['having'].append(value)
            self.current_state = 'HAVING'
        elif keyword == 'ORDER_BY':
            self.sql_parts['order_by'].append(value)
            self.current_state = 'ORDER_BY'
        elif keyword == 'BY':
            # self.sql_parts['order_by'].append(value)
            self.current_state = 'BY'
            pass  # 其他可能的状态处理
            
        self.finalize()

    def finalize(self):
        # 改成模板方法进行构建步骤
        sql_query = f"SELECT {' ,'.join(self.sql_parts['select'])} FROM {self.sql_parts['from']} "
        if self.sql_parts['where']:
            sql_query += f"WHERE {' AND '.join(self.sql_parts['where'])} "
        if self.sql_parts['group_by']:
            sql_query += f"GROUP BY {' ,'.join(self.sql_parts['group_by'])} "
        if self.sql_parts['having']:
            sql_query += f"HAVING {' AND '.join(self.sql_parts['having'])} "
        if self.sql_parts['order_by']:
            sql_query += f"ORDER BY {' ,'.join(self.sql_parts['order_by'])} "
        
        self.sql_query = sql_query
        self.current_state = 'FINAL'


T = TypeVar('T', bound='LaModel')

class LaModel(metaclass=ABCMeta):
    # def __new__(self) -> None:
    #     self.excuteSql = ''

    excuteSql = ''
    state_machine = SqlStateMachine()    
    @classmethod
    def select(cls: type[T], params:str = "*" ):
        print("SELECT", print(id(cls.state_machine)))
        return cls
    @classmethod
    def sql(cls: type[T]):
        print("sql:"+ cls.excuteSql)
        return cls   
    @classmethod
    def where(cls: type[T],*args):
        print("sql:"+ cls.excuteSql)
        return cls

    # 结束方法,需要进行sql的构建,执行

    @classmethod
    def get(cls: type[T], primaryId: Union[int, str]):
        print("get one", print(id(cls.state_machine)))
       
    @classmethod
    def getList(cls: type[T], primaryIdList: Union[List[int], List[str]]):
        print("getList", primaryIdList)   

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
            tablename = _table_name if _table_name else cls.__name__.lower()  # 将表名存储到类属性中
        return DecoratedModel
    return wrapper


@table('user')
class User:
    id:str = FieldDescriptor(primary=True)
    name:str = FieldDescriptor()

@table('user2')
class User2:
    id:str = FieldDescriptor(primary=True)
    name:str = FieldDescriptor()




User.select().sql().get(1)


# User2.select().sql().get(1)

#2. FieldDescriptor属性赋值方法，可以对字段进行收集，为后续的功能打下环境基础
# print(User.tablename,User.dictMap)


