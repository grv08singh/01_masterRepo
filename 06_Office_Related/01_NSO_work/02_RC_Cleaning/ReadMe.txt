Follow these instructions:

1) Install python/anaconda Distribution and update environment variable path.

2) Copy below files from "ASSOFTWARE" & "ICS_Scheme" folders:
	  (i) "RC123kharif.accdb"		----for Kharif
	 (ii) "RC123Rabi.accdb"			----for Rabi
	(iii) "NSSAS2024.mdb"			----For year 2024-25 (reference year may change)
	
   And Paste these files in folder "01_software" of this project.
	

3) In folder "02_meta_data", Open "Meta_Data.xlsx" and 
	fill all the sheets with relevant information.

4) In folder "03_PY_CY_Old", Copy and Paste two excel files from Annexure folder:
	(i) "PY State Details & Capital-N .xlsx"
	(ii) "CY State Details & Capital-N.xlsx"

5) Double Click "CleanRCs.bat".
	Wait for A black screen to open and Press Any Key when Prompted.

6) "RC1237_clean_v1.xlsx" is generated in folder "04_Clean_RCs".
	Check "log.txt" file for any changes to be done manually in "RC1237_clean_v1.xlsx".

7) Double Click "GenerateCY_PY.bat"
	Wait for A black screen to open and Press Any Key when Prompted.

8) Final PY, CY excel files are generated in "06_PY_CY_New" folder.