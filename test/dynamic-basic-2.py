import re

from stream import FieldDescriptor, SqlStateMachine, table


@table("user")
class User:
    id: str = FieldDescriptor(primary=True)
    name: str = FieldDescriptor()


state_machine = SqlStateMachine()
state_machine.process_keyword("from", "user")


# 测试数据
combined_input = "selectByAccountAndPassword"
result = User.parseMethodToSql(combined_input)
state_machine.finalize()
print(state_machine.execute_sql)

# parsql 完成后得到查询字符串然后只要直接用ppa执行exec即可
