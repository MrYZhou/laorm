import asyncio
import time
from typing import List
from fastapi import APIRouter


from laorm.stream import FieldDescriptor, sql, table
from laorm.PPA import PPA


from util.response import AppResult


router = APIRouter(
    prefix="/example",
    tags=["示例代码"],
    responses={404: {"description": "Not found"}},
)


@table("config")
class Config1:
    id: str = FieldDescriptor(primary=True)
    name: str = FieldDescriptor()

    @sql
    def selectByName(name: str) -> list["Config1"]:
        pass

    # @sql
    # def selectByName(name:str)->'Config1':pass


# 读取自定义方法的返回类型
@router.get("/config2/getdy")
async def getdy2():
    res: List[Config1] = await Config1.selectByName(22)
    return AppResult.success(res)


# dynamic 都是查询数组回来
@router.get("/config2/getdy2")
async def getdy():
    res = await Config1.dynamic("selectByIdAndName", [2, 456])
    # res = await Config1.dynamic('selectByName',123)
    return AppResult.success(res)


# 默认get是查询首个对象, getList自动为数组
@router.get("/config2/get")
async def get_config2():
    res = await Config1.where(name=22).get()
    # res = await Config1.where(name=22).getList()
    return AppResult.success(res)


@router.post("/config2/add")
async def addone():
    await Config1.delete(1)
    await Config1.delete(2)
    config1 = Config1()
    config1.id = 1
    config1.name = 123
    config12 = Config1()
    config12.id = 2
    config12.name = 456
    configlist = [config12]
    await Config1.post(config1)
    await Config1.post(configlist)
    return AppResult.success()


@router.delete("/config2/delete")
async def deleteone():
    await Config1.delete(1)
    # res = await Config1.where(name=22).delete()
    return AppResult.success()


@router.delete("/config2/deletedy")
async def deletedy():
    config1 = Config1()
    config1.id = 1
    config1.name = 123
    await Config1.post(config1)
    await Config1.dynamic("deleteById", 1)
    return AppResult.success()


@router.put("/config2/update")
async def updateone():
    config1 = Config1()
    config1.id = 1
    config1.name = 123
    res = await Config1.where(name=22).update(config1)
    return AppResult.success(res)


@router.get("/config")
async def get_config():
    start_time = time.time()
    # 创建并发任务
    tasks = [
        PPA.exec("SELECT * FROM config where id=1"),
        # PPA.exec("SELECT * FROM config where id!={name}",{"name":1}),
        # PPA.exec("SELECT * FROM config where id!=?",[1]),
        # PPA.exec("SELECT * FROM config where id!=?", (1,)),
    ]

    # 并发执行并获取结果
    results = await asyncio.gather(*tasks)
    print(results)
    end_time = time.time()
    execution_time = end_time - start_time
    for i in results:
        print(i[0].get("id"))
    print(f"代码执行时间aio: {execution_time} 秒")
    return AppResult.success(results[0])