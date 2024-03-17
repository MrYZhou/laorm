提交执行格式化
ruff format .

打包
poetry build --format=sdist

发布
python -m twine upload dist/*

快捷发布
1.全局搜索上一次的版本号。然后替换为新的
2.执行./build.bat脚本一键上传

先安装在本地调试
pip install . 