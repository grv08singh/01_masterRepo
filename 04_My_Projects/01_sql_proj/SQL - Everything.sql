-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################

-- Demo 01: 01-02-2025
-- ###########################################################################################





--  Key-Value store DBMS
-- --XML, JSON, BSON
-- 
-- {
--   "USEr123": "John Doe",
--   "USEr124": "Jane Smith",
--   "first_NAME": "John",
--   "USEr125": "Alice Johnson",
--   "lASt_NAME": "Doe"
-- }
-- 
-- --COLUMN store DBMS
-- {
--   "USErs": {
--     "COLUMNs": ["USEr_id", "first_NAME", "lASt_NAME", "age"],
--     "data": [
--       ["1", "John", "Doe", "30"],
--       ["2", "Jane", "Smith", "25"],
--       ["3", "Alice", "Johnson", "28"]
--     ]
--   }
-- }
-- Document store DBMS:
-- {
--   "USEr123": {
--     "_id": "USEr123",
--     "first_NAME": "John",
--     "lASt_NAME": "Doe",
--     "profile": {
--       "email": "john.doe@example.com",
--       "age": 30
--     },
--     "INTerests": ["reading", "skiing", "hiking"]
--   }
-- }
-- 
-- Graph DBMS
-- {
--   "nodes": [
--     {"id": "1", "type": "Person", "NAME": "John Doe"},
--     {"id": "2", "type": "Person", "NAME": "Jane Smith"},
--     {"id": "3", "type": "Company", "NAME": "Tech Solutions"}
--   ],
--   "edges": [
--     {"source": "1", "target": "3", "type": "EMPLOYED_BY"},
--     {"source": "2", "target": "3", "type": "EMPLOYED_BY"}
--   ]
-- }
-- 
-- 
-- {
--   "nodes": [
--     {"id": "USEr1", "type": "USEr", "NAME": "Alice"},
--     {"id": "USEr2", "type": "USEr", "NAME": "Bob"},
--     {"id": "Post1", "type": "Post", "content": "Loving the new camera I GOt!", "TIMEstamp": "2023-02-01T12:00:00Z"},
--     {"id": "Comment1", "type": "Comment", "content": "Looks awesome, Alice!", "TIMEstamp": "2023-02-01T13:00:00Z"}
--   ],
--   "edges": [
--     {"source": "USEr1", "target": "USEr2", "type": "FRIENDS_WITH"},
--     {"source": "USEr1", "target": "Post1", "type": "POSTED"},
--     {"source": "USEr2", "target": "Comment1", "type": "COMMENTED_ON"},
--     {"source": "USEr2", "target": "Post1", "type": "LIKES"}
--   ]
-- }
-- 
-- 
-- {
--   "nodes": [
--     {"id": "Router1", "type": "Router", "location": "Data Center 1"},
--     {"id": "Switch1", "type": "Switch", "location": "Data Center 1"},
--     {"id": "USEr1", "type": "USEr", "ADDress": "123 Elm St"},
--     {"id": "ServicePoINT1", "type": "Service PoINT", "service": "INTernet"}
--   ],
--   "edges": [
--     {"source": "Router1", "target": "Switch1", "type": "CONNECTED_TO"},
--     {"source": "USEr1", "target": "ServicePoINT1", "type": "USES"}
--   ]
-- }
-- 
-- 
-- ###########################################################################################
-- --XML
-- <person>
--   <NAME>Alice</NAME>
--   <age>30</age>
--   <city>New YORk</city>
-- </person>
-- 
-- --JSON
-- {
--   "person": {
--     "NAME": "Alice",
--     "age": 30,
--     "city": "New YORk"
--   }
-- }
-- 
-- --txt , csv, excel , xml , json , ......

























-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################

Demo 02: 02-02-2025
-- ###########################################################################################



--Sql server Adventure wORks restore,SSMS INTroduction,Data type( numeric)
-- ###########################################################################################
--Self learning 
--	https://learn.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver16
--XML data IN SQL Server
--	https://learn.microsoft.com/en-us/sql/relational-DATABASEs/xml/xml-data-sql-server?view=sql-server-ver16
--JSON data IN SQL Server
--	https://learn.microsoft.com/en-us/sql/relational-DATABASEs/json/json-data-sql-server?view=sql-server-ver16
-- ###########################################################################################
-- 	-- comment = INfORmational message 
-- 	-- single lINe comment
-- 	--	sql server IS NOT a cASe sensitive language 
-- 	--  32767 connection to the sql server
-- 
-- 
-- /*  start
-- 
-- 	Multi lINe comment
-- 
-- 	INstance NAME =DATADOX\DEMO
-- 	USErNAME =DATADOX\Balje
-- 	session id = 58
-- 	DATABASE NAME =mASter
-- 
-- end */
-- 
-- --session 1- 50 reserved fOR system process
-- 
-- ###########################################################################################
-- 	--Download backup files
-- 	--Step 1 
-- 	--Open --> sql server management studio--> New Query -->run a commAND 
-- 	
-- 		SELECT @@version
-- 		
-- 	--Step 2
-- 	https://learn.microsoft.com/en-us/sql/samples/adventurewORks-INstall-configure?view=sql-server-ver16&tabs=ssms
-- 	--download the -->OLTP  -->AdventureWorks2022.bak
-- 
-- 	--step 3 
-- 	--CREATE the folder IN C drive with your NAME AND copy the backup file
-- 
-- 
-- 	--step 4
-- 	--Restore
-- 
-- ###########################################################################################
-- --System DATABASEs
-- https://learn.microsoft.com/en-us/sql/relational-DATABASEs/DATABASEs/system-DATABASEs?view=sql-server-ver16
-- 
-- --mASter DATABASE(Critical)
-- 	--records all the system-level INfORmation fOR an INstance of SQL Server.
-- 
-- --model DATABASE	
-- 	--IS USEd AS the template fOR all DATABASEs CREATEd on the INstance of SQL Server.
-- 	CREATE DATABASE sqldemo
-- 
-- 		--how many  files 
-- 		--size of files
-- 		--path of files 
-- 		--NAME of files
-- 
-- --msdb DATABASE	
-- 	--IS USEd by SQL Server Agent fOR scheduling alerts AND jobs.
-- 
-- --tempdb DATABASE(Critical)	
-- 	--IS a wORkspace fOR holding tempORary objects OR INTermediate result SETs.
-- 	--tempORary data,  It reSETs every TIME the SQL Server restarts.
-- 
-- 
-- --Resource DATABASE	
-- 	--IS a read-only DATABASE that contaINs system objects that are INcluded with SQL Server. 
-- 
-- 	https://learn.microsoft.com/en-us/sql/relational-DATABASEs/DATABASEs/resource-DATABASE?view=sql-server-ver16
-- 	--INstallation drive>:\Program Files\Microsoft SQL Server\MSSQL<version>.<INstance_NAME>\MSSQL\BINn\ 
-- 	--NAME  =  mssqlsystemresource
-- 
-- 
-- ###########################################################################################
-- --Numbers 
-- --Exact numerics
-- 
-- 	16163163
-- 	31
-- 	1
-- 	0
-- 	-465
-- 	-8
-- 	-45646
-- --DECLARE , help us to INTialISe a temp variable
-- --SET , ASsign temp variable a value
-- --SELECT , dISplay the value
-- @= tempORary
-- age = variabele
-- @age= tempORary variabele


DECLARE @age INT;
SET @age =43;
SELECT @age age;

--TINYINT, range(0-255), 1 Byte.

	DECLARE @val TINYINT;
	SET @val =0;
	SELECT @val;

	DECLARE @val TINYINT;
	SET @val =255;
	SELECT @val;

	DECLARE @val TINYINT;
	SET @val =55;
	SELECT @val;
	
	DECLARE @val TINYINT;
	SET @val =100;
	SELECT @val AS newdata;
	
	DECLARE @val TINYINT;
	SET @val =150;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;

	DECLARE @val TINYINT;
	SET @val =256;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;


-- ###########################################################################################
--SMALLINT, range(-32768 to 32767), 2 byte  
	DECLARE @val SMALLINT;
	SET @val =-32768;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;


	DECLARE @val SMALLINT;
	SET @val =-1;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;


	DECLARE @val SMALLINT;
	SET @val =-32 ;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;

	
	DECLARE @val SMALLINT;
	SET @val =32767;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;

	DECLARE @val SMALLINT;
	SET @val =32768;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;
-- ###########################################################################################
--INT (-2,147,483,648 to 2,147,483,647), 4 byte


	DECLARE @val  INT;
	SET @val =-2147 ;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;


	DECLARE @val  INT;
	SET @val =-214748 ;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;

	
	DECLARE @val  INT;
	SET @val =-2147483648;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;


	DECLARE @val  INT;
	SET @val =214;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;


	DECLARE @val  INT;
	SET @val =1;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;
	
	
	DECLARE @val  INT;
	SET @val =2147483647;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;
	
	
	DECLARE @val  INT;
	SET @val =2147483648;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;

-- ###########################################################################################
--BIGINT (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807), 8 byte

	DECLARE @val  BIGINT;
	SET @val =-9223372036854775808;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;


	DECLARE @val  BIGINT;
	SET @val =-1;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;


	DECLARE @val  BIGINT;
	SET @val =-922 ;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;


	DECLARE @val  BIGINT;
	SET @val =1;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;

-- ###########################################################################################
--Approximate numerics
	--PrecISion (data which IS present towards the left AND right of the DECIMAL poINt)
	--Scale(data which IS present towards right of the DECIMAL poINT)

-- 968457.789654958
-- 123456 789012345
-- 789654958
-- 123456789
-- (p=15, s=9)

--Float, 15 PrecISion , 8 byte
	DECLARE @val  Float;
	SET @val =123456789012345;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;
	
	DECLARE @val  Float;
	SET @val =1234567.89012345;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;
	
	DECLARE @val  Float;
	SET @val =1234567.890123456;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;

	DECLARE @val  Float;
	SET @val =1234567896564567.89012345 ;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;


-- 1234567896564567.89012345
-- 1.23456789656457E+15
-- 1.23456789656457* 10 raISed to power of 15


-- ###########################################################################################
--  DECIMAL(precISion , scale)
--	PrecISion			StORage bytes
--	1 - 9					5
--	10-19					9
--	20-28					13
--	29-38					17
	
	DECLARE @val  DECIMAL(38,0);
	SET @val =123456;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;
	   
	DECLARE @val  DECIMAL(38,0);
	SET @val =12345678901;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;

	DECLARE @val  DECIMAL(38,0);
	SET @val =123456789012345678900;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;
	   
	DECLARE @val  DECIMAL(38,0);
	SET @val =92233720368547758089223372036854775892;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;


--Scale

	DECLARE @val  DECIMAL(38,2);
	SET @val =1.123123123;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;
	   
	DECLARE @val  DECIMAL(38,2);
	SET @val =5.345435345;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;
	   
	DECLARE @val  DECIMAL(38,2);
	SET @val =16161;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;
	   
	DECLARE @val  DECIMAL(38,2);
	SET @val =1.2 ;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;
	   
	DECLARE @val  DECIMAL(38,2);
	SET @val =6511616;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;

	DECLARE @val  DECIMAL(38,2);
	SET @val =92233720368547758089223372036854775892;
	SELECT @val AS Val, DATALENGTH(@val) AS Byte;






































-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################

-- Demo 03: 07-02-2025
-- ###########################################################################################




--String,unicode,DATETIME,ddl(CREATE, ALTER, DROP, USE) 

-- ###########################################################################################
-- '12 3#$%^&*DFGH J KL:123 123sdAS d'

--CHAR(n), range (1 to 8000)
	--It IS a fixed length data type
	--USEd to store non-Unicode CHARacters
	--Occupies 1 byte of space fOR each CHARacter
	--Static memORy allocation

	DECLARE @val CHAR ;
	SET @val='alp';
	SELECT @val, DATALENGTH(@val) AS Byte;

	DECLARE @val CHAR(1);
	SET @val='alp';
	SELECT @val, DATALENGTH(@val) AS Byte;
	
	DECLARE @val CHAR(10);
	SET @val='alpha beta';
	SELECT @val, DATALENGTH(@val) AS Byte;

	DECLARE @val CHAR(5);
	SET @val='alpha beta';
	SELECT @val, DATALENGTH(@val) AS Byte;
	
	DECLARE @val CHAR(10);
	SET @val='alpha';
	SELECT @val, DATALENGTH(@val) AS Byte;
	
	DECLARE @val CHAR(8000);
	SET @val='alpha';
	SELECT @val, DATALENGTH(@val) AS Byte;

-- ###########################################################################################
--VARCHAR(n), range 1-8000 / MAX
	--It IS a variable-length data type
	--USEd to store Unicode CHARacters
	--Occupies 1 bytes of space fOR each CHARacter
	--dynamic memORy allocation

	DECLARE @val VARCHAR(10);
	SET @val='alpha';
	SELECT @val, DATALENGTH(@val) AS Byte;

	DECLARE @val VARCHAR ;
	SET @val='alp';
	SELECT @val, DATALENGTH(@val) AS Byte;

	DECLARE @val VARCHAR(1);
	SET @val='alp';
	SELECT @val, DATALENGTH(@val) AS Byte;
	
	DECLARE @val VARCHAR(10);
	SET @val='alpha beta';
	SELECT @val, DATALENGTH(@val) AS Byte;

	DECLARE @val VARCHAR(5);
	SET @val='alpha beta';
	SELECT @val, DATALENGTH(@val) AS Byte;
	
	DECLARE @val VARCHAR(10);
	SET @val='alpha';
	SELECT @val, DATALENGTH(@val) AS Byte;
		
	DECLARE @val VARCHAR(8000);
	SET @val='alpha';
	SELECT @val, DATALENGTH(@val) AS Byte;

	
	DECLARE @val VARCHAR(MAX);
	SET @val='alpha';
	SELECT @val, DATALENGTH(@val) AS Byte;

-- ###########################################################################################

	DECLARE @val VARCHAR(MAX);
	SET @val='नमस्ते दुनिया';
	SELECT @val, DATALENGTH(@val) AS Byte;


-- ###########################################################################################
--Unicode (nCHAR & nvaCHAR)
--nCHAR(1 to 4000) 
	--It IS a fixed length data type
	--USEd to store Unicode CHARacters
	--Occupiers 2 byte of space fOR each CHARacter
	--static memORy allocation
	
	DECLARE @val nCHAR(20);	--20*2
	SET @val=N'नमस्ते दुनिया';
	SELECT @val, DATALENGTH(@val) AS Byte;
	
	DECLARE @val nCHAR(10);	--10*2
	SET @val=N'alpha';
	SELECT @val, DATALENGTH(@val) AS Byte;
		
	DECLARE @val nCHAR(15);	--15*2
	SET @val=N'नमस्ते你好，世界';
	SELECT @val, DATALENGTH(@val) AS Byte;

-- ###########################################################################################
--nVARCHAR()--1-4000
--It IS a variable-length data type
--USEd to store Unicode CHARacters
--Occupies 2 bytes of space fOR each CHARacter
--dynamic memORy allocation
		
	DECLARE @val nVARCHAR(30);
	SET @val=N'hello';
	SELECT @val, DATALENGTH(@val) AS Byte;
	
	DECLARE @val nVARCHAR(30);
	SET @val=N'नमस्ते दुनिया';
	SELECT @val, DATALENGTH(@val) AS Byte;
	
	DECLARE @val nVARCHAR(30);
	SET @val=N'你好，世界';
	SELECT @val, DATALENGTH(@val) AS Byte;

	
	DECLARE @val nVARCHAR(30);
	SET @val=N'नमस्ते दुनिया 你好，世界';
	SELECT @val, DATALENGTH(@val) AS Byte;





	
-- ###########################################################################################
-- ###########################################################################################
-- datatypes:	DATE, TIME, SMALLDATETIME, DATETIME, DATETIME2, DATETIMEOFFSET
-- functions:	GETDATE(), SYSDATETIME(), 
-- ###########################################################################################
-- ###########################################################################################
--DATE (3 byte)
	--INput ='YYYY-MM-DD' OR 'MM-DD-YYYY'
	--Output ='YYYY-MM-DD'

	DECLARE @val DATE;
	SET @val= '2025-02-08';
	SELECT @val, DATALENGTH(@val) AS Byte;

	DECLARE @val DATE;
	SET @val= GETDATE();
	SELECT @val, DATALENGTH(@val) AS Byte;

	DECLARE @val DATE;
	SET @val= SYSDATETIME();
	SELECT @val, DATALENGTH(@val) AS Byte;
		
	DECLARE @val DATE;
	SET @val= '02/15/2025';
	SELECT @val, DATALENGTH(@val) AS Byte;
--Conversion failed when converting DATE AND/OR TIME FROM CHARacter string.
	DECLARE @val DATE;
	SET @val= '15-02-2025';
	SELECT @val, DATALENGTH(@val) AS Byte;

-- ###########################################################################################

--TIME(5 byte)	
	--INput 'HH:MM:SS'
	--output'HH:MM:SS:MMMMMMM'
	
	DECLARE @val TIME;
	SET @val= '00:15:21';
	SELECT @val, DATALENGTH(@val) AS Byte;

	DECLARE @val TIME;
	SET @val= '23:15:21';
	SELECT @val, DATALENGTH(@val) AS Byte;

	SELECT GETDATE(), DATALENGTH(GETDATE()) AS Byte;
	SELECT SYSDATETIME(), DATALENGTH(SYSDATETIME()) AS Byte;

-- ###########################################################################################
--TIMEstamp 'YYYY-MM-DD HH:MM:SS'

--SMALLDATETIME(4 byte)'YYYY-MM-DD HH:MM:SS'
	DECLARE @val SMALLDATETIME;
	SET @val= '2025-02-08 23:15:21';
	SELECT @val, DATALENGTH(@val) AS Byte;

--DATETIME(8 byte), 'YYYY-MM-DD HH:MM:SS:mmm'3 milISecond INfo

	DECLARE @val DATETIME;
	SET @val= '2025-02-08 23:15:21';
	SELECT @val, DATALENGTH(@val) AS Byte;

--DATETIME2(8 byte), 'YYYY-MM-DD HH:MM:SS:mmmMMMM'7 milISecond INfo

	DECLARE @val DATETIME2;
	SET @val= '2025-02-08 23:15:21';
	SELECT @val, DATALENGTH(@val) AS Byte;

	SELECT *  FROM sys.TIME_zone_INfo;

--DATETIMEOFFSET (10 byte), 'YYYY-MM-DD HH:MM:SS:mmmMMMM'7 milISecond INfo
	DECLARE @val DATETIMEOFFSET;
	SET @val= '2025-02-08 23:15:21 +5:30';
	SELECT @val, DATALENGTH(@val) AS Byte;


	DECLARE @val DATETIMEOFFSET;
	SET @val= SYSDATETIME();
	SELECT @val, DATALENGTH(@val) AS Byte;


	DECLARE @val DATETIMEOFFSET;
	SET @val= CONCAT(SYSDATETIME(),'-5:30');
	SELECT @val, DATALENGTH(@val) AS Byte;

-- ###########################################################################################
--DDL(Data DefINition Language)
--CREATE
	--CREATE DATABASE
		--Syntax: CREATE DATABASE DATABASENAME

		
	CREATE DATABASE Demo ;
	CREATE DATABASE SQlDemo ;
	CREATE DATABASE Hello ;

--[] = Qoute identifier	
	CREATE DATABASE [sql 123];

---TASk to CREATE TABLE employee (eid, eNAME , age , gender, salary)
	USE demo;
	CREATE TABLE employee (eid INT , eNAME VARCHAR(10), age TINYINT , gender CHAR(10), salary DECIMAL(10,2));

-- Which DATABASE & datatype
-- ###########################################################################################
--SYNATX:
--CREATE TABLE TABLE_NAME	(COLUMN1_NAME datatype ,COLUMN2_NAME datatype,COLUMN3_NAME datatype,...)

---TASk to CREATE TABLE dep (eid, eNAME , age , gender, salary)
	USE SQlDemo;
	CREATE TABLE dep eid INT , eNAME VARCHAR(10), age TINYINT , gender CHAR(10), salary DECIMAL(10,2));
-- ###########################################################################################
--ALTER
--ALTER to ADD a COLUMN 
/*Syntax:
	ALTER TABLE TABLENAME 
	ADD COLUMNNAME datatype,COLUMNNAME datatype,.....
*/

--Task to ADD COLUMN phnum INT, email VARCHAR(50)

	USE SQlDemo;
	ALTER TABLE dep	ADD phnum INT, email VARCHAR(50);

--tASk to ADD COLUMN reg INT, hoUSE VARCHAR(50)

	USE demo;
	ALTER TABLE employee ADD reg INT, house VARCHAR(50);


--ALTER to DROP a COLUMN 
/*Syntax:
	ALTER TABLE TABLENAME 
	DROP COLUMN COLUMNNAME,COLUMNNAME
*/ 
	USE SQlDemo;
	ALTER TABLE dep	DROP COLUMN age, salary, phnum;

	USE demo
	ALTER TABLE employee DROP COLUMN eid, reg, age;


--ALTER to MODIFY the datatype of a COLUMN
/*Syntax:
	ALTER TABLE TABLENAME 
	ALTER COLUMN COLUMNNAME datype
*/ 

	USE SQlDemo;
	ALTER TABLE dep	ALTER COLUMN eNAME CHAR(30);

	USE demo;
	ALTER TABLE employee ALTER COLUMN gender VARCHAR(20);

--DROP TABLE
	--Syntax: DROP TABLE TABLENAME

--DROP TABLE [dbo].[dep]
	USE SQlDemo;
	DROP TABLE dep;

--DROP DATABASE 
	--Syntax: DROP DATABASE NAME

	USE master;
	DROP DATABASE SQlDemo;

--32767 session user userid SPID LogIN
--sp_who2
	--remove the connection = Kill SPID
	SP_WHO;
	SP_WHO2;

 












-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################

-- Demo 04: 08-02-2025
-- ###########################################################################################




--SCHEMA, renaming, DML(SELECT , INSERT, UPDATE, DELETE, TRUNCATE), import/ export
--Filter(WHERE, IS NULL, NOT,  BETWEEN, AND, OR, LIKE) 




-- ###########################################################################################
https://learn.microsoft.com/en-us/sql/t-sql/queries/SELECT-ORder-by-claUSE-transact-sql?view=sql-server-ver16
https://learn.microsoft.com/en-us/sql/t-sql/queries/WHERE-transact-sql?view=sql-server-ver16
-- ###########################################################################################
-- Database file saved location

	DROP DATABASE demo;
	CREATE DATABASE [demo]
	 CONTAINMENT = NONE
	 ON  PRIMARY 
	( NAME = N'demo', 
	FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.DEMO\MSSQL\DATA\demo.mdf' , SIZE = 8192KB , FILEGROWTH = 65536KB )
	 LOG ON 
	( NAME = N'demo_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.DEMO\MSSQL\DATA\demo_log.ldf' , SIZE = 8192KB , FILEGROWTH = 65536KB )
	 WITH LEDGER = OFF;

-- ###########################################################################################
-- organisation(HR, FIN, SAL, MAR)
	CREATE DATABASE organisation;
	USE organisation;

-- ###########################################################################################
-- organisation(HR, FIN, SAL, MAR)
	CREATE DATABASE organisation;
	USE organisation;

	--hr
	CREATE TABLE t1 (c1 INT, c2 INT);
	CREATE TABLE t2 (c1 INT, c2 INT);
	CREATE TABLE t3 (c1 INT, c2 INT);
	--fIN							
	CREATE TABLE t4 (c1 INT, c2 INT);
	CREATE TABLE t5 (c1 INT, c2 INT);
	CREATE TABLE t6 (c1 INT, c2 INT);
	--sales							
	CREATE TABLE t7 (c1 INT, c2 INT);
	CREATE TABLE t8 (c1 INT, c2 INT);
	CREATE TABLE t9 (c1 INT, c2 INT);
	--mark
	CREATE TABLE t10 (c1 INT, c2 INT);
	CREATE TABLE t11 (c1 INT, c2 INT);
	CREATE TABLE t12 (c1 INT, c2 INT);

-- ###########################################################################################


	CREATE DATABASE neworg;	
	USE neworg;

	--hr
	CREATE SCHEMA hr;
	CREATE TABLE hr.t1 (c1 INT, c2 INT);
	CREATE TABLE hr.t2 (c1 INT, c2 INT);
	CREATE TABLE hr.t3 (c1 INT, c2 INT);

	--fIN
	CREATE SCHEMA fIN;
	CREATE TABLE fIN.t4 (c1 INT, c2 INT);
	CREATE TABLE fIN.t5 (c1 INT, c2 INT);
	CREATE TABLE fIN.t6 (c1 INT, c2 INT);

	--sales
	CREATE SCHEMA sales;
	CREATE TABLE sales.t7 (c1 INT, c2 INT);
	CREATE TABLE sales.t8 (c1 INT, c2 INT);
	CREATE TABLE sales.t9 (c1 INT, c2 INT);

	--mark
	CREATE SCHEMA mark;
	CREATE TABLE mark.t10 (c1 INT, c2 INT);
	CREATE TABLE mark.t11 (c1 INT, c2 INT);
	CREATE TABLE mark.t12 (c1 INT, c2 INT);

-- DATABASE.SCHEMANAME.TABLENAME
-- ###########################################################################################
	CREATE DATABASE Demo;
	USE Demo;

	CREATE TABLE department (eid INT, eNAME VARCHAR(20), age TINYINT, gender CHAR(10), salary DECIMAL(10,2));

--Renaming 
--RENAME a DATABASE 
	--Syntax: ALTER DATABASE OldDATABASENAME MODIFY NAME = NewDATABASENAME
	
	ALTER DATABASE [Demo] MODIFY NAME =Advent;

--Caution: Changing any part of an object NAME could break scripts AND stored procedures.		

--RENAME a TABLE 
	--Syntax: EXEC SP_RENAME 'SCHEMANAME.OldTABLENAME', 'NewTABLENAME'
	USE Advent;
	EXEC SP_RENAME 'dbo.department', 'records';

--DefINiton of the stored procedure 
--sp_helptext SP_RENAME 

--RENAME a COLUMN  
	--Syntax: EXEC SP_RENAME 'OldTABLENAME.COLUMNNAME', 'COLUMNNAME','COLUMN '
	EXEC SP_RENAME 'records.eid','emp_id','COLUMN';


-- ###########################################################################################
	CREATE DATABASE SQLDemo;
	USE SQLDemo;

	CREATE TABLE department (eid INT, ename VARCHAR(20), age TINYINT, gender CHAR(10), salary DECIMAL(10,2));

-- ###########################################################################################
--DML(Data Manipulation language)
--SELECT 
	--Syntax: SELECT COLUMN1,COLUMN2, COLUMN3,.... FROM TABLE 
	
	SELECT eid,ename,age, gender,salary FROM department;
	SELECT eid FROM department;
	SELECT age, gender,eid,ename,salary FROM department;
	SELECT * FROM department;
	
	
--INSERT
	--Syntax: 
	--INSERT INTO  TABLE(COLUMN1,COLUMN2, COLUMN3,....)
	--VALUES(value1,value2, value3,....)
	
	INSERT INTO  department(eid,eNAME,age, gender,salary) VALUES
	(101,'alpha',21,'Male',1232 );

	INSERT INTO  department(age, gender,eid,eNAME,salary) VALUES
	(22,'Female',102,'beta' ,23423 );
	   	  
	INSERT INTO  department	VALUES
	(103,'CHARles',23,'Male',34543 );
	
	INSERT INTO  department	VALUES
	(108,'fox',24,'Female',654334),
	(106,'echo',24,'Female',45774),
	(105,'delta',23,'male',654334),
	(107,'tom,',26,'male',98765);

	
	INSERT INTO  department	VALUES
	(110,'CHARles',23,'123',98765);

--COLUMN NAME OR number of supplied VALUES does NOT match TABLE defINition.

	INSERT INTO  department(eid,salary)	VALUES
	(104,34543 );

--VALUES = empty/absent / NOT available == NULL

	INSERT INTO  department	VALUES
	(109,'NULL',NULL,NULL,34543 );

	INSERT INTO  department	VALUES
	(NULL,NULL,NULL,NULL,NULL );

-- ###########################################################################################


--UPDATE( MODIFY the TABLE-data)
/*Syntax:
	UPDATE TABLENAME 
	SET COLUMN=value,COLUMN=value,.....
	WHERE COLUMN=value
*/

	UPDATE department
	SET gender='male'
	WHERE eid =110;


	UPDATE department
	SET eNAME ='john',gender='male',age =29
	WHERE eid =109;

	UPDATE department
	SET eid=111,eNAME ='rave',gender='male',age =29, salary =8754
	WHERE eid IS NULL;
	
	
	UPDATE department
	SET eNAME ='john',gender='male',age =29
	WHERE eid =104;
	
	UPDATE department
	SET eNAME ='john' ,age =29, salary =8754
	WHERE gender='male';

-- ###########################################################################################
--DELETE (remove a records/ multiple records FROM TABLE )
	--syntax : DELETE FROM TABLENAME WHERE COLUMN=value 
	   
	DELETE FROM department	WHERE eid =101;
	
	DELETE FROM department	WHERE eid  IN (102,103,110);
	
	DELETE FROM department;

-- ###########################################################################################
--TRUNCATE (remove all records FROM TABLE )
	--Syntax: TRUNCATE TABLE TABLENAME
	TRUNCATE TABLE department WHERE eid =101;	-- INCORRECT SYNTAX
	TRUNCATE TABLE department;					-- CORRECT SYNTAX

	SELECT * FROM department;
-- ###########################################################################################
	DROP TABLE test;
	CREATE TABLE test (id INT, ename VARCHAR(20), phnum INT);
	
	INSERT INTO test VALUES 
	(101, 'alphabetacharlie',3456789),
	(102, 'alphabetacharlie',3456789),
	(103, 'alphabetacharlie',3456789),
	(104, 'alphabetacharlie',3456789),
	(105, 'alphabetacharlie',3456789),
	(106, 'alphabetacharlie',3456789),
	(107, 'alphabetacharlie',3456789),
	(108, 'alphabetacharlie',3456789),
	(109, 'alphabetacharlie',3456789),
	(110, 'alphabetacharlie',3456789);

	GO 5000;
--GO (n)

	SELECT  * FROM test;
 

---capture the TIME to DELETE
	DECLARE @StartTime_delete DATETIME2 = SYSDATETIME(); --capture start TIME 
	DELETE FROM  test;
	DECLARE @EndTime_delete DATETIME2 = SYSDATETIME(); --capture end TIME 
	SELECT 'TIME taken to DELETE : ' + CONVERT(VARCHAR(20), DATEDIFF(MILLISECOND, @StartTime_delete, @EndTime_delete)) + ' millISeconds';


---capture the TIME to TRUNCATE
	DECLARE @StartTIME_DELETE DATETIME2 = SYSDATETIME(); --capture start TIME 
	TRUNCATE TABLE test
	DECLARE @EndTIME_DELETE DATETIME2 = SYSDATETIME(); --capture end TIME 
	SELECT 'TIME taken to TRUNCATE : ' + CONVERT(VARCHAR(20), DATEDIFF(MILLISECOND, @StartTIME_DELETE, @EndTIME_DELETE)) + ' millISeconds';
	
	--TIME taken to DELETE : 41 millISeconds
	--TIME taken to TRUNCATE : 6 millISeconds



-- ###########################################################################################
--Import Export
	CREATE DATABASE importexport;
	USE importexport;

	SELECT * FROM [import_export- data-txt] ;
	SELECT * FROM [dbo].[import_export- datas-csv];
	SELECT * FROM [dbo].[Sheet1$];




-- ###########################################################################################
	USE AdventureWorks2022;
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON;

--WHERE 
-- Comparison Operators
-- Equal ( = )


	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID=111;
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE FirstName='GIGI';
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE ModifiedDate ='2009-01-09 00:00:00.000';

-- NOT equal (!=   OR   <> )
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID != 1;
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE FirstName <> 'TERRI';


-- Greater than OR equal to(>=  )

	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID >= 20000;
	
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE ModifiedDate >= '2014-01-09 00:00:00.000';

-- Less than OR equal to(<= )

	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID <= 100;
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE ModifiedDate <= '2007-01-09 00:00:00.000';


-- ###########################################################################################
--WHERE COLUMNNAME =value AND COLUMNNAME =value AND COLUMNNAME =value AND COLUMNNAME =value ......

	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID = 10;
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE FirstName = 'Michael'	;
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID=10 AND  FirstName='Michael';
		
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID=10 AND  FirstName='Michael' AND ModifiedDate='2009-04-26 00:00:00.000';
	
--WHERE COLUMNNAME =value OR COLUMNNAME =value OR COLUMNNAME =value OR COLUMNNAME =value ......


	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID=10;
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE FirstName='Michael'	;
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID=10 OR  FirstName='Michael';
		
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID=10 AND  FirstName='Michael' AND ModifiedDate='2009-04-26 00:00:00.000';
	
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE 
	BusinessEntityID=1  OR
	BusinessEntityID=11 OR
	BusinessEntityID=111 OR
	BusinessEntityID=1111 OR
	BusinessEntityID=11111 OR
	BusinessEntityID=111111 ;


		 
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM Person.Person
	WHERE
	FirstName ='Thomas' OR
	FirstName ='Eugene' OR
	FirstName ='Andrew' OR
	FirstName ='Ruth' OR
	FirstName ='Barry' OR
	FirstName ='Sidney';

-- ###########################################################################################
--WHERE COLUMN IN (VALI, VAL2, VAL3 ,....)
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID IN (1,11,111,1111,11111);
		 
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM Person.Person
	WHERE FirstName  IN ('Thomas' ,'Eugene' ,'Aanrew' ,'Ruth' ,'Barry' ,'Sidney');



--WHERE COLUMN NOT  IN (VALI, VAL2, VAL3 ,....)



	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID  NOT IN (1,2,3,4,5);
		 
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM Person.Person
	WHERE FirstName NOT IN('ThomAS' ,'Eugene' ,'ANDrew' ,'Ruth' ,'Barry' ,'Sidney');

--WHERE IS NULL OR IS NOT NULL
	SELECT BusinessEntityID,FirstName,MIDDLENAME,LastName,ModifiedDate 
	FROM Person.Person
	WHERE MiddleNAME IS NULL;
		
	SELECT * FROM Person.Person
	WHERE MiddleNAME IS NOT NULL


--WHERE  BETWEEN  range value1 AND value2 


	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE BusinessEntityID BETWEEN 1 AND 100;

	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE  ModifiedDate BETWEEN '2008-12-22' AND '2009-01-09';



--WHERE LIKE ( % _)

	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE  FirstName LIKE 'A%';

	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE  FirstName LIKE 'ALE%';
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE  BusinessEntityID LIKE '111%';
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE  FirstName LIKE '%ED';

	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate 
	FROM PERSON.PERSON
	WHERE  FirstName LIKE '%OM%';
	
	
-- ###########################################################################################


--QUESTION TO PRACTICE 
--step 1
	CREATE DATABASE school ;
--step 2
	USE school;
--step 3

--1. Teachers TABLE:
	--COLUMNs: TeacherID INT, NAME VARCHAR(20), Age INT , ClASs VARCHAR(20)
	DROP TABLE Teachers;
	CREATE TABLE Teachers (TeacherID INT, NAME VARCHAR(20), Age INT , Class VARCHAR(20));

--2. Students TABLE:
	--COLUMNs: StudentID, FirstName, LastName, Age, Class, TeacherID
	DROP TABLE Students;
	CREATE TABLE Students (StudentID INT, FirstName VARCHAR(20), LastName VARCHAR(20), Age INT , Class VARCHAR(20), TeacherID INT);
	
--3. Courses TABLE:
	--COLUMNs: CourseID, CourseNAME, Department, TeacherID
	DROP TABLE Courses;
	CREATE TABLE Courses (CourseID INT, CourseNAME VARCHAR(20) , Department VARCHAR(20), TeacherID INT);
	
--4. Departments TABLE:
	--COLUMNs: DepartmentID, DepartmentNAME
	DROP TABLE Departments;
	CREATE TABLE Departments (DepartmentID INT, DepartmentNAME VARCHAR(20));
	
--5. Enrollments TABLE:
	--COLUMNs: EnrollmentID, StudentID, CourseID, EnrollmentDATE
	DROP TABLE Enrollments;
	CREATE TABLE Enrollments (EnrollmentID INT, StudentID INT, CourseID INT, EnrollmentDATE DATE);
	
	
--6. Teachers_Departments TABLE:
	--COLUMNs: TeacherDepartmentID, TeacherID, DepartmentID
	DROP TABLE Teachers_Departments;
	CREATE TABLE Teachers_Departments (TeacherDepartmentID INT, TeacherID INT, DepartmentID INT);
	
-- ###########################################################################################
-- ###########################################################################################
--practice question
 DROP DATABASE hospital;
 CREATE DATABASE hospital;

 USE hospital;

-- 1. Doctors TABLE:
   -- COLUMNs: DoctorID, FirstName, LastName, Specialization, Age
	DROP TABLE Doctors;
	CREATE TABLE Doctors ( DoctorID INT , FirstName VARCHAR(20), LastName VARCHAR(20), Specialization  VARCHAR(20), Age INT);

-- 2. Patients TABLE:
   -- COLUMNs: PatientID, FirstName, LastName, Age, Admissiondate, Dischargedate, DoctorID
	DROP TABLE Patients;
	CREATE TABLE Patients 
	(PatientID INT, FirstName VARCHAR(20), LastName VARCHAR(20), Age TINYINT, Admissiondate DATE, Dischargedate DATE, DoctorID INT);
   
-- 3. Departments TABLE:
   -- COLUMNs: DepartmentID, DepartmentNAME, HeaddoctorID
	DROP TABLE Departments;
	CREATE TABLE Departments (DepartmentID INT, DepartmentNAME VARCHAR(20), HeaddoctorID INT);
   
-- 4. Nurses TABLE:
   -- COLUMNs: NurseID, FirstName, LastName, Age, DepartmentID
	DROP TABLE Nurses;
	CREATE TABLE Nurses (NurseID INT, FirstName VARCHAR(20), LastName VARCHAR(20), Age TINYINT, DepartmentID INT);
   
-- 5. Medications TABLE:
   -- COLUMNs: MedicationID, MedicationNAME, Dosage
	DROP TABLE Medications;
	CREATE TABLE Medications (MedicationID INT, MedicationNAME VARCHAR(20), Dosage INT);
   
-- 6. Prescriptions TABLE:
   -- COLUMNs: PrescriptionID, PatientID, DoctorID, MedicationID, Prescribeddate, DosageInstructions
	DROP TABLE Prescriptions;
	CREATE TABLE Prescriptions 
	(PrescriptionID INT, PatientID INT, DoctorID INT, MedicationID INT, Prescribeddate DATE, DosageInstructions VARCHAR(20));
   
















-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################

-- Demo 05: 14-02-2025
-- ###########################################################################################




--ORDER BY ,top offSET fetch, aggregate functions,GROUP BY HAVing 
--ConstraINT ( NOT NULL , check,default ), INDEX , CLUSTERED , non CLUSTERED
-- ###########################################################################################
 --Self learning  
--	https://learn.microsoft.com/en-us/traINing/modules/transfORm-data-by-implementing-pivot-unpivot-rollup-cube/
--
--	https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver16
--
--	https://learn.microsoft.com/en-us/sql/relational-DATABASEs/INDEXes/CLUSTERED-AND-NONCLUSTERED-INDEXes-described?view=sql-server-ver16

-- ###########################################################################################
	CREATE DATABASE Demo;
	USE Demo;

	CREATE TABLE Department
	(
		did INT,
		eNAME VARCHAR(50) ,
		gender VARCHAR(50) ,
		salary INT ,
		dept VARCHAR(50) 
	);

	INSERT INTO Department  VALUES
	(1, 'David', 'Male', 5000, 'Sales'),
	(5, 'Shane', 'Female', 5500, 'Finance'),
	(6, 'Shed', 'Male', 8000, 'Sales'),
	(7, 'Vik', 'Male', 7200, 'HR'),
	(2, 'Jim', 'Female', 6000, 'HR'),
	(13, 'Julie', 'Female', 7100, 'IT'),
	(14, 'Elice', 'Female', 6800,'Marketing'),
	(3, 'Kate', 'Female', 7500, 'IT'),
	(4, 'Will', 'Male', 6500, 'Marketing'),
	(10, 'Laura', 'Female', 6300, 'Finance'),
	(11, 'Mac', 'Male', 5700, 'Sales'),
	(12, 'Pat', 'Male', 7000, 'HR'),
	(8, 'Vince', 'Female', 6600, 'IT'),
	(9, 'Jane', 'Female', 5400, 'Marketing'),
	(15, 'Wayne', 'Male', 6800, 'Finance'),	
	(NULL,NULL, NULL, NULL,NULL);
	
	INSERT INTO Department  VALUES 
	(-5, 'Shane', 'Female',  -121, 'Finance'),
	(6, 'Shed', 'Male', 8000, 'Sales');

	SELECT * FROM department ;

-- ###########################################################################################

--COLUMN sort --> ASC /DESC
--ORDER BY COLUMN ASc, COLUMN desc

	SELECT * FROM department ORDER BY DID ASC;
	SELECT * FROM department ORDER BY ENAME ASC;
	SELECT * FROM department ORDER BY SALARY ASC;

	SELECT * FROM department ORDER BY DID DESC;	
	SELECT * FROM department ORDER BY ENAME DESC;
	SELECT * FROM department ORDER BY SALARY DESC;
	
	SELECT * FROM department ORDER BY DID ASC, ENAME ASC;



	USE AdventureWorks2022;

	SELECT   FirstName, LastName 
	FROM person.person
	--WHERE FirstName='Aaron'
	ORDER BY FirstName ASC, LastName  DESC;


	
-- ###########################################################################################
-- ###########################################################################################
-- Syntax...
-- SELECT     TOP N      * FROM TABLE;
-- SELECT * FROM TABLE          OFFSET N ROWS;
-- SELECT * FROM TABLE          OFFSET N ROWS         FETCH NEXT M ROWS ONLY
-- TOP N & OFFSET can't be used together.
-- ###########################################################################################
-- ###########################################################################################

	SELECT * FROM person.person;

--TOP N
	SELECT TOP 1 * FROM person.person;
	SELECT TOP 10 * FROM person.person;
	SELECT TOP 5 FirstName FROM person.person;
	SELECT TOP 10 FirstName, LastName FROM person.person;

--HiGHEST ID 
	SELECT TOP 1 * FROM person.person ORDER BY BusinessEntityID DESC;

--LOWID 
	SELECT TOP 1 * FROM person.person ORDER BY BusinessEntityID ASC;

--OFFSET(SKIP) & fetch 
		--SELECT COLUMN1, COLUMN2, ...
		--FROM TABLE_NAME
		--ORDER BY COLUMN_NAME
		--OFFSET n ROWS       -- Skip the first 'n' rows
		--FETCH NEXT m ROWS ONLY; -- Then fetch the next 'm' rows

--2ND HIGHEST RECORD ONWARDS
	SELECT * 
	FROM person.person 
	ORDER BY BusinessEntityID DESC
	OFFSET 1 ROWS;

--3RD HIGHEST RECORD
	SELECT * 
	FROM person.person 
	ORDER BY BusinessEntityID DESC
	OFFSET 2 ROWS;

-- ###########################################################################################
	SELECT  * 
	FROM person.person 
	ORDER BY BusinessEntityID DESC
	OFFSET 1 ROWS
	FETCH NEXT 1 ROWS ONLY;

	SELECT  * FROM person.person 
	ORDER BY BusinessEntityID DESC
	OFFSET 10 ROWS
	FETCH NEXT 5 ROWS ONLY;


-- ###########################################################################################
--Aggregate function 

--COUNT(*): Counts the number of rows IN a datASET INclude the NULL VALUES .
	SELECT  COUNT(*) AS Counts FROM person.person ;

--COUNT(COLUMN_NAME) counts non-NULL VALUES IN a specified COLUMN.
	SELECT  COUNT(BusinessEntityID) AS Counts FROM person.person ;
	SELECT  COUNT(FirstName) AS Counts FROM person.person ;
	SELECT  COUNT(MiddleNAME) AS Counts FROM person.person ;

--MAX(): Returns the MAXimum value FROM a COLUMN.(non-NULL VALUES IN a specified COLUMN.)
	SELECT  MAX(BusinessEntityID) AS MAXval FROM person.person ;
	SELECT  MAX(FirstName) AS MAXval FROM person.person ;
	SELECT  MAX(ModifiedDate) AS MAXval FROM person.person ;

--MIN(): Returns the MINIMUM VALUE FROM a COLUMN.(non-NULL VALUES IN a specified COLUMN.)
	SELECT  MIN(BusinessEntityID) AS MINval FROM person.person ;
	SELECT  MIN(FirstName) AS MINval FROM person.person ;
	SELECT  MIN(ModifiedDate) AS MINval FROM person.person ;

--Sum()  & average() (wORk with numeric data only)

--SUM(): ADDs together all the VALUES IN a specific COLUMN.(non-NULL VALUES IN a specified COLUMN.)
	SELECT  SUM(BusinessEntityID) AS total FROM person.person ;

--AVG(): Calculates the average of a SET of VALUES IN a COLUMN.(non-NULL VALUES IN a specified COLUMN.)
	SELECT  AVG(BusinessEntityID) AS avgval FROM person.person ;

	USE demo;
	
	SELECT 	
		COUNT(*) AS Counts,	
		MAX(did) AS max_val ,	
		MIN(did) AS min_val ,	
		AVG(did) AS avg_val ,	
		SUM(salary) AS Total  
	FROM Department;




-- ###########################################################################################
 --GROUP BY ... HAVing 
 --break the result set into subsets

 SELECT did, ename, gender, salary, dept FROM Department;
 SELECT did FROM Department GROUP BY did;
 SELECT ename FROM Department GROUP BY ename;
 SELECT salary FROM Department GROUP BY salary;
 SELECT gender FROM Department GROUP BY gender;
 SELECT dept FROM Department GROUP BY dept;
 

--group with agg function 
	SELECT  gender, COUNT(*) AS counts FROM Department GROUP BY gender;
	SELECT  dept, sum(salary) AS total  FROM Department GROUP BY dept;
	SELECT  dept,gender, COUNT(*) AS counts, sum(salary) AS total FROM Department GROUP BY dept,gender;

	SELECT  
		dept,
		gender, 
		COUNT(*) AS counts, 
		sum(salary) AS total 
	FROM Department
	GROUP BY dept,gender 
	HAVing COUNT(*)>2;


	SELECT  
		dept,
		gender, 
		COUNT(*) AS counts, 
		sum(salary) AS total 
	FROM Department
	GROUP BY dept,gender 
	HAVing gender='Female';


-- ###########################################################################################
  --LOGICAL PROCESSing ORDER / SEQUENCE OF THE SELECT STATEMENT 
  --Sequence to execute IN sql server


  --SELECT
  --TOP
  --FROM
  --OFFSET N ROWS
  --FETCH NEXT M ROWS ONLY
  --JOIN
  --ON 
  --WHERE
  --GROUP BY 
  --WITH (CUBE/ ROLLUP)
  --HAVing 
  --SELECT 
  --DISTINCT
  --ORDER BY

-- ###########################################################################################

	SELECT * FROM Department ORDER BY did ASC;

--duplicate VALUES		--> Unqiue 
--NULL VALUES			--> NOT NULL
--VALUES out of range	--> check
--default				--> default


	CREATE TABLE emp
	(
		did INT NOT NULL UNIQUE,
		eNAME VARCHAR(50)  NOT NULL ,
		gender VARCHAR(50)  NOT NULL ,
		salary INT  NOT NULL check (salary >=5000) ,
		phnum BIGINT NOT NULL check (len(phnum )=10) ,
		dept VARCHAR(50)  NOT NULL default 'value IS unknown'
	);

--TABLE defINTion 
	--Syntax: sp_help TABLENAME 
	  sp_help emp


INSERT INTO emp  VALUES
	(11, 'David', 'Male',  5001, 1234567890,'Sales'),
	(5, 'Shane', 'Female',  5500,1234567899, 'Finance'),
	(6, 'Shed', 'Male', 8000,1234567899, 'Sales'),
	(7, 'Vik', 'Male', 7200,1234567899, 'HR');

	

-- CanNOT INSERT duplicate key IN object 'dbo.emp
	INSERT INTO emp  VALUES
	(11, 'David', 'Male',  5001, 1234567890,'Sales');

-- COLUMN does NOT allow NULLs. INSERT fails.
	INSERT INTO emp  VALUES
	(NULL,NULL,NULL,  5001, 1234567890,'Sales');

--The INSERT statement conflicted with the CHECK constraINT
	INSERT INTO emp  VALUES
	(111, 'David', 'Male',  4999, 1234567890,'Sales');

--The INSERT statement conflicted with the CHECK constraINT
	INSERT INTO emp  VALUES
	(111, 'David', 'Male',  6999, 1267890,'Sales');

--COLUMN NAME OR number of supplied VALUES does NOT match TABLE defINition.
	 INSERT INTO emp (did,ename,gender,salary,phnum) VALUES
	(22, 'David', 'Male',  6999, 1234567890);

	SELECT * FROM emp;

	INSERT INTO emp (did,ename,gender,salary,phnum) VALUES
	(33, 'Dave', 'Female',  7999, 1934567890);



-- ###########################################################################################
-- CONSTRAINTS
-- ###########################################################################################
	
	SELECT * FROM DEPARTMENT;

--NOT NULL 
	ALTER TABLE DEPARTMENT ALTER COLUMN did INT NOT NULL;

--UNIQUE 
	ALTER TABLE DEPARTMENT ADD CONSTRAINT dep_UK UNIQUE(DID);
	
--CHECK 
	ALTER TABLE DEPARTMENT ADD CONSTRAINT CK_SAL CHECK(SALARY >=5000);
	ALTER TABLE DEPARTMENT ADD CONSTRAINT DPDEP CHECK(DEPT LIKE '[A-Z]%');

--DEFAULT 
	ALTER TABLE DEPARTMENT ADD CONSTRAINT DF_DEPT DEFAULT 'NOVALUE'  FOR DEPT;
	ALTER TABLE DEPARTMENT ADD CONSTRAINT DF_DEP1T DEFAULT 'NOVALUE'  FOR DEPT;
	



-- ###########################################################################################
--Execution plan = Ctrl + M
--INDEX 
	SELECT * FROM DEPARTMENT  WHERE did =1;

--INDEX (search fast , improve the speed of read)
--B+ tree

--CLUSTERED INDEX
	--sort AND store data  IN  (existing & new records)
	--1 CLUSTERED INDEX IN 1 TABLE
	-- improve the speed of read when searching

--Syntax: CREATE CLUSTERED INDEX INDEX_Name  on TABLENAME(COLUMN NAME ASc/desc)

	CREATE CLUSTERED INDEX ci_did on department(did);
	CREATE CLUSTERED INDEX ci_ename on department(ename);
	SELECT *  FROM DEPARTMENT  WHERE did =1;


--Cannot create more than one CLUSTERED INDEX 
--DROP the existing CLUSTERED INDEX 
	SELECT ename FROM department WHERE ename ='david';


--Non CLUSTERED INDEX
	-- 999 non CLUSTERED INDEX can exist IN 1 TABLE
	-- improves the speed of read when searching

	CREATE NONCLUSTERED INDEX nci_eNAME ON department(ename);

	SELECT ename 
	FROM department 
	WHERE ename ='david';
	
	SELECT ename,salary,dept
	FROM department 
	WHERE ename='Kate' AND salary=7500 AND dept='IT';

--composite INDEX
	CREATE NONCLUSTERED INDEX nci_three on department(eNAME,salary,dept) ;

	SELECT ename,salary,dept  
	FROM department 
	WHERE salary=7500 AND ename='Kate' AND dept='IT';

	SELECT ename,salary,dept  
	FROM department 
	WHERE ename='Kate' AND salary=7500  ;

	SELECT ename,salary,dept  
	FROM department 
	WHERE ename='Kate'   AND dept='IT';

	SELECT ename,salary,dept  
	FROM department 
	WHERE ename='Kate'  ;

	SELECT ename,salary,dept 
	FROM department 
	WHERE salary=7500 AND dept='IT';

--covering INDEX 





















-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################

-- Demo 06: 15-02-2025
-- ###########################################################################################

 --PK, FK,SQL SERVER  CrossjoINs,EQUI, self joIN,merge,

-- ###########################################################################################

	CREATE DATABASE Demo	
	GO
	USE Demo	
	GO
	CREATE TABLE Department
	(
		did INT,
		eNAME VARCHAR(50) ,
		gender VARCHAR(50) ,
		salary INT ,
		dept VARCHAR(50) 
	)
	INSERT INTO Department  VALUES
	(1, 'David', 'Male', 5000, 'Sales'),
	(5, 'Shane', 'Female', 5500, 'Finance'),
	(6, 'Shed', 'Male', 8000, 'Sales'),
	(7, 'Vik', 'Male', 7200, 'HR'),
	(2, 'Jim', 'Female', 6000, 'HR'),
	(13, 'Julie', 'Female', 7100, 'IT'),
	(14, 'Elice', 'Female', 6800,'Marketing'),
	(3, 'Kate', 'Female', 7500, 'IT'),
	(4, 'Will', 'Male', 6500, 'Marketing'),
	(10, 'Laura', 'Female', 6300, 'Finance'),
	(11, 'Mac', 'Male', 5700, 'Sales'),
	(12, 'Pat', 'Male', 7000, 'HR'),
	(8, 'VINce', 'Female', 6600, 'IT'),
	(9, 'Jane', 'Female', 5400, 'Marketing'),
	(15, 'Wayne', 'Male', 6800, 'Finance') 

	SELECT * FROM department

-- ###########################################################################################
--primary key(UNIQUE + NOT NULL)// COLUMN (OR a SET of COLUMNs)
	--1 primary key  IN TABLE 
	--CLUSTERED INDEX (sort & store, SEEK FASTER)

	CREATE TABLE emp
	(
		did INT primary key, --UNIQUE + NOT NULL --clUSEred INDEX -- 1ci
		eNAME VARCHAR(50) ,
		gender VARCHAR(50) ,
		phnum INT UNIQUE ,--UNIQUE data + non clUSEred INDEX  999 nci
		dept VARCHAR(50) 
	)
	INSERT INTO emp  VALUES
	  (1, 'David', 'Male', 5000, 'Sales'),
	  (5, 'Shane', 'Female', 5500, 'Finance'),
	  (6, 'Shed', 'Male', 8000, 'Sales'),
	  (7, 'Vik', 'Male', 7200, 'HR'),
	  (2, 'Jim', 'Female', 6000, 'HR'),
	  (13, 'Julie', 'Female', 7100, 'IT'),
	  (14, 'Elice', 'Female', 6800,'Marketing'),
	  (3, 'Kate', 'Female', 7500, 'IT'),
	  (4, 'Will', 'Male', 6510, 'Marketing')

	SELECT * FROM emp

--composite primary key (COLUMN1 ,COLUMN,......)

	CREATE TABLE hr
	(
		did INT,
		eNAME VARCHAR(50) ,
		gender VARCHAR(50) ,
		phnum INT ,
		dept VARCHAR(50) ,
		primary key(did, phnum)
	)
	INSERT INTO hr  VALUES
	(1, 'David', 'Male', 5000, 'Sales'),
	(2, 'Shane', 'Female', 7200, 'Finance'),
	(3, 'Shed', 'Male', 8000, 'Sales'),
	(1, 'Vik', 'Male', 7200, 'HR'),
	(2, 'Jim', 'Female', 5000, 'HR'),
	(3, 'Julie', 'Female', 7100, 'IT')

	SELECT * FROM HR

-- ###########################################################################################
--FOReign key -->(Primary key  OR UNIQUE )
	 --Refrential INTegrity --> ADD records (Primary , UNIQUE)
	 --CAScading INTegrity --> DELETE (fOReign key)

	 CREATE TABLE Employees (
		EmployeeID INT primary key  ,
		FirstName NVARCHAR(50),
		LastName NVARCHAR(50)
	)

	CREATE TABLE USErs (
		USErID INT primary key    ,
		Email NVARCHAR(100) UNIQUE,
		USErNAME NVARCHAR(50) 
	)

	CREATE TABLE ORders (
		ORderID INT primary key  ,
		ORderDATE DATE,
		CustomerID INT UNIQUE,
		EID INT ,
		Email NVARCHAR(100) ,
		fOReign key(eid) references Employees (EmployeeID), 
		fOReign key(Email) references USErs (Email) 
		 
		)
--REFRENCTIAL INTEGRITY (PK, OR UK)

	INSERT INTO Employees VALUES 
	(1, 'John', 'Doe'),
	(2, 'Jane', 'Smith'),
	(3, 'Michael', 'Johnson'),
	(4, 'Emily', 'DavIS'),
	(5, 'ChrIS', 'Brown')

	INSERT INTO USErs VALUES 
	(1, 'john.doe@example.com', 'johndoe'),
	(2, 'jane.smith@example.com', 'janesmith'),
	(3, 'michael.johnson@example.com', 'mikejohnson'),
	(4, 'emily.davIS@example.com', 'emilydavIS'),
	(5, 'chrIS.brown@example.com', 'chrISbrown')

	INSERT INTO ORders VALUES 
	(1, '2024-08-15', 1, 1, 'john.doe@example.com'),
	(2, '2024-08-16', 2, 2, 'jane.smith@example.com'),
	(3, '2024-08-17', 3, 3, 'michael.johnson@example.com'),
	(4, '2024-08-18', 4, 4, 'emily.davIS@example.com'),
	(5, '2024-08-19', 5, 5, 'chrIS.brown@example.com'),
	(6, '2024-08-15', 1, 1, 'john.doe@example.com'),
	(7, '2024-08-16', 2, 2, 'jane.smith@example.com'),
	(8, '2024-08-17', 3, 3, 'michael.johnson@example.com')



	SELECT * FROM Employees;
	SELECT * FROM USErs;
	SELECT * FROM ORders;

--CAScading INTegrity (DELETE , UPDATE)
	DELETE FROM Employees;   
	DELETE FROM USErs 
	DELETE FROM ORders --- DELETE FROM FK FIRST

-- ###########################################################################################
--SQL SERVER JOINS

CREATE DATABASE Ecommerce
GO
USE Ecommerce
GO
-- CREATE Customers TABLE
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerNAME VARCHAR(50)
);
GO

INSERT INTO Customers (CustomerID, CustomerNAME)
VALUES
    (1, 'John Smith'),
    (2, 'Jane Doe'),
    (3, 'Alice Johnson'),
    (4, 'Bob Williams'),
    (15, 'Emily Brown'),
    (6, 'Michael DavIS'),
    (17, 'Olivia Wilson'),
    (8, 'William TaylOR'),
    (19, 'Sophia MartINez'),
    (10, 'Liam ANDerson');

GO
-- CREATE ORders TABLE
CREATE TABLE ORders (
    ORderID INT PRIMARY KEY,
    CustomerID INT,
    ORderDATE DATE
);
GO

INSERT INTO ORders (ORderID, CustomerID, ORderDATE)
VALUES
    (101, 1, '2023-08-01'),
    (102, 2, '2023-08-02'),
    (103, 3, '2023-08-03'),
    (104, 4, '2023-08-04'),
    (115, 5, '2023-08-05'),
    (106, 6, '2023-08-06'),
    (117, 7, '2023-08-07'),
    (108, 8, '2023-08-08'),
    (119, 9, '2023-08-09'),
    (110, 10, '2023-08-10');

GO
-- CREATE Products TABLE
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductNAME VARCHAR(50),
    Price DECIMAL(10, 2)
);

GO
INSERT INTO Products (ProductID, ProductNAME, Price)
VALUES
    (501, 'Widget', 10.99),
    (502, 'Gadget', 24.99),
    (503, 'AccessORy', 5.99),
    (504, 'Tool', 15.49),
    (515, 'Toy', 7.95),
    (506, 'Device', 49.99),
    (517, 'Appliance', 89.00),
    (508, 'Book', 12.50),
    (519, 'Clothing', 29.95),
    (510, 'Jewelry', 59.00);

GO
-- CREATE ORderDetails TABLE
CREATE TABLE ORderDetails (
    DetailID INT PRIMARY KEY,
    ORderID INT,
    ProductID INT,
    Quantity INT
);
GO
INSERT INTO ORderDetails (DetailID, ORderID, ProductID, Quantity)
VALUES
    (1001, 101, 501, 3),
    (1002, 101, 502, 2),
    (1003, 102, 503, 5),
    (1004, 103, 504, 1),
    (1005, 104, 505, 2),
    (1006, 105, 506, 1),
    (1007, 106, 507, 1),
    (1008, 107, 508, 3),
    (1009, 108, 509, 2),
    (1010, 109, 510, 1);



SELECT top 1 * FROM Customers
SELECT top 1 * FROM ORders
SELECT top 1  * FROM ORderDetails
SELECT top 1 * FROM products

-- ###########################################################################################
--Relationship 
	--Customers		-->ORders		=	 CustomerID
	--ORders		-->ORderDetails	=	 ORderID 
	--ORderDetails	-->products		=	 ProductID
	--Customers		-->products		=	 CustomerID-->ORderID-->ProductID

-- ###########################################################################################
/*SYNTAX JoINs:
	SELECT COLUMNs
	FROM TABLE1  JOIN TABLE2 	ON TABLE1.COLUMN = TABLE2.COLUMN
	JOIN TABLE3 	ON TABLE1.COLUMN = TABLE3.COLUMN
	JOIN TABLE4 	ON TABLE2.COLUMN = TABLE4.COLUMN
*/
-- ###########################################################################################


SELECT top 1 * FROM Customers
SELECT top 1 * FROM ORders
SELECT top 1  * FROM ORderDetails
SELECT top 1 * FROM products

--CustomerID-->ORderID-->ProductID

	SELECT  * FROM Customers INNER JOIN ORders ON Customers.CustomerID=ORders.CustomerID
	
	SELECT  * FROM Customers c INNER JOIN ORders O ON C.CustomerID=O.CustomerID
		
	SELECT  * FROM Customers AS c INNER JOIN ORders AS O ON C.CustomerID=O.CustomerID
	INNER JOIN ORderDetails  AS od ON O.ORderID=OD.ORderID

	SELECT  * FROM Customers AS c INNER JOIN ORders AS O ON C.CustomerID=O.CustomerID
	INNER JOIN ORderDetails  AS od ON O.ORderID=OD.ORderID
	INNER JOIN products AS p ON OD.ProductID=P.ProductID

--Query designer 
--cNTRL+SHIFT +q
	SELECT c.CustomerNAME, O.ORderDATE, od.Quantity, p.ProductNAME, p.Price
	FROM  Customers AS c INNER JOIN
	ORders AS O ON c.CustomerID = O.CustomerID INNER JOIN
	ORderDetails AS od ON O.ORderID = od.ORderID INNER JOIN
	Products AS p ON od.ProductID = p.ProductID

	SELECT  C.*,P.* FROM Customers AS c INNER JOIN ORders AS O ON C.CustomerID=O.CustomerID
	INNER JOIN ORderDetails  AS od ON O.ORderID=OD.ORderID
	INNER JOIN products AS p ON OD.ProductID=P.ProductID

-- ###########################################################################################
--Left outer joIN 

	SELECT  * FROM Customers Left outer  JOIN ORders ON Customers.CustomerID=ORders.CustomerID
	
	SELECT  * FROM Customers c Left    JOIN ORders O ON C.CustomerID=O.CustomerID
		
	SELECT  * FROM Customers AS c Left JOIN ORders AS O ON C.CustomerID=O.CustomerID
	Left JOIN ORderDetails  AS od ON O.ORderID=OD.ORderID

	SELECT  * FROM Customers AS c Left JOIN ORders AS O ON C.CustomerID=O.CustomerID
	Left JOIN ORderDetails  AS od ON O.ORderID=OD.ORderID
	Left JOIN products AS p ON OD.ProductID=P.ProductID

--DISplay the records of customers without ORder

	SELECT  * FROM Customers c Left JOIN ORders O ON C.CustomerID=O.CustomerID
	WHERE O.ORderID IS NULL
	
-- ###########################################################################################
--Right outer joIN 

	SELECT  * FROM Customers Right outer  JOIN ORders ON Customers.CustomerID=ORders.CustomerID
	
	SELECT  * FROM Customers c Right    JOIN ORders O ON C.CustomerID=O.CustomerID
		
	SELECT  * FROM Customers AS c Right JOIN ORders AS O ON C.CustomerID=O.CustomerID
	Right JOIN ORderDetails  AS od ON O.ORderID=OD.ORderID

	SELECT  * FROM Customers AS c Right JOIN ORders AS O ON C.CustomerID=O.CustomerID
	Right JOIN ORderDetails  AS od ON O.ORderID=OD.ORderID
	Right JOIN products AS p ON OD.ProductID=P.ProductID

--DISplay the records of ORder MISSing  customers INFO

	SELECT  * FROM Customers c Right JOIN ORders O ON C.CustomerID=O.CustomerID
	WHERE  C.CustomerID IS NULL

-- ###########################################################################################
--Full outer joIN 

	SELECT  * FROM Customers Full outer  JOIN ORders ON Customers.CustomerID=ORders.CustomerID
	
	SELECT  * FROM Customers c Full    JOIN ORders O ON C.CustomerID=O.CustomerID
		
	SELECT  * FROM Customers AS c Full JOIN ORders AS O ON C.CustomerID=O.CustomerID
	Full JOIN ORderDetails  AS od ON O.ORderID=OD.ORderID

	SELECT  * FROM Customers AS c Full JOIN ORders AS O ON C.CustomerID=O.CustomerID
	Full JOIN ORderDetails  AS od ON O.ORderID=OD.ORderID
	Full JOIN products AS p ON OD.ProductID=P.ProductID


--DISplay the records of ORder without  customers  AND customers without ORder
	SELECT  * FROM Customers c Full JOIN ORders O ON C.CustomerID=O.CustomerID
	WHERE  C.CustomerID IS NULL OR O.CustomerID IS NULL

-- ###########################################################################################
--Cross joIN 
	--Cartesian product of the two TABLEs
	--possible combINations of rows BETWEEN two OR mORe TABLEs.
	CREATE TABLE Meals(MealNAME VARCHAR(100))
	CREATE TABLE DrINks(DrINkNAME VARCHAR(100))

	INSERT INTO DrINks VALUES('ORange Juice'), ('Tea'), ('Cofee')
	INSERT INTO Meals VALUES('Omlet'), ('Fried Egg'), ('Sausage')

	SELECT * FROM Meals
	SELECT * FROM DrINks
	
	SELECT * FROM Meals cross joIN DrINks







-- ###########################################################################################

	CREATE TABLE emp(
		employee_id INT PRIMARY KEY,
		employee_NAME VARCHAR(50)	)
	INSERT INTO dep
	VALUES		(1, 'John Smith'),		(2, 'Jane Doe'),		(3, 'Bob Johnson');

	CREATE TABLE dep(
		department_id INT PRIMARY KEY,
		department_NAME VARCHAR(50)	);

	INSERT INTO emp
	VALUES		(101, 'HR'),		(102, 'EngINeering'),		(103, 'Sales');


		SELECT * FROM emp
		SELECT * FROM dep

		
		SELECT * FROM emp cross joIN dep

-- ###########################################################################################
--equi joIN
	SELECT  * FROM Customers INNER JOIN ORders ON Customers.CustomerID=ORders.CustomerID

	SELECT * FROM Customers c , ORders o WHERE  c.customerid=o.customerid

	SELECT * FROM emp cross joIN dep

	SELECT * FROM emp , dep



-- ###########################################################################################
CREATE TABLE INfo (
		EmployeeID INT PRIMARY KEY,
		EmployeeNAME VARCHAR(255),
		ManagerID INT
	)

	INSERT INTO INfo (EmployeeID, EmployeeNAME, ManagerID) VALUES
	(1, 'Alice Johnson', NULL),
	(2, 'Bob Smith', 1),
	(3, 'CatherINe Brown', 1),
	(4, 'Daniel Garcia', 1),
	(5, 'Emma Wilson', 1),
	(6, 'FranklIN MoORe', 2),
	(7, 'GeORgia TaylOR', 2),
	(8, 'Henry ANDerson', 2),
	(9, 'ISabel ThomAS', 3),
	(10, 'Jack MartINez', 3),
	(11, 'Kylie RobINson', 3),
	(12, 'Liam Clark', 4),
	(13, 'Mia Rodriguez', 4),
	(14, 'Noah LewIS', 4),
	(15, 'Olivia Lee', 5),
	(16, 'Parker Walker', 5),
	(17, 'QuINn Hall', 5),
	(18, 'Ryan Allen', 6),
	(19, 'Sophia Young', 6),
	(20, 'Tyler HernANDez', 6);

	SELECT * FROM INfo





--employee NAME AND manager NAME 
	SELECT Emp.employeeNAME, mgr.employeeNAME AS MgrNAME
	FROM INfo emp left joIN INfo mgr
	on mgr.employeeid = emp.managerid





CREATE TABLE Prod (
		ProductID INT PRIMARY KEY,
		ProductNAME NVARCHAR(50),
		LIStPrice DECIMAL(10, 2)
	)

	INSERT INTO Prod (ProductID, ProductNAME, LIStPrice)
	VALUES 
	(1, 'Product A', 100.00),
	(2, 'Product B', 150.00),
	(3, 'Product C', 100.00),
	(4, 'Product D', 200.00),
	(5, 'Product E', 150.00);

	INSERT INTO Prod (ProductID, ProductNAME, LIStPrice)
	VALUES(6, 'Product f', 150.00)

	SELECT * FROM PROD

--Product with same price

	SELECT * FROM 
	PROD p1 INner joIN  PROD p2 
	on p1.lIStprice=p2.lIStprice
	WHERE p1.productid>p2.productid













-- ###########################################################################################

/*Merge Syntax
		MERGE  target_TABLE USing source_TABLE ON merge_condition
		WHEN MATCHED THEN
			UPDATE SET COLUMN1 = value1, COLUMN2 = value2, ...
		WHEN NOT MATCHED BY TARGET THEN
			INSERT (COLUMN1, COLUMN2, ...) VALUES (value1, value2, ...)
		WHEN NOT MATCHED BY SOURCE THEN
			DELETE;
*/


-- ###########################################################################################
	CREATE TABLE Employees (
		EmployeeID INT PRIMARY KEY,
		FirstName VARCHAR(50),
		LastName VARCHAR(50),
		Department VARCHAR(50),
		Email VARCHAR(100)
	)

	INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Email)
	VALUES
		(1, 'John', 'Doe', 'Finance', 'john.doe@example.com'),
		(2, 'Jane', 'Doe', 'IT', 'jane.doe@example.com'),
		(3, 'Jim', 'Beam', 'Marketing', 'jim.beam@example.com'),
		(4, 'Jack', 'Daniels', 'Sales', 'jack.daniels@example.com'),
		(5, 'Josie', 'Wales', 'HR', 'josie.wales@example.com');


	CREATE TABLE UPDATEdEmployees (
		EmployeeID INT PRIMARY KEY,
		FirstName VARCHAR(50),
		LastName VARCHAR(50),
		Department VARCHAR(50),
		Email VARCHAR(100)
	)

	INSERT INTO UPDATEdEmployees (EmployeeID, FirstName, LastName, Department, Email)
	VALUES
		(1, 'John', 'sdf', 'sfsd', 'jsdfsdfe.com'),  -- UPDATEd email
		(2, 'Jane', 'sd', 'sdf', 'sdf.doe@example.com'),
		(3, 'Jim', 'Beam', 'dsdf', 'jim.fsd@sdf.com'),  -- UPDATEd email
		(6, 'Jill', 'ValentINe', 'IT', 'jill.valentINe@example.com'), -- New employee
		(7, 'ChrIS', 'Redfield', 'Security', 'chrIS.redfield@example.com');  -- New employee


	
	SELECT * FROM UPDATEdEmployees
	SELECT * FROM Employees
	 
--UPDATE
	merge UPDATEdEmployees ue using employees ee
	on ue.employeeid =ee.employeeid
	when matched then 
		UPDATE SET
			ue.FirstName=	ee.FirstName,
			ue.LastName	=ee.LastName	,
			ue.Department	=ee.Department	,
			ue.Email=ee.Email
		;
--INSERT
	merge UPDATEdEmployees ue using employees ee
	on ue.employeeid =ee.employeeid
	when NOT matched by target then 
		INSERT(EmployeeID, FirstName, LastName, Department, Email)
		VALUES(EE.EmployeeID, EE.FirstName, EE.LastName, EE.Department, EE.Email)
;
--DELETE
	merge UPDATEdEmployees ue using employees ee
	on ue.employeeid =ee.employeeid
	when NOT matched by SOURCE then 
	DELETE
;


--UPDATE
merge UPDATEdEmployees ue using employees ee
on ue.employeeid =ee.employeeid
	when matched then 
		UPDATE SET
			ue.FirstName=	ee.FirstName,
			ue.LastName	=ee.LastName	,
			ue.Department	=ee.Department	,
			ue.Email=ee.Email 
--INSERT 
	when NOT matched by target then 
		INSERT(EmployeeID, FirstName, LastName, Department, Email)
		VALUES(EE.EmployeeID, EE.FirstName, EE.LastName, EE.Department, EE.Email)
 
--DELETE 
	when NOT matched by SOURCE then 
		DELETE
;


	SELECT * FROM UPDATEdEmployees
	SELECT * FROM Employees
-- ###########################################################################################
-- ###########################################################################################

--FIND COLUMN--FirstName

	SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE COLUMN_NAME ='FirstName'
--FIND TABLE WITHIN A DATABASE

	SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE '%EMPLOYEE%'


--Practice Question fOR AdventureWorks2022 DATABASE 
--1. INner JoIN:
	 Question: Write a query to retrieve the `BusinessEntityID`, `JobTitle`, `FirstName`, AND `LastName` of 
	all employees by joINing the `HumanResources.Employee` AND `Person.Person` TABLEs on `BusinessEntityID`.


	SELECT He.BusinessEntityID,JobTitle,FirstName,LastName
	FROM humanResources.Employee HE INner JoIN Person.Person  PP on He.BusinessEntityID=PP.BusinessEntityID

--2. Left JoIN:
	Question: Write a query to lISt all persons with their ADDresses, INcluding those who do NOT have an 
	ADDress. USE the `Person.Person` TABLE AND the `Person.ADDress` TABLE, joINing on `BusinessEntityID`.

--3. Right JoIN:
	 Question: Write a query to lISt all product reviews along with the NAMEs of the reviewers.
	 INclude all reviews even if the reviewer s NAME IS NOT available. 
	USE the `Production.ProductReview` TABLE AND the `Person.Person` TABLE, joINing on 	`ReviewerID`.

--4. Full Outer JoIN:
	Question: Write a query to lISt all employees AND their ASsociated departments. 
	INclude employees without departments AND departments without employees.
	 USE the `HumanResources.Employee` AND `HumanResources.Department` TABLEs, joINing on `DepartmentID`.

--5. JoIN with Aggregates:
	Question: Write a query to fINd the total sales amount fOR each sales person.
	 USE the `Sales.SalesORderHeader` AND `Sales.SalesPerson` TABLEs, joINing on `SalesPersonID`.

--6. JoIN with Multiple TABLEs:
	Question: Write a query to retrieve the `ProductID`, `NAME`, `SalesORderID`, AND `ORderDATE`
	 fOR all sales ORders. USE the `Sales.SalesORderDetail`, `Production.Product`, AND `Sales.SalesORderHeader` 
	TABLEs, joINing on `ProductID` AND `SalesORderID`.

--7. JoIN with Subquery:
	Question: Write a query to fINd the NAMEs of employees who have placed an ORder. 
	USE a subquery to fINd the `EmployeeID` FROM the `Sales.SalesORderHeader` TABLE AND joIN it with the 
	`HumanResources.Employee` AND `Person.Person` TABLEs to get the `FirstName` AND `LastName`.
	 





















-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################

Demo 07: 21-02-2025
-- ###########################################################################################






 --SQL SERVER SET operatORs ,Function (string, DATE TIME )
-- ###########################################################################################
--Self learning  
--	https://learn.microsoft.com/en-us/traINing/modules/transfORm-data-by-implementing-pivot-unpivot-rollup-cube/
--	https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver16
-- ###########################################################################################
 

--7. JoIN with Subquery:
	Question: Write a query to fINd the NAMEs of employees who have placed an ORder. 
	USE a subquery to fINd the `EmployeeID` FROM the `Sales.SalesORderHeader` TABLE AND joIN it with the 
	`HumanResources.Employee` AND `Person.Person` TABLEs to get the `FirstName` AND `LastName`.
	 

	 SELECT  FirstName, LastName 
     FROM HumanResources.Employee AS HRE INner joIN  Person.Person AS PP
     on PP. BusinessEntityID = HRE. BusinessEntityID
	 WHERE PP. BusinessEntityID IN( SELECT SalesPersonID FROM 	  Sales.SalesORderHeader )

-- ###########################################################################################
	CREATE DATABASE  SQLDEMO
	GO
	USE SQLDEMO
	GO

	CREATE TABLE Department
	(
	did INT,
	eNAME VARCHAR(50) ,
	gender VARCHAR(50) ,
	salary INT ,
	dept VARCHAR(50) 
	)

	GO
	INSERT INTO Department  VALUES
	(1, 'David', 'Male', 5000, 'Sales'),
	(5, 'Shane', 'Female', 5500, 'Finance'),
	(6, 'Shed', 'Male', 8000, 'Sales'),
	(7, 'Vik', 'Male', 7200, 'HR'),
	(2, 'Jim', 'Female', 6000, 'HR'),
	(13, 'Julie', 'Female', 7100, 'IT'),
	(14, 'Elice', 'Female', 6800,'Marketing'),
	(3, 'Kate', 'Female', 7500, 'IT'),
	(4, 'Will', 'Male', 6500, 'Marketing'),
	(10, 'Laura', 'Female', 6300, 'Finance'),
	(11, 'Mac', 'Male', 5700, 'Sales'),
	(12, 'Pat', 'Male', 7000, 'HR'),
	(8, 'VINce', 'Female', 6600, 'IT'),
	(9, 'Jane', 'Female', 5400, 'Marketing'),
	(15, 'Wayne', 'Male', 6800, 'Finance')

	GO
	SELECT *  FROM Department
-- ###########################################################################################
	CREATE TABLE emp 
	( empid INT, eNAME VARCHAR(20), eage INT , dob DATE)


	CREATE TABLE dep  
	(depid INT ,empNAME VARCHAR(20),salary INT ,age INT  ,
	Company VARCHAR(20) Default 'IBM')

	INSERT INTO EMP  VALUES 
	(101,'ALPHA',21,'2010-08-11') ,
	(103,'BETA',22,'2009-08-11'),
	(102,'CHARLIE',21,'2010-08-11'),
	(105,'DELTA',25,'2008-08-11'),
	(106,'ECHO',23,'2006-08-11'),
	(104,'FOX',21,'2004-08-11'),
	(109,'CHARLIE',24,'2010-08-11'),
	(107,NULL,25,'2008-08-11')


	INSERT INTO dep  VALUES 
	(101,'Alpha',6000,21,'VendOR'), 
	(102,'fox',7000,21,'VendOR'), 
	(105,'Echo',5100,29,'VendOR'),
	(103,'beta',5100,29,'VendOR'),
	(104,'fox',5100,21,'VendOR'), 
	(105,'tim',5100,25,'VendOR')

	SELECT * FROM emp 
	SELECT * FROM dep 

--All queries combINed using a UNION, INTERSECT OR EXCEPT operatOR 
--must have an equal number of expressions/COLUMN IN their target lISts.
--OperAND type clASh: INT IS INcompatible with DATE

--union all (CombINe + duplicate VALUES)


	
	
	SELECT depid,empNAME,age	  FROM dep 
	union all
	SELECT empid,eNAME,eage  FROM emp 
	
	SELECT empid,eNAME,eage  FROM emp 
	union all
	SELECT depid,empNAME,age FROM dep ORDER BY empid ASc

--union   (CombINe + UNIQUE VALUES)	
	SELECT empid,eNAME,eage  FROM emp 
	union  
	SELECT depid,empNAME,age FROM dep ORDER BY empid ASc

--INTersect  (matching  + UNIQUE VALUES)
	SELECT empid,eNAME,eage  FROM emp 
	INTersect  
	SELECT depid,empNAME,age FROM dep ORDER BY empid ASc

--Except   (mINus UNIQUE VALUES)

	SELECT empid,eNAME,eage  FROM emp 
	Except  
	SELECT depid,empNAME,age FROM dep ORDER BY empid ASc


-- ###########################################################################################
-- Function 
--String function 
	USE AdventureWorks2022

--Aggregate(Count, MAX , mIN , avg , sum)

--String 'dat '

--DATETIME

--COnversion

--WINdows
	USE AdventureWorks2022
	SELECT BusinessEntityID, FirstName, LastName FROM Person.Person 


--len(expression/COLUMN NAME)
	SELECT FirstName,len(FirstName)  AS lengths FROM Person.Person 
	SELECT len('CHARles')
	SELECT len('Ch ar le s')
	SELECT len('  Ch ar le s    ')

--trim(expression) remove the lead AND trial spaces 
	SELECT len('  Ch ar le s    ')
	SELECT trim('  Ch ar le s    ')
	SELECT len(trim('  Ch ar le s    '))


--Left(expression, n) & Right(expression, n)
	SELECT BusinessEntityID, FirstName 
	, left(FirstName,1), right(FirstName,1)
	FROM Person.Person 

	SELECT BusinessEntityID, FirstName 
	, left(FirstName,10), right(FirstName,6)
	FROM Person.Person 

--Upper(expression) AND lower(expression)

	SELECT BusinessEntityID, FirstName 
	,upper(FirstName), lower(FirstName)
	FROM Person.Person 

--Concat(expression,expression,expression,...)

	SELECT BusinessEntityID, FirstName,MiddleNAME, LastName ,
	concat(FirstName,MiddleNAME, LastName ) AS FullNAME
	FROM Person.Person 
	
	SELECT BusinessEntityID, FirstName,MiddleNAME, LastName ,
	concat(FirstName,' ',MiddleNAME,' ', LastName ) AS FullNAME
	FROM Person.Person 

	SELECT BusinessEntityID, FirstName,MiddleNAME, LastName ,
	concat(FirstName,';',MiddleNAME,';', LastName ) AS FullNAME
	FROM Person.Person 
--Concat_ws('',expression,expression,expression,...)

	SELECT BusinessEntityID, FirstName,MiddleNAME, LastName ,
	concat_ws(';',FirstName,MiddleNAME, LastName ) AS FullNAME
	FROM Person.Person 
	SELECT BusinessEntityID, FirstName,MiddleNAME, LastName ,
	concat_ws(' ',FirstName,MiddleNAME, LastName ) AS FullNAME
	FROM Person.Person 

--Scenario
	--INput = syed  OR aLPha OR aLExen
	--Output =Syed
	DECLARE @NAME VARCHAR(30)
	SET @NAME ='aLPha'
	SELECT @NAME,concat(upper(left(@NAME,1)), lower(right(@NAME, len(@NAME)-1)))

-- ###########################################################################################
--replace ( string , old value, new value)

	SELECT replace ('Hello 123 WORld', '123', 'SQL')

	
	SELECT replace ('Hello 123 WORld', ' 123 ', '')

	SELECT BusinessEntityID, FirstName, LastName ,
	replace(FirstName, 'e', '111111111111111')
	FROM Person.Person 


--STUFF ( string, start, length, new_string )
Hello 123 WORld
123456789012345678
Hello SQL123 WORld
 
	SELECT stuff ('Hello 123 WORld',7,0,'SQL')
alphabeta@gmail.com
1234567890123456789
	SELECT stuff ('alphabeta@gmail.com',6,0,'.')

Hello 123 WORld
123456789012345678
Hello SQL123 WORld
	SELECT stuff ('Hello 123 WORld',7,0,'SQL')
	
	SELECT stuff ('Hello 123 WORld',7,3,'SQL')
	
	SELECT stuff ('Hello 123 WORld',7,4,'SQL')

	SELECT stuff ('Hello 123 WORld',7,9,'SQL')

--CHARINDEX ( substring, string, [start_position] ) 
alphabeta@gmail.com
1234567890123456789

1234-5689
123456789

	SELECT CHARINDEX ('@','alphabeta@gmail.com')
	SELECT CHARINDEX ('-','1234-5689')
	
	SELECT CHARINDEX ('j','demo tom john')
	SELECT CHARINDEX ('m','demo tom john')
	SELECT CHARINDEX ('m ','demo tom john')
	SELECT CHARINDEX ('oh','demo tom john')
	SELECT CHARINDEX ('om','demo tom john')

demo tom john
1234567890123 
	SELECT CHARINDEX ('o','demo tom john',6)

--SUBSTRing ( string, start, length )

demo tom john
1234567890123 
	SELECT  SUBSTRing ( 'demo tom john',1,4)
	SELECT  SUBSTRing ( 'demo tom john',6,3)
	SELECT  SUBSTRing ( 'demo tom john',10,4)




	SELECT BusinessEntityID, FirstName,MiddleNAME, LastName ,
	SUBSTRing ( FirstName,1,4)
	FROM Person.Person 




	CREATE TABLE datAS
	(email VARCHAR(100))


	INSERT INTO datAS (email) VALUES 
	('jane.doe@example.com'),
	('john.smith@wORkmail.net'),
	('alex.jones@university.edu'),
	('lISa.wong@techhub.ORg'),
	('mike.brown@services.co.uk'),
	('sara.lee@marketplace.com'),
	('dave.wilson@creativeagency.us'),
	('emily.harrIS@globalenterprISe.com'),
	('carlos.garcia@netwORksolutions.es'),
	('anna.zhao@researchINst.cn');

	SELECT * FROM datAS

	--Scenarios 
	--INput--> jane.doe@example.com
	--output--> example.com

	
	SELECT email, SUBSTRing(email,	CHARINDEX('@',email)+1,len(email)) AS domaIN
	FROM datAS




-- ###########################################################################################
CREATE TABLE Transactions (
    custNAME VARCHAR(50),
    tran_DATE DATE
);

INSERT INTO Transactions (custNAME, tran_DATE) VALUES
('J', '2025-02-20'),
('X', '2025-02-20'),
('E', '2025-02-20'),
('E', '2025-02-21');


SELECT * FROM transactions
WHERE tran_DATE= '2025-02-20' AND tran_DATE='2025-02-21'



SELECT * FROM transactions
WHERE tran_DATE IN( '2025-02-20'  ,'2025-02-21')  AND custNAME='Satyam'

SELECT * FROM transactions
WHERE tran_DATE BETWEEN '2025-02-20' AND'2025-02-21'



SELECT * FROM transactions
WHERE custNAME IN (SELECT custNAME FROM transactions  GROUP BY custNAME HAVing COUNT(*)>1)



SELECT custNAME FROM transactions 
WHERE tran_DATE IN( '2025-02-20'  ,'2025-02-21') 
GROUP BY custNAME 
HAVing COUNT(DISTINCT tran_DATE )>1

-- ###########################################################################################
--DATE TIME 'yyyy-MM-dd hh:mm:ss'
	--DATE(Year, month, day, quarter, week, weekday, day of year)
	--TIME (Hours, mINutes, second, milISeconds, microseconds, nanoseconds)

	USE AdventureWorks2022
	SELECT BusinessEntityID,BirthDATE,HireDATE FROM HumanResources.Employee

	SELECT BirthDATE,
	 YEAR(BirthDATE) AS yEARS,
	 MONTH(BirthDATE) AS MONTHS,
	 DAY(BirthDATE) AS DAYS
	FROM HumanResources.Employee



-- System TIME (laptop machINe)
	SELECT GETDATE()
	SELECT SYSDATETIME()

--TIME offSET

	SELECT SYSDATETIMEOFFSET()

	SELECT * FROM sys.TIME_zone_INfo
	   	  

	SELECT 	year('2025-02-22 02:13:54.927'),month('2025-02-22 02:13:54.927'),day('2025-02-22 02:13:54.927')

--DATENAME ( DATE AND TIME parts - returns nVARCHAR )

	SELECT DATENAME(YEAR,GETDATE())
	SELECT DATENAME(MONTH,GETDATE())
	SELECT DATENAME(DAY,GETDATE())
	SELECT DATENAME(DAYOFYEAR,GETDATE())
	SELECT DATENAME(WEEK,GETDATE())
	SELECT DATENAME(WEEKDAY,GETDATE())
	SELECT DATENAME(QUARTER,GETDATE())

	SELECT DATENAME(HOUR,GETDATE())
	SELECT DATENAME(MINUTE,GETDATE())
	SELECT DATENAME(SECOND,GETDATE())
	SELECT DATENAME(MILLISECOND,GETDATE())
	SELECT DATENAME(MICROSECOND,GETDATE())
	SELECT DATENAME(NANOSECOND,GETDATE())
	
--DATEPART()returns an INTeger cORresponding to the DATEpart specified
	SELECT  DATEpart(year,GETDATE() )
	SELECT  DATEpart(MONTH,GETDATE() )
	SELECT  DATEpart(DAY,GETDATE() )
	SELECT  DATEpart(DAYOFYEAR,GETDATE() )
	SELECT  DATEpart(WEEK,GETDATE() )
	SELECT  DATEpart(WEEKDAY,GETDATE() )
	SELECT  DATEpart(QUARTER,GETDATE() )

	SELECT  DATEpart(HOUR,GETDATE() )
	SELECT  DATEpart(MINUTE,GETDATE() )
	SELECT  DATEpart(SECOND,GETDATE() )
	SELECT  DATEpart(MILLISECOND,GETDATE() )
	SELECT  DATEpart(MICROSECOND,GETDATE() )
	SELECT  DATEpart(NANOSECOND,GETDATE() )

--DATEDiff( DATEPART, lowerDATE, higherDATE )
--returns an INTeger cORresponding

	SELECT BusinessEntityID,BirthDATE,HireDATE,
	DATEDiff( year, BirthDATE, HireDATE ) AS [Year],
	DATEDiff( MONTH, BirthDATE, HireDATE ) AS [Month],
	DATEDiff( day, BirthDATE, HireDATE ) AS [day],
	DATEDiff( WEEK, BirthDATE, HireDATE ) AS[week],
	DATEDiff( WEEKDAY, BirthDATE, HireDATE ) AS[WEEKDAY],
	DATEDiff( QUARTER, BirthDATE, HireDATE ) AS[QUARTER],
	DATEDiff( hour, BirthDATE, HireDATE ) AS[hour],
	DATEDiff( MINUTE, BirthDATE, HireDATE ) AS[MINUTE] 
	FROM HumanResources.Employee

--DATEADD(DATEpart, number, DATE)

	SELECT BusinessEntityID,BirthDATE,HireDATE, 
	DATEADD( year, 2, HireDATE ) AS [Year],
	DATEADD( MONTH, 150, HireDATE ) AS [Month],
	DATEADD( day, 579, HireDATE ) AS [day],
	DATEADD( WEEK, 33, HireDATE ) AS[week],
	DATEADD( WEEKDAY, 52, HireDATE ) AS[WEEKDAY]
	FROM HumanResources.Employee
	 
	SELECT BusinessEntityID,BirthDATE,HireDATE, 
	DATEADD( year, -2, HireDATE ) AS [Year],
	DATEADD( MONTH, -50, HireDATE ) AS [Month],
	DATEADD( day, -79, HireDATE ) AS [day],
	DATEADD( WEEK, -3, HireDATE ) AS[week],
	DATEADD( WEEKDAY, -52, HireDATE ) AS[WEEKDAY]
	FROM HumanResources.Employee
-- ###########################################################################################

--Scenarios 
--hINT(ParseNAME)
	--INput =Syed E AbbAS
	--output 
		--c1=Syed	
		--c2=E	
		--c3=AbbAS	

--Scenarios
	--INput SSN: '123-45-6789'
	--Expected Output MASked SSN: '***-**-6789'

--Scenarios
	--INput Product Code: 'ABC-123-XYZ'
	--Expected Output New Product Code: 'ABC-789-XYZ'
--Scenarios
	--INput Full NAME: 'John A. Doe'
	--Expected Output INitials: 'JAD'

--Scenarios
	--INput Phone Number: '1234567890'
	--Expected Output FORmatted Phone Number: '(123) 456-7890'


-- SET OperatORs Questions AdventureWorks2022

--1. UNION:
--   - Question: Write a query to lISt all `BusinessEntityID` VALUES that appear IN either the `Person.Person` TABLE OR the `Sales.Customer` TABLE, OR both.

--2. UNION ALL:
--   - Question: Write a query to lISt all `BusinessEntityID` VALUES, INcluding duplicates, FROM both the `Person.Person` TABLE AND the `Sales.Customer` TABLE.

--3. INTERSECT:
--   - Question: Write a query to fINd all `BusinessEntityID` VALUES that are present IN both the `Person.Person` TABLE AND the `Sales.Customer` TABLE.

--4. EXCEPT:
--   - Question: Write a query to fINd all `BusinessEntityID` VALUES that are present IN the `Person.Person` TABLE but NOT IN the `Sales.Customer` TABLE.

--5. UNION with ADDitional COLUMNs:
--   - Question: Write a query to lISt all `FirstName` AND `LastName` combINations FROM both the `Person.Person` TABLE AND the `HumanResources.Employee` TABLE. Ensure there are no duplicates.

--6. UNION ALL with filtering:
--   - Question: Write a query to lISt all `EmailADDress` VALUES FROM the `Person.EmailADDress` TABLE AND `Sales.SalesPersonEmailADDress` TABLE, INcluding duplicates.

--7. INTERSECT with condition:
--   - Question: Write a query to fINd all `ProductID` VALUES that are IN both the `Sales.SalesORderDetail` TABLE AND the `Production.Product` TABLE AND have a `ProductID` less than 1000.

--8. EXCEPT with condition:
--   - Question: Write a query to fINd all `SalesORderID` VALUES IN the `Sales.SalesORderHeader` TABLE that are NOT IN the `Sales.SalesORderDetail` TABLE AND WHERE the `ORderDATE` IS IN the year 2022.

--9. Complex UNION:
--   - Question: Write a query to combINe the `NAME` FROM `Production.Product` AND `Production.ProductSubcatery` TABLEs. Ensure that the combINed lISt IS UNIQUE.

--10. Complex EXCEPT:
--    - Question: Write a query to lISt all `EmployeeID` VALUES FROM the `HumanResources.Employee` TABLE that do NOT appear IN the `Sales.SalesORderHeader` TABLE, ensuring that the lISt only INcludes active employees.




















-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################

Demo 08: 22-02-2025
-- ###########################################################################################






--Function (  conversion , wINdows function, CTE ),USER DEFINED (TABLE valued & Scalar valued function  )
--view AND procedure 
-- ###########################################################################################
--Self learning  
	https://learn.microsoft.com/en-us/sql/t-sql/queries/with-common-TABLE-expression-transact-sql?view=sql-server-ver16
	https://learn.microsoft.com/en-us/traINing/modules/transfORm-data-by-implementing-pivot-unpivot-rollup-cube/
	https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver16
-- ###########################################################################################
	CREATE DATABASE  SQLDEMO
	GO
	USE SQLDEMO
	GO

	CREATE TABLE Department
	(
	did INT,
	eNAME VARCHAR(50) ,
	gender VARCHAR(50) ,
	salary INT ,
	dept VARCHAR(50) 
	)

	GO
	INSERT INTO Department  VALUES
	(1, 'David', 'Male', 5000, 'Sales'),
	(5, 'Shane', 'Female', 5500, 'Finance'),
	(6, 'Shed', 'Male', 8000, 'Sales'),
	(7, 'Vik', 'Male', 7200, 'HR'),
	(2, 'Jim', 'Female', 6000, 'HR'),
	(13, 'Julie', 'Female', 7100, 'IT'),
	(14, 'Elice', 'Female', 6800,'Marketing'),
	(3, 'Kate', 'Female', 7500, 'IT'),
	(4, 'Will', 'Male', 6500, 'Marketing'),
	(10, 'Laura', 'Female', 6300, 'Finance'),
	(11, 'Mac', 'Male', 5700, 'Sales'),
	(12, 'Pat', 'Male', 7000, 'HR'),
	(8, 'VINce', 'Female', 6600, 'IT'),
	(9, 'Jane', 'Female', 5400, 'Marketing'),
	(15, 'Wayne', 'Male', 6800, 'Finance')

	GO
	SELECT *  FROM Department
-- ###########################################################################################
--Conversion
	--data type -->
		--Numeric-->string -->numeric -->DATETIME 
		--string-->string -->DATETIME 
		--DATETIME-->string -->DATETIME 

	SELECT 1+2

	SELECT 'a'+'b'

	SELECT 'a'+2

	SELECT BusinessEntityID,LogINID  
	FROM AdventureWorks2022.HumanResources.Employee
		
	SELECT BusinessEntityID,LogINID,
	BusinessEntityID +LogINID 
	FROM AdventureWorks2022.HumanResources.Employee

--Conversion
--CAST ( expression AS target_data_type )
	
	SELECT 'a'+cASt(2 AS CHAR)

	SELECT BusinessEntityID,LogINID,	cASt(BusinessEntityID AS VARCHAR) +LogINID
	FROM AdventureWorks2022.HumanResources.Employee
--CONVERT ( target_data_type, expression , [style] )
		
	SELECT 'a'+CONVERT( CHAR,2)

	SELECT BusinessEntityID,LogINID,	convert( VARCHAR,BusinessEntityID) +LogINID
	FROM AdventureWorks2022.HumanResources.Employee
https://www.mssqltips.com/sqlservertip/1145/DATE-AND-TIME-conversions-using-sql-server/
--GETDATE()
	
	SELECT  cASt(GETDATE() AS VARCHAR(11))
	 
		
	SELECT  CONVERT( VARCHAR(11),GETDATE())

--DATETIME	
	SELECT GETDATE(), cASt(GETDATE() AS VARCHAR)
	SELECT GETDATE(), convert(VARCHAR,GETDATE() )
	

	SELECT convert(VARCHAR,GETDATE(),1)
	SELECT convert(VARCHAR,GETDATE(),4)
	SELECT convert(VARCHAR,GETDATE(),5)
	SELECT convert(VARCHAR,GETDATE(),6)
	SELECT convert(VARCHAR,GETDATE(),11)
	SELECT convert(VARCHAR,GETDATE(),21)
	SELECT convert(VARCHAR,GETDATE(),33)
	SELECT convert(VARCHAR,GETDATE(),35)
	SELECT convert(VARCHAR,GETDATE(),104)

	SELECT convert(VARCHAR,GETDATE(),8)
	SELECT convert(VARCHAR,GETDATE(),9)
	SELECT convert(VARCHAR,GETDATE(),24)
	SELECT convert(VARCHAR,GETDATE(),108)

	 SELECT CONVERT(VARCHAR, GETDATE(),0)
	 SELECT CONVERT(VARCHAR, GETDATE(),13)
	 SELECT CONVERT(VARCHAR, GETDATE(),20)
	 SELECT CONVERT(VARCHAR, GETDATE(),21)
	 SELECT CONVERT(VARCHAR, GETDATE(),27)
	 SELECT CONVERT(VARCHAR, GETDATE(),127)
	  
--FORMAT(expression, fORmat, [culture])
	SELECT BusinessEntityID,Rate,
	FORMAT(rate, 'c', 'en-IN') AS INR,
	FORMAT(rate, 'c', 'en-us') AS us,
	FORMAT(rate, 'c', 'en-gb') AS gb
	FROM AdventureWorks2022.HumanResources.EmployeePayHIStORy

--'yyyy-dd-MM hh-mm-ss'

	SELECT  GETDATE() 
	SELECT  fORmat(GETDATE(),'yyyy-dddd-MMMM hh-mm-ss')

	SELECT  fORmat(GETDATE(),'yyy-ddd-MMM hh-mm-ss')

	SELECT  fORmat(GETDATE(),'yy-dd-MM hh-mm-ss')
	   	
	SELECT  fORmat(GETDATE(),'ddd-MMMM-yy')

	
	SELECT  fORmat(GETDATE(),'MMM-yy, dddd')

	
	SELECT  fORmat(GETDATE(),'yyy-ddd-MMM hh:mm:ss tt')

-- ###########################################################################################
--WINdows  function(ranking function ) 
--ranking_function() over(partition by  COLUMNNAME  ORDER BY COLUMNNAME ASc/desc)
--partition by = GROUP BY 


	SELECT  did ,salary 
	,RANK() over(ORDER BY salary desc) AS Ranks
	,Dense_RANK() over(ORDER BY salary desc) AS denseRanks
	,Row_number() over(ORDER BY salary desc) AS rownum
	FROM Department 

	   
	SELECT  did ,salary  
	,Row_number() over(ORDER BY salary desc) AS rownum
	FROM Department 

	SELECT  did ,salary 
	,RANK() over(ORDER BY salary desc, did ASc) AS Ranks 
	FROM Department 


--NTILE(n) over(partition by  COLUMNNAME  ORDER BY COLUMNNAME ASc/desc)


	SELECT  did ,salary  
	,NTILE(5) over(ORDER BY salary desc) AS tiles
	FROM Department 

	SELECT  did ,salary  
	,NTILE(4) over(ORDER BY salary desc) AS tiles
	FROM Department 

--LAG(COLUMN_NAME, offSET, default_value) OVER (PARTITION BY COLUMN_NAME ORDER BY COLUMN_NAME)
--Lag --Previous row 

	SELECT  did ,salary  
	,lag(salary) over(ORDER BY salary desc) AS lags
	FROM Department
	
	SELECT  did ,salary  
	,lag(salary,1,1234) over(ORDER BY salary desc) AS lags
	FROM Department
	
	SELECT  did ,salary  
	,lag(salary,3,1234) over(ORDER BY salary desc) AS lags
	FROM Department

	SELECT  did ,salary,lag(salary,1,0) over(ORDER BY salary desc) AS lags,
	salary -lag(salary,1,0) over(ORDER BY salary desc) AS diff
	FROM Department


 --LEAD(COLUMN_NAME, offSET, default_value) OVER (PARTITION BY COLUMN_NAME ORDER BY COLUMN_NAME)
 --Lead() -- next row

 
	SELECT  did ,salary  
	,LEAD(salary) over(ORDER BY salary desc) AS leads
	FROM Department
	
	SELECT  did ,salary  
	,LEAD(salary,1,1234) over(ORDER BY salary desc) AS leads
	FROM Department
	
	SELECT  did ,salary  
	,LEAD(salary,3,1234) over(ORDER BY salary desc) AS leads
	FROM Department

	SELECT  did ,salary,LEAD(salary,1,0) over(ORDER BY salary desc) AS leads,
	salary -LEAD(salary,1,0) over(ORDER BY salary desc) AS diff
	FROM Department

--FINd high salary bASed on their rank =3

	   
	SELECT  did ,salary  
	,Row_number() over(ORDER BY salary desc) AS rownum
	FROM Department 
	WHERE Row_number() over(ORDER BY salary desc)=3

--errOR message 
	--WINdowed functions can only appear IN the SELECT OR ORDER BY claUSEs.

-- ###########################################################################################
 --CTE(Common TABLE experssion)
  /* --TempORary result SET IN SQL Server( SELECT, INSERT, UPDATE, OR DELETE)
  WITH CTE_NAME (COLUMN1, COLUMN2, ...)
	AS
	(
		-- CTE query
		SELECT COLUMN1, COLUMN2, ...
		FROM TABLENAME
		WHERE Condition
	)
	-- MaIN query referencing the CTE
	SELECT *	FROM CTE_NAME;


 */

 
--FINd high salary bASed on their rank =3
--scenario 1
	with highsal 
	AS		
	(	SELECT  did ,salary,Row_number() over(ORDER BY salary desc) AS rownum FROM Department 		)

	SELECT * FROM highsal WHERE rownum =3


--scenario 2
	with groups  	AS		
	(		SELECT  did ,salary ,NTILE(5) over(ORDER BY salary desc) AS tiles 	FROM Department 		)

	SELECT * FROM groups WHERE tiles =2

	
	SELECT * FROM (
	SELECT  did ,salary  
	,Row_number() over(ORDER BY salary desc) AS rownum
	FROM Department 
	)  abc WHERE abc.rownum=2
	


	GO

	with highsal 
	AS		
	(	SELECT  did ,salary,Row_number() over(ORDER BY salary desc) AS rownum FROM Department 		)

	SELECT * FROM highsal WHERE rownum =3


--scenario 3

--FINd dept  high salary bASed on their rank =3

	SELECT  did ,salary,dept,Row_number() over(  partition by dept  ORDER BY salary desc) AS rownum FROM Department 


	with deptsal 
	AS		
	(SELECT  did ,salary,dept,Row_number() over(  partition by dept  ORDER BY salary desc) AS rownum FROM Department )

	SELECT * FROM deptsal WHERE rownum =1





--duplicate records
	SELECT  * FROM Department  ORDER BY did ASc


--== duplicate records 
	with duprec 
	AS 
	(	SELECT  did ,salary,dept,Row_number() over(  partition by did  ORDER BY did ASc) AS rownum FROM Department )
	SELECT * FROM duprec  WHERE rownum>1


--== UNIQUE records 

	with duprec 
	AS 
	(	SELECT  did ,salary,dept,Row_number() over(  partition by did  ORDER BY did ASc) AS rownum FROM Department )
	SELECT * FROM duprec  WHERE rownum=1



--== remove duplicate records 
	with duprec 
	AS 
	(	SELECT  did ,salary,dept,Row_number() over(  partition by did  ORDER BY did ASc) AS rownum FROM Department )
	DELETE FROM duprec  WHERE rownum>1



--
	with lowsal
	AS
		(SELECT top 1 * FROM Department  ORDER BY salary ASc)
	SELECT * FROM lowsal

	GO


	with highsal
	AS
		(SELECT   top 1 * FROM Department  ORDER BY salary desc)
	SELECT * FROM highsal

--combINe two cte together
with 
	lowsal
		AS		(SELECT top 1 * FROM Department  ORDER BY salary ASc)

	,highsal
		AS 		(SELECT   top 1 * FROM Department  ORDER BY salary desc)
	
		SELECT * FROM lowsal
		union all
		SELECT * FROM highsal




-- ###########################################################################################
--USEr defINed function
	--Scalar valued function 
	/*syntax
	CREATE FUNCTION function_NAME (@parameter1 datatype [, @parameter2 datatype, ...])
	RETURNS DATATYPE
	AS
	RETURN (
				-- A single SELECT statement
				SELECT COLUMN1, COLUMN2, ...
				FROM TABLEs   WHERE conditions
			)

*/
--CUBE OF A NUMBER 
	DECLARE @num INT
	SET @num=5
	SET @num=@num*@num*@num
	SELECT @num

--CREATE FUNCTION
	CREATE FUNCTION cubes()
	returns INT
	AS
	begIN	
		DECLARE @num INT
		SET @num=5
		SET @num=@num*@num*@num
		return @num
	end

--call function 
	SELECT dbo.cubes()

--ALTER function 

	ALTER FUNCTION cubes(@num float)
	returns float
	AS
	begIN	 
		return @num*@num*@num
	end

--call function 
	SELECT dbo.cubes(4)

	SELECT dbo.cubes(15.4)

	SELECT dbo.cubes(93.8)

	SELECT dbo.cubes(2.64)





	
--call function 
	SELECT dbo.cubes() 

-- ###########################################################################################
	 CREATE TABLE Products
	(
		ProductID INT PRIMARY KEY,
		ProductNAME VARCHAR(255),
		Price DECIMAL(10, 2),
		AgeINMonths INT
	);

	INSERT INTO Products (ProductID, ProductNAME, Price, AgeINMonths) VALUES
	(1, 'Laptop', 1000.00, 5),
	(2, 'TABLEt', 450.00, 9),
	(3, 'Smartphone', 800.00, 15),
	(4, 'MonitOR', 300.00, 30);

	SELECT * FROM products


--dp=price - (price * dIS/100)

CREATE function DP(@price float, @dIS float)
returns float
 AS 
  begIN
	return @price - (@price * @dIS/100)
  end 



  
	SELECT *, dbo.dp(price, 15.80) AS newprice FROM products


-- ###########################################################################################
---conditional statement  
	if 1=1
		prINT'true'
	else
		prINT'false'
-- ###########################################################################################
	if 1=10
		prINT'true'
	else
		prINT'false'
-- ###########################################################################################





















-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################

Demo 09: 28-02-2025
-- ###########################################################################################






--TABLE valued  function,IF , IF ELSE ,VIEW, stored PROCEDURE,TCL, 
-- ###########################################################################################
CREATE DATABASE Demo 
USE Demo
CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Email VARCHAR(100)
);

CREATE TABLE PurchASes (
    PurchASeID INT PRIMARY KEY,
    CustomerID INT,
    PurchASeDATE DATE,
    Amount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

-- INSERTing customers
INSERT INTO Customer VALUES
(1, 'John', 'Doe', 'johndoe@email.com'),
(2, 'Jane', 'Smith', 'janesmith@email.com'),
(3, 'Alice', 'Johnson', 'alicejohnson@email.com'),
(4, 'Bob', 'Brown', 'bobbrown@email.com'),
(5, 'Carol', 'DavIS', 'caroldavIS@email.com'),
(6, 'David', 'Wilson', 'davidwilson@email.com'),
(7, 'Eve', 'TaylOR', 'evetaylOR@email.com'),
(8, 'Frank', 'MoORe', 'frankmoORe@email.com'),
(9, 'Grace', 'ANDerson', 'graceANDerson@email.com'),
(10, 'Hank', 'ThomAS', 'hankthomAS@email.com'),
(11, 'Irene', 'Edwards', 'ireneedwards@email.com'),
(12, 'Jerry', 'Mitchell', 'jerrymitchell@email.com'),
(13, 'Katie', 'RobINson', 'katierobINson@email.com'),
(14, 'LouIS', 'Walker', 'louISwalker@email.com'),
(15, 'Megan', 'Lee', 'meganlee@email.com'),
(16, 'Nancy', 'Hall', 'nancyhall@email.com'),
(17, 'Oscar', 'Young', 'oscaryoung@email.com'),
(18, 'Patty', 'King', 'pattyking@email.com'),
(19, 'QuINcy', 'Scott', 'quINcyscott@email.com'),
(20, 'Rachel', 'Wright', 'rachelwright@email.com');

-- INSERTing purchASes
INSERT INTO PurchASes VALUES
(1, 10, '2023-07-01', 2000.00),
(2, 1, '2023-07-02', 300.00),
(3, 2, '2023-07-01', 450.00),
(4, 3, '2023-07-01', 120.00),
(5, 3, '2023-07-02', 130.00),
(6, 3, '2023-07-03', 150.00),
(7, 4, '2023-07-01', 250.00),
(8, 5, '2023-07-01', 650.00),
(9, 5, '2023-07-02', 150.00),
(10, 6, '2023-07-01', 550.00),
(11, 6, '2023-07-02', 500.00),
(12, 7, '2023-07-01', 350.00),
(13, 8, '2023-07-01', 280.00),
(14, 9, '2023-07-01', 700.00),
(15, 9, '2023-07-02', 100.00),
(16, 10, '2023-07-01', 400.00),
(17, 11, '2023-07-01', 300.00),
(18, 12, '2023-07-01', 110.00),
(19, 13, '2023-07-01', 105.00),
(20, 14, '2023-07-01', 205.00);


SELECT * FROM customer
SELECT * FROM PurchASes
UPDATE PurchASes
 SET Amount =5000
 WHERE CustomerID=1

--Scenario Description:
--A retail company wants to implement a dynamic dIScount system WHERE customers get 
--dIScounts bASed on the total amount they have spent hIStORically. The dIScount IS calculated using a tiered system:
	--Customers who have spent over $5000 get a 15% dIScount on future purchASes.
	--Customers who have spent BETWEEN $1000 AND $5000 get a 10% dIScount.
	--Customers who have spent less than $1000 get a 5% dIScount.


	CREATE function getdIS(@id INT)
	returns float 
	AS
	begIN 
		DECLARE @spent  float , @dIS float 

		SELECT @spent=sum(amount) FROM PurchASes WHERE CustomerID=@id
		IF @SPENT > =5000
			SET @dIS=15
		ELSE IF @SPENT BETWEEN 1000 AND 5000
			SET @dIS=10	
		ELSE IF @SPENT<1000
			SET @dIS=5
		RETURN @DIS
	end 


	SELECT * , DBO.getdIS(CUSTOMERID)  AS dISCOUNT FROM PurchASes


-- ###########################################################################################
--Practice question 3
--healthcare system

CREATE TABLE Patient (
    PatientID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    DOB DATE
);

CREATE TABLE HealthMetrics (
    MetricID INT PRIMARY KEY,
    PatientID INT,
    MetricDATE DATE,
    BloodPressure INT,
    Cholesterol INT,
    Smoker BIT,
    FOREIGN KEY (PatientID) REFERENCES Patient(PatientID)
);
-- INSERTing patients
INSERT INTO Patient VALUES
(1, 'John', 'Doe', '1970-05-15'),
(2, 'Jane', 'Smith', '1982-07-20'),
(3, 'Alice', 'Johnson', '1990-11-01'),
(4, 'Bob', 'Brown', '1955-01-22'),
(5, 'Carol', 'DavIS', '1965-03-15'),
(6, 'David', 'Wilson', '1945-12-09'),
(7, 'Eve', 'TaylOR', '1975-04-05'),
(8, 'Frank', 'MoORe', '1985-05-19'),
(9, 'Grace', 'ANDerson', '1978-08-25'),
(10, 'Hank', 'ThomAS', '1968-09-30');

-- INSERTing health metrics
INSERT INTO HealthMetrics VALUES
(1, 1, '2023-07-10', 120, 190, 0),
(2, 2, '2023-07-11', 130, 200, 1),
(3, 3, '2023-07-12', 125, 180, 0),
(4, 4, '2023-07-13', 140, 220, 1),
(5, 5, '2023-07-14', 135, 210, 0),
(6, 6, '2023-07-15', 145, 230, 1),
(7, 7, '2023-07-16', 130, 195, 0),
(8, 8, '2023-07-17', 138, 205, 1),
(9, 9, '2023-07-18', 128, 198, 0),
(10, 10, '2023-07-19', 132, 207, 1);

Metric					GOod Range			Bad Range				NOTes
Age	-					-					> 50 years			Higher age INcreASes rISk, but no "GOod" range fOR age.
Blood Pressure (mmHg)	<= 120/80			> 130/80			VALUES above 130/80 are considered high.
Cholesterol (mg/dL)		< 200				> 200				High cholesterol INcreASes cardiovAScular rISk.
Smoker					No (0)				Yes (1)				Smoking IS a majOR rISk factOR fOR many dISeASes.

SELECT * FROM Patient
SELECT * FROM HealthMetrics

--Scenario Description:
--A healthcare system wants to ASsess patient rISk fOR cardiovAScular dISeASes bASed on 
--various parameters such AS age, blood pressure, cholesterol levels, AND smoking status.
--The rISk scORe will help healthcare providers priORitize INTerventions.
--TABLEs:
	--Patient: stores patient demographics AND identifiers.
	--HealthMetrics: Tracks health metrics fOR each patient over TIME.
	DECLARE @AGE  INT , @BP INT ,@CH INT , @SM INT 
	SELECT 
	@AGE= DATEDIFF(YEAR,DOB, GETDATE())  
	, @BP= BloodPressure 
	,@CH =Cholesterol, 
	@SM =Smoker
	FROM Patient P INNER JOIN  HealthMetrics H ON P.PatientID=H.PatientID
	WHERE P.PatientID= @ID 
	IF @AGE >50
		SET @sCORE =25 
	IF @BP 	>130
		SET @sCORE =SCORE +25
	IF @CH 	>200
		SET @sCORE =SCORE +25
	IF @SM 	=1
		SET @sCORE =SCORE +25

	RETURN @SCORE 

-- ###########################################################################################

--1. Healthcare Cost Calculation
--FORmula:TotalCost = BASeFee + MedicationFee + (BASeFee + MedicationFee) * TaxRate / 100


	CREATE TABLE PatientBills
	(
		BillID INT PRIMARY KEY,
		BASeFee DECIMAL(10,2),
		MedicationFee DECIMAL(10,2),
		TaxRate DECIMAL(5,2)
	);

	INSERT INTO PatientBills (BillID, BASeFee, MedicationFee, TaxRate) VALUES
	(1, 200, 50, 10),
	(2, 300, 75, 12),
	(3, 150, 25, 8),
	(4, 400, 100, 15),
	(5, 250, 60, 9);

--GOvernment Subsidy Calculation
--FORmula:SubsidyAmount = ServiceCost * SubsidyRate / 100

	CREATE TABLE HealthcareServices
	(
		ServiceID INT PRIMARY KEY,
		ServiceCost DECIMAL(10,2),
		SubsidyRate DECIMAL(5,2)
	);

	INSERT INTO HealthcareServices (ServiceID, ServiceCost, SubsidyRate) VALUES
	(1, 500, 20),
	(2, 800, 25),
	(3, 300, 15),
	(4, 1000, 30),
	(5, 750, 10);
	
--Taxation on Medical Devices
--FORmula:TaxAmount = DeviceCost * TaxPercentage / 100

	CREATE TABLE MedicalDevices
	(
		DeviceID INT PRIMARY KEY,
		DeviceNAME NVARCHAR(50),
		DeviceCost DECIMAL(10,2),
		TaxPercentage DECIMAL(5,2)
	);

	INSERT INTO MedicalDevices (DeviceID, DeviceNAME, DeviceCost, TaxPercentage) VALUES
	(1, 'X-Ray MachINe', 50000, 18),
	(2, 'MRI MachINe', 100000, 12),
	(3, 'UltrASound MachINe', 30000, 15),
	(4, 'VentilatOR', 75000, 10),
	(5, 'ECG MachINe', 20000, 5);

--INsurance Coverage Calculation
--FORmula:CoverageAmount = TotalBill * CoveragePercentage / 100

	CREATE TABLE INsuranceClaims
	(
		ClaimID INT PRIMARY KEY,
		TotalBill DECIMAL(10,2),
		CoveragePercentage DECIMAL(5,2)
	);

	INSERT INTO INsuranceClaims (ClaimID, TotalBill, CoveragePercentage) VALUES
	(1, 5000, 80),
	(2, 3000, 70),
	(3, 10000, 90),
	(4, 7500, 85),
	(5, 2500, 75);
--Monthly Premium Calculation
--FORmula:MonthlyPremium = AnnualPremium / Months
	CREATE TABLE HealthPlans
	(
		PlanID INT PRIMARY KEY,
		AnnualPremium DECIMAL(10,2),
		Months INT
	);

	INSERT INTO HealthPlans (PlanID, AnnualPremium, Months) VALUES
	(1, 1200, 12),
	(2, 2400, 24),
	(3, 3600, 36),
	(4, 4800, 48),
	(5, 6000, 60);
-- ###########################################################################################
--TABLE valued function 

/*syntax
	CREATE FUNCTION function_NAME (@parameter1 datatype [, @parameter2 datatype, ...])
	RETURNS DATATYPE
	AS
	RETURN (
				-- A single SELECT statement
				SELECT COLUMN1, COLUMN2, ...
				FROM TABLEs   WHERE conditions
			)

*/



CREATE TABLE Department
	(
	did INT,
	eNAME VARCHAR(50) ,
	gender VARCHAR(50) ,
	salary INT ,
	dept VARCHAR(50) 
	)

	GO
	INSERT INTO Department  VALUES
	(1, 'David', 'Male', 5000, 'Sales'),
	(5, 'Shane', 'Female', 5500, 'Finance'),
	(6, 'Shed', 'Male', 8000, 'Sales'),
	(7, 'Vik', 'Male', 7200, 'HR'),
	(2, 'Jim', 'Female', 6000, 'HR'),
	(13, 'Julie', 'Female', 7100, 'IT'),
	(14, 'Elice', 'Female', 6800,'Marketing'),
	(3, 'Kate', 'Female', 7500, 'IT'),
	(4, 'Will', 'Male', 6500, 'Marketing'),
	(10, 'Laura', 'Female', 6300, 'Finance'),
	(11, 'Mac', 'Male', 5700, 'Sales'),
	(12, 'Pat', 'Male', 7000, 'HR'),
	(8, 'VINce', 'Female', 6600, 'IT'),
	(9, 'Jane', 'Female', 5400, 'Marketing'),
	(15, 'Wayne', 'Male', 6800, 'Finance')

	GO
	SELECT *     FROM Department

--CREATE FUNCTION
	CREATE FUNCTION highsal(@id INT)
	RETURNS TABLE 
	AS 
	RETURN 
	(
		with highsal 
		AS 
		( 	SELECT *  , row_number() over( ORDER BY salary desc) AS rownum FROM Department )
		SELECT * FROM highsal WHERE rownum =@id
 )
 
 --CALL FUNCTION 
 SELECT * FROM DBO.highsal(1)


--CALL FUNCTION 
	 SELECT * FROM DBO.highsal( )

	 SELECT * FROM DBO.highsal(2)

	 SELECT * FROM DBO.highsal(3)


-- ###########################################################################################

--Scenario Description:
--The mobile carrier wants to help customers monitOR their usage agaINst their plan limits.
--The system will UPDATE the remaINing balance of mINutes after each call AND generate detailed repORts 
--showing their usage AND the remaINing mINutes.

--TABLEs:
--	Customer: stores customer INfORmation.
--	CallLogs: Tracks each call made by customers, INcluding duration, type, AND TIME of day.
--	CustomerPlans: Details about each customer's plan, INcluding total mINutes available.
	CREATE TABLE Customer (
		CustomerID INT PRIMARY KEY,
		FirstName VARCHAR(100),
		LastName VARCHAR(100),
		PhoneNumber VARCHAR(15),
		PlanID INT
	);

	CREATE TABLE CallLogs (
		LogID INT PRIMARY KEY,
		CustomerID INT,
		CallDATE DATE,
		CallTIME TIME,
		DurationMINutes INT,
		DestINationType VARCHAR(50), -- 'Local', 'INTernational', 'Premium'
		FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
	);

	CREATE TABLE CustomerPlans (
		PlanID INT PRIMARY KEY,
		TotalMINutes INT, -- Total mINutes available IN the plan
		RemaINingMINutes INT -- MINutes remaINing after calls
	);


	INSERT INTO Customer VALUES
	(1, 'John', 'Doe', '123-456-7890', 1),
	(2, 'Jane', 'Smith', '234-567-8901', 2),
	(3, 'Alice', 'Johnson', '345-678-9012', 3),
	(4, 'Bob', 'MartIN', '456-789-0123', 4),
	(5, 'CHARlie', 'Garcia', '567-890-1234', 5),
	(6, 'Diana', 'Clark', '678-901-2345', 6),
	(7, 'Evan', 'Rodriguez', '789-012-3456', 7),
	(8, 'Fiona', 'Lopez', '890-123-4567', 8),
	(9, 'GeORge', 'HarrIS', '901-234-5678', 9),
	(10, 'Hannah', 'Lee', '012-345-6789', 10);


	INSERT INTO CallLogs VALUES
	(1, 1, '2023-07-01', '10:00:00', 30, 'Local'),
	(2, 1, '2023-07-01', '15:00:00', 45, 'INTernational'),
	(3, 2, '2023-07-01', '09:00:00', 5, 'Premium'),
	(4, 2, '2023-07-02', '21:00:00', 60, 'Local'),
	(5, 3, '2023-07-03', '14:00:00', 25, 'INTernational'),
	(6, 3, '2023-07-04', '16:00:00', 30, 'Local'),
	(7, 4, '2023-07-04', '17:00:00', 15, 'Premium'),
	(8, 4, '2023-07-05', '18:00:00', 20, 'Local'),
	(9, 5, '2023-07-05', '19:00:00', 35, 'INTernational'),
	(10, 5, '2023-07-06', '20:00:00', 40, 'Local'),
	(11, 6, '2023-07-06', '08:00:00', 10, 'Premium'),
	(12, 6, '2023-07-07', '22:00:00', 50, 'INTernational'),
	(13, 7, '2023-07-07', '23:00:00', 55, 'Local'),
	(14, 7, '2023-07-08', '12:00:00', 60, 'Premium'),
	(15, 8, '2023-07-08', '13:00:00', 45, 'INTernational'),
	(16, 8, '2023-07-09', '14:00:00', 25, 'Local'),
	(17, 9, '2023-07-09', '15:00:00', 5, 'Premium'),
	(18, 9, '2023-07-10', '10:00:00', 30, 'INTernational'),
	(19, 10, '2023-07-10', '11:00:00', 15, 'Local'),
	(20, 10, '2023-07-11', '12:00:00', 20, 'Premium');

	INSERT INTO CustomerPlans VALUES
	(1, 1000, 925),   
	(2, 500, 375),
	(3, 1500, 1395),
	(4, 800, 725),
	(5, 1200, 1085),
	(6, 300, 240),
	(7, 400, 280),
	(8, 750, 630),
	(9, 600, 550),
	(10, 1000, 965);



	SELECT * FROM Customer
	SELECT * FROM CallLogs
	SELECT * FROM CustomerPlans
--Scenario Description:
--The mobile carrier wants to help customers monitOR their usage agaINst their plan limits.
--The system will UPDATE the remaINing balance of mINutes after each call AND generate detailed repORts 
--showing their usage AND the remaINing mINutes.

--TABLEs:
--	Customer: stores customer INfORmation.
--	CallLogs: Tracks each call made by customers, INcluding duration, type, AND TIME of day.
--	CustomerPlans: Details about each customer's plan, INcluding total mINutes available.



;LOCAL .5
INTERNATIONAL .20
pREMIUM .50

	CREATE  function carrier(@id INT )
	returns TABLE 
	AS
	return 
	(
		SELECT cl.CallDATE,cl.CallTIME,cl.DurationMINutes,cl.DestINationType,
		cASe
			when cl.DestINationType='LOCAL' then cl.DurationMINutes *.5
			when cl.DestINationType='INTERNATIONAL' then cl.DurationMINutes*.20
			when cl.DestINationType='Premium' then cl.DurationMINutes *.50 
		end AS callcost
		FROM Customer  cc INNER JOIN CallLogs  CL on cc.CustomerID=cl.CustomerID
		INNER JOIN CustomerPlans CP  on cc.PlanID= cp.PlanID
		WHERE cc.CustomerID=@id 

	)

	SELECT * FROM carrier(1)



-- ###########################################################################################
-- ###########################################################################################
--SQl server views
--Virtual TABLEs
	/*Syntax:
			CREATE view viewNAME 
			AS 
			SELECT statement
	*/


SELECT did,eNAME,gender,salary,dept  FROM Department

SELECT did,eNAME,dept  FROM Department

--CREATE view 
	CREATE view vw_read
	AS
	SELECT did,eNAME,dept  FROM Department

--call view 
	SELECT * FROM vw_read
  SELECT * FROM Department


--PerfORm operation on TABLE 

	DELETE FROM Department
	
	INSERT INTO Department  VALUES
	  (1, 'David', 'Male', 5000, 'Sales'),
	  (5, 'Shane', 'Female', 5500, 'Finance'),
	  (6, 'Shed', 'Male', 8000, 'Sales'),
	  (7, 'Vik', 'Male', 7200, 'HR'),
	  (2, 'Jim', 'Female', 6000, 'HR'),
	  (13, 'Julie', 'Female', 7100, 'IT'),
	  (14, 'Elice', 'Female', 6800,'Marketing'),
	  (3, 'Kate', 'Female', 7500, 'IT'),
	  (4, 'Will', 'Male', 6500, 'Marketing'),
	  (10, 'Laura', 'Female', 6300, 'Finance'),
	  (11, 'Mac', 'Male', 5700, 'Sales'),
	  (12, 'Pat', 'Male', 7000, 'HR'),
	  (8, 'VINce', 'Female', 6600, 'IT'),
	  (9, 'Jane', 'Female', 5400, 'Marketing'),
	  (15, 'Wayne', 'Male', 6800, 'Finance')

	  UPDATE Department SET eNAME ='UNKNOWN'


--PerfORm operation on VIEW 
	DELETE FROM vw_read

	INSERT INTO vw_read  VALUES
	(1, 'David',  'Sales'),
	(5, 'Shane', 'Finance'),
	(6, 'Shed', 'Sales'),
	(7, 'Vik',  'HR'),
	(2, 'Jim', 'HR')

	UPDATE VW_READ SET DEPT ='sql'




--call view 
	SELECT * FROM vw_read
  SELECT * FROM Department


--DROP TABLE department 
	DROP TABLE department 


--Could NOT USE view OR function 'vw_read' becaUSE of bINding errORs.




--View 1 
	CREATE view USErINfo
	AS 
	SELECT PP.BusinessEntityID AS Empid,FirstName,LastName
	,NationalIDNumber,JobTitle,BirthDATE,Gender,HireDATE,LogINID
	FROM AdventureWorks2022.Person.Person PP INner joIN 
	AdventureWorks2022.HumanResources.Employee HE
	on PP.BusinessEntityID=HE.BusinessEntityID

	SELECT * FROM USErINfo

--View 2
 
	CREATE view ADDINfo
	AS 
	SELECT BusinessEntityID,ADDressLINe1,City,PostalCode 	FROM 
	AdventureWorks2022.Person.ADDress PA INner joIN 
	AdventureWorks2022.Person.BusINessEntityADDress PB
	on PA.ADDressID=PB.ADDressID
	
	SELECT * FROM ADDINfo
--JoIN View  1 & 2
	CREATE view empINfo 
	AS

	SELECT * FROM USErINfo INner joIN ADDINfo
	on Empid=BusinessEntityID


	SELECT * FROM empINfo









 
-- ###########################################################################################
 
	CREATE TABLE Sales (SaleID INT PRIMARY KEY,SaleDATE DATE,Amount DECIMAL(10, 2)	);
	   	 
	INSERT INTO Sales (SaleID, SaleDATE, Amount) VALUES
	(21, '2024-01-01', NULL),
	(2, '2024-01-01', 150.50),
	(3, '2024-01-02', 120.00),
	(4, '2024-01-02', 80.00),
	(5, '2024-01-03', 200.00),
	(6, '2024-01-03', 50.00),
	(7, '2024-01-04', 75.00),
	(8, '2024-01-04', 125.50),
	(9, '2024-01-05', 180.00),
	(10, '2024-01-05', 90.00),
	(11, '2024-01-06', 60.00),
	(12, '2024-01-06', 110.00),
	(13, '2024-01-07', 100.00),
	(14, '2024-01-07', 130.00),
	(15, '2024-01-08', 85.00),
	(16, '2024-01-08', 145.00),
	(17, '2024-01-09', 95.00),
	(18, '2024-01-09', 105.00),
	(19, '2024-01-10', 250.00),
	(20, '2024-01-10', 100.00);

	CREATE  view vw_INDEX WITH SCHEMABINDing
	AS
	SELECT SaleDATE, count_big(*) AS counts, sum(ISNULL(amount,0)) AS Amount 
	FROM dbo.Sales GROUP BY SaleDATE


	SELECT * FROM vw_INDEX
--DROP TABLE 
	DROP TABLE Sales 

--Could NOT USE view OR function 'vw_INDEX' becaUSE of bINding errORs.


SELECT * FROM vw_INDEX

--IMPROVE SPEED OF VIEW (ADD INDEX)
CREATE UNIQUE CLUSTERED  INDEX VW_ID ON vw_INDEX(SALEDATE)


SELECT * FROM vw_INDEX

-- ###########################################################################################
--conditional statement  
	if 1=1
		prINT'true'
	else
		prINT'false'
-- ###########################################################################################
	if 1=2
		prINT'true'
	else
		prINT'false'
-- ###########################################################################################

	if 'a'='A'
		prINT'true'
	else
		prINT'false'
-- ###########################################################################################

	if 1=18
		prINT'true1'
	else if 12=1
		prINT'true2'
	else if 1=1
		prINT'true3'
	else if 1=1
		prINT'true4'
	else if 1=1
		prINT'true5'
	else
		prINT'false' 

-- ###########################################################################################
	DECLARE @stock INT =500
	if @stock >100
		prINT'stock IS high '
	else
		prINT'stock IS low '
		-- ######################
	DECLARE @action VARCHAR(20)
	SET @action ='INSERTs'	

	if @action ='INSERT' 
		prINT'True-INSERT '
	else if @action ='UPDATE' 
		prINT'True UPDATE '
	else if @action ='DELETE' 
		prINT'True DELETE '
	else if @action ='SELECT' 
		prINT'True SELECT '
	else
		prINT'False, INvalid action'

-- ###########################################################################################
--logic (SELECT,INSERT, UPDATE , DELETE )
--stored procedure 

--perfORmance , security ,maINTaIN
/*Syntax:
	CREATE PROCEDURE procedure_NAME   
		@parameter1 datatype [= default] [OUTPUT],
		@parameter2 datatype [= default] [OUTPUT],
    ...
	AS
	BEGIN
		-- SQL statements here(INSERT, SELECT , UPDATE, DELETE )
	END;
*/

--CREATE PROCEDURE

	CREATE PROCEDURE sp_dep
	AS 
	SELECT * FROM department

--call PROCEDURE
	exec sp_dep



--ALTER PROCEDURE

	ALTER PROCEDURE sp_dep @id INT
	AS 
	SELECT * FROM department WHERE did =@id

--call PROCEDURE
	exec sp_dep @id =15

	exec sp_dep  11

	exec sp_dep 1


--CREATE PROCEDURE

	CREATE PROCEDURE sp_view
	AS 
	SELECT * FROM [dbo].[empINfo]

exec sp_view


--CREATE PROCEDURE

	ALTER PROCEDURE sp_view @eid INT
	AS 
	SELECT * FROM [dbo].[empINfo] WHERE empid =@eid



exec sp_view @eid =192
exec sp_view @eid =166
exec sp_view @eid =112


-- ###########################################################################################




--CREATE TABLE
	CREATE TABLE USErdata (id INT , eNAME VARCHAR(20), age  INT)
	
--logic (SELECT,INSERT, UPDATE , DELETE )

	CREATE procedure sp_auto
	@action VARCHAR(20),@id INT=NULL , @eNAME VARCHAR(20)=NULL, @age  INT =NULL
	AS
	begIN 
		if @action ='INSERT' 
			begIN 
				INSERT INTO USErdata VALUES (@id, @eNAME,@age)
			end 
		else if @action ='UPDATE' 
			begIN 
				UPDATE USErdata SET eNAME=@eNAME,age=@age WHERE id =@id 
			end 
		else if @action ='DELETE' 
			begIN 
				DELETE FROM USErdata  WHERE id =@id 
			end 
		else if @action ='SELECT' 
			begIN 
				SELECT * FROM USErdata  WHERE id =@id 
			end
		else
			prINT'False, INvalid action' 
	end
--call stored procedure
	exec sp_auto @action ='SELECT'   ,@id =103
	
	exec sp_auto @action ='INSERT' ,@id =101 , @eNAME ='alpha', @age= 31

	exec sp_auto 'INSERT' , 102 ,  'beta',  32
	
	exec sp_auto [INSERT] , 103 ,   fox ,  33


	exec sp_auto [UPDATE] , 103 ,   john ,  64
	
	exec sp_auto [DELETE] , 102


-- ###########################################################################################
--TCL Transaction Control Language 
	--Save		Commit
	--dont'save	Rollback 

SELECT * FROM department


	BEGIN TRAN --START TRANSACTIN

			--SQL LOGIC

	Commit		--Save		
	Rollback	--dont'save

--Scenario
	BEGIN TRAN --START TRANSACTIN
	--Completion TIME: 2025-03-01T02:13:21.4734654-05:00

	
	SELECT * FROM department

	DELETE FROM department WHERE gender ='Female'
	UPDATE department SET dept ='unknown' , salary =99999
	 	
	Rollback	--dont'save

--Scenario
	BEGIN TRAN --START TRANSACTIN
 
	
		TRUNCATE TABLE  department
	
		SELECT * FROM department

	Rollback	--dont'save


--mINimal logged tran

--Scenario
	BEGIN TRAN --START TRANSACTIN 
	SELECT * FROM department

	DELETE FROM department WHERE gender ='Female'
	UPDATE department SET dept ='unknown' , salary =99999
	 	
	rollback	--dont'save




















-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################
-- ###########################################################################################

Demo 10: 01-03-2025
-- ###########################################################################################









--SQl server DML trigger , exception hANDling , cASes,
-- ###########################################################################################
CREATE DATABASE  SQLDEMO
	GO
	USE SQLDEMO
	GO

	CREATE TABLE Department
	  (
		  did INT,
		  eNAME VARCHAR(50) ,
		  gender VARCHAR(50) ,
		  salary INT ,
		  dept VARCHAR(50) 
	   )

	GO
		INSERT INTO Department  VALUES
	  (1, 'David', 'Male', 5000, 'Sales'),
	  (5, 'Shane', 'Female', 5500, 'Finance'),
	  (6, 'Shed', 'Male', 8000, 'Sales'),
	  (7, 'Vik', 'Male', 7200, 'HR'),
	  (2, 'Jim', 'Female', 6000, 'HR'),
	  (13, 'Julie', 'Female', 7100, 'IT'),
	  (14, 'Elice', 'Female', 6800,'Marketing'),
	  (3, 'Kate', 'Female', 7500, 'IT'),
	  (4, 'Will', 'Male', 6500, 'Marketing'),
	  (10, 'Laura', 'Female', 6300, 'Finance'),
	  (11, 'Mac', 'Male', 5700, 'Sales'),
	  (12, 'Pat', 'Male', 7000, 'HR'),
	  (8, 'VINce', 'Female', 6600, 'IT'),
	  (9, 'Jane', 'Female', 5400, 'Marketing'),
	  (15, 'Wayne', 'Male', 6800, 'Finance')

	GO
	  SELECT * FROM Department
-- ###########################################################################################
--Trigger IN SQL server (event  --> Action  IS perfORmed)

--DML(INSERT, UPDATE , DELETE)	--> Data --> TABLE


--Two logical trigger IN DML trigger 
		--INSERTed (ADD a new records,new INfo will be records)
		--DELETEd (removal old recORd,old INfo  will be records )
	/*
		Syntax:
			CREATE trigger TriggerNAME 
			on TABLENAME 
			fOR INSERT, UPDATE, DELETE
			AS 
			begIN 
				--sql logic 
			end
	*/


-- freeze chnages 	--02-03-2025 (i, u, d)
	CREATE trigger TG_freeze 
	on department  
	fOR INSERT, UPDATE, DELETE
	AS 
		begIN 
			if GETDATE()<'03-03-2025'
			begIN 
				prINT 'all changes have been freezed'
				rollback
			end 
		end


	INSERT INTO Department  VALUES
	  (1, 'David', 'Male', 5000, 'Sales'),
	  (5, 'Shane', 'Female', 5500, 'Finance')

	DELETE FROM Department
	  
 
	  SELECT * FROM Department

-- Enable/ dISable a trigger
	--Enable TRIGGER trigger_NAME ON TABLE_NAME;
	--DISABLE TRIGGER trigger_NAME ON TABLE_NAME;
	Enable TRIGGER TG_freeze ON Department;
	DISABLE TRIGGER TG_freeze ON Department;

-- ###########################################################################################
--Trigger copy data FROM 1 TABLE to aNOTher TABLE
	SELECT * FROM Department

	CREATE TABLE DepthISt
	(
		sno INT identity(1,1),
		TIMEstamps DATETIME default  GETDATE(),
		logINNAME VARCHAR(20) default sUSEr_NAME(),
		DMLOPS VARCHAR(20),

		new_did INT,
		new_eNAME VARCHAR(50) ,
		new_gender VARCHAR(50) ,
		new_salary INT ,
		new_dept VARCHAR(50) ,
		
		old_did INT,
		old_eNAME VARCHAR(50) ,
		old_gender VARCHAR(50) ,
		old_salary INT ,
		old_dept VARCHAR(50) 
	)



--CREATE trigger INSERT 
	CREATE trigger TG_INSERT 
	on department  
	fOR INSERT 
	AS 
		begIN 
			INSERT INTO DepthISt(DMLOPS,new_did,new_eNAME,new_gender,new_salary,new_dept,old_did,old_eNAME,old_gender,old_salary,old_dept)
			SELECT 'INSERT',did,eNAME,gender,salary,dept, NULL, NULL, NULL, NULL, NULL FROM INSERTed
		end


--PerfORm INSERT
	INSERT INTO Department  VALUES
	  (1, 'David', 'Male', 5000, 'Sales'),
	  (5, 'Shane', 'Female', 5500, 'Finance'),
	  (6, 'Shed', 'Male', 8000, 'Sales'),
	  (7, 'Vik', 'Male', 7200, 'HR'),
	  (2, 'Jim', 'Female', 6000, 'HR')





--CREATE trigger DELETE 
	CREATE trigger TG_DELETE
	on department  
	fOR DELETE 
	AS 
		begIN 
			INSERT INTO DepthISt(DMLOPS,new_did,new_eNAME,new_gender,new_salary,new_dept,old_did,old_eNAME,old_gender,old_salary,old_dept)
			SELECT 'DELETE', NULL, NULL, NULL, NULL, NULL,did,eNAME,gender,salary,dept FROM DELETEd
		end

	SELECT * FROM Department

	SELECT * FROM  DepthISt

DELETE FROM DEPARTMENT WHERE gender='male'





--CREATE trigger UPDATE 
	CREATE trigger TG_UPDATE
	on department  
	fOR UPDATE 
	AS 
		begIN 
			INSERT INTO DepthISt(DMLOPS,new_did,new_eNAME,new_gender,new_salary,new_dept,old_did,old_eNAME,old_gender,old_salary,old_dept)
			SELECT 'UPDATE', i.did, i.eNAME, i.gender, i.salary, i.dept,d.did,d.eNAME,d.gender,d.salary,d.dept 
			FROM DELETEd d INner joIN INSERTed i on i.did=d.did
		end

UPDATE DEPARTMENT SET SALARY =11111111 , DEPT='unknown'

-- ###########################################################################################
--DDL trigger (CREATE_TABLE, ALTER_TABLE, DROP_TABLE)

--XML datatype IN SQL server --EVENTDATA()

	/*
	Syntax:
		CREATE trigger TriggerNAME 
		on DATABASE 
		fOR CREATE_TABLE, ALTER_TABLE, DROP_TABLE
		AS 
		--sql logic 
	*/

	--sql logic 

--CREATE TABLE DDL LOGS 

--CREATE TABLE 
	CREATE TABLE DDLLOGS (sno INT identity, eventss xml )


	CREATE trigger TG_monddl 
	on DATABASE 
	fOR CREATE_TABLE, ALTER_TABLE, DROP_TABLE
	AS 
	begIN 
		INSERT INTO DDLLOGS VALUES(EVENTDATA())
	end 


-- ###########################################################################################
--PerfORm DDL operation
--CREATE TABLE
	CREATE TABLE test	(id INT , age INT, ph INT)

--ALTER TABLE 
	ALTER TABLE test DROP COLUMN id

--DROP TABLE 
	DROP TABLE test

SELECT * FROM DDLLOGS




-- ###########################################################################################
-- USEr NOT allowed to CREATE a TABLE which hAS NAME = temp
	CREATE trigger checktbl
	on DATABASE 
	fOR CREATE_TABLE, ALTER_TABLE, DROP_TABLE 
	AS 
		begIN 

		DECLARE @tblnme VARCHAR(30)
		SET @tblnme=eventdata().value('(/EVENT_INSTANCE/ObjectNAME)[1]','VARCHAR(20)')
		if @tblnme LIKE '%temp%'
			begIN 
				prINT 'USEr NOT allowed to CREATE TABLE AS TEMP'
				rollback
			end
		end
--CREATE TABLE
	CREATE TABLE temp	(id INT , age INT, ph INT)

	CREATE TABLE q2131temp312312cAS	(id INT , age INT, ph INT)


-- ###########################################################################################
--Exception /ErrOR hANDling (ErrOR related function)
SELECT errOR_message(), errOR_lINe(), errOR_state(), errOR_Severity(),errOR_procedure(),errOR_number()

--ScenASrios ErrOR hANDling 
	SELECT * FROM Department 
--ScenASrios ErrOR hANDling 
	SELECT 1/0
--ScenASrios ErrOR hANDling 
	CREATE TABLE demo101
	(id INT identity , phnum INT UNIQUE)

	INSERT INTO demo101
	VALUES (3467)

	SELECT * FROM demo101
--ScenASrios ErrOR hANDling 

	SELECT * FROM sys.messages WHERE message_id =2627



--ErrOR hANDling 
	BegIN Try
			--SQL stmt
	end Try

	BegIN Catch
			--generate ErrORs
			--Write to TABLE
	end Catch

	

--ErrOR hANDling 
	BegIN Try
		--ScenASrios ErrOR hANDling 
		SELECT 1/0
	end Try

	BegIN Catch
			--generate ErrORs
			prINT 'errOR related to calculations'
	end Catch


--ErrOR hANDling 
	BegIN Try
		--ScenASrios ErrOR hANDling 
		INSERT INTO demo101 	VALUES (3467)

	end Try

	BegIN Catch
			--generate ErrORs
			prINT 'errOR related to duplicate entries'
	end Catch


--ErrOR hANDling 
	BegIN Try
		--ScenASrios ErrOR hANDling 
		SELECT 1/0
	end Try

	BegIN Catch
			--generate ErrORs
			SELECT errOR_message(), errOR_lINe(), errOR_state(), errOR_Severity(),errOR_procedure(),errOR_number()

	end Catch

-- ###########################################################################################
	CREATE TABLE errORlog
		(	sno INT identity(1,1),
			TIMEstamps VARCHAR(100) default GETDATE(),
			ERRORLINE VARCHAR(200),
			ERRORMESSAGE VARCHAR(200),
			ERRORNUMBER VARCHAR(200), 
			ERRORSTATE VARCHAR(200),
			ERRORSEVERITY VARCHAR(200), 
			ERRORPROCEDURE VARCHAR(200)
			)


--ErrOR hANDling 
	BegIN Try
		--ScenASrios ErrOR hANDling 
		SELECT 1/0
	end Try

	BegIN Catch
			INSERT INTO errORlog(ERRORLINE,ERRORMESSAGE,ERRORNUMBER,ERRORSTATE,ERRORSEVERITY,ERRORPROCEDURE) 
			VALUES( ERROR_LINE(),ERROR_MESSAGE(),ERROR_NUMBER(),ERROR_STATE(),ERROR_SEVERITY(),ERROR_PROCEDURE())
			
	end Catch


	SELECT * FROM errORlog

--ErrOR hANDling 
	BegIN Try
			--ScenASrios ErrOR hANDling 
		INSERT INTO demo101 	VALUES (3467)

	end Try

	BegIN Catch
			INSERT INTO errORlog(ERRORLINE,ERRORMESSAGE,ERRORNUMBER,ERRORSTATE,ERRORSEVERITY,ERRORPROCEDURE) 
			VALUES( ERROR_LINE(),ERROR_MESSAGE(),ERROR_NUMBER(),ERROR_STATE(),ERROR_SEVERITY(),ERROR_PROCEDURE())
			
	end Catch


-- ###########################################################################################


--CASes IN SQL server
/*
	CASE
		WHEN condition1 THEN result1
		WHEN condition2 THEN result2
		WHEN condition3 THEN result3
		WHEN condition1 THEN result4
		WHEN condition2 THEN result5
		WHEN condition3 THEN result6
		...
		ELSE default_result
	END
*/


	  SELECT did,eNAME,gender,dept,salary,
	  IIF(SALARY >6500, 'GOOD SAL', 'BAD SAL') AS COMMENTS
	  FROM Department ORDER BY salary ASC



	  SELECT did,eNAME,gender,dept,salary
	  
	  FROM Department


	  
	  
	  SELECT did,eNAME,gender,dept,salary,
	  CASE 
		when salary <=5000 then 'INcrement 50 %'
		when salary BETWEEN 5001 AND 6500 then 'INcrement 40 %'
		when salary BETWEEN 6501 AND 7000 then 'INcrement 30 %'
		when salary BETWEEN 7001 AND 7500  then 'INcrement 20 %'
		when salary >=7501 then 'INcrement 10 %'
		else 'salary =6000'
	  END AS Comments
	  FROM Department ORDER BY salary ASC

	  
	  SELECT did,eNAME,gender,dept,salary,
	  CASE 
		when salary <=5000 then salary*1.5
		when salary BETWEEN 5001 AND 6500 then salary*1.4
		when salary BETWEEN 6501 AND 7000 then  salary*1.3
		when salary BETWEEN 7001 AND 7500  then salary*1.2
		when salary >=7501 then  salary*1.1
		else  6000
	  END AS Comments
	  FROM Department ORDER BY salary ASC
	   

	  UPDATE Department
	  SET salary=CASE 
					when salary <=5000 then salary*1.5
					when salary BETWEEN 5001 AND 6500 then salary*1.4
					when salary BETWEEN 6501 AND 7000 then  salary*1.3
					when salary BETWEEN 7001 AND 7500  then salary*1.2
					when salary >=7501 then  salary*1.1
					else  6000
				  END 


				SELECT * FROM Department








-- SQL MANDatORy ASsignment 1: Gaurav Singh (grv08singh@gmail.com)

CREATE DATABASE ASsignment1;
USE ASsignment1;

--Creating Pre-requISite TABLEs AND INSERTing data AS per ASsignment
DROP TABLE Salesman;

CREATE TABLE Salesman (SalesmanId INT,NAME VARCHAR(255),CommISsion DECIMAL(10, 2),City VARCHAR(255),Age INT);
INSERT INTO Salesman (SalesmanId, NAME, CommISsion, City, Age) VALUES
(101, 'Joe', 50, 'CalifORnia', 17),
(102, 'Simon', 75, 'TexAS', 25),
(103, 'Jessie', 105, 'FlORida', 35),
(104, 'Danny', 100, 'TexAS', 22),
(105, 'Lia', 65, 'New Jersey', 30);

DROP TABLE Customer;

CREATE TABLE Customer (SalesmanId INT,CustomerId INT,CustomerNAME VARCHAR(255),PurchASeAmount INT);
INSERT INTO Customer (SalesmanId, CustomerId, CustomerNAME, PurchASeAmount)VALUES
(101, 2345, 'ANDrew', 550),
(103, 1575, 'Lucky', 4500),
(104, 2345, 'ANDrew', 4000),
(107, 3747, 'Remona', 2700),
(110, 4004, 'Julia', 4545);

DROP TABLE ORders;

CREATE TABLE ORders (ORderId INT, CustomerId INT, SalesmanId INT, ORderDATE DATE, Amount money);
INSERT INTO ORders VALUES
(5001,2345,101,'2021-07-01',550),
(5003,1234,105,'2022-02-15',1500);

-- Fetching Raw Data
SELECT * FROM Salesman;
SELECT * FROM Customer;
SELECT * FROM ORders;

-- TASks to be perfORmed



-- TASk 1) INSERT a new recORd IN your ORders TABLE.
INSERT INTO ORders VALUES (5005,3747,104,'2023-09-05',337);




-- TASk 2) 
-- 2.1) ADD Primary key constraINT fOR SalesmanId COLUMN IN Salesman TABLE. 
-- ADDing NOT NULL constraINT befORe making the PRIMARY KEY
ALTER TABLE Salesman ALTER COLUMN SalesmanId INT NOT NULL;

-- Making PRIMARY KEY: two ways
ALTER TABLE Salesman ADD CONSTRAINT PK_SalesmanId PRIMARY KEY(SalesmanId);
-- OR
ALTER TABLE Salesman ADD PRIMARY KEY(SalesmanId);

-- 2.2) ADD default constraINT fOR City COLUMN IN Salesman TABLE.
ALTER TABLE Salesman ADD CONSTRAINT DF_city DEFAULT 'No_City' FOR city;

-- 2.3) ADD FOReign key constraINT fOR SalesmanId COLUMN IN Customer TABLE.
-- ADDing data fOR referential INTegrity
INSERT INTO Salesman (SalesmanId, NAME, CommISsion, City, Age) VALUES
(107, 'MAX', 33, 'NYC', 24),
(110, 'Stallion', 25, 'WDC', 27);

-- Creating FOReign key
ALTER TABLE Customer ADD FOREIGN KEY (SalesmanId) REFERENCES Salesman(SalesmanId);
-- OR
ALTER TABLE ORders ADD CONSTRAINT FK_SalesmanId FOREIGN KEY (SalesmanId) REFERENCES Salesman(SalesmanId);

-- 2.4) ADD NOT NULL constraINT IN Customer_NAME COLUMN fOR the Customer TABLE.
ALTER TABLE Customer ALTER COLUMN CustomerNAME VARCHAR(255) NOT NULL;





-- TASk 3) Fetch the data WHERE the Customer’s NAME IS ending with ‘N’ also get the purchASe amount value greater than 500.
SELECT * FROM Customer WHERE CustomerNAME LIKE '%n';
SELECT * FROM Customer WHERE PurchASeAmount > 500;
SELECT * FROM Customer WHERE CustomerNAME LIKE '%n' AND PurchASeAmount > 500;




-- TASk 4) 
-- 4.1) Using SET operatORs, retrieve the first result with UNIQUE SalesmanId VALUES FROM two TABLEs
SELECT DISTINCT SalesmanId FROM Customer
UNION
SELECT DISTINCT SalesmanId FROM Salesman;

-- 4.2) Using SET operatORs, retrieve the 2nd result contaINing SalesmanId with duplicates FROM two TABLEs.
SELECT DISTINCT SalesmanId FROM Customer
UNION ALL
SELECT DISTINCT SalesmanId FROM Salesman;





-- TASk 5) DISplay the below COLUMNs which hAS the matching data.
--         ORderDATE, Salesman NAME, Customer NAME, CommISsion, AND 
--         City which hAS the range of PurchASe Amount BETWEEN 500 to 1500.
SELECT DIStINct(o.ORderId),o.ORderDATE, s.NAME AS salesman_NAME, c.CustomerNAME, s.CommISsion, s.City
	FROM ORders o
	INNER JOIN Salesman s ON o.SalesmanId = s.SalesmanId
	INNER JOIN Customer c ON o.CustomerId = c.CustomerId
	WHERE o.Amount >= 500 AND o.Amount <= 1500;





-- TASk 6) Using right joIN fetch all the results FROM Salesman AND ORders TABLE.
SELECT * FROM Salesman s
	RIGHT JOIN ORders o
	ON s.SalesmanId = o.SalesmanId;






-- SQL MANDatORy ASsignment 2: Gaurav Singh (grv08singh@gmail.com)

CREATE DATABASE ASsignment2;
USE ASsignment2;


-- DatASET: Jomato
-- About the datASET:
-- You wORk fOR a data analytics company, AND your client IS a food delivery platfORm similar to
-- Jomato. They have provided you with a datASET contaINing INfORmation about various
-- restaurants IN a city. Your tASk IS to analyze thIS datASET using SQL queries to extract valuable
-- INsights AND generate repORts fOR your client.
-- 
-- TASks to be perfORmed:
-- ImpORting the csv FLAT FILE Jomato
SELECT * FROM [dbo].[Jomato];




-- TASk 1. CREATE a USEr-defINed functions to stuff the Chicken INTO ‘Quick Bites’. 
-- Eg: ‘Quick Chicken Bites’.
DROP FUNCTION stuff_wORd;

CREATE FUNCTION stuff_wORd(@phrASe VARCHAR(255), @wORd VARCHAR(50))
RETURNS VARCHAR(255)
AS
BEGIN
	RETURN STUFF(@phrASe,CHARINDEX(' ',@phrASe,1),0,CONCAT(' ', @wORd))
END;


SELECT dbo.stuff_wORd('Quick Bites','Chicken');
SELECT dbo.stuff_wORd('Once a TIME','upon');





-- TASk 2. USE the function to dISplay the restaurant NAME AND cuISINe type which hAS the
-- MAXimum number of rating.

SELECT TOP 1 [RestaurantNAME], [CuISINesType]  FROM Jomato ORDER BY [No_of_Rating] DESC;





-- TASk 3. CREATE a Rating Status COLUMN to dISplay the rating AS ‘Excellent’ if it hAS mORe the 4
-- start rating, ‘GOod’ if it hAS above 3.5 AND below 5 star rating, ‘Average’ if it IS above 3
-- AND below 3.5 AND ‘Bad’ if it IS below 3 star rating.


ALTER TABLE Jomato ADD Rating_Status VARCHAR(20);
UPDATE Jomato SET Rating_Status = 
	CASE 
		WHEN [Rating] >= 4 THEN 'Excellent'
		WHEN [Rating] >= 3.5 THEN 'GOod'
		WHEN [Rating] >= 3 THEN 'Average'
		ELSE 'Bad'
	END;



-- TASk 4. FINd the Ceil, floOR AND absolute VALUES of the rating COLUMN AND dISplay the current DATE
-- AND separately dISplay the year, month_NAME AND day.
SELECT Rating, CEILing(Rating) AS CEIL, FLOOR(Rating) AS FLOOR, ABS(Rating) ABSOLUT FROM Jomato;

SELECT GETDATE() AS DATE, YEAR(GETDATE()) AS YEAR, DATENAME(MONTH,GETDATE()) AS MONTH, DAY(GETDATE()) AS DAY ;
OR
SELECT GETDATE() AS DATE, DATEPART(YEAR,GETDATE()) AS YEAR, DATENAME(MONTH,GETDATE()) AS MONTH, DATEPART(DAY,GETDATE()) AS DAY ;



-- TASk 5. DISplay the restaurant type AND total average cost using rollup.
SELECT COALESCE(RestaurantType, 'Overall Average'), AVG(AverageCost) FROM Jomato
	GROUP BY ROLLUP(RestaurantType) ;





-- SQL MANDatORy ASsignment 3: Gaurav Singh (grv08singh@gmail.com)

CREATE DATABASE ASsignment3;
USE ASsignment3;


-- DatASET: Jomato
-- About the datASET:
-- You wORk fOR a data analytics company, AND your client IS a food delivery platfORm similar to
-- Jomato. They have provided you with a datASET contaINing INfORmation about various
-- restaurants IN a city. Your tASk IS to analyze thIS datASET using SQL queries to extract valuable
-- INsights AND generate repORts fOR your client
-- 
-- TASks to be perfORmed:
-- ImpORting the csv FLAT FILE Jomato
SELECT * FROM [dbo].[Jomato];


-- 1. CREATE a stored procedure to dISplay the restaurant NAME, type AND cuISINe WHERE the
-- TABLE booking IS NOT zero.
CREATE PROCEDURE sp_TABLE_NOT_zero 
AS
BEGIN
	SELECT [RestaurantNAME], [RestaurantType], [CuISINesType] FROM [dbo].[Jomato] WHERE [TABLEBooking] <> 0
END;

EXEC sp_TABLE_NOT_zero;


-- 2. CREATE a transaction AND UPDATE the cuISINe type ‘Cafe’ to ‘Cafeteria’. Check the result
-- AND rollback it.
BEGIN TRAN
UPDATE [dbo].[Jomato] SET [CuISINesType] = 'Cafeteria' WHERE [CuISINesType] = 'Cafe';
SELECT * FROM [dbo].[Jomato] WHERE [CuISINesType] = 'Cafe';
ROLLBACK



-- 3. Generate a row number COLUMN AND fINd the top 5 areAS with the highest rating of
-- restaurants.
WITH top_rated AS
(	SELECT [Area], [Rating], 
	ROW_NUMBER() OVER (ORDER BY [Rating] DESC) AS row_num 
	FROM [dbo].[Jomato]
)
SELECT * FROM top_rated WHERE row_num <= 5;



-- 4. USE the while loop to dISplay the 1 to 50.
DECLARE @loop INT = 1;
WHILE @loop <= 50
BEGIN
	WITH top_rated AS
	(	SELECT *, ROW_NUMBER() OVER (ORDER BY [Rating] DESC) AS row_num 
		FROM [dbo].[Jomato]
	)
	SELECT * FROM top_rated WHERE row_num = @loop
    SET @loop = @loop + 1;
END;





-- 5. Write a query to CREATE a Top rating view to store the generated top 5 highest rating of
-- restaurants.
CREATE VIEW vw_top_rating AS SELECT TOP 5 * FROM [dbo].[Jomato] ORDER BY [Rating] DESC;

SELECT * FROM vw_top_rating;



-- 6. CREATE a trigger that give an message whenever a new recORd IS INSERTed.
DROP TRIGGER tg_INSERT;
CREATE TRIGGER tg_INSERT ON [dbo].[Jomato] FOR INSERT AS
BEGIN
	PRINT 'Wow!!! A new recORd IS being INSERTed.'
END;

INSERT INTO [dbo].[Jomato] VALUES(7105,'Avb','cdc',3.5454556,52,123,1,0,'Italian','Delhi','CP',60);









-- SQL CASe Study 1: Gaurav Singh (grv08singh@gmail.com)

CREATE DATABASE cASe_study1;
USE cASe_study1;

SELECT * FROM [dbo].[fact];
SELECT * FROM [dbo].[Location];
SELECT * FROM [dbo].[Product];


-- Problem Statement:
-- You are a DATABASE admINIStratOR. You want to USE the data to answer a few
-- questions about your customers, especially about the sales AND profit coming
-- FROM different states, money spent IN Marketing AND various other factORs such AS
-- COGS (Cost of GOods Sold), budget profit etc. You plan on using these INsights
-- to help fINd out which items are being sold the most. You have been provided
-- with the sample of the overall customer data due to privacy ISsues. But you hope
-- that these samples are enough fOR you to write fully functioning SQL queries to
-- help answer the questions.

-- DatASET:
-- The 3 key datASETs fOR thIS cASe study:
-- a. FactTABLE: The Fact TABLE hAS 14 COLUMNs mentioned below AND 4200
-- rows. DATE, ProductID, Profit, Sales, MargIN, COGS, Total Expenses,
-- Marketing, INventORy, Budget Profit, Budget COGS, Budget MargIN, Budget
-- Sales, AND Area Code
-- NOTe: COGS stANDs fOR Cost of GOods Sold

-- b. ProductTABLE: The ProductTABLE hAS four COLUMNs NAMEd Product Type,
-- Product, ProductID, AND Type. It hAS 13 rows which can be broken down
-- INTO further details to retrieve the INfORmation mentioned IN theFactTABLE.

-- c. LocationTABLE: FINally, the LocationTABLE hAS 156 rows AND follows a
-- similar approach to ProductTABLE. It hAS four COLUMNs NAMEd Area Code,
-- State, Market, AND Market Size.


-- TASks to be perfORmed:
-- 1. DISplay the number of states present IN the LocationTABLE.
SELECT * FROM [dbo].[Location];
SELECT COUNT(DISTINCT([State])) AS State_Count FROM [dbo].[Location];


-- 2. How many products are of regular type?
SELECT * FROM [dbo].[Product];
SELECT COUNT([Product_Type]) FROM [dbo].[Product] WHERE [Type] = 'Regular';


-- 3. How much spending hAS been done on Marketing of product ID 1?
SELECT * FROM [dbo].[fact];
SELECT SUM([Marketing]) FROM [dbo].[fact] WHERE [ProductId] = 1;



-- 4. What IS the mINimum sales of a product?
SELECT * FROM [dbo].[Product];
SELECT MIN([Sales]) FROM [dbo].[fact];
SELECT * FROM [dbo].[fact] WHERE [Sales] = (SELECT MIN([Sales]) FROM [dbo].[fact]);

-- 5. DISplay the MAX Cost of GOod Sold (COGS).
SELECT MAX(COGS) AS MAX_cogs FROM [dbo].[fact];



-- 6. DISplay the details of the product WHERE product type IS coffee.
SELECT * FROM [dbo].[Product] WHERE [Product_Type] = 'Coffee';



-- 7. DISplay the details WHERE total expenses are greater than 40.
SELECT * FROM [dbo].[fact] WHERE [Total_Expenses] > 40;



-- 8. What IS the average sales IN area code 719?
SELECT AVG([Sales]) AS avg_sales_719 FROM [dbo].[fact] WHERE [Area_Code] = 719;



-- 9. FINd out the total profit generated by ColORado state.
SELECT SUM([Profit]) AS colORado_profit FROM [dbo].[fact] f
INNER JOIN [dbo].[Location] l
ON f.[Area_Code] = l.[Area_Code]
WHERE l.[State] = 'ColORado';



-- 10. DISplay the average INventORy fOR each product ID.
SELECT [ProductId],AVG([INventORy]) AS avg_INventORy FROM [dbo].[fact]
GROUP BY [ProductId];



-- 11. DISplay state IN a sequential ORder IN a Location TABLE.
SELECT DISTINCT [State] FROM [dbo].[Location] ORDER BY [State] ASC;



-- 12. DISplay the average budget of the Product WHERE the average budget
-- margIN should be greater than 100.
SELECT [ProductId], AVG([Budget_Profit]) AS avg_budget, AVG([Budget_MargIN]) AS avg_bud_margIN 
FROM [dbo].[fact] GROUP BY [ProductId] HAVing AVG([Budget_MargIN]) > 100;



-- 13. What IS the total sales done on DATE 2010-01-01?
SELECT SUM([Sales]) AS total_sales FROM [dbo].[fact] WHERE [DATE] = '2010-01-01';



-- 14. DISplay the average total expense of each product ID on an INdividual DATE.
SELECT [DATE], [ProductId], AVG([Total_Expenses]) FROM [dbo].[fact] GROUP BY [DATE], [ProductId];



-- 15. DISplay the TABLE with the following attributes such AS DATE, productID,
-- product_type, product, sales, profit, state, area_code.
SELECT f.DATE, f.productID,p.product_type, p.product, f.sales, f.profit, l.state, f.area_code
FROM [dbo].[fact] f
JOIN [dbo].[Product] p
ON f.[ProductId] = p.[ProductId]
JOIN [dbo].[Location] l
ON f.[Area_Code] = l.[Area_Code];
-- INNER JOIN IS default.



-- 16. DISplay the rank without any gap to show the sales wISe rank.
-- WINdows functions: rank, dense_rank, rownumber
SELECT [DATE], [ProductId], [Sales],
DENSE_RANK() OVER (ORDER BY [Sales] DESC) AS sales_rank
FROM [dbo].[fact];



-- 17. FINd the state wISe profit AND sales.
SELECT l.[State], SUM(f.[Profit]) AS profit, SUM(f.[Sales]) AS sales FROM [dbo].[fact] f
JOIN [dbo].[Location] l
ON f.[Area_Code] = l.[Area_Code]
GROUP BY l.[State];



-- 18. FINd the state wISe profit AND sales along with the product NAME.
SELECT l.[State], p.[Product], SUM(f.[Profit]) AS profit, SUM(f.[Sales])  AS sales FROM [dbo].[fact] f
JOIN [dbo].[Location] l
ON f.[Area_Code] = l.[Area_Code]
JOIN [dbo].[Product] p
ON f.[ProductId] = p.[ProductId]
GROUP BY l.[State], p.[Product];



-- 19. If there IS an INcreASe IN sales of 5%, calculate the INcreASed sales.
SELECT *, [Sales]*1.05 AS INc_sales FROM [dbo].[fact];



-- 20. FINd the MAXimum profit along with the product ID AND producttype.
SELECT f.[ProductId], p.[Product_Type], f.[Profit]
FROM [dbo].[fact] f
JOIN [dbo].[Product] p
ON f.[ProductId] = p.[ProductId]
WHERE f.[Profit] = (SELECT MAX([Profit]) FROM [dbo].[fact]);



-- 21. CREATE a stored procedure to fetch the result accORding to the product type
-- FROM Product TABLE.
-- system defINed procedure
sp_help Product;

-- USEr defINed procedure
DROP PROCEDURE sp_GetProductType;

CREATE PROCEDURE sp_GetProductType @ProductType VARCHAR(30)
AS
BEGIN
	SELECT * FROM [dbo].[Product] WHERE [Product_Type] = @ProductType
END;


EXEC sp_GetProductType 'Coffee';
EXEC sp_GetProductType 'Espresso';
EXEC sp_GetProductType 'Herbal Tea';




-- 22. Write a query by creating a condition IN which if the total expenses IS less than
-- 60 then it IS a profit OR else loss.
SELECT * FROM [dbo].[fact];

SELECT *, 
CASE
	WHEN [Total_Expenses] < 60 THEN 'Profit'
	ELSE 'Loss'
END AS Profit_Loss
FROM [dbo].[fact];



-- 23. Give the total weekly sales value with the DATE AND product ID details. USE
-- roll-up to pull the data IN hierarchical ORder.
SELECT DATEPART(YEAR, [DATE]) AS YEAR,
DATEPART(WEEK, [DATE]) AS WEEK,
[ProductId],
SUM([Sales]) AS WEEKLY_SALES
FROM [dbo].[fact]
GROUP BY ROLLUP(DATEPART(YEAR, [DATE]), DATEPART(WEEK, [DATE]), [ProductId]);





-- 24. Apply union AND INTersection operatOR on the TABLEs which consISt of
-- attribute area code.
SELECT [Area_Code] FROM [dbo].[fact]
UNION
SELECT [Area_Code] FROM [dbo].[Location];


SELECT [Area_Code] FROM [dbo].[fact]
INTERSECT
SELECT [Area_Code] FROM [dbo].[Location];


SELECT [Area_Code] FROM [dbo].[fact]
EXCEPT
SELECT [Area_Code] FROM [dbo].[Location];



-- 25. CREATE a USEr-defINed function fOR the product TABLE to fetch a particular
-- product type bASed upon the USEr’s preference.
DROP FUNCTION fq_ProductType;

CREATE FUNCTION fq_ProductType(@Type VARCHAR(30))
RETURNS TABLE
AS
	RETURN
	SELECT * FROM [dbo].[Product] WHERE [Product_Type] = @Type;

SELECT * FROM fq_ProductType('Tea');



-- 26. Change the product type FROM coffee to tea WHERE product ID IS 1 AND undo
-- it.
BEGIN TRAN
BEGIN TRANSACTION
UPDATE [dbo].[Product] SET [Product_Type]='Tea' WHERE [ProductId]=1;
ROLLBACK

SELECT * FROM [dbo].[Product];



-- 27. DISplay the DATE, product ID AND sales WHERE total expenses are
-- BETWEEN 100 to 200.
SELECT [DATE], [ProductId], [Sales] FROM [dbo].[fact] WHERE [Total_Expenses] BETWEEN 100 AND 200;



-- 28. DELETE the records IN the Product TABLE fOR regular type.
SELECT * FROM [dbo].[Product];

BEGIN TRANSACTION
DELETE FROM [dbo].[Product] WHERE [Type]='Regular';
ROLLBACK



-- 29. DISplay the ASCII value of the fifth CHARacter FROM the COLUMNProduct.
SELECT [Product],SUBSTRing([Product],5,1),ASCII(SUBSTRing([Product],5,1)) AS AScii_5th_CHAR FROM [dbo].[Product];





-- SQL CASe Study 2: Gaurav Singh (grv08singh@gmail.com)


-- Pre-RequISite TABLEs

CREATE DATABASE cASe_study2;
USE cASe_study2;

DROP TABLE LOCATION;
CREATE TABLE LOCATION (
  Location_ID INT PRIMARY KEY,
  City VARCHAR(50)
);

INSERT INTO LOCATION (Location_ID, City)
VALUES (122, 'New YORk'),
       (123, 'DallAS'),
       (124, 'ChicaGO'),
       (167, 'Boston');


DROP TABLE DEPARTMENT;
  CREATE TABLE DEPARTMENT (
  Department_Id INT PRIMARY KEY,
  NAME VARCHAR(50),
  Location_Id INT,
  FOREIGN KEY (Location_Id) REFERENCES LOCATION(Location_ID)
);


INSERT INTO DEPARTMENT (Department_Id, NAME, Location_Id)
VALUES (10, 'Accounting', 122),
       (20, 'Sales', 124),
       (30, 'Research', 123),
       (40, 'Operations', 167);


DROP TABLE JOB;
CREATE TABLE JOB
(JOB_ID INT PRIMARY KEY,
DESIGNATION VARCHAR(20));

INSERT  INTO JOB VALUES
(667, 'CLERK'),
(668,'STAFF'),
(669,'ANALYST'),
(670,'SALES_PERSON'),
(671,'MANAGER'),
(672, 'PRESIDENT');


CREATE TABLE EMPLOYEE
(EMPLOYEE_ID INT,
LAST_NAME VARCHAR(20),
FIRST_NAME VARCHAR(20),
MIDDLE_NAME CHAR(1),
JOB_ID INT FOREIGN KEY
REFERENCES JOB(JOB_ID),
MANAGER_ID INT,
HIRE_DATE DATE,
SALARY INT,
COMM INT,
DEPARTMENT_ID  INT FOREIGN KEY
REFERENCES DEPARTMENT(DEPARTMENT_ID));

INSERT INTO EMPLOYEE VALUES
(7369,'SMITH','JOHN','Q',667,7902,'17-DEC-84',800,NULL,20),
(7499,'ALLEN','KEVIN','J',670,7698,'20-FEB-84',1600,300,30),
(7505,'DOYLE','JEAN','K',671,7839,'04-APR-85',2850,NULL,30),
(7506,'DENNIS','LYNN','S',671,7839,'15-MAY-85',2750,NULL,30),
(7507,'BAKER','LESLIE','D',671,7839,'10-JUN-85',2200,NULL,40),
(7521,'WARK','CYNTHIA','D',670,7698,'22-FEB-85',1250,500,30);






-----------------------------------------------------------
-- Simple Queries:
-----------------------------------------------------------
-- 1. LISt all the employee details.
SELECT * FROM [dbo].[EMPLOYEE];



-- 2. LISt all the department details.
SELECT * FROM [dbo].[DEPARTMENT];



-- 3. LISt all job details.
SELECT * FROM [dbo].[JOB];



-- 4. LISt all the locations.
SELECT * FROM [dbo].[LOCATION];



-- 5. LISt out the First NAME, LASt NAME, Salary, CommISsion fOR all Employees.
SELECT [FIRST_NAME], [LAST_NAME], [SALARY], [COMM] FROM [dbo].[EMPLOYEE];



-- 6. LISt out the Employee ID, LASt NAME, Department ID fOR all employees AND
-- aliAS Employee ID AS "ID of the Employee", LASt NAME AS "NAME of the
-- Employee", Department ID AS "Dep_id".
SELECT 
	[EMPLOYEE_ID] AS [ID of the Employee], 
	[LAST_NAME] AS [NAME of the Employee], 
	[DEPARTMENT_ID] AS Dep_id
FROM
	[dbo].[EMPLOYEE];



-- 7. LISt out the annual salary of the employees with their NAMEs only.
SELECT [FIRST_NAME], [LAST_NAME], 12*[SALARY] AS annual_salary FROM [dbo].[EMPLOYEE];



-----------------------------------------------------------
-- WHERE Condition:
-----------------------------------------------------------
-- 1. LISt the details about "Smith".
SELECT * FROM [dbo].[EMPLOYEE] WHERE [LAST_NAME] = 'Smith';



-- 2. LISt out the employees who are wORking IN department 20.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [DEPARTMENT_ID] = 20;



-- 3. LISt out the employees who are earning salary BETWEEN 2000 AND 3000.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [SALARY] BETWEEN 2000 AND 3000;



-- 4. LISt out the employees who are wORking IN department 10 OR 20.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [DEPARTMENT_ID] IN (20,30);



-- 5. FINd out the employees who are NOT wORking IN department 10 OR 30.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [DEPARTMENT_ID] NOT IN (10,30);



-- 6. LISt out the employees whose NAME starts with 'L'.7. LISt out the employees whose NAME starts with 'L' AND ends with 'E'.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [FIRST_NAME] LIKE 'L%';
SELECT * FROM [dbo].[EMPLOYEE] WHERE [FIRST_NAME] LIKE 'L%E';



-- 8. LISt out the employees whose NAME length IS 4 AND start with 'J'.
SELECT * FROM [dbo].[EMPLOYEE] WHERE LEN([FIRST_NAME]) = 4 AND [FIRST_NAME] LIKE 'J%';



-- 9. LISt out the employees who are wORking IN department 30 AND draw the
-- salaries mORe than 2500.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [DEPARTMENT_ID] = 30 AND [SALARY] > 2500;



-- 10. LISt out the employees who are NOT receiving commISsion.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [COMM] IS NULL ;




-----------------------------------------------------------
-- ORDER BY ClaUSE:
-----------------------------------------------------------
-- 1. LISt out the Employee ID AND LASt NAME IN AScending ORder bASed on the
-- Employee ID.
SELECT [EMPLOYEE_ID], [LAST_NAME] FROM [dbo].[EMPLOYEE] ORDER BY [EMPLOYEE_ID] ASC;



-- 2. LISt out the Employee ID AND NAME IN descending ORder bASed on salary.
SELECT [EMPLOYEE_ID], [LAST_NAME] FROM [dbo].[EMPLOYEE] ORDER BY [SALARY] DESC;



-- 3. LISt out the employee details accORding to their LASt NAME IN AScending-ORder.
SELECT * FROM [dbo].[EMPLOYEE] ORDER BY [LAST_NAME] ASC;



-- 4. LISt out the employee details accORding to their LASt NAME IN AScending
-- ORder AND then Department ID IN descending ORder.
SELECT * FROM [dbo].[EMPLOYEE] ORDER BY [LAST_NAME] ASC, [DEPARTMENT_ID] DESC;



-----------------------------------------------------------
-- GROUP BY AND HAVing ClaUSE:
-----------------------------------------------------------
-- 1. LISt out the department wISe MAXimum salary, mINimum salary AND
-- average salary of the employees.
SELECT 
	[DEPARTMENT_ID], 
	MAX([SALARY]) AS MAX_salary, 
	MIN([SALARY]) AS mIN_salary, 
	AVG([SALARY]) AS avg_salary
FROM [dbo].[EMPLOYEE]
GROUP BY [DEPARTMENT_ID];



-- 2. LISt out the job wISe MAXimum salary, mINimum salary AND average
-- salary of the employees.
SELECT 
	[JOB_ID], 
	MAX([SALARY]) AS MAX_salary, 
	MIN([SALARY]) AS mIN_salary, 
	AVG([SALARY]) AS avg_salary
FROM [dbo].[EMPLOYEE]
GROUP BY [JOB_ID];



-- 3. LISt out the number of employees who joINed each month IN AScending ORder.
SELECT 
	DATEPART(MONTH, [HIRE_DATE]) AS mnth_num, 
	DATENAME(MONTH, [HIRE_DATE]) AS mnth_NAME, 
	COUNT([EMPLOYEE_ID]) AS emp_joINed
FROM [dbo].[EMPLOYEE]
GROUP BY 
	DATEPART(MONTH, [HIRE_DATE]),
	DATENAME(MONTH, [HIRE_DATE]) 
ORDER BY 
	DATEPART(MONTH, [HIRE_DATE]);



-- 4. LISt out the number of employees fOR each month AND year IN
-- AScending ORder bASed on the year AND month.
SELECT 
	DATEPART(YEAR, [HIRE_DATE]) AS yr,
	DATEPART(MONTH, [HIRE_DATE]) AS mnth_num, 
	DATENAME(MONTH, [HIRE_DATE]) AS mnth_NAME, 
	COUNT([EMPLOYEE_ID]) AS emp_joINed
FROM [dbo].[EMPLOYEE]
GROUP BY 
	DATEPART(YEAR, [HIRE_DATE]),
	DATEPART(MONTH, [HIRE_DATE]),
	DATENAME(MONTH, [HIRE_DATE]) 
ORDER BY 
	DATEPART(YEAR, [HIRE_DATE]),
	DATEPART(MONTH, [HIRE_DATE]);




-- 5. LISt out the Department ID HAVing at leASt four employees.
SELECT 
	[DEPARTMENT_ID], 
	COUNT([EMPLOYEE_ID]) AS emp_count
FROM [dbo].[EMPLOYEE]
GROUP BY [DEPARTMENT_ID]
HAVing COUNT([EMPLOYEE_ID]) >= 4;



-- 6. How many employees joINed IN February month.
SELECT COUNT([EMPLOYEE_ID]) AS feb_count 
FROM [dbo].[EMPLOYEE] 
WHERE DATEPART(MONTH,[HIRE_DATE]) = 2;



-- 7. How many employees joINed IN May OR June month.
SELECT COUNT([EMPLOYEE_ID]) AS may_jun_count 
FROM [dbo].[EMPLOYEE] 
WHERE DATEPART(MONTH,[HIRE_DATE]) IN (5,6);



-- 8. How many employees joINed IN 1985?
SELECT COUNT([EMPLOYEE_ID]) AS yr_1985_count 
FROM [dbo].[EMPLOYEE] 
WHERE DATEPART(YEAR,[HIRE_DATE]) = 1985;



-- 9. How many employees joINed each month IN 1985?
SELECT DATENAME(MONTH,[HIRE_DATE]) AS mnth, COUNT([EMPLOYEE_ID]) AS monthly_count 
FROM [dbo].[EMPLOYEE]
GROUP BY DATEPART(YEAR,[HIRE_DATE]), DATENAME(MONTH,[HIRE_DATE])
HAVing DATEPART(YEAR,[HIRE_DATE]) = 1985;



-- 10. How many employees were joINed IN April 1985?
SELECT COUNT([EMPLOYEE_ID]) AS Apr_1985_count 
FROM [dbo].[EMPLOYEE] 
WHERE DATEPART(YEAR,[HIRE_DATE]) = 1985 AND DATEPART(MONTH,[HIRE_DATE]) = 4;



-- 11. Which IS the Department ID HAVing greater than OR equal to 3 employees
-- joINing IN April 1985?JoINs:
SELECT 
	[DEPARTMENT_ID]
FROM [dbo].[EMPLOYEE]
WHERE
	DATEPART(YEAR,[HIRE_DATE]) = 1985 AND
	DATEPART(MONTH,[HIRE_DATE]) = 4
GROUP BY
	[DEPARTMENT_ID]
HAVing COUNT([EMPLOYEE_ID]) >= 3;




-----------------------------------------------------------
-- JoINs:
-----------------------------------------------------------

-- 1. LISt out employees with their department NAMEs.
SELECT e.[FIRST_NAME], e.[LAST_NAME], d.[NAME] AS dept_nm
FROM [dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id];



-- 2. DISplay employees with their designations.
SELECT e.[FIRST_NAME], e.[LAST_NAME], j.[DESIGNATION]
FROM [dbo].[EMPLOYEE] e
INNER JOIN [dbo].[JOB] j
ON e.[JOB_ID] = j.[JOB_ID];



-- 3. DISplay the employees with their department NAMEs AND city.
SELECT 
	e.[FIRST_NAME], 
	e.[LAST_NAME], 
	d.[NAME] AS department, 
	loc.[City]
FROM
	[dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id]
INNER JOIN [dbo].[LOCATION] loc
ON d.[Location_Id] = loc.[Location_ID];
	


-- 4. How many employees are wORking IN different departments? 
-- DISplay with department NAMEs.
SELECT 
	d.[NAME] AS department, 
	COUNT(e.[EMPLOYEE_ID]) AS num_of_employees
FROM [dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id]
GROUP BY d.[NAME];




-- 5. How many employees are wORking IN the sales department?
SELECT 
	COUNT(e.[EMPLOYEE_ID]) AS sales_employees
FROM [dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id]
WHERE d.[NAME] = 'sales'
GROUP BY d.[NAME];




-- 6. Which IS the department HAVing greater than OR equal to 3
-- employees AND dISplay the department NAMEs IN AScending ORder.
SELECT 
	d.[NAME] AS department, 
	COUNT(e.[EMPLOYEE_ID]) AS num_of_employees
FROM [dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id]
GROUP BY d.[NAME]
HAVing COUNT(e.[EMPLOYEE_ID]) >= 3
ORDER BY d.[NAME];





-- 7. How many employees are wORking IN 'DallAS'?
SELECT 
	COUNT(e.[EMPLOYEE_ID]) AS dallAS_employees
FROM
	[dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id]
INNER JOIN [dbo].[LOCATION] loc
ON d.[Location_Id] = loc.[Location_ID]
WHERE loc.[City] = 'DallAS';




-- 8. DISplay all employees IN sales OR operations departments.
SELECT 
	e.[FIRST_NAME],
	e.[LAST_NAME],
	d.[NAME] AS dept
FROM [dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id]
WHERE d.[NAME] IN ('sales','operations');





-----------------------------------------------------------
-- CONDITIONAL STATEMENT
-----------------------------------------------------------
-- 1. DISplay the employee details with salary grades. USE conditional statement to
-- CREATE a grade COLUMN.
SELECT *,
	CASE
		WHEN [SALARY] > 2700 THEN 'A'
		WHEN [SALARY] > 1800 THEN 'B'
		WHEN [SALARY] > 900 THEN 'C'
		WHEN [SALARY] <= 900 THEN 'D'
	END AS grade
FROM [dbo].[EMPLOYEE];




-- 2. LISt out the number of employees grade wISe. USE conditional statement to
-- CREATE a grade COLUMN.
WITH grade_wISe AS
(
	SELECT *,
		CASE
			WHEN [SALARY] > 2700 THEN 'A'
			WHEN [SALARY] > 1800 THEN 'B'
			WHEN [SALARY] > 900 THEN 'C'
			WHEN [SALARY] <= 900 THEN 'D'
		END AS grade
	FROM [dbo].[EMPLOYEE]
)
SELECT grade, COUNT([EMPLOYEE_ID]) AS num_of_employees
FROM grade_wISe
GROUP BY grade;




-- 3. DISplay the employee salary grades AND the number of employees BETWEEN
-- 2000 to 5000 range of salary.
WITH sal_grd AS
(
	SELECT *,
		CASE
			WHEN [SALARY] BETWEEN 4000 AND 5000 THEN 'A'
			WHEN [SALARY] BETWEEN 3000 AND 4000 THEN 'B'
			WHEN [SALARY] BETWEEN 2000 AND 3000 THEN 'C'
		END AS grade
	FROM [dbo].[EMPLOYEE]
)
SELECT grade, COUNT([EMPLOYEE_ID]) num_of_emp
FROM sal_grd
WHERE [SALARY] BETWEEN 2000 AND 5000
GROUP BY grade;







-----------------------------------------------------------
-- Subqueries:
-----------------------------------------------------------

-- 1. DISplay the employees lISt who GOt the MAXimum salary.
SELECT * 
FROM [dbo].[EMPLOYEE] 
WHERE [SALARY] = (SELECT MAX([SALARY]) FROM [dbo].[EMPLOYEE]);



-- 2. DISplay the employees who are wORking IN the sales department.
SELECT * 
FROM [dbo].[EMPLOYEE] 
WHERE [DEPARTMENT_ID] = (SELECT [Department_Id] FROM [dbo].[DEPARTMENT] WHERE [NAME] = 'sales');



-- 3. DISplay the employees who are wORking AS 'Clerk'.
SELECT * 
FROM [dbo].[EMPLOYEE] 
WHERE [JOB_ID] = (SELECT [JOB_ID] FROM [dbo].[JOB] WHERE [DESIGNATION] = 'clerk');



-- 4. DISplay the lISt of employees who are living IN 'Boston'.
SELECT * 
FROM [dbo].[EMPLOYEE] 
WHERE [Department_Id] IN 
	(
	SELECT [Department_Id] 
	FROM [dbo].[DEPARTMENT]
	WHERE [Location_Id] =
		(
			SELECT [Location_ID] 
			FROM [dbo].[LOCATION] 
			WHERE [City] = 'Boston'
		)
	);



-- 5. FINd out the number of employees wORking IN the sales department.
SELECT COUNT([EMPLOYEE_ID]) AS sales_emp
FROM [dbo].[EMPLOYEE]
WHERE [DEPARTMENT_ID] = 
	(
		SELECT [Department_Id]
		FROM [dbo].[DEPARTMENT]
		WHERE [NAME] = 'sales'
	);




-- 6. UPDATE the salaries of employees who are wORking AS clerks on the bASIS of 10%.
UPDATE [dbo].[EMPLOYEE]
SET [SALARY] = 1.1*[SALARY]
WHERE [JOB_ID] = 
	(
		SELECT [JOB_ID] 
		FROM [dbo].[JOB] 
		WHERE [DESIGNATION] = 'clerk'
	);




-- 7. DISplay the second highest salary drawing employee details.
SELECT *
FROM [dbo].[EMPLOYEE]
ORDER BY [SALARY] DESC
OFFSET 1 ROWS
FETCH NEXT 1 ROWS ONLY;



-- 8. LISt out the employees who earn mORe than every employee IN department 30.
SELECT *
FROM [dbo].[EMPLOYEE]
WHERE [SALARY] > 
	(
		SELECT MAX([SALARY]) AS MAX_sal_IN_dept_30
		FROM [dbo].[EMPLOYEE] 
		WHERE [DEPARTMENT_ID] = 30
	);



-- 9. FINd out which department hAS no employees.
SELECT [NAME] 
FROM [dbo].[DEPARTMENT]
WHERE [Department_Id] NOT IN
	(
		SELECT DISTINCT [DEPARTMENT_ID]
		FROM [dbo].[EMPLOYEE]
	);



-- 10. FINd out the employees who earn greater than the average salary fOR
-- their department.
WITH dept_avg_sal AS
(
	SELECT [DEPARTMENT_ID], AVG([SALARY]) AS dept_avg
	FROM [dbo].[EMPLOYEE]
	GROUP BY [DEPARTMENT_ID]
)
SELECT e.*,d.dept_avg
FROM [dbo].[EMPLOYEE] e
INNER JOIN dept_avg_sal d
ON e.[DEPARTMENT_ID] = d.[DEPARTMENT_ID] AND e.[SALARY] > d.dept_avg;


