
链式操作

流式操作

User.select("*").where(name="123").orderby("date").where(age=18).get()

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