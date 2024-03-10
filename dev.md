提交执行格式化
ruff format .

打包
poetry build --format=sdist

发布
python -m twine upload dist/*

快捷发布
./build.bat

先安装在本地调试
pip install . 