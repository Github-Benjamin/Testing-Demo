:input
::bat标题
@echo =====================================================
@echo 输入"1" adb devices
@echo -----------------------------------------------------
@echo 输入"2" adb install ES文件浏览器
@echo -----------------------------------------------------
@echo 输入"3" 清理点击过的广告记录文件，.downloadinfo
@echo -----------------------------------------------------
@echo 输入"4" 清理Android获取到的接口信息，.adinfo
@echo -----------------------------------------------------
@echo 输入"5" 清理Android888，等其他所有缓存文件资源
@echo -----------------------------------------------------
@echo 输入"6" dump /sdcard/tencent/.adinfo 并打开该文件
@echo -----------------------------------------------------
@echo 输入"7" dump /sdcard/tencent/.downloadinfo 并打开该文件
@echo -----------------------------------------------------
@echo 输入"8" dump /sdcard/tencent/.cltimes 并打开该文件
@echo -----------------------------------------------------
@echo 输入"9" adb kill-server
@echo =====================================================
@echo off
set /p   "num=请输入数字，然后按下回车键："
if "%num%"=="1" cls & goto 1
if "%num%"=="2" cls & goto 2
if "%num%"=="3" cls & goto 3
if "%num%"=="4" cls & goto 4
if "%num%"=="5" cls & goto 5
if "%num%"=="6" cls & goto 6
if "%num%"=="61" cls & goto 61
if "%num%"=="7" cls & goto 7
if "%num%"=="71" cls & goto 71
if "%num%"=="8" cls & goto 8
if "%num%"=="81" cls & goto 81
if "%num%"=="9" cls & goto 9

echo. & echo 不能输入除了“1至8”之外的其他字符！ & pause>nul & cls & goto input


:1
echo ======================================================================
echo ===========================adb devices================================
echo ======================================================================
adb devices
pause
pause>nul
cls & goto input

:2
echo =======================================================================
echo ========================adb install 安装APP============================
echo =======================================================================
adb install C:\Users\whoami\Desktop\ad\test_apk\ESFileExplorerTV.pc6.apk
pause
pause>nul
cls & goto input

:3
echo ======================================================================
echo ===============清理点击过的广告记录文件，downloadinfo=================
echo ======================================================================
adb shell rm /sdcard/tencent/.downloadinfo　　
pause
pause>nul
cls & goto input

:4
echo ======================================================================
echo ================清理Android获取到的接口信息，.adinfo==================
echo ======================================================================
adb shell rm /sdcard/tencent/.adinfo　
pause
pause>nul
cls & goto input


:5
echo ======================================================================
echo ===============清理Android888，等其他所有缓存文件资源=================
echo ======================================================================
adb shell rm -r /sdcard/android888
adb shell rm /sdcard/tencent/.adinfo
adb shell rm /sdcard/tencent/.cllock
adb shell rm /sdcard/tencent/.cllog
adb shell rm /sdcard/tencent/.cltimes
adb shell rm /sdcard/tencent/.clauto
adb shell rm /sdcard/tencent/.downloadinfo
pause
pause>nul
cls & goto input

:6
echo ======================================================================
echo =============dump /sdcard/tencent/.adinfo 并打开该文件================
echo ======================================================================
del C:\Users\whoami\Desktop\ad_test\.adinfo
adb pull /sdcard/tencent/.adinfo /Users/whoami/Desktop/ad_test
C:/Users/whoami/Desktop/ad_test/.adinfo
pause
pause>nul
cls & goto input

:61
echo ======================================================================
echo ======================push /sdcard/tencent/.adinfo ===================
echo ======================================================================
adb shell rm /sdcard/tencent/.adinfo
adb push /Users/whoami/Desktop/ad_test/.adinfo /sdcard/tencent
pause
pause>nul
cls & goto input

:7
echo ======================================================================
echo ===========dump /sdcard/tencent/.downloadinfo 并打开该文件============
echo ======================================================================
del C:\Users\whoami\Desktop\ad_test\.downloadinfo
adb pull /sdcard/tencent/.downloadinfo /Users/whoami/Desktop/ad_test
C:/Users/whoami/Desktop/ad_test/.downloadinfo　
pause
pause>nul
cls & goto input


:71
echo ======================================================================
echo =================push /sdcard/tencent/.downloadinfo ==================
echo ======================================================================
adb shell rm /sdcard/tencent/.downloadinfo
adb push /Users/whoami/Desktop/ad_test/.downloadinfo /sdcard/tencent
pause
pause>nul
cls & goto input

:8
echo ======================================================================
echo ==============dump /sdcard/tencent/.cltimes 并打开该文件================
echo ======================================================================
del C:\Users\whoami\Desktop\ad_test\.cltimes
adb pull /sdcard/tencent/.cltimes /Users/whoami/Desktop/ad_test
C:/Users/whoami/Desktop/ad_test/.cltimes　
pause
pause>nul
cls & goto input


:81
echo ======================================================================
echo ====================push /sdcard/tencent/.cltimes ====================
echo ======================================================================
adb shell rm /sdcard/tencent/.cltimes
adb push /Users/whoami/Desktop/ad_test/.cltimes /sdcard/tencent
pause
pause>nul
cls & goto input

:9
echo ======================================================================
echo ===============================adb kill-server========================
echo ======================================================================
adb kill-server
adb kill-server
adb start-server
pause
pause>nul
cls & goto input
