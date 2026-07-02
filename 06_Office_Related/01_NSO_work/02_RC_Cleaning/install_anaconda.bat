@echo off
setlocal EnableDelayedExpansion

:: ============================================================
::  Anaconda Auto-Downloader, Silent Installer & Cleanup Script
::  Run this script as Administrator
:: ============================================================

:: --- Configuration ---
set ANACONDA_URL=https://repo.anaconda.com/archive/Anaconda3-2025.12-2-Windows-x86_64.exe
set INSTALLER_FILE=%TEMP%\Anaconda3-installer.exe
set INSTALL_DIR=C:\Anaconda3

echo =====================================================
echo   Anaconda Automated Installation Script
echo =====================================================
echo.

:: -----------------------------------------------
:: STEP 1: Download Anaconda Installer
:: -----------------------------------------------
echo [1/3] Downloading Anaconda installer...
echo       URL : %ANACONDA_URL%
echo       Dest: %INSTALLER_FILE%
echo.

curl -L --progress-bar -o "%INSTALLER_FILE%" "%ANACONDA_URL%"

if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Download failed. Check your internet connection.
    exit /b 1
)
echo [OK] Download complete.
echo.

:: -----------------------------------------------
:: STEP 2: Silent Installation with PATH setup
:: -----------------------------------------------
echo [2/3] Installing Anaconda silently to %INSTALL_DIR% ...
echo       This may take a few minutes. Please wait...
echo.

start /wait "" "%INSTALLER_FILE%" ^
    /InstallationType=JustMe ^
    /RegisterPython=1 ^
    /AddToPath=1 ^
    /S ^
    /D=%INSTALL_DIR%

if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Installation failed with error code %ERRORLEVEL%.
    del /f /q "%INSTALLER_FILE%"
    exit /b 1
)
echo [OK] Installation complete.
echo.

:: -----------------------------------------------
:: STEP 3: Set Environment Variables Permanently
:: -----------------------------------------------
echo [3/3] Setting environment variable paths...

setx PATH "%INSTALL_DIR%;%INSTALL_DIR%\Scripts;%INSTALL_DIR%\Library\bin;%PATH%" /M

if %ERRORLEVEL% NEQ 0 (
    echo [WARN] Could not set system-wide PATH. Trying user-level PATH...
    setx PATH "%INSTALL_DIR%;%INSTALL_DIR%\Scripts;%INSTALL_DIR%\Library\bin;%PATH%"
)
echo [OK] Environment variables updated.
echo.

:: -----------------------------------------------
:: STEP 4: Remove Installer File
:: -----------------------------------------------
echo [4/4] Cleaning up installer file...
del /f /q "%INSTALLER_FILE%"

if %ERRORLEVEL% NEQ 0 (
    echo [WARN] Could not delete installer. Please remove manually: %INSTALLER_FILE%
) else (
    echo [OK] Installer removed.
)

echo.
echo =====================================================
echo   Anaconda installed successfully at: %INSTALL_DIR%
echo   Please restart your terminal / system to apply
echo   the updated PATH environment variables.
echo =====================================================

endlocal
pause
