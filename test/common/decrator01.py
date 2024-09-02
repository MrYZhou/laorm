import asyncio
import threading
import aiomysql


# def id(field):
#     def wrapper(cls):
#         pass    
#     return field
# class TaskInfo:
#     @id()
#     id:str
conMap={}
async def main():
    try:
       
        startup_params ={
                "host": "127.0.0.1",
                "port": 3306,
                "user": "root",
                "password": "root",
                "db": "study",
                "charset": "utf8mb4",
                "autocommit": True,
            }
        pool=await aiomysql.create_pool(**startup_params)

        current_thread = threading.current_thread()
        # conMap.put(current_thread.getName(),pool.acquire())
        # print(conMap)
        params = ('1234516', 'task1')
        async with pool.acquire() as conn:
             # 开始事务
            conn.start_transaction()

            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute("insert into book(id,name) values(%s,%s)", params)
                res= await cur.fetchone()
                print(res)
            print(1/0)

            #提交事务
            conn.commit()    
    except Exception as e:
        print(e)
        # 发生错误时回滚事务
        conn.rollback()
        return None
    
loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()