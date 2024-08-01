chcp 65001
@echo off
echo 当前工作目录：%cd%
setx JAVA_HOME "%cd%\tools\jdk11\jre"
setx classpath "%%JAVA_HOME%%\bin"
setx PATH "%cd%\tools\Python3111\Scripts;%cd%\tools\Python3111;%cd%\tools\obs-gen-210512\win;%cd%\tools\Git\bin;%cd%\tools\Sdk\platform-tools;%cd%\tools\Sdk\tools;%cd%\tools\Sdk\build-tools\33.0.0;%%JAVA_HOME%%\bin;%PATH%;"
pause