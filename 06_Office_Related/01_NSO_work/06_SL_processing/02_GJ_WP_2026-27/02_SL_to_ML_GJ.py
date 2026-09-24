import os
import json
import glob
import pandas as pd
import xlrd
import re
from pathlib import Path
import numpy as np
import xlsxwriter
import openpyxl
from openpyxl import load_workbook
def correct_distt_name(incorrect_distt):
    with open("distt_correction.json", "r") as file:
        distt_correction = json.load(file)

    for correct, incorrect_list in distt_correction.items():
        for incorrect in incorrect_list:
            if incorrect.lower() in incorrect_distt.lower():
                correct_distt = correct
                return correct_distt

    return incorrect_distt
def correct_crop_name(incorrect_crop):
    with open("crop_correction.json", "r") as file:
        crop_correction = json.load(file)

    for correct, incorrect_list in crop_correction.items():
        for incorrect in incorrect_list:
            if incorrect.lower() in incorrect_crop.lower():
                if '(ui)' in incorrect_crop.lower():
                    crop = correct + '_UI'
                elif '(i)' in incorrect_crop.lower() or '(ir)' in incorrect_crop.lower():
                    crop = correct + '_IR'
                else:
                    crop = correct
                return crop
    
    return incorrect_crop
def get_first_row(worksheet, row_text_list):
    for text in row_text_list:
        text = text.lower()
        for row in worksheet.iter_rows():
            for cell in row:
                if cell.value and text in str(cell.value).lower():
                    return cell.row
    return -1
def get_first_col(worksheet, col_text_list):
    for text in col_text_list:
        text = text.lower()
        for row in worksheet.iter_rows():
            for cell in row:
                if cell.value and text in str(cell.value).lower():
                    return cell.column
    return -1
def apply_join(df_ML, df_state, df_samples, df_districts, df_crops):
    #df_ML left join df_state ON  'STATE'
    for feature in ['STATENAME', 'SHORTSTATE', 'HSTATENAME']:
        df_ML[feature] = (df_ML['STATE']
                .map(df_state.set_index('STATE')[feature])
                .fillna(df_ML[feature])
            )
    #df_ML left join df_samples ON  'SAMPLE'
    for feature in ['SAMPLENAME', 'HSAMPLENAME']:
        df_ML[feature] = (df_ML['SAMPLE']
                .map(df_samples.set_index('SAMPLE')[feature])
                .fillna(df_ML[feature])
            )
    #df_ML left join df_districts ON  'DISTRICT'
    for feature in ['DISTRICTNAME', 'HDISTRICTNAME', 'ROCODE', 'RONAME', 'HRONAME', 'SROCODE', 'SRONAME', 'HSRONAME']:
        df_ML[feature] = (df_ML['DISTRICT']
                .map(df_districts.set_index('DISTRICT')[feature])
                .fillna(df_ML[feature])
            )
    #df_ML left join df_crops ON  'CROPCODE'
    for feature in ['CROPNAME', 'HCROPNAME', 'SEASONNAME', 'HSEASONNAME']:
        df_ML[feature] = (df_ML['CROPCODE']
                .map(df_crops.set_index('CROPCODE')[feature])
                .fillna(df_ML[feature])
            )
    return df_ML
