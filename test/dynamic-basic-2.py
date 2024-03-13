import asyncio
from laorm.stream import FieldDescriptor, table


@table("user")
class User:
    id: str = FieldDescriptor(primary=True)
    name: str = FieldDescriptor()



# 测试数据
loop = asyncio.get_event_loop()
result = loop.run_until_complete(
   User.dynamic('selectByAccountAndPassword',[1,2])
)

# 打印结果
print(result)


