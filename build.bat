@echo off

REM 删除dist目录下的所有文件（不包括子目录）
del /Q dist\*

REM 如果上面命令执行成功，则继续构建和上传
if %errorlevel% equ 0 (
    poetry build --format=sdist
    if %errorlevel% equ 0 (
        python -m twine upload dist/*
    )
)