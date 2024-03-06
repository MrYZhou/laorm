from typing import List

from stream import sql


class User:
    name: str
    id: str

    @sql
    def selectByAccountAndPassword(a: int, b: str) -> "List[User]":
        pass


# 示例调用
user_count: List[User] = User.selectByAccountAndPassword(1, 2)
print(user_count)

# 转变为User.dynamic('selectByAccountAndPassword',[1,2])