def get_SL_to_ML(directory):
    records = []

    #df to use
    df_state = pd.read_excel("ML_Template.xlsx", sheet_name="State", dtype=str)
    state = df_state['STATE'].iloc[0]
    year = df_state['YEAR'].iloc[0]
    season = df_state['SEASONCODE'].iloc[0]
    
    df_seasons = pd.read_excel("ML_Template.xlsx", sheet_name="Seasons", dtype=str)
    df_seasons = df_seasons[df_seasons['SEASONCODE']==season]
    
    df_samples = pd.read_excel("ML_Template.xlsx", sheet_name="Samples", dtype=str)
    df_districts = pd.read_excel("ML_Template.xlsx", sheet_name="Districts", dtype=str)
    df_crops = pd.read_excel("ML_Template.xlsx", sheet_name="Crops", dtype=str)
    df_crops = df_crops[df_crops['SEASONCODE']==season]

    #df to create
    df_Vill = pd.DataFrame(columns=['STATE','SEASONCODE','SAMPLE','DISTRICT',
                                    'CROPCODE','TALUKA','CIRCLE','VILLAGE'])
    
    df_ML = pd.DataFrame(columns=['YEAR','SEASONCODE','SEASONNAME','HSEASONNAME',
                                  'SAMPLE','SAMPLENAME','HSAMPLENAME','STATE',
                                  'STATENAME','SHORTSTATE','HSTATENAME','ROCODE',
                                  'RONAME','HRONAME','SROCODE','SRONAME','HSRONAME',
                                  'DISTRICT','DISTRICTNAME','HDISTRICTNAME',
                                  'SELORDER','EXPT','CROPCODE','CROPNAME',
                                  'HCROPNAME','STATUS','EXPTID',])
    
    # Get all .xlsx files in the directory
    excel_files = glob.glob(os.path.join(directory, "*.xlsx"))

    #for each excel workbook
    for file_path in excel_files:
        file_name = os.path.basename(file_path)
        incorrect_distt = Path(file_name).stem.strip().title()

        district_name = correct_distt_name(incorrect_distt)     ############################## usable
        district_code = df_districts[df_districts['DISTRICTNAME']==district_name]['DISTRICT'].iloc[0]
        
        # Determine file type and use appropriate library
        if file_path.endswith('.xlsx'):
            try:
                wb = load_workbook(file_path, data_only=True)
                #for each sheet in excel workbook
                for sheet_name in wb.sheetnames:
                    if "cent" in sheet_name.lower() or "sta" in sheet_name.lower():
                        sample = '1' if "cent" in sheet_name.lower() else '2'     ############################## usable
                        
                        ws = wb[sheet_name]
                        
                        # setting which cells to scan
                        row_text_list = ['taluka', 'circle', 'vill', 'exp', 'os']
                        start_row = 0
                        title_row = 0
                        while start_row <= 0:
                            title_row = get_first_row(ws, row_text_list)
                            crop_row = title_row-1
                            start_row = title_row + 1
                            
                        col_text_list = ['vill']
                        start_col = 0
                        while start_col <= 0:
                            start_col = get_first_col(ws, col_text_list) + 1
                            taluka_col = start_col - 3
                            circle_col = start_col - 2
                            village_col = start_col - 1
                        
                        end_row = ws.max_row + 1
                        end_col = ws.max_column + 1

                        if start_row > 0 and start_col > 0:
                            for col_idx in range(start_col, end_col):
                                # get crop name and type
                                incorrect_crop = ws.cell(row=crop_row, column=col_idx).value     ############################## usable
                                if isinstance(incorrect_crop, str) and incorrect_crop is not None:
                                    incorrect_crop = re.sub(r'\s+', '', incorrect_crop)
                                else:
                                    incorrect_crop = ws.cell(row=crop_row, column=col_idx-1).value
                                    if isinstance(incorrect_crop, str) and incorrect_crop is not None:
                                        incorrect_crop = re.sub(r'\s+', '', incorrect_crop)
                                    else:
                                        incorrect_crop = None
    
                                # set season
                                if incorrect_crop is not None:
                                    crop_raw = correct_crop_name(incorrect_crop)
                                    crop = crop_raw
                                    
                                    
                                    plan = 0
                                    for row_idx in range(start_row, end_row):
                                        cell_val = ws.cell(row=row_idx, column=col_idx).value
                                        if isinstance(cell_val, str) and cell_val is not None:
                                            cell_val = cell_val.strip()
                                            
                                        cell_header = ws.cell(row=title_row, column=col_idx).value
                                        if isinstance(cell_header, str) and cell_header is not None:
                                            cell_header = cell_header.strip()
                                        
                                        if cell_val is not None:
                                            if taluka_col>0 and circle_col>0 and village_col>0:
                                                taluka = ws.cell(row=row_idx, column=taluka_col).value     ############################## usable
                                                circle = ws.cell(row=row_idx, column=circle_col).value     ############################## usable
                                                village = ws.cell(row=row_idx, column=village_col).value     ############################## usable

                                                if isinstance(taluka, str) and taluka is not None:
                                                    if isinstance(village, str) and village is not None:
                                                        #if taluka is not None and village is not None:
                                                        if 'os' in str(cell_header).lower():
                                                            if 'A' in str(cell_val):
                                                                crop = crop_raw + '_A'
                                                            elif 'B' in str(cell_val):
                                                                crop = crop_raw + '_B'

                                                            crop_code = df_crops[df_crops['CROPNAME']==crop]['CROPCODE'].iloc[0]
        
                                                            m_digit  = re.search(r"\d+", str(cell_val))
                                                            if m_digit is not None:
                                                                selorder = m_digit.group()
                                                                selorder = str(selorder)
        
                                                                if len(selorder) == 1:
                                                                    selorder = '0' + selorder
                                                                
                                                                if str(taluka) is not None:
                                                                    taluka = taluka.upper()
                                                                if str(circle) is not None:
                                                                    circle = circle.upper()
                                                                if str(village) is not None:
                                                                    village = village.upper()
                                                                
                                                                df_village_row = {
                                                                    'STATE': state,
                                                                    'SEASONCODE': season,
                                                                    'SAMPLE': sample,
                                                                    'DISTRICT': district_code,
                                                                    'DISTRICTNAME': district_name,
                                                                    'CROPCODE': crop_code,
                                                                    'TALUKA': taluka,
                                                                    'CIRCLE': circle,
                                                                    'VILLAGE': village
                                                                }
                                                                df_Vill = pd.concat([df_Vill, pd.DataFrame([df_village_row])], 
                                                                                    ignore_index=True)
                                                                
                                                                df_ML_row = {
                                                                    'YEAR': [year, year],
                                                                    'STATE': [state, state],
                                                                    'SEASONCODE': [season, season],
                                                                    'SAMPLE': [sample, sample],
                                                                    'DISTRICT': [district_code, district_code],
                                                                    'DISTRICTNAME': [district_name, district_name],
                                                                    'CROPCODE': [crop_code, crop_code],
                                                                    'SELORDER': [selorder, selorder],
                                                                    'EXPT': ['1','2']
                                                                }
                                                                
                                                                df_ML = pd.concat([df_ML, pd.DataFrame(df_ML_row, dtype=str)], ignore_index=True)

            except Exception as e:
                print(f"Error reading {file_name}, season:{season}, sample:{sample}, distt_code: {district_code}, crop:{crop_code}, {village}")
                raise e

    #joins
    df_ML = apply_join(df_ML, df_state, df_samples, df_districts, df_crops)
    
    return df_Vill, df_ML


if __name__ == "__main__":
    curr_dir = Path.cwd()
    directory = curr_dir / "SL 2.0"
    excel_path = curr_dir / "SL_to_ML.xlsx"

    df_Vill, df_ML = get_SL_to_ML(directory)

    with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
        df_Vill.to_excel(writer, sheet_name="Villages", index=False)
        df_ML.to_excel(writer, sheet_name="ML", index=False)

