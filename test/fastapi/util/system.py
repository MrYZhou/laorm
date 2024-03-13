import importlib
import os
import sys

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from fastapi.responses import JSONResponse

from util.PPAFastAPI import PPAFastAPI


class Env:
    # 路由注册
    def initRouter(app: FastAPI):
        # 是否为已打包环境
        if getattr(sys, "frozen", False):
            base_path = os.path.join(sys._MEIPASS, "router")
        else:
            base_path = os.path.join(os.getcwd(), "test/fastapi/router")

        # 获取当前目录下所有非目录项（即文件）
        files_in_current_dir = [
            f
            for f in os.listdir(base_path)
            if os.path.isfile(os.path.join(base_path, f))
        ]

        # 解析规则:放在router模块下面的文件 (文件夹下文件)
        for file in files_in_current_dir:
            file = file.replace(".py", "")
            if file in ["__init__", ".pyc"]:
                continue
            m = importlib.import_module("router." + file)
            app.include_router(m.router)

    def initHttp(app: FastAPI):
        # 资源访问
        origins = [
            "http://localhost",
        ]

        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def initDataBase(app):
        PPAFastAPI.init_app(app)
        PPAFastAPI.showSql(True)

  

    @staticmethod
    def init(app: FastAPI):
        Env.initDataBase(app)
        Env.initHttp(app)
        Env.initRouter(app)

   
