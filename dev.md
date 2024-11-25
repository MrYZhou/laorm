1.依赖安装
pip install poetry
poetry update

2.格式化(可选)
pip install ruff (如果没安装 ruff)
提交执行格式化
ruff format .

3.测试
在本地调试安装测试
pip install .
然后只需要让当前项目的 venv 环境和测试项目的一致即可。

4.快捷发布 1.全局搜索上一次的版本号。然后替换为新的 2.执行./build.bat 脚本一键上传
