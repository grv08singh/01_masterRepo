--Function (  conversion , windows function, CTE ),USER DEFINED (Table valued & Scalar valued function  )
--view and procedure 
--#######################################################
--Self learning  
	https://learn.microsoft.com/en-us/sql/t-sql/queries/with-common-table-expression-transact-sql?view=sql-server-ver16
	https://learn.microsoft.com/en-us/training/modules/transform-data-by-implementing-pivot-unpivot-rollup-cube/
	https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver16
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
--##################################
--Conversion
	--data type -->
		--Numeric-->string -->numeric -->datetime 
		--string-->string -->datetime 
		--datetime-->string -->datetime 

	select 1+2

	select 'a'+'b'

	select 'a'+2

	select BusinessEntityID,LoginID  
	from AdventureWorks2022.HumanResources.Employee
		
	select BusinessEntityID,LoginID,
	BusinessEntityID +LoginID 
	from AdventureWorks2022.HumanResources.Employee

--Conversion
--CAST ( expression AS target_data_type )
	
	select 'a'+cast(2 as char)

	select BusinessEntityID,LoginID,	cast(BusinessEntityID as varchar) +LoginID
	from AdventureWorks2022.HumanResources.Employee
--CONVERT ( target_data_type, expression , [style] )
		
	select 'a'+CONVERT( char,2)

	select BusinessEntityID,LoginID,	convert( varchar,BusinessEntityID) +LoginID
	from AdventureWorks2022.HumanResources.Employee
https://www.mssqltips.com/sqlservertip/1145/date-and-time-conversions-using-sql-server/
--getdate()
	
	select  cast(getdate() as varchar(11))
	 
		
	select  CONVERT( varchar(11),getdate())

--datetime	
	select getdate(), cast(getdate() as varchar)
	select getdate(), convert(varchar,getdate() )
	

	select convert(varchar,GETDATE(),1)
	select convert(varchar,GETDATE(),4)
	select convert(varchar,GETDATE(),5)
	select convert(varchar,GETDATE(),6)
	select convert(varchar,GETDATE(),11)
	select convert(varchar,GETDATE(),21)
	select convert(varchar,GETDATE(),33)
	select convert(varchar,GETDATE(),35)
	select convert(varchar,GETDATE(),104)

	select convert(varchar,GETDATE(),8)
	select convert(varchar,GETDATE(),9)
	select convert(varchar,GETDATE(),24)
	select convert(varchar,GETDATE(),108)

	 select CONVERT(varchar, GETDATE(),0)
	 select CONVERT(varchar, GETDATE(),13)
	 select CONVERT(varchar, GETDATE(),20)
	 select CONVERT(varchar, GETDATE(),21)
	 select CONVERT(varchar, GETDATE(),27)
	 select CONVERT(varchar, GETDATE(),127)
	  
--FORMAT(expression, format, [culture])
	select BusinessEntityID,Rate,
	FORMAT(rate, 'c', 'en-in') as INR,
	FORMAT(rate, 'c', 'en-us') as us,
	FORMAT(rate, 'c', 'en-gb') as gb
	from AdventureWorks2022.HumanResources.EmployeePayHistory

--'yyyy-dd-MM hh-mm-ss'

	select  getdate() 
	select  format(getdate(),'yyyy-dddd-MMMM hh-mm-ss')

	select  format(getdate(),'yyy-ddd-MMM hh-mm-ss')

	select  format(getdate(),'yy-dd-MM hh-mm-ss')
	   	
	select  format(getdate(),'ddd-MMMM-yy')

	
	select  format(getdate(),'MMM-yy, dddd')

	
	select  format(getdate(),'yyy-ddd-MMM hh:mm:ss tt')

--############################################################
--Windows  function(ranking function ) 
--ranking_function() over(partition by  columnname  order by columnname asc/desc)
--partition by = group by 


	select  did ,salary 
	,RANK() over(order by salary desc) as Ranks
	,Dense_RANK() over(order by salary desc) as denseRanks
	,Row_number() over(order by salary desc) as rownum
	from Department 

	   
	select  did ,salary  
	,Row_number() over(order by salary desc) as rownum
	from Department 

	select  did ,salary 
	,RANK() over(order by salary desc, did asc) as Ranks 
	from Department 


--NTILE(n) over(partition by  columnname  order by columnname asc/desc)


	select  did ,salary  
	,NTILE(5) over(order by salary desc) as tiles
	from Department 

	select  did ,salary  
	,NTILE(4) over(order by salary desc) as tiles
	from Department 

--LAG(column_name, offset, default_value) OVER (PARTITION BY column_name ORDER BY column_name)
--Lag --Previous row 

	select  did ,salary  
	,lag(salary) over(order by salary desc) as lags
	from Department
	
	select  did ,salary  
	,lag(salary,1,1234) over(order by salary desc) as lags
	from Department
	
	select  did ,salary  
	,lag(salary,3,1234) over(order by salary desc) as lags
	from Department

	select  did ,salary,lag(salary,1,0) over(order by salary desc) as lags,
	salary -lag(salary,1,0) over(order by salary desc) as diff
	from Department


 --LEAD(column_name, offset, default_value) OVER (PARTITION BY column_name ORDER BY column_name)
 --Lead() -- next row

 
	select  did ,salary  
	,LEAD(salary) over(order by salary desc) as leads
	from Department
	
	select  did ,salary  
	,LEAD(salary,1,1234) over(order by salary desc) as leads
	from Department
	
	select  did ,salary  
	,LEAD(salary,3,1234) over(order by salary desc) as leads
	from Department

	select  did ,salary,LEAD(salary,1,0) over(order by salary desc) as leads,
	salary -LEAD(salary,1,0) over(order by salary desc) as diff
	from Department

--Find high salary based on their rank =3

	   
	select  did ,salary  
	,Row_number() over(order by salary desc) as rownum
	from Department 
	where Row_number() over(order by salary desc)=3

--error message 
	--Windowed functions can only appear in the SELECT or ORDER BY clauses.

---###########################################################
 --CTE(Common table experssion)
  /* --Temporary result set in SQL Server( SELECT, INSERT, UPDATE, or DELETE)
  WITH CTE_Name (Column1, Column2, ...)
	AS
	(
		-- CTE query
		SELECT Column1, Column2, ...
		FROM TableName
		WHERE Condition
	)
	-- Main query referencing the CTE
	SELECT *	FROM CTE_Name;


 */

 
--Find high salary based on their rank =3
--scenario 1
	with highsal 
	as		
	(	select  did ,salary,Row_number() over(order by salary desc) as rownum from Department 		)

	select * from highsal where rownum =3


--scenario 2
	with groups  	as		
	(		select  did ,salary ,NTILE(5) over(order by salary desc) as tiles 	from Department 		)

	select * from groups where tiles =2

	
	select * from (
	select  did ,salary  
	,Row_number() over(order by salary desc) as rownum
	from Department 
	)  abc where abc.rownum=2
	


	go

	with highsal 
	as		
	(	select  did ,salary,Row_number() over(order by salary desc) as rownum from Department 		)

	select * from highsal where rownum =3


--scenario 3

--Find dept  high salary based on their rank =3

	select  did ,salary,dept,Row_number() over(  partition by dept  order by salary desc) as rownum from Department 


	with deptsal 
	as		
	(select  did ,salary,dept,Row_number() over(  partition by dept  order by salary desc) as rownum from Department )

	select * from deptsal where rownum =1





--duplicate records
	select  * from Department  order by did asc


--== duplicate records 
	with duprec 
	as 
	(	select  did ,salary,dept,Row_number() over(  partition by did  order by did asc) as rownum from Department )
	select * from duprec  where rownum>1


--== unique records 

	with duprec 
	as 
	(	select  did ,salary,dept,Row_number() over(  partition by did  order by did asc) as rownum from Department )
	select * from duprec  where rownum=1



--== remove duplicate records 
	with duprec 
	as 
	(	select  did ,salary,dept,Row_number() over(  partition by did  order by did asc) as rownum from Department )
	delete from duprec  where rownum>1



--
	with lowsal
	as
		(select top 1 * from Department  order by salary asc)
	select * from lowsal

	go


	with highsal
	as
		(select   top 1 * from Department  order by salary desc)
	select * from highsal

--combine two cte together
with 
	lowsal
		as		(select top 1 * from Department  order by salary asc)

	,highsal
		as 		(select   top 1 * from Department  order by salary desc)
	
		select * from lowsal
		union all
		select * from highsal




--##########################################
--User defined function
	--Scalar valued function 
	/*syntax
	CREATE FUNCTION function_name (@parameter1 datatype [, @parameter2 datatype, ...])
	RETURNS DATATYPE
	AS
	RETURN (
				-- A single SELECT statement
				SELECT column1, column2, ...
				FROM tables   WHERE conditions
			)

*/
--CUBE OF A NUMBER 
	declare @num int
	set @num=5
	set @num=@num*@num*@num
	select @num

--CREATE FUNCTION
	CREATE FUNCTION cubes()
	returns int
	as
	begin	
		declare @num int
		set @num=5
		set @num=@num*@num*@num
		return @num
	end

--call function 
	select dbo.cubes()

--Alter function 

	Alter FUNCTION cubes(@num float)
	returns float
	as
	begin	 
		return @num*@num*@num
	end

--call function 
	select dbo.cubes(4)

	select dbo.cubes(15.4)

	select dbo.cubes(93.8)

	select dbo.cubes(2.64)





	
--call function 
	select dbo.cubes() 

--########################################
	 CREATE TABLE Products
	(
		ProductID INT PRIMARY KEY,
		ProductName VARCHAR(255),
		Price DECIMAL(10, 2),
		AgeInMonths INT
	);

	INSERT INTO Products (ProductID, ProductName, Price, AgeInMonths) VALUES
	(1, 'Laptop', 1000.00, 5),
	(2, 'Tablet', 450.00, 9),
	(3, 'Smartphone', 800.00, 15),
	(4, 'Monitor', 300.00, 30);

	select * from products


--dp=price - (price * dis/100)

create function DP(@price float, @dis float)
returns float
 as 
  begin
	return @price - (@price * @dis/100)
  end 



  
	select *, dbo.dp(price, 15.80) as newprice from products


---conditional statement  
	if 1=1
		print'true'
	else
		print'false'
--####################
	if 1=10
		print'true'
	else
		print'false'
--####################











































































