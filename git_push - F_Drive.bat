@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION

:: ---------------------------------------------------------------
::  MULTI-REPO GIT SYNC SCRIPT — Gaurav's Repositories
:: ---------------------------------------------------------------

SET BASE_PATH=F:\Grv\Grv\05 GIT
SET BRANCH=main
SET PASS=0
SET FAIL=0
SET SKIPPED=0
SET PULL_PASS=0
SET PULL_FAIL=0
SET PULL_UP_TO_DATE=0

:: --- REPOSITORY NAMES ------------------------------------------
SET REPOS[0]=01_masterRepo
SET REPOS[1]=14_Proj_ML_99Acres
:: ----------------------------------------------------------------

:: Count repos
SET REPO_COUNT=0
:COUNT_LOOP
    IF DEFINED REPOS[%REPO_COUNT%] (
        SET /A REPO_COUNT+=1
        GOTO COUNT_LOOP
    )

:: --- MAIN LOOP -------------------------------------------------
SET INDEX=0
:REPO_LOOP
    ECHO ******************************************************************************************
    IF NOT DEFINED REPOS[%INDEX%] GOTO SUMMARY

    SET REPO_NAME=!REPOS[%INDEX%]!
    SET FULL_PATH=%BASE_PATH%\!REPO_NAME!
    SET /A DISPLAY_NUM=%INDEX%+1
    SET /A INDEX+=1

    ECHO ¦ [%DISPLAY_NUM%/%REPO_COUNT%] !REPO_NAME!
    ECHO +----------------------------------------------------------

    :: -- Validate path exists ----------------------------------
    IF NOT EXIST "!FULL_PATH!" (
        ECHO   [ERROR] Path does not exist: !FULL_PATH!
        SET /A FAIL+=1
        ECHO.
        GOTO REPO_LOOP
    )

    :: -- Navigate to repo --------------------------------------
    cd /d "!FULL_PATH!"
    IF ERRORLEVEL 1 (
        ECHO   [ERROR] Could not navigate to: !FULL_PATH!
        SET /A FAIL+=1
        ECHO.
        GOTO REPO_LOOP
    )

    :: -- Validate it's a git repo ------------------------------
    git rev-parse --is-inside-work-tree >NUL 2>&1
    IF ERRORLEVEL 1 (
        ECHO   [ERROR] Not a valid git repository: !FULL_PATH!
        SET /A FAIL+=1
        ECHO.
        GOTO REPO_LOOP
    )

    :: -- STEP 1: Pull --------------------------------------------
	::-------------------------------------------------------------------------------------------------
	pause
    ECHO   ^> [1/3] Pulling from origin/%BRANCH%...
    SET PULL_OUTPUT_FILE=%TEMP%\git_pull_!INDEX!.txt
    git pull origin %BRANCH% > "!PULL_OUTPUT_FILE!" 2>&1

    SET PULL_RC=!ERRORLEVEL!
    TYPE "!PULL_OUTPUT_FILE!"

    IF !PULL_RC! NEQ 0 (
        ECHO   [ERROR] git pull failed. Skipping commit/push.
        SET /A PULL_FAIL+=1
        SET /A FAIL+=1
        ECHO.
        GOTO REPO_LOOP
    )

    :: Check if pull brought in new changes or was already up to date
    FINDSTR /I /C:"Already up to date" "!PULL_OUTPUT_FILE!" >NUL 2>&1
    IF !ERRORLEVEL! == 0 (
        ECHO   [PULL] Already up to date.
        SET /A PULL_UP_TO_DATE+=1
    ) ELSE (
        ECHO   [PULL] New changes pulled successfully.
        SET /A PULL_PASS+=1
    )

    :: -- STEP 2: Check Status ----------------------------------
    ECHO   ^> [2/3] Checking status...
    git status

    git status --porcelain > "%TEMP%\git_status_!INDEX!.txt" 2>&1
    SET FILE_SIZE=0
    FOR %%A IN ("%TEMP%\git_status_!INDEX!.txt") DO SET FILE_SIZE=%%~zA

    IF "!FILE_SIZE!"=="0" (
        ECHO   [SKIPPED] No local changes detected.
        SET /A SKIPPED+=1
        ECHO.
        GOTO REPO_LOOP
    )

    :: -- STEP 3: Add, Commit, Push -----------------------------
    ECHO   ^> [3/3] Staging all changes...
    git add .

    SET COMMIT_MSG=Auto-sync: %DATE% %TIME%

    ECHO   ^> Committing...
    git commit -m "!COMMIT_MSG!"
    IF ERRORLEVEL 1 (
        ECHO   [ERROR] git commit failed.
        SET /A FAIL+=1
        ECHO.
        GOTO REPO_LOOP
    )

    ECHO   ^> Pushing to origin/%BRANCH%...
    git push origin %BRANCH% 2>&1
    IF ERRORLEVEL 1 (
        ECHO   [ERROR] git push failed. Check your credentials/remote.
        SET /A FAIL+=1
        ECHO.
        GOTO REPO_LOOP
    )

    ECHO   [SUCCESS] !REPO_NAME! synced successfully!
    SET /A PASS+=1
    ECHO.
    GOTO REPO_LOOP

:: --- SUMMARY ---------------------------------------------------
:SUMMARY
ECHO +----------------------------------------------------------+
ECHO |                PULL SUMMARY                              |
ECHO +----------------------------------------------------------+
ECHO |  Total Repositories  : %REPO_COUNT%
ECHO |  New Changes Pulled  : !PULL_PASS!
ECHO |  Already Up To Date  : !PULL_UP_TO_DATE!
ECHO |  Pull Failed         : !PULL_FAIL!
ECHO +----------------------------------------------------------+
ECHO |                PUSH SUMMARY                              |
ECHO +----------------------------------------------------------+
ECHO |  Total Repositories  : %REPO_COUNT%
ECHO |  Pushed Successfully : !PASS!
ECHO |  No Changes (Skipped): !SKIPPED!
ECHO |  Push Failed         : !FAIL!
ECHO +----------------------------------------------------------+
ECHO.

PAUSE
ENDLOCAL