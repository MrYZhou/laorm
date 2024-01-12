方式1 动态查询

class User:
    name:str
    id:str
    @sql
    def selectByAccountAndPassword(a: int, b: str) -> 'List[User]':pass

# 示例调用
user_count:List[User] = User.selectByAccountAndPassword(1,2)
print(user_count)

或者 User.dynamic('selectByAccountAndPassword',a,b) 

方式2 链式操作

User.select("*").where(name="123").orderby("date").where(age=18).get()

方式3 sql直接执行

PPA.exec("SELECT * FROM config where id!=1")

支持的api

select()
sql()
group()
get(string id)
getList(list[] ids)
update(u:User)
updateBatch(u:List[User])
insert(u:User)
insertBatch(u:List[User])
delete(u:User)
deleteBatch(u:List[id])