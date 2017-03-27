:input
::bat标题
@echo =====================================================
@echo 输入"1" 获取本机IP配置信息，并生成‘txt’文件。
@echo -----------------------------------------------------
@echo 输入"2" 上传路由器固件，修改IP地址并自动打开指定地址。
@echo -----------------------------------------------------
@echo 输入"3" 设置本地连接为自动获取（DHCP）。
@echo =====================================================
@echo off
set /p   "num=请输入数字，然后按下回车键："

if "%num%"=="1" cls & goto 1
if "%num%"=="2" cls & goto 2
if "%num%"=="3" cls & goto 3

if "%num%"=="3" cls & goto 3
echo. & echo 不能输入除了“1至3”之外的其他字符！ & pause>nul & cls & goto input


:1
echo =====================================================
echo ===================网卡信息获取成功==================
echo =====================================================
ipconfig /all >本地网络连接信息.txt
@echo ----                                            ----
@echo               请等待通知，进行第二步操作
@echo ----                                            ----
pause
pause>nul
cls & goto input


:2
echo =====================================================
echo ============请在IE浏览器中，上传路由器固件===========
echo =====================================================
for /f "tokens=1*" %%a in ('ipconfig^|findstr "以太网适配器"') do set "ipname=%%b"
netsh interface ip set address "%ipname:~0,-1%" static 192.168.1.111 255.255.255.0 192.168.1.1 1
start "" "iexplore" "192.168.1.1"
@echo ----                                            ----
@echo               请等待固件上传完成，再操作
@echo ----                                            ----
pause
pause>nul
cls & goto input


:3
echo =====================================================
echo ===========设置本地连接为自动获取（DHCP）============
echo =====================================================
for /f "tokens=1*" %%a in ('ipconfig^|findstr "以太网适配器"') do set "ipname=%%b"
netsh interface ip set address name=""%ipname:~0,-1%"" source=dhcp
netsh interface ip set dns name="%ipname:~0,-1%" source=dhcp
pause
pause>nul
cls & goto input
