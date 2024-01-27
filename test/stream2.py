from typing import Any, Dict, Sequence, TypeVar, Union
from abc import ABCMeta
from core.stream import PPA,table,FieldDescriptor





@table("user")
class User:
    id:str = FieldDescriptor(primary=True)
    name:str = FieldDescriptor()

# 1.测试打印sql    
# print(User.select().sql())
# 2.测试select    
# User.select().get(1) 
#3.测试直接查询
# User.get(1) 
# 4.测试where

User.where('name',1).match('age',18).get(1)       


# 二、FieldDescriptor测试
#2. FieldDescriptor属性赋值方法，可以对字段进行收集，为后续的功能打下环境基础
# print(User.tablename,User.dictMap)


