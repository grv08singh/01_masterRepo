--order by ,top offset fetch, aggregate functions,group by having 
--Constraint ( not null , check,default ), index , clustered , non clustered
 --##################################################################
 --Self learning  
	https://learn.microsoft.com/en-us/training/modules/transform-data-by-implementing-pivot-unpivot-rollup-cube/

	https://learn.microsoft.com/en-us/sql/t-sql/functions/functions?view=sql-server-ver16

	https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described?view=sql-server-ver16

---########################################################
	create database Demo	
	go
	use Demo	
	go
	CREATE TABLE Department
	(
		did INT,
		ename VARCHAR(50) ,
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
	(8, 'Vince', 'Female', 6600, 'IT'),
	(9, 'Jane', 'Female', 5400, 'Marketing'),
	(15, 'Wayne', 'Male', 6800, 'Finance'),	
	(null,null, null, null,null)
	
	INSERT INTO Department  VALUES 
	(-5, 'Shane', 'Female',  -121, 'Finance'),
	(6, 'Shed', 'Male', 8000, 'Sales')

	select * from department 

--#############################################

--COLUMN SORT --> ASC /DESC
--Order by column asc, column desc

	select * from department ORDER BY DID ASC		
	select * from department ORDER BY ENAME ASC	
	select * from department ORDER BY SALARY ASC

	select * from department ORDER BY DID DESC		
	select * from department ORDER BY ENAME DESC	
	select * from department ORDER BY SALARY DESC
	
	select * from department ORDER BY DID ASC, ENAME ASC	

	USE AdventureWorks2022

	select   FirstName, LastName	from person.person
	--WHERE FirstName='Aaron'
	ORDER BY FirstName ASC, LASTNAME  DESC
--###################################
--Top offset fetch

	select * from person.person

--TOP n
	select TOP 1 * from person.person
	
	select TOP 10 * from person.person

	select TOP 5 FirstName from person.person

	select TOP 10 FirstName, LastName from person.person

--HiGHEST ID 
	
	select TOP 1 * from person.person ORDER BY BusinessEntityID DESC
--LOWID 
	
	select TOP 1 * from person.person ORDER BY BusinessEntityID ASC

--OFFSET(SKIP) & fetch 
		--SELECT column1, column2, ...
		--FROM table_name
		--ORDER BY column_name
		--OFFSET n ROWS       -- Skip the first 'n' rows
		--FETCH NEXT m ROWS ONLY; -- Then fetch the next 'm' rows

--2ND HIGH RECORD
	select * from person.person 
	ORDER BY BusinessEntityID DESC
	OFFSET 1 ROWS
--3RD HIGH RECORD
	select * from person.person 
	ORDER BY BusinessEntityID DESC
	OFFSET 1 ROWS
--#######################################
--A TOP can not be used in the same query or sub-query as a OFFSET.
	select  * from person.person 
	ORDER BY BusinessEntityID DESC
	OFFSET 1 ROWS
	FETCH NEXT 1 ROWS ONLY

	select  * from person.person 
	ORDER BY BusinessEntityID DESC
	OFFSET 10 ROWS
	FETCH NEXT 5 ROWS ONLY
---######################################
--Aggregate function 

--COUNT(*): Counts the number of rows in a dataset include the null values .
	select  cOUNT(*) AS Counts from person.person 

--COUNT(column_name) counts non-NULL values in a specified column.
	select  cOUNT(BusinessEntityID) AS Counts from person.person 
	select  cOUNT(FirstName) AS Counts from person.person 
	select  cOUNT(MiddleName) AS Counts from person.person 
--MAX(): Returns the maximum value from a column.(non-NULL values in a specified column.)
	select  MAX(BusinessEntityID) AS Maxval from person.person 
	select  MAX(FirstName) AS Maxval from person.person 
	select  MAX(ModifiedDate) AS Maxval from person.person 

--MIN(): Returns the MINIMUM VALUE from a column.(non-NULL values in a specified column.)
	select  MIN(BusinessEntityID) AS MINval from person.person 
	select  MIN(FirstName) AS MINval from person.person 
	select  MIN(ModifiedDate) AS MINval from person.person 

--Sum()  & average() (work with numeric data only)
--SUM(): Adds together all the values in a specific column.(non-NULL values in a specified column.)
	select  SUM(BusinessEntityID) AS total from person.person 

--AVG(): Calculates the average of a set of values in a column.(non-NULL values in a specified column.)
	select  AVG(BusinessEntityID) AS avgval from person.person 

	use demo

	select 	Count(*) as Counts,	MAX(did) as Maxval ,	
	Min(did) as Minval ,	avg(did) as Avgal ,	sum(salary) as Total  
	FROM Department

--#############################
 --group by -- having 
 --break the resultset into subsets
 select did,ename,gender,salary,dept from Department
 
 select did from Department group by did
 
 select  ename from Department group by ename

 select  salary from Department group by salary
 
 select  gender from Department group by gender
select  dept from Department group by dept
 

--group with agg function 
	select  gender, count(*) as COunts from Department group by gender
 
	select  dept, sum(salary) as total  from Department group by dept

	select  dept,gender, count(*) as COunts, sum(salary) as total 
	from Department group by dept,gender 
	   
	select  dept,gender, count(*) as COunts, sum(salary) as total 
	from Department
	group by dept,gender 
	having count(*)>2

	select  dept,gender, count(*) as COunts, sum(salary) as total 
	from Department
	group by dept,gender 
	having gender='female'
---###########
	select 
	top column 
	 from table 
	 where col=val 
	 group by col 
	 having col=val 
	 order by 
	 offset 
	 fetch


---#############################
  --LOGICAL PROCESSING ORDER OF THE SELECT  STATEMENT 
  --Sequence to execute in sql server 
  --FROM
  --ON 
  --JOIN
  --WHERE
  --GROUP BY 
  --WITH (CUBE/ ROLLUP)
  --HAVING 
  --SELECT 
  --DISTINCT
  --ORDER BY 
  --TOP 

--#################################################

	select * from Department order by did asc

--duplicate values		--> Unqiue 
--null values			--> not null
--values out of range	--> check
--default				--> default


	CREATE TABLE emp
	(
		did INT not null unique,
		ename VARCHAR(50)  not null ,
		gender VARCHAR(50)  not null ,
		salary INT  not null check (salary >=5000) ,
		phnum bigint not null check (len(phnum )=10) ,
		dept VARCHAR(50)  not null default 'value is unknown'
	)

--Table defintion 
	--Syntax: sp_help tablename 
	  sp_help emp


INSERT INTO emp  VALUES
	(11, 'David', 'Male',  5001, 1234567890,'Sales'),
	(5, 'Shane', 'Female',  5500,1234567899, 'Finance'),
	(6, 'Shed', 'Male', 8000,1234567899, 'Sales'),
	(7, 'Vik', 'Male', 7200,1234567899, 'HR')

	

-- Cannot insert duplicate key in object 'dbo.emp
	INSERT INTO emp  VALUES
	(11, 'David', 'Male',  5001, 1234567890,'Sales')

-- column does not allow nulls. INSERT fails.
	INSERT INTO emp  VALUES
	(null,null,null,  5001, 1234567890,'Sales')

--The INSERT statement conflicted with the CHECK constraint
	INSERT INTO emp  VALUES
	(111, 'David', 'Male',  4999, 1234567890,'Sales')

--The INSERT statement conflicted with the CHECK constraint
	INSERT INTO emp  VALUES
	(111, 'David', 'Male',  6999, 1267890,'Sales')
--Column name or number of supplied values does not match table definition.
	 INSERT INTO emp (did,ename,gender,salary,phnum) VALUES
	(22, 'David', 'Male',  6999, 1234567890)

		select * from emp

	INSERT INTO emp (did,ename,gender,salary,phnum) VALUES
	(33, 'Dave', 'feMale',  7999, 1934567890)

--##########################################
--nOT NULL 

	ALTER TABLE DEPARTMENT 
	ALTER COLUMN DID INt NOT NULL
	
	select * from DEPARTMENT

--uNIQUE 
	ALTER TABLE DEPARTMENT 
	ADD CONSTRAINT DEP_UK UNIQUE(DID)
	
--CHECK 
	ALTER TABLE DEPARTMENT 
	ADD CONSTRAINT CK_SAL CHECK(SALARY >=5000)

--DEFAULT 
	ALTER TABLE DEPARTMENT 
	ADD CONSTRAINT DF_DEPT DEFAULT 'NOVALUE'  FOR DEPT

	
	ALTER TABLE DEPARTMENT 
	ADD CONSTRAINT DF_DEP1T DEFAULT 'NOVALUE'  FOR DEPT 
	
	ALTER TABLE DEPARTMENT 
	ADD CONSTRAINT DPDEP CHECK(DEPT LIKE '[A-Z]%')


--###############################################
--Execution plan =Cntrl+ M
--INDEX 
	SELECT * FROM DEPARTMENT  where did =1

--Index (search fast , improve the speed of read)
--B+ tree

--Clustered Index
	--Sort and store data  in  (existing & new records)
	--1 clustered index in 1 table
	-- improve the speed of read when searching

--Syntax: Create clustered Index Indexname  on tablename(column name Asc/desc)

	create clustered index ci_did on department(did)

	create clustered index ci_ename on department(ename)

	SELECT *  FROM DEPARTMENT  where did =1


--Cannot create more than one clustered index 
--Drop the existing clustered index 
	select ename from department where ename ='david'
--Non Clustered Index
	--999 non clustered index in 1 table
	-- improve the speed of read when searching

	create nonclustered index nci_ename on department(ename)
	
	select ename from department where ename ='david'
	
	select ename,salary,dept  from department where
	ename='Kate' and salary=7500 and dept='IT'

--composite index
	create nonclustered index nci_three on department(ename,salary,dept) 
	
	select ename,salary,dept  from department where
	 salary=7500 and ename='Kate' and dept='IT'

	select ename,salary,dept  from department where
	ename='Kate' and salary=7500  

	select ename,salary,dept  from department where
	ename='Kate'   and dept='IT'

	select ename,salary,dept  from department where
	ename='Kate'  


	
	select ename,salary,dept  from department where
	  salary=7500 and dept='IT'

--covering index 

































































































































































































































































































