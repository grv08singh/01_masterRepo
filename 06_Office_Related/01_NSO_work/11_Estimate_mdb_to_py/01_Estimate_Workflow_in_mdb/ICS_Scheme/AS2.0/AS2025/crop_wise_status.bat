@echo off
title NSSAS Data Processing
color 0A

echo ==========================================
echo      NSSAS DATA PROCESSOR
echo ==========================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python and add it to your system PATH
    pause
    exit /b 1
)

echo Python is installed:
python --version
echo.

:: Check and install required packages
echo Checking required packages...
python -c "import pandas" >nul 2>&1
if errorlevel 1 (
    echo Installing pandas...
    pip install pandas
)

python -c "import pyodbc" >nul 2>&1
if errorlevel 1 (
    echo Installing pyodbc...
    pip install pyodbc
)

python -c "import openpyxl" >nul 2>&1
if errorlevel 1 (
    echo Installing openpyxl...
    pip install openpyxl
)

echo All dependencies are installed.
echo.

:: Run the Python script
echo Starting data processing...
echo.

python -c ^
"from pathlib import Path; ^
import numpy as np; ^
import pandas as pd; ^
import pyodbc; ^
import sys; ^
import os; ^
import time; ^
from datetime import date; ^
import re; ^
import openpyxl; ^
from openpyxl import Workbook, load_workbook; ^
from openpyxl.utils.dataframe import dataframe_to_rows; ^
import warnings as wr; ^
wr.filterwarnings('ignore'); ^
^
curr_path = Path.cwd(); ^
print(f'Processing files in: {curr_path}'); ^
for file_path in curr_path.iterdir(): ^
	if file_path.is_file(): ^
		if 'NSSAS' in file_path.stem and file_path.suffix == '.mdb': ^
			year = file_path.stem[-4:]; ^
			print(f'Processing file: {file_path.name}'); ^
			print(f'Year: {year}'); ^
			^
			conn_str = ( ^
				r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' ^
				f'DBQ={file_path};' ^
			); ^
			conn = pyodbc.connect(conn_str); ^
			^
			#get data from the table - EXPTMASTER and Sch20RC7 ^
			cols_ml = ['YEAR', 'SEASONCODE', 'SEASONNAME', 'SAMPLE', 'SAMPLENAME', 'STATE', 'STATENAME', 'RONAME', 'SRONAME',  ^
					   'DISTRICT', 'DISTRICTNAME', 'SELORDER', 'EXPT', 'CROPCODE', 'CROPNAME', 'EXPTID']; ^
			cols_rc7 = ['EXPTID','STAGIN','REXML','REJ']; ^
			^
			sql_ML7 = 'SELECT * FROM \"EXPTMASTER\"'; ^
			sql_query7 = 'SELECT * FROM \"Sch20RC7\"'; ^
			^
			ml = pd.read_sql(sql_ML7, conn)[cols_ml]; ^
			rc7 = pd.read_sql(sql_query7, conn)[cols_rc7]; ^
			^
			conn.close(); ^
			^
			df = pd.merge(ml,rc7,how='left',left_on='EXPTID',right_on='EXPTID'); ^
			df['REJ'] = df['REJ'].fillna(0); ^
			df['STAGIN'] = df['STAGIN'].fillna(0); ^
			^
			patterns = ['_UI_A', '_UI_B', '_IR_A', '_IR_B', '_UI', '_IR']; ^
			for pattern in patterns: ^
				df['CROPNAME'] = df['CROPNAME'].str.replace(pattern, ''); ^
			states = list(df['STATE'].unique()); ^
			^
			print(f'Processing {len(states)} states...'); ^
			for state in states: ^
				crop_wise_status = {}; ^
				crop_wise_status['State'] = state; ^
				df_status = pd.DataFrame(columns=['State','Season','Sample','Crop','Plan','Received','Harvest','Missed','Lost','Rejected','NR']); ^
				^
				df_state = df[df['STATE'] == state]; ^
				seasons = list(df['SEASONCODE'].unique()); ^
				for season in seasons: ^
					crop_wise_status['Season'] = season; ^
					df_state_season = df_state[df_state['SEASONCODE'] == season]; ^
					sts = list(df_state_season['SAMPLE'].unique()); ^
					for st in sts: ^
						crop_wise_status['Sample'] = st; ^
						df_state_season_st = df_state_season[df_state_season['SAMPLE'] == st]; ^
						crops = list(df_state_season_st['CROPNAME'].unique()); ^
						for crop in crops: ^
							if crop is not np.nan: ^
								crop_wise_status['Crop'] = crop; ^
								df_state_season_st_crop = df_state_season_st[df_state_season_st['CROPNAME'] == crop]; ^
								^
								crop_wise_status['Plan'] = df_state_season_st_crop.shape[0]; ^
								^
								df_state_season_st_crop_nonrej = df_state_season_st_crop[df_state_season_st_crop['REJ'] != '1']; ^
								crop_wise_status['Received'] = df_state_season_st_crop_nonrej[df_state_season_st_crop_nonrej['STAGIN'].isin(['1','2','3'])].shape[0]; ^
								crop_wise_status['Harvest'] = df_state_season_st_crop_nonrej[df_state_season_st_crop_nonrej['STAGIN'] == '1'].shape[0]; ^
								crop_wise_status['Missed'] = df_state_season_st_crop_nonrej[df_state_season_st_crop_nonrej['STAGIN'] == '2'].shape[0]; ^
								crop_wise_status['Lost'] = df_state_season_st_crop_nonrej[df_state_season_st_crop_nonrej['STAGIN'] == '3'].shape[0]; ^
								crop_wise_status['NR'] = df_state_season_st_crop[df_state_season_st_crop['STAGIN'] == '0'].shape[0]; ^
								^
								df_state_season_st_crop_rej = df_state_season_st_crop[df_state_season_st_crop['REJ'] == '1']; ^
								crop_wise_status['Rejected'] = df_state_season_st_crop_rej.shape[0]; ^
								^
								df_status = pd.concat([df_status, pd.DataFrame(crop_wise_status, index=[0])], ignore_index=True); ^
				^
				df_status.to_excel(f'state_{state}.xlsx', index=False); ^
				print(f'Created file: state_{state}.xlsx'); ^
			print(f'Completed processing for year: {year}'); ^
^"

if errorlevel 1 (
    echo.
    echo ERROR: Script execution failed
    echo Please check the error messages above
) else (
    echo.
    echo ==========================================
    echo      PROCESSING COMPLETED SUCCESSFULLY
    echo ==========================================
    echo.
    echo Files created: state_*.xlsx
)

echo.
pause