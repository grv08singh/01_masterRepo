--Sql server Adventure works restore,SSMS introduction,Data type( numeric)
--#################################################
--Self learning 
	https://learn.microsoft.com/en-us/sql/t-sql/data-types/data-types-transact-sql?view=sql-server-ver16
--XML data in SQL Server
	https://learn.microsoft.com/en-us/sql/relational-databases/xml/xml-data-sql-server?view=sql-server-ver16
--JSON data in SQL Server
	https://learn.microsoft.com/en-us/sql/relational-databases/json/json-data-sql-server?view=sql-server-ver16
--###########################################################
	-- comment = Informational message 
	-- single line comment
	--	sql server is not a case sensitive language 
	--  32767 connection to the sql server


/*  start

	Multi line comment

	Instance name =DATADOX\DEMO
	Username =DATADOX\Balje
	session id = 58
	database name =master

end */

--session 1- 50 reserved for system process

--#################################################
	--Download backup files
	--Step 1 
	--Open --> sql server management studio--> New Query -->run a command 
	
		Select @@version
		
	--Step 2
	https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms
	--download the -->OLTP  -->AdventureWorks2022.bak

	--step 3 
	--create the folder in C drive with your name and copy the backup file


	--step 4
	--Restore

--##################################################
--System Databases
https://learn.microsoft.com/en-us/sql/relational-databases/databases/system-databases?view=sql-server-ver16

--master Database(Critical)
	--Records all the system-level information for an instance of SQL Server.

--model Database	
	--Is used as the template for all databases created on the instance of SQL Server.
	create database sqldemo

		--how many  files 
		--size of files
		--path of files 
		--name of files

--msdb Database	
	--Is used by SQL Server Agent for scheduling alerts and jobs.

--tempdb Database(Critical)	
	--Is a workspace for holding temporary objects or intermediate result sets.
	--temporary data,  It resets every time the SQL Server restarts.


--Resource Database	
	--Is a read-only database that contains system objects that are included with SQL Server. 

	https://learn.microsoft.com/en-us/sql/relational-databases/databases/resource-database?view=sql-server-ver16
	--Installation drive>:\Program Files\Microsoft SQL Server\MSSQL<version>.<instance_name>\MSSQL\Binn\ 
	--Name  =  mssqlsystemresource


--##########################################################
--Numbers 
--Exact numerics

	16163163
	31
	1
	0
	-465
	-8
	-45646
--Declare , help us to intialise a temp variable
--set , assign temp variable a value
--select , display the value
@= temporary
age = variabele
@age= temporary variabele


declare @age int
set @age =43
select @age

--Tinyint, range(0-255), 1 Byte.

	declare @val Tinyint
	set @val =0
	select @val

	declare @val Tinyint
	set @val =255
	select @val

	declare @val Tinyint
	set @val =55
	select @val
	
	declare @val Tinyint
	set @val =100
	select @val as newdata
	
	declare @val Tinyint
	set @val =150
	select @val as Val, datalength(@val) as Byte

	declare @val Tinyint
	set @val =256
	select @val as Val, datalength(@val) as Byte


--##########################################################
--smallint, range(-32768 to 32767), 2 byte  
	declare @val smallint
	set @val =-32768
	select @val as Val, datalength(@val) as Byte


	declare @val smallint
	set @val =-1
	select @val as Val, datalength(@val) as Byte


	declare @val smallint
	set @val =-32 
	select @val as Val, datalength(@val) as Byte

	
	declare @val smallint
	set @val =32767
	select @val as Val, datalength(@val) as Byte

	declare @val smallint
	set @val =32768
	select @val as Val, datalength(@val) as Byte
--##########################################################
--Int (-2,147,483,648 to 2,147,483,647), 4 byte


	declare @val  int
	set @val =-2147 
	select @val as Val, datalength(@val) as Byte


	declare @val  int
	set @val =-214748 
	select @val as Val, datalength(@val) as Byte

	
	declare @val  int
	set @val =-2147483648
	select @val as Val, datalength(@val) as Byte


	declare @val  int
	set @val =214
	select @val as Val, datalength(@val) as Byte


	declare @val  int
	set @val =1
	select @val as Val, datalength(@val) as Byte
	
	
	declare @val  int
	set @val =2147483648
	select @val as Val, datalength(@val) as Byte

--#######################################################
--Bigint (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807), 8 byte

	declare @val  Bigint
	set @val =-9223372036854775808
	select @val as Val, datalength(@val) as Byte


	declare @val  Bigint
	set @val =-1
	select @val as Val, datalength(@val) as Byte


	declare @val  Bigint
	set @val =-922 
	select @val as Val, datalength(@val) as Byte


	declare @val  Bigint
	set @val =1
	select @val as Val, datalength(@val) as Byte

---###################################################################
--Approximate numerics
	--Precision (data which is presenet towards the left and right of the decimal point)
	--Scale(data which is present towards right of the decimal point)

968457.789654958
123456 789012345
789654958
123456789
(p=15, s=9)

--Float, 15 Precision , 8 byte
	declare @val  Float
	set @val =123456789012345
	select @val as Val, datalength(@val) as Byte
	
	declare @val  Float
	set @val =1234567.89012345
	select @val as Val, datalength(@val) as Byte
	
	declare @val  Float
	set @val =1234567.890123456
	select @val as Val, datalength(@val) as Byte

	declare @val  Float
	set @val =1234567896564567.89012345 
	select @val as Val, datalength(@val) as Byte


1234567896564567.89012345
1.23456789656457E+15
1.23456789656457* 10 raised to power of 15


--#####################################################################
--decimal(precision , scale)
	Precision			Storage bytes
	1 - 9					5
	10-19					9
	20-28					13
	29-38					17
	
	declare @val  decimal(38,0)
	set @val =123456
	select @val as Val, datalength(@val) as Byte
	   
	declare @val  decimal(38,0)
	set @val =12345678901
	select @val as Val, datalength(@val) as Byte

	declare @val  decimal(38,0)
	set @val =123456789012345678900
	select @val as Val, datalength(@val) as Byte
	   
	declare @val  decimal(38,0)
	set @val =92233720368547758089223372036854775892
	select @val as Val, datalength(@val) as Byte


--Scale

	declare @val  decimal(38,2)
	set @val =1.123123123
	select @val as Val, datalength(@val) as Byte
	   
	declare @val  decimal(38,2)
	set @val =5.345435345
	select @val as Val, datalength(@val) as Byte
	   
	declare @val  decimal(38,2)
	set @val =16161
	select @val as Val, datalength(@val) as Byte
	   
	declare @val  decimal(38,2)
	set @val =1.2 
	select @val as Val, datalength(@val) as Byte
	   
	declare @val  decimal(38,2)
	set @val =6511616
	select @val as Val, datalength(@val) as Byte

	declare @val  decimal(38,2)
	set @val =92233720368547758089223372036854775892
	select @val as Val, datalength(@val) as Byte
















