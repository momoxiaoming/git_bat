chcp 65001
@echo off
del /q /s ".\apk\*.*"
echo 目录清理完成...
set /p input=aab路径:
set /p input2=签名路径:
set /p input3=输入签名别名:
set /p input4=输入签名密码:

set  outputFile=.\apk\app.apks
echo 输出apks文件...
bundletool-all-1.15.2.jar build-apks --bundle=%input% --output=%outputFile% --overwrite --mode=universal --ks=%input2% --ks-key-alias=%input3% --ks-pass=pass:%input4%  --key-pass=pass:%input4%
echo 安装apks文件...
bundletool-all-1.15.2.jar install-apks --apks=%outputFile%
pause
