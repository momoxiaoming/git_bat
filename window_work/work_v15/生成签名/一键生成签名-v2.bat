chcp 65001
@echo off
del /q /s ".\file\*.*"
del /q /s ".\output\*.*"
set /p input=输入签名国家: 
set /p input2=输入签名省市: 
set /p input3=输入签名地区: 
set /p input4=输入签名别名:
set /p input5=输入签名密码:

set GOOGLE_PATH=.\\output\\google_%input4%.zip
set JKS_PATH=.\\%input4%.tar
set KEYSTORE_PATH=.\\file\\%input4%.jks
set KEYSTORE_ALIAS=%input4%
set KEYSTORE_PASSWORD=%input5%
set KEYSTORE_KEY_PASSWORD=%input5%
set OUTPUT_PATH=.\\output\\%input4%.tar

keytool -genkey -v -keystore %KEYSTORE_PATH% -alias %KEYSTORE_ALIAS% -keyalg RSA -keysize 2048 -validity 10000 -storepass %KEYSTORE_PASSWORD% -keypass %KEYSTORE_KEY_PASSWORD% -dname "CN=%input4%,OU=%input4%,O=%input4%,L=%input%,ST=%input2%,C=%input3%"
echo 签名生成完成
echo 别名:%input4% >> .\\file\\签名说明.txt
echo 密码:%input5% >> .\\file\\签名说明.txt
tar -cvf %OUTPUT_PATH% .\\file
java -jar .\\tools\pepk.jar --keystore=%KEYSTORE_PATH% --alias=%KEYSTORE_ALIAS% --keystore-pass=%KEYSTORE_PASSWORD% --key-pass=%KEYSTORE_KEY_PASSWORD% --output=%GOOGLE_PATH% --include-cert --rsa-aes-encryption --encryption-key-path=.\\tools\encryption_public_key.pem
echo 托管签名生成完成
pause

