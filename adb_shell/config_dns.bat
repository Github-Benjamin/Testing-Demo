:input
::bat标题
@echo =====================================================
@echo 输入"1" 修改DNS为：115.182.62.xx
@echo -----------------------------------------------------
@echo 输入"2" 设置本地ip地址、dns连接外网的值
@echo -----------------------------------------------------
@echo 输入"3" 查看本机DNS值
@echo =====================================================
@echo off
set /p   "num=请输入数字，然后按下回车键："
if "%num%"=="1" cls & goto 1
if "%num%"=="2" cls & goto 2
if "%num%"=="3" cls & goto 3
if "%num%"=="DISABLED" cls & goto DISABLED

echo. & echo 不能输入除了“1至3”之外的其他字符！ & pause>nul & cls & goto input


:1
echo =======================================================================
echo ======================修改DNS为：115.182.62.xx=========================
echo =======================================================================
netsh interface ip set dns "以太网" source=dhcp
netsh interface ip set dns "以太网" source=static addr=115.182.62.xx
@echo 修改DNS为：115.182.62.xx
@echo ----------------------------------------------------------------------　　
pause
pause>nul
cls & goto input

:2
echo ======================================================================
echo ====================设置本地ip地址、dns连接外网的值===================
echo ======================================================================
netsh interface ip set dns "以太网" source=dhcp
netsh interface ip set dns "以太网" source=static addr=192.168.29.1
netsh interface ip add dns name="以太网" addr=61.139.2.69 index=2
@echo --------------设置本地ip地址、dns连接外网的值  成功------------------
pause
pause>nul
cls & goto input

:3
echo ======================================================================
echo ========================查看本机IP与DNS配置值=========================
echo ======================================================================
echo ----------------------------------------------------------------------
echo ------------------------------DNS判断---------------------------------
ipconfig /all |find "192.168.29.1"
ipconfig /all |find "61.139.2.69"
ipconfig /all |find "115.182.62.xx"
echo -----------------------------完美分割符-------------------------------
pause
pause>nul
cls & goto input

:DISABLED
netsh interface set interface name="以太网" admin=DISABLED
pause
pause>nul
cls & goto input
