 --SQL SERVER set operators ,Function (string, date time )
--#########################################################################
--Self learning  
--	https://learn.microsoft.com/en-us/training/modules/transform-data-by-implementing-pivot-unpivot-rollup-cube/
--	https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver16
--#########################################################################
 

--7. Join with Subquery:
	Question: Write a query to find the names of employees who have placed an order. 
	Use a subquery to find the `EmployeeID` from the `Sales.SalesOrderHeader` table and join it with the 
	`HumanResources.Employee` and `Person.Person` tables to get the `FirstName` and `LastName`.
	 

	 Select  FirstName, LastName      From HumanResources.Employee as HRE inner join  Person.Person as PP     on PP. BusinessEntityID = HRE. BusinessEntityID	 where PP. BusinessEntityID in( select SalesPersonID from 	  Sales.SalesOrderHeader )

--#######################################################
	Create database  SQLDEMO
	go
	use SQLDEMO
	go

	CREATE TABLE Department
	(
	did INT,
	ename VARCHAR(50) ,
	gender VARCHAR(50) ,
	salary INT ,
	dept VARCHAR(50) 
	)

	go
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
	(15, 'Wayne', 'Male', 6800, 'Finance')

	go
	SELECT *  FROM Department
--#################################################################
	Create table emp 
	( empid int, ename varchar(20), eage int , dob date)


	Create table dep  
	(depid int ,empname varchar(20),salary int ,age int  ,
	Company varchar(20) Default 'IBM')

	INSERT INTO EMP  values 
	(101,'ALPHA',21,'2010-08-11') ,
	(103,'BETA',22,'2009-08-11'),
	(102,'CHARLIE',21,'2010-08-11'),
	(105,'DELTA',25,'2008-08-11'),
	(106,'ECHO',23,'2006-08-11'),
	(104,'FOX',21,'2004-08-11'),
	(109,'CHARLIE',24,'2010-08-11'),
	(107,NULL,25,'2008-08-11')


	insert into dep  values 
	(101,'Alpha',6000,21,'Vendor'), 
	(102,'fox',7000,21,'Vendor'), 
	(105,'Echo',5100,29,'Vendor'),
	(103,'beta',5100,29,'Vendor'),
	(104,'fox',5100,21,'Vendor'), 
	(105,'tim',5100,25,'Vendor')

	select * from emp 
	select * from dep 

--All queries combined using a UNION, INTERSECT or EXCEPT operator 
--must have an equal number of expressions/column in their target lists.
--Operand type clash: int is incompatible with date

--union all (Combine + duplicate values)


	
	
	select depid,empname,age	  from dep 
	union all
	select empid,ename,eage  from emp 
	
	select empid,ename,eage  from emp 
	union all
	select depid,empname,age from dep order by empid asc

--union   (Combine + UNIQUE values)	
	select empid,ename,eage  from emp 
	union  
	select depid,empname,age from dep order by empid asc

--intersect  (matching  + Unique values)
	select empid,ename,eage  from emp 
	intersect  
	select depid,empname,age from dep order by empid asc

--Except   (minus Unique values)

	select empid,ename,eage  from emp 
	Except  
	select depid,empname,age from dep order by empid asc


--#######################################################
-- Function 
--String function 
	use AdventureWorks2022

--Aggregate(Count, max , min , avg , sum)

--String 'dat '

--datetime

--COnversion

--Windows
	use AdventureWorks2022
	select BusinessEntityID, FirstName, LastName from Person.Person 


--len(expression/column name)
	select FirstName,len(FirstName)  as lengths from Person.Person 
	select len('Charles')
	select len('Ch ar le s')
	select len('  Ch ar le s    ')

--trim(expression) remove the lead and trial spaces 
	select len('  Ch ar le s    ')
	select trim('  Ch ar le s    ')
	select len(trim('  Ch ar le s    '))


