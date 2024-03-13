import asyncio
from typing import List

from laorm import table

from laorm.stream import sql


@table
class User:
    name: str
    id: str

    @sql
    async def selectByAccountAndPassword(a: int, b: str) -> "List[User]":
        pass


# 示例调用

loop = asyncio.get_event_loop()
# user_count: List[User] = loop.run_until_complete(
#     User.selectByAccountAndPassword(1, "123")
# )
User.selectByAccountAndPassword(1, "123")
# 打印结果
# print(user_count)
