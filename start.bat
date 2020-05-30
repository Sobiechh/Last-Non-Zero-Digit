@echo off
SETLOCAL EnableDelayedExpansion

title %LastNon0Digit%

set tajm=%TIME:~0,8%

set currdate=d%DATE:.=_%h%tajm::=-%

rmdir in
rmdir out

:main
cls
echo.
echo            DZISIEJSZA DATA: %DATE%
echo ----------------------------------------------
echo LastNon0Digit - Ostatnia niezerowa cyfra silni
echo ----------------------------------------------
echo.
echo.
echo 1. Start
echo 2. Informacje
echo 3. Kopia zapasowa
echo 4. Zakoncz
echo.
echo.
echo.

set /p chose="Wybierz opcje: "

if %chose%==1 goto start
if %chose%==2 goto informacje
if %chose%==3 goto kopia
if %chose%==4 goto exit

:start

py last_zero.py
timeout 2 >nul
py program.py

goto main

:kopia
cls

xcopy /s out\*.txt backup\%currdate%\*.txt


echo Ukonczono! Nacisnij spacje.
pause
goto main

:informacje
cls
echo --------------------------------INFROMACJE-----------------------------------
echo Ostatnia niezerowa cyfra silni
echo W plikach *.txt znajduja sie kolejno w kazdej linii cyfry/liczby
echo z kazdej z tych cyfr/liczb wydobywana jest ostatnia niezerowa cyfra jej silni
echo autor: Piotr Sobieszczyk
echo -----------------------------------------------------------------------------
pause
goto main

:exit
cls
pause
echo on