--Left(expression, n) & Right(expression, n)
	select BusinessEntityID, FirstName 
	, left(FirstName,1), right(firstname,1)
	from Person.Person 

	select BusinessEntityID, FirstName 
	, left(FirstName,10), right(firstname,6)
	from Person.Person 

--Upper(expression) and lower(expression)

	select BusinessEntityID, FirstName 
	,upper(FirstName), lower(FirstName)
	from Person.Person 

--Concat(expression,expression,expression,...)

	select BusinessEntityID, FirstName,MiddleName, LastName ,
	concat(FirstName,MiddleName, LastName ) as Fullname
	from Person.Person 
	
	select BusinessEntityID, FirstName,MiddleName, LastName ,
	concat(FirstName,' ',MiddleName,' ', LastName ) as Fullname
	from Person.Person 

	select BusinessEntityID, FirstName,MiddleName, LastName ,
	concat(FirstName,';',MiddleName,';', LastName ) as Fullname
	from Person.Person 
--Concat_ws('',expression,expression,expression,...)

	select BusinessEntityID, FirstName,MiddleName, LastName ,
	concat_ws(';',FirstName,MiddleName, LastName ) as Fullname
	from Person.Person 
	select BusinessEntityID, FirstName,MiddleName, LastName ,
	concat_ws(' ',FirstName,MiddleName, LastName ) as Fullname
	from Person.Person 

--Scenario
	--Input = syed  or aLPha or aLExen
	--Output =Syed
	declare @name varchar(30)
	set @name ='aLPha'
	select @name,concat(upper(left(@name,1)), lower(right(@name, len(@name)-1)))

--####################################################
--replace ( string , old value, new value)

	select replace ('Hello 123 World', '123', 'SQL')

	
	select replace ('Hello 123 World', ' 123 ', '')

	select BusinessEntityID, FirstName, LastName ,
	replace(FirstName, 'e', '111111111111111')
	from Person.Person 


--STUFF ( string, start, length, new_string )
Hello 123 World
123456789012345678
Hello SQL123 World
 
	select stuff ('Hello 123 World',7,0,'SQL')
alphabeta@gmail.com
1234567890123456789
	select stuff ('alphabeta@gmail.com',6,0,'.')

Hello 123 World
123456789012345678
Hello SQL123 World
	select stuff ('Hello 123 World',7,0,'SQL')
	
	select stuff ('Hello 123 World',7,3,'SQL')
	
	select stuff ('Hello 123 World',7,4,'SQL')

	select stuff ('Hello 123 World',7,9,'SQL')

--CHARINDEX ( substring, string, [start_position] ) 
alphabeta@gmail.com
1234567890123456789

1234-5689
123456789

	select CHARINDEX ('@','alphabeta@gmail.com')
	select CHARINDEX ('-','1234-5689')
	
	select CHARINDEX ('j','demo tom john')
	select CHARINDEX ('m','demo tom john')
	select CHARINDEX ('m ','demo tom john')
	select CHARINDEX ('oh','demo tom john')
	select CHARINDEX ('om','demo tom john')

demo tom john
1234567890123 
	select CHARINDEX ('o','demo tom john',6)

--SUBSTRING ( string, start, length )

demo tom john
1234567890123 
	select  SUBSTRING ( 'demo tom john',1,4)
	select  SUBSTRING ( 'demo tom john',6,3)
	select  SUBSTRING ( 'demo tom john',10,4)




	select BusinessEntityID, FirstName,MiddleName, LastName ,
	SUBSTRING ( FirstName,1,4)
	from Person.Person 




	create table datas
	(email varchar(100))


	INSERT INTO datas (email) VALUES 
	('jane.doe@example.com'),
	('john.smith@workmail.net'),
	('alex.jones@university.edu'),
	('lisa.wong@techhub.org'),
	('mike.brown@services.co.uk'),
	('sara.lee@marketplace.com'),
	('dave.wilson@creativeagency.us'),
	('emily.harris@globalenterprise.com'),
	('carlos.garcia@networksolutions.es'),
	('anna.zhao@researchinst.cn');

	select * from datas

	--Scenarios 
	--input--> jane.doe@example.com
	--output--> example.com

	
	select email, SUBSTRING(email,	charindex('@',email)+1,len(email)) as domain
	from datas




