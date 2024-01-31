先进行一定的配置然后调用初始化init_app
1.在fastapi中使用
```
from laorm.core.PPA import PPA
from fastapi import FastAPI

class PPAFastAPI(PPA):
    _instance = None

    # 集成主要就是注册对应框架的开启和结束的生命周期
    @classmethod
    def init_app(cls, app: FastAPI, *args):
        if cls._instance is None:
            default_values = {
                "host": "127.0.0.1",
                "port": 3306,
                "user": "root",
                "password": "root",
                "db": "study",
                "charset": "utf8mb4",
                "autocommit": True,
            }
            args = {**default_values, **args[0]} if len(args) == 1 else default_values
            cls._instance = cls()
            # 将更新后的args传递给startup方法以便初始化数据库连接池
            cls.startup_params = args
            app.add_event_handler("startup", cls.startup)
            app.add_event_handler("shutdown", cls.shutdown)

```
```
app = FastAPI()
PPAFastAPI.init_app(app)
```
2.flask中使用
```
from flask import Flask
from laorm.core.PPA import PPA

class PPAFlask(PPA):
    _instance = None

    @classmethod
    def init_app(cls, app: Flask, *args):
        if cls._instance is None:
            default_values = {
                "host": "127.0.0.1",
                "port": 3306,
                "user": "root",
                "password": "root",
                "db": "study",
                "charset": "utf8mb4",
                "autocommit": True,
            }
            args = {**default_values, **args[0]} if len(args) == 1 else default_values
            cls._instance = cls()
            # 将更新后的args传递给startup方法以便初始化数据库连接池
            cls.startup_params = args
            app.before_first_request(cls.startup)
            app.teardown_appcontext(cls.shutdown)

```
```
# 创建 Flask 应用实例
app = Flask()
# 初始化 PPAFlask
PPAFlask.init_app(app, {"host": "your_host", "password": "your_password"})  # 示例参数
```
3.django中使用
使用自带的就成，或者自己处理连接池关闭事件。

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