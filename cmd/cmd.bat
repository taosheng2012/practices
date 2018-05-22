@echo off
cls
goto MAIN


rem *********************************************************************
rem subroutines

:PROC1
    echo This is proc1 called.
    echo %%0=%0 %%1=%1 %%2=%2
    goto :EOF

:PROC2
	set /p user_name=Please input your first name: 
	set /p user_year=Please input the year in which you're born: 
	set /a user_age=2018-user_year
	echo Hello, %user_name%. You're %user_age% years old.
	goto :EOF

:PROC3
	echo CMD search path: %path%
	goto :EOF

:ADMIN_TEST
    echo Administrative permissions required. Detecting permissions...

    net session >nul 2>&1
    if %errorLevel% == 0 (
        echo Success: Administrative permissions confirmed.
    ) else (
        echo Failure: Current permissions inadequate.
    )

    rem pause >nul

    goto :EOF

:MAIN_EXIT
	exit 1
	

rem *********************************************************************
:MAIN

echo *********************************************************************
set PROGRAm=DD-CMD
title %PROGRAM%
echo ==== %PROGRAM% ====
date /t
time /t
echo(
echo Description: My first Windows CMD script(.bat file).
echo *********************************************************************
echo(
echo(

rem *********************************************************************
:MAIN_LOOP

echo List of supported functions:
echo     1 function usage
echo     2 input and output
echo     3 print system info
echo     4 check admin

echo     9 Exit the program
echo(

set /p num=Please select function NUM, then press ENTER:


if %num%==1 call :PROC1 par1 para2
if %num%==2 call :PROC2
if %num%==3 call :PROC3
if %num%==4 call :ADMIN_TEST

if %num%==9 call :MAIN_EXIT


echo(
echo(
echo *********************************************************************

goto :MAIN_LOOP