--###############################
CREATE TABLE Transactions (
    custname VARCHAR(50),
    tran_date DATE
);

INSERT INTO Transactions (custname, tran_date) VALUES
('J', '2025-02-20'),
('X', '2025-02-20'),
('E', '2025-02-20'),
('E', '2025-02-21');


select * from transactions
where tran_date= '2025-02-20' and tran_date='2025-02-21'



select * from transactions
where tran_date in( '2025-02-20'  ,'2025-02-21')  AND custname='Satyam'

select * from transactions
where tran_date between '2025-02-20' and'2025-02-21'



select * from transactions
where custname IN (SELECT custname FROM transactions  GROUP BY custname HAVING COUNT(*)>1)



SELECT custname FROM transactions 
WHERE tran_date in( '2025-02-20'  ,'2025-02-21') 
GROUP BY custname 
HAVING COUNT(DISTINCT tran_date )>1

--###############################
--Date Time 'yyyy-MM-dd hh:mm:ss'
	--Date(Year, month, day, quarter, week, weekday, day of year)
	--Time (Hours, minutes, second, miliseconds, microseconds, nanoseconds)

	use AdventureWorks2022
	SELECT BusinessEntityID,BirthDate,HireDate FROM HumanResources.Employee

	SELECT BirthDate,
	 YEAR(BirthDate) AS yEARS,
	 MONTH(BirthDate) AS MONTHS,
	 DAY(BirthDate) AS DAYS
	FROM HumanResources.Employee



-- System time (laptop machine)
	SELECT GETDATE()
	SELECT sysdatetime()

--time offset

	SELECT sysdatetimeoffset()

	select * from sys.time_zone_info
	   	  

	select 	year('2025-02-22 02:13:54.927'),month('2025-02-22 02:13:54.927'),day('2025-02-22 02:13:54.927')

--Datename ( date and time parts - returns nvarchar )

	select Datename(YEAR,getdate())
	select Datename(MONTH,getdate())
	select Datename(DAY,getdate())
	select Datename(DAYOFYEAR,getdate())
	select Datename(WEEK,getdate())
	select Datename(WEEKDAY,getdate())
	select Datename(QUARTER,getdate())

	select Datename(HOUR,getdate())
	select Datename(MINUTE,getdate())
	select Datename(SECOND,getdate())
	select Datename(MILLISECOND,getdate())
	select Datename(MICROSECOND,getdate())
	select Datename(NANOSECOND,getdate())
	
--DATEPART()returns an integer corresponding to the datepart specified
	SELECT  Datepart(year,GETDATE() )
	SELECT  Datepart(MONTH,GETDATE() )
	SELECT  Datepart(DAY,GETDATE() )
	SELECT  Datepart(DAYOFYEAR,GETDATE() )
	SELECT  Datepart(WEEK,GETDATE() )
	SELECT  Datepart(WEEKDAY,GETDATE() )
	SELECT  Datepart(QUARTER,GETDATE() )

	SELECT  Datepart(HOUR,GETDATE() )
	SELECT  Datepart(MINUTE,GETDATE() )
	SELECT  Datepart(SECOND,GETDATE() )
	SELECT  Datepart(MILLISECOND,GETDATE() )
	SELECT  Datepart(MICROSECOND,GETDATE() )
	SELECT  Datepart(NANOSECOND,GETDATE() )

