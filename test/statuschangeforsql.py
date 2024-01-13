class SqlStateMachine:
    def __init__(self):
        self.states = ['INITIAL', 'SELECT', 'FROM', 'WHERE', 'GROUP_BY', 'HAVING', 'ORDER_BY', 'FINAL']
        self.current_state = 'INITIAL'
        self.sql_parts = {
            'select': [],
            'from': '',
            'where': [],
            'group_by': [],
            'having': [],
            'order_by': []
        }

    def process_keyword(self, keyword, value=None):
        if keyword in ['SELECT', 'FROM', 'WHERE', 'GROUP BY', 'HAVING', 'ORDER BY']:
            if self.current_state not in ['INITIAL', keyword.lower()]:
                raise ValueError("Invalid state transition")
            
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
            sql_query += "WHERE {' AND '.join(self.sql_parts['where'])} "
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
state_machine.process_keyword('SELECT', '*')
state_machine.process_keyword('FROM', 'table_name')
state_machine.process_keyword('WHERE', 'column1 = value1')
state_machine.process_keyword('ORDER BY', 'column2 DESC')

print(state_machine.sql_query)