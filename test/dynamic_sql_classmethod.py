import inspect
from typing import List

def sql(func):
   
    sig = inspect.signature(func)
    return_annotation = sig.return_annotation
    def wrapper(*args, **kwargs):
        
        # 获取方法名和参数
        method_name = func.__name__
        method_cache_name = func.__qualname__
        params = [str(arg) for arg in args]
        print(params, method_name,method_cache_name)
          
        # 检查并处理返回类型
        
        print(f"Method '{method_name}' has a return type annotation of: {return_annotation}")

        # 翻译方法成SQL语句
        if method_name == 'selectByAccountAndPassword':
            # 这里模拟根据return_annotation返回对应类型的值,比如列表处理为列表,单个处理单个对象
            # todo 后期优化为从对象内部的局部map获取类定义，然后用反射创建对象

            return params[1:]
        raise ValueError(f"Unsupported SQL operation for method: {method_name}")

    # 转换为类方法并返回
    return classmethod(wrapper)


class User:
    name:str
    id:str
    @sql
    def selectByAccountAndPassword(a: int, b: str) -> 'List[User]':pass

# 示例调用
user_count:List[User] = User.selectByAccountAndPassword(1,2)
print(user_count)