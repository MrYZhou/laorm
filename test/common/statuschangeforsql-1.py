from laorm.stream import SqlStateMachine

state_machine = SqlStateMachine()
state_machine.process_keyword("select", "username")
state_machine.process_keyword("from", "user")
state_machine.process_keyword("where", "Account = admin")
state_machine.process_keyword("where", "Password = 123")
state_machine.process_keyword("order_by", "column2 DESC")
state_machine.finalize()
print(state_machine.execute_sql)


# selectByAccountAndPassword [1, 2] ==>
# ['select', 'By', 'Account', 'And', 'Password']