--DateDiff( DATEPART, lowerdate, higherdate )
--returns an integer corresponding

	SELECT BusinessEntityID,BirthDate,HireDate,
	DateDiff( year, BirthDate, HireDate ) as [Year],
	DateDiff( MONTH, BirthDate, HireDate ) as [Month],
	DateDiff( day, BirthDate, HireDate ) as [day],
	DateDiff( WEEK, BirthDate, HireDate ) as[week],
	DateDiff( WEEKDAY, BirthDate, HireDate ) as[WEEKDAY],
	DateDiff( QUARTER, BirthDate, HireDate ) as[QUARTER],
	DateDiff( hour, BirthDate, HireDate ) as[hour],
	DateDiff( MINUTE, BirthDate, HireDate ) as[MINUTE] 
	FROM HumanResources.Employee

--dateadd(datepart, number, date)

	SELECT BusinessEntityID,BirthDate,HireDate, 
	dateadd( year, 2, HireDate ) as [Year],
	dateadd( MONTH, 150, HireDate ) as [Month],
	dateadd( day, 579, HireDate ) as [day],
	dateadd( WEEK, 33, HireDate ) as[week],
	dateadd( WEEKDAY, 52, HireDate ) as[WEEKDAY]
	FROM HumanResources.Employee
	 
	SELECT BusinessEntityID,BirthDate,HireDate, 
	dateadd( year, -2, HireDate ) as [Year],
	dateadd( MONTH, -50, HireDate ) as [Month],
	dateadd( day, -79, HireDate ) as [day],
	dateadd( WEEK, -3, HireDate ) as[week],
	dateadd( WEEKDAY, -52, HireDate ) as[WEEKDAY]
	FROM HumanResources.Employee
--##################################

--Scenarios 
--hint(Parsename)
	--Input =Syed E Abbas
	--output 
		--c1=Syed	
		--c2=E	
		--c3=Abbas	

--Scenarios
	--Input SSN: '123-45-6789'
	--Expected Output Masked SSN: '***-**-6789'

--Scenarios
	--Input Product Code: 'ABC-123-XYZ'
	--Expected Output New Product Code: 'ABC-789-XYZ'
--Scenarios
	--Input Full Name: 'John A. Doe'
	--Expected Output Initials: 'JAD'

--Scenarios
	--Input Phone Number: '1234567890'
	--Expected Output Formatted Phone Number: '(123) 456-7890'


-- Set Operators Questions AdventureWorks2022

--1. UNION:
--   - Question: Write a query to list all `BusinessEntityID` values that appear in either the `Person.Person` table or the `Sales.Customer` table, or both.

--2. UNION ALL:
--   - Question: Write a query to list all `BusinessEntityID` values, including duplicates, from both the `Person.Person` table and the `Sales.Customer` table.

--3. INTERSECT:
--   - Question: Write a query to find all `BusinessEntityID` values that are present in both the `Person.Person` table and the `Sales.Customer` table.

--4. EXCEPT:
--   - Question: Write a query to find all `BusinessEntityID` values that are present in the `Person.Person` table but not in the `Sales.Customer` table.

--5. UNION with additional columns:
--   - Question: Write a query to list all `FirstName` and `LastName` combinations from both the `Person.Person` table and the `HumanResources.Employee` table. Ensure there are no duplicates.

--6. UNION ALL with filtering:
--   - Question: Write a query to list all `EmailAddress` values from the `Person.EmailAddress` table and `Sales.SalesPersonEmailAddress` table, including duplicates.

--7. INTERSECT with condition:
--   - Question: Write a query to find all `ProductID` values that are in both the `Sales.SalesOrderDetail` table and the `Production.Product` table and have a `ProductID` less than 1000.

--8. EXCEPT with condition:
--   - Question: Write a query to find all `SalesOrderID` values in the `Sales.SalesOrderHeader` table that are not in the `Sales.SalesOrderDetail` table and where the `OrderDate` is in the year 2022.

--9. Complex UNION:
--   - Question: Write a query to combine the `Name` from `Production.Product` and `Production.ProductSubcatery` tables. Ensure that the combined list is unique.

--10. Complex EXCEPT:
--    - Question: Write a query to list all `EmployeeID` values from the `HumanResources.Employee` table that do not appear in the `Sales.SalesOrderHeader` table, ensuring that the list only includes active employees.












































