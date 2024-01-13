class SqlStateMachine:
    def __init__(self):
        self.states = ['INITIAL', 'SELECT', 'FROM', 'WHERE', 'GROUP_BY', 'HAVING', 'ORDER_BY', 'FINAL']
        self.current_state = 'INITIAL'
        self.keyword = ['SELECT', 'FROM', 'WHERE', 'GROUP BY', 'HAVING', 'ORDER BY']
        self.sql_parts = {
            'select': [],
            'from': '',
            'where': [],
            'group_by': [],
            'having': [],
            'order_by': []
        }
    def process_keyword(self, keyword, value=None):
        print( self.sql_parts)
        if keyword in  self.keyword:
            
            if keyword == 'SELECT':
                self.sql_parts['select'].append(value)
                self.current_state = 'SELECT'
            elif keyword == 'FROM':
                self.sql_parts['from'] = value
                self.current_state = 'FROM'
            elif keyword == 'WHERE':
                self.sql_parts['where'].append(value)
                self.current_state = 'WHERE'
            elif keyword == 'GROUP BY':
                self.sql_parts['group_by'].append(value)
                self.current_state = 'GROUP_BY'
            elif keyword == 'HAVING':
                self.sql_parts['having'].append(value)
                self.current_state = 'HAVING'
            elif keyword == 'ORDER BY':
                self.sql_parts['order_by'].append(value)
                self.current_state = 'ORDER_BY'
            else:
                pass  # 其他可能的状态处理
            
        self.finalize()

    def finalize(self):
        sql_query = f"SELECT {' ,'.join(self.sql_parts['select'])} FROM {self.sql_parts['from']} "
        if self.sql_parts['where']:
            sql_query += f"WHERE {' AND '.join(self.sql_parts['where'])} "
        if self.sql_parts['group_by']:
            sql_query += f"GROUP BY {' ,'.join(self.sql_parts['group_by'])} "
        if self.sql_parts['having']:
            sql_query += f"HAVING {' AND '.join(self.sql_parts['having'])} "
        if self.sql_parts['order_by']:
            sql_query += f"ORDER BY {' ,'.join(self.sql_parts['order_by'])} "
        
        self.sql_query = sql_query
        self.current_state = 'FINAL'

# 使用状态机构建SQL语句
state_machine = SqlStateMachine()
state_machine.process_keyword('SELECT', 'username')
state_machine.process_keyword('FROM', 'user')
state_machine.process_keyword('WHERE', 'Account = admin')
state_machine.process_keyword('WHERE', 'Password = 123')
state_machine.process_keyword('ORDER BY', 'column2 DESC')

print(state_machine.sql_query)


#通过状态机来对一个sql方法解析为sql语句,下一个阶段dynamic-basic
# selectByAccountAndPassword [1, 2] ==>
# ['select', 'By', 'Account', 'And', 'Password']