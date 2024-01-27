import re

from stream import FieldDescriptor, table




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

#parsql 完成后得到查询字符串然后只要直接用ppa执行exec即可