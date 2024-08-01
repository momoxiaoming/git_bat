@echo off
echo %cd
set/p option=alias:
del output.zip
"jre\bin\java.exe" -jar pepk.jar --keystore=%1 --alias=%option% --output=output.zip --include-cert --encryptionkey=eb10fe8f7c7c9df715022017b00c6471f8ba8170b13049a11e6c09ffe3056a104a3bbe4ac5a955f4ba4fe93fc8cef27558a3eb9d2a529a2092761fb833b656cd48b9de6a
pause