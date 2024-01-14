from core.index import PPA
from fastapi import FastAPI


class PPAFastAPI(PPA):
    _instance = None
    pool = None

    @classmethod
    def init_app(cls, app: FastAPI, **kwargs):
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
            kwargs.update(default_values)

            cls._instance = cls()

            # 将更新后的kwargs传递给startup方法以便初始化数据库连接池
            cls.startup_params = kwargs
            app.add_event_handler("startup", cls.startup)
            app.add_event_handler("shutdown", cls.shutdown)

