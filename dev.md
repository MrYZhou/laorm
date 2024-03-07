提交执行格式化
ruff format .

打包
poetry build --format=sdist

发布
python -m twine upload dist/*

快捷
./build.bat