





from stream import SqlStateMachine


state_machine = SqlStateMachine()
state_machine.process_keyword('SELECT', 'username')
state_machine.process_keyword('FROM', 'user')
state_machine.process_keyword('WHERE', 'Account = admin')
state_machine.process_keyword('WHERE', 'Password = 123')
state_machine.process_keyword('ORDER BY', 'column2 DESC')
state_machine.finalize()
print(state_machine.execute_sql)


#通过状态机来对一个sql方法解析为sql语句,下一个阶段dynamic-basic
# selectByAccountAndPassword [1, 2] ==>
# ['select', 'By', 'Account', 'And', 'Password']