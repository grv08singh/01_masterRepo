--String,unicode,datetime,ddl(create, alter, drop, use) 

--##################################################
'12 3#$%^&*DFGH J KL:123 123sdas d'

--Char(n), range (1 to 8000)
	--It is a fixed length data type
	--Used to store non-Unicode characters
	--Occupiers 1 byte of space for each character
	--Static memory allocation

	declare @val char 
	set @val='alp'
	select @val, datalength(@val) as Byte

	declare @val char(1)
	set @val='alp'
	select @val, datalength(@val) as Byte
	
	declare @val char(10)
	set @val='alpha beta'
	select @val, datalength(@val) as Byte

	declare @val char(5)
	set @val='alpha beta'
	select @val, datalength(@val) as Byte
	
	declare @val char(10)
	set @val='alpha'
	select @val, datalength(@val) as Byte
	
	declare @val char(8000)
	set @val='alpha'
	select @val, datalength(@val) as Byte

--##########################################################
--varchar(n), range 1-8000 / max
	--It is a variable-length data type
	--Used to store Unicode characters
	--Occupies 1 bytes of space for each character
	--dynamic memory allocation

	declare @val varchar(10)
	set @val='alpha'
	select @val, datalength(@val) as Byte

	declare @val varchar 
	set @val='alp'
	select @val, datalength(@val) as Byte

	declare @val varchar(1)
	set @val='alp'
	select @val, datalength(@val) as Byte
	
	declare @val varchar(10)
	set @val='alpha beta'
	select @val, datalength(@val) as Byte

	declare @val varchar(5)
	set @val='alpha beta'
	select @val, datalength(@val) as Byte
	
	declare @val varchar(10)
	set @val='alpha'
	select @val, datalength(@val) as Byte
		
	declare @val varchar(8000)
	set @val='alpha'
	select @val, datalength(@val) as Byte

	
	declare @val varchar(max)
	set @val='alpha'
	select @val, datalength(@val) as Byte

---###################################

	declare @val varchar(max)
	set @val='नमस्ते दुनिया'
	select @val, datalength(@val) as Byte


--###############################################
--Unicode (nchar & nvachar)
--nchar(1 to 4000) 
	--It is a fixed length data type
	--Used to store Unicode characters
	--Occupiers 2 byte of space for each character
	--static memory allocation
	
	declare @val nchar(20)	--20*2
	set @val=N'नमस्ते दुनिया'
	select @val, datalength(@val) as Byte
	
	declare @val nchar(10)	--10*2
	set @val=N'alpha'
	select @val, datalength(@val) as Byte
		
	declare @val nchar(15)	--15*2
	set @val=N'नमस्ते你好，世界'
	select @val, datalength(@val) as Byte

--###########################################################
--nvarchar()--1-4000
--It is a variable-length data type
--Used to store Unicode characters
--Occupies 2 bytes of space for each character
--dynamic memory allocation
		
	declare @val nvarchar(30)	 
	set @val=N'hello'
	select @val, datalength(@val) as Byte
	
	declare @val nvarchar(30)	 
	set @val=N'नमस्ते दुनिया'
	select @val, datalength(@val) as Byte
	
	declare @val nvarchar(30)	 
	set @val=N'你好，世界'
	select @val, datalength(@val) as Byte

	
	declare @val nvarchar(30)	 
	set @val=N'नमस्ते दुनिया 你好，世界'
	select @val, datalength(@val) as Byte
--###########################################################
--Date (3 byte)
	--input ='YYYY-MM-DD' or 'MM-DD-YYYY'
	--Output ='YYYY-MM-DD'

	declare @val date
	set @val= '2025-02-08'
	select @val, datalength(@val) as Byte
		
	declare @val date
	set @val= '02/15/2025'
	select @val, datalength(@val) as Byte
--Conversion failed when converting date and/or time from character string.
	declare @val date
	set @val= '15-02-2025'
	select @val, datalength(@val) as Byte

--##########################################################

--Time(5 byte)	
	--input 'HH:MM:SS'
	--output'HH:MM:SS:MMMMMMM'
	
	declare @val time
	set @val= '00:15:21'
	select @val, datalength(@val) as Byte

	declare @val time
	set @val= '23:15:21'
	select @val, datalength(@val) as Byte

	select getdate()
	select sysdatetime()

--#####################################################
--Timestamp 'YYYY-MM-DD HH:MM:SS'

--Smalldatetime(4 byte)'YYYY-MM-DD HH:MM:SS'
	declare @val Smalldatetime
	set @val= '2025-02-08 23:15:21'
	select @val, datalength(@val) as Byte

--datetime(8 byte), 'YYYY-MM-DD HH:MM:SS:mmm'3 milisecond info

	declare @val datetime
	set @val= '2025-02-08 23:15:21'
	select @val, datalength(@val) as Byte

--datetime2(8 byte), 'YYYY-MM-DD HH:MM:SS:mmmMMMM'7 milisecond info

	declare @val datetime2
	set @val= '2025-02-08 23:15:21'
	select @val, datalength(@val) as Byte

	select *  from sys.time_zone_info

--datetimeoffset (10 byte), 'YYYY-MM-DD HH:MM:SS:mmmMMMM'7 milisecond info
	declare @val datetimeoffset
	set @val= '2025-02-08 23:15:21 +5:30'
	select @val, datalength(@val) as Byte

--#################################################
--DDL(Data Definition Language)
--Create
	--Create database
		--Syntax: create database DatabaseName

		
	create database Demo 

	create database SQlDemo 

	create database Hello 

--[] = Qoute identifier	

	create database [sql 123]

---Task to create table employee (eid, ename , age , gender, salary)
	use demo

	create table employee 
	(eid int , ename varchar(10), age tinyint , gender char(10), salary decimal(10,2))

-- Which database & datatype
--##############################################################
--SYNATX:
	--CREATE TABLE table_name	(column1_name datatype ,column2_name datatype,column3_name datatype,...)

---Task to create table dep (eid, ename , age , gender, salary)

	use SQlDemo
	create table dep 
	(eid int , ename varchar(10), age tinyint , gender char(10), salary decimal(10,2))
--########################################################
--Alter
--Alter to add a column 
/*Syntax:
	alter table tablename 
	add columnname datatype,columnname datatype,.....
*/

--task to add column phnum int, email varchar(50)

	use SQlDemo

	alter table dep
	add phnum int, email varchar(50)

--task to add column reg int, house varchar(50)

	use demo

	alter table employee
	add  reg int, house varchar(50)


--Alter to drop a column 
/*Syntax:
	alter table tablename 
	drop column columnname,columnname
*/ 
	use SQlDemo

	alter table dep
	drop column age, salary, phnum


	use demo
	alter table employee
	drop column eid ,  reg , age


--Alter to modify the datatype of a column
/*Syntax:
	alter table tablename 
	alter column columnname datype
*/ 

	use SQlDemo

	alter table dep
	alter column ename char(30)


	use demo
	alter table employee
	alter column gender varchar(20)

--DROP TABLE
	--Syntax: drop table tablename

--DROP TABLE [dbo].[dep]
	use SQlDemo
	drop  table dep

--Drop database 
	--Syntax: Drop database name

	use master
	Drop database SQlDemo

--32767 session user

--sp_who2
	--remove the connection = Kill SPID
	sp_who2 

 




























































































































































