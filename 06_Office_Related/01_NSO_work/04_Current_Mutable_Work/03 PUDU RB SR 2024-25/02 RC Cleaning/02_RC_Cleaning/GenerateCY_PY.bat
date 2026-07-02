@echo off
cd "00_py_script"
call conda activate base
python "02_PY_CY_Data_Interchange_Script.py"
pause
cd ..
