流式操作
User.select("*").where(name="123").orderby("date").where(age=18).get()

支持的api
select()
sql()
where()
get(string id)
getList(list[] ids)
update(u:User)
insert(u:User)
delete(u:User)