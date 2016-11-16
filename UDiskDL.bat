@echo off
color 0a
Title UDiskDL2.0
setlocal enabledelayedexpansion

:MENU
cls
echo.
echo                      UDiskDL2.0 
echo         =======================================
echo                     Machine Model
echo.
echo         1.K320                 2.K360
echo         3.K370                 4.G810
echo         5.G870                 6.G870(upgrade)
echo         7.G3
echo.
echo         d.DEL ALL              e.EXIT 
echo.
echo         =======================================      
echo.
set /p choice=        	Pls Select Machine Model: 

if /i "%choice%"=="1" goto case1
if /i "%choice%"=="2" goto case2
if /i "%choice%"=="3" goto case3
if /i "%choice%"=="4" goto case4
if /i "%choice%"=="5" goto case5
if /i "%choice%"=="6" goto case6
if /i "%choice%"=="7" goto case7
if /i "%choice%"=="d" goto DEL_ALL
if /i "%choice%"=="e" goto EX
goto MENU

:case1
SET MachineMode=K320
SET SubDir=1A
goto Run

:case2
SET MachineMode=K360
SET SubDir=16
goto Run

:case3
SET MachineMode=K370
SET SubDir=17
goto Run

:case4
SET MachineMode=G810
SET SubDir=42
goto Run

:case5
SET MachineMode=G870
SET SubDir=47
goto Run

:case6
SET MachineMode=G870
SET SubDir=4B
goto Run

:case7
SET MachineMode=G3
SET SubDir=31
goto Run

:DEL_ALL
del /f/q mtd0\*
del /f/q mtd0_res\*
del /f/q mtd0_dll\*
echo.
echo         Empty folder mtd0/mtd0_dll/mtd0_res successfully
ping 127.1 -n 2 >nul
goto MENU


:Run
for /f %%i in ('dir /s/b/a-d "mtd0" "mtd0_dll" "mtd0_res" 2^>nul') do (
set /a s+=1
)

echo [History]>config.ini
echo RecentCount=!s!>>config.ini

::files under mtd0
cd mtd0
set /a s=0
for /f %%i in ('dir /b/a-d 2^>nul') do (
cd ..
if not "%%i"=="hl.bin" (
echo Recent!s!=1;%%i;/mtd0/%%i>>config.ini
set /a s+=1
)
cd mtd0
)

if exist "hl.bin" (
cd ..
echo Recent!s!=1;hl.bin;/mtd0/hl.bin>>config.ini
set /a s+=1
cd mtd0
)

::files under mtd0_dll
cd ..\mtd0_dll
for /f %%i in ('dir /b/a-d 2^>nul') do (
cd ..
echo Recent!s!=1;%%i;/mtd0/dll/%%i>>config.ini
set /a s+=1
cd mtd0_dll
)

::files under mtd0_res
cd ..\mtd0_res
for /f %%i in ('dir /b/a-d 2^>nul') do (
cd ..
echo Recent!s!=1;%%i;/mtd0/res/%%i>>config.ini
set /a s+=1
cd mtd0_res
)

::create folder
cd ..
if exist %MachineMode%   rd /s/q %MachineMode%
md %MachineMode%
md %MachineMode%\%SubDir%

::copy files
copy mtd0\* %MachineMode%\%SubDir% 1>nul 2>nul
copy mtd0_dll\* %MachineMode%\%SubDir% 1>nul 2>nul
copy mtd0_res\* %MachineMode%\%SubDir% 1>nul 2>nul
copy config.ini %MachineMode%\%SubDir% 1>nul 2>nul
del config.ini

::for K platform
::if /i "%MachineMode%"=="K320" goto case7
::if /i "%MachineMode%"=="K360" goto case7
::if /i "%MachineMode%"=="K370" goto case7

goto Done

:case7
copy %MachineMode%\%SubDir%\* %MachineMode% 1>nul 2>nul

:Done
echo.
echo         Create downloading folder %MachineMode% successfully
pause

:EX
exit