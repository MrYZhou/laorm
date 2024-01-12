import inspect
from typing import List

def sql(func):
    if hasattr(func, '__func__'):  # 检查func是否已经是类方法（具有__func__属性）
        is_classmethod = True
    else:
        is_classmethod = False
    
    sig = inspect.signature(func)
    return_annotation = sig.return_annotation
    def wrapper(*args, **kwargs):
        # nonlocal is_classmethod
        
        # 获取方法名和参数
        method_name = func.__name__
        method_cache_name = func.__qualname__
        params = [str(arg) for arg in args]
        print(params, method_name,method_cache_name)
          
        # 检查并处理返回类型
        if return_annotation is not inspect.Signature.empty:
            print(f"Method '{method_name}' has a return type annotation of: {return_annotation}")

       

        # 翻译方法成SQL语句
        if method_name == 'selectByAccountAndPassword':
            # 这里模拟根据return_annotation返回对应类型的值,比如列表处理为列表,单个处理单个对象
            # todo 后期优化为从对象内部的局部map获取类定义，然后用反射创建对象

            return params[1:]
        raise ValueError(f"Unsupported SQL operation for method: {method_name}")

         
        
    # 如果原函数不是类方法，则将其转换为类方法并返回
    if not is_classmethod:
        wrapper = classmethod(wrapper)

    return wrapper


class User:
    name:str
    id:str
    @sql
    def selectByAccountAndPassword(a: int, b: str) -> 'List[User]':pass

# 示例调用
user_count = User.selectByAccountAndPassword(1,2)
print(user_count)