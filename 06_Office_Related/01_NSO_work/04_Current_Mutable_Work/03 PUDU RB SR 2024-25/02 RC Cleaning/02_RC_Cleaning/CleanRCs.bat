@echo off
cd "00_py_script"
call conda activate base
python "01_RC_Cleaning_Script.py"
cd ..
pause
endlocal