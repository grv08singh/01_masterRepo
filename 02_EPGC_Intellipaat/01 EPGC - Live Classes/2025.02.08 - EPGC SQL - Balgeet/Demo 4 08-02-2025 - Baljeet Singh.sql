--schema, renaming, DML(select , INsert, update, delete, truncate), import/ export
--Filter(where is null, not,  between,like) 
--########################################################
https://learn.microsoft.com/en-us/sql/t-sql/queries/select-order-by-clause-transact-sql?view=sql-server-ver16
https://learn.microsoft.com/en-us/sql/t-sql/queries/where-transact-sql?view=sql-server-ver16
--######################################################### 
	CREATE DATABASE [demo] 
	 CONTAINMENT = NONE
	 ON  PRIMARY 
	( NAME = N'demo', 
	FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.DEMO\MSSQL\DATA\demo.mdf' , SIZE = 8192KB , FILEGROWTH = 65536KB )
	 LOG ON 
	( NAME = N'demo_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.DEMO\MSSQL\DATA\demo_log.ldf' , SIZE = 8192KB , FILEGROWTH = 65536KB )
	 WITH LEDGER = OFF

 --##################################################################
--organisation(HR, FIN, SAL, MAR)
	Create database organisation
	
	use organisation
	--########################################
--organisation(HR, FIN, SAL, MAR)
	Create database organisation
	
	
	use organisation
	--hr
	create table t1 (c1 int, c2 int)
	create table t2 (c1 int, c2 int)
	create table t3 (c1 int, c2 int)
	--fin
	create table t4 (c1 int, c2 int)
	create table t5 (c1 int, c2 int)
	create table t6 (c1 int, c2 int)
	--sales
	create table t7 (c1 int, c2 int)
	create table t8 (c1 int, c2 int)
	create table t9 (c1 int, c2 int)
	--mark
	create table t10 (c1 int, c2 int)
	create table t11 (c1 int, c2 int)
	create table t12 (c1 int, c2 int)

	--########################################


	Create database neworg
	
	use neworg
	--hr
	create schema HR
	create table hr.t1 (c1 int, c2 int)
	create table hr.t2 (c1 int, c2 int)
	create table hr.t3 (c1 int, c2 int)
	--fin
	create schema fin
	create table fin.t4 (c1 int, c2 int)
	create table fin.t5 (c1 int, c2 int)
	create table fin.t6 (c1 int, c2 int)
	--sales
	create schema sales
	create table sales.t7 (c1 int, c2 int)
	create table sales.t8 (c1 int, c2 int)
	create table sales.t9 (c1 int, c2 int)
	--mark
	create schema mark
	create table mark.t10 (c1 int, c2 int)
	create table mark.t11 (c1 int, c2 int)
	create table mark.t12 (c1 int, c2 int)

-- database.schemaname.tablename
--################################################################
	Create database Demo 

	use Demo

	create table department 
	(eid int, ename varchar(20), age tinyint, gender char(10), salary decimal(10,2))

--Renaming 
--Rename a database 
	--Syntax: ALTER DATABASE OldDatabaseName MODIFY NAME = NewDatabaseName
	
	alter database [Demo] modify name =Advent

--Caution: Changing any part of an object name could break scripts and stored procedures.		

--Rename a Table 
	--Syntax: EXEC sp_rename 'SchemaName.OldTableName', 'NewTableName'
	use Advent
	EXEC sp_rename 'dbo.department', 'records'

--Definiton of the stored procedure 
--sp_helptext sp_rename 

--Rename a Column  
	--Syntax: EXEC sp_rename 'OldTableName.ColumnName', 'ColumnName','Column '
	EXEC sp_rename 'records.eid', 'emp_id','Column '


--####################################################
	Create database SQLDemo 

	use SQLDemo
	
	create table department 
	(eid int, ename varchar(20), age tinyint, gender char(10), salary decimal(10,2))

--####################################################
--DML(Data Manipulation language)
--Select 
	--Syntax: Select Column1,column2, column3,.... from table 
	
	select eid,ename,age, gender,salary From department

	select eid From department
	
	select age, gender,eid,ename,salary From department

	select * From department
	
	
--Insert
	--Syntax: 
	--Insert into  table(Column1,column2, column3,....)
	--values(value1,value2, value3,....)
	
	Insert into  department(eid,ename,age, gender,salary)
	values(101,'alpha',21,'Male',1232 )

	Insert into  department(age, gender,eid,ename,salary)
	values(22,'feMale',102,'beta' ,23423 )
	   	  
	Insert into  department	values
	(103,'charles',23,'Male',34543 )
	
	Insert into  department	values
	(108,'fox',24,'female',654334),
	(106,'echo',24,'female',45774),
	(105,'delta',23,'male',654334),
	(107,'tom,',26,'male',98765)

	
	Insert into  department	values
	(110,'charles',23,'123',98765)

--Column name or number of supplied values does not match table definition.

	Insert into  department(eid,salary)	values
	(104,34543 )

--values = empty/absent / not available == NULL

	Insert into  department	values
	(109,'null',null,null,34543 )

	Insert into  department	values
	(null,null,null,null,null )

--####################################################	


--UPDATE( modify the table-data)
/*Syntax:
	update tablename 
	set column=value,column=value,.....
	where column=value
*/

	update department
	set gender='male'
	where eid =110


	update department
	set ename ='john',gender='male',age =29
	where eid =109

	update department
	set eid=111,ename ='rave',gender='male',age =29, salary =8754
	where eid is null
	
	
	update department
	set ename ='john',gender='male',age =29
	where eid =104
	
	update department
	set ename ='john' ,age =29, salary =8754
	where gender='male'

--######################################
--delete (remove a records/ multiple records from table )
	--syntax : delete from tablename where COLUMN=value 
	   
	delete from department	where eid =101
	
	delete from department	where eid  in (102,103,110)
	
	delete from department

--######################################
--Truncate (remove all records from table )
	--Syntax: Truncate table tablename
	Truncate table department where eid =101

	select * From department
--######################################
	Create table test
	(id int, ename varchar(20), phnum int)

	insert into test values 
	(101, 'alphabetacharlie',3456789)
	go 5000
--Go (n)


	select  * from test
 

---capture the time to Delete
	DECLARE @StartTime_Delete DATETIME2 = SYSDATETIME(); --capture start time 
	delete from  test
	DECLARE @EndTime_Delete DATETIME2 = SYSDATETIME(); --capture end time 
	SELECT 'Time taken to delete : ' + CONVERT(VARCHAR(20), DATEDIFF(MILLISECOND, @StartTime_Delete, @EndTime_Delete)) + ' milliseconds';

	--Time taken to delete : 41 milliseconds
	--Time taken to Truncate : 6 milliseconds

---capture the time to Truncate
	DECLARE @StartTime_Delete DATETIME2 = SYSDATETIME(); --capture start time 
	Truncate table test
	DECLARE @EndTime_Delete DATETIME2 = SYSDATETIME(); --capture end time 
	SELECT 'Time taken to Truncate : ' + CONVERT(VARCHAR(20), DATEDIFF(MILLISECOND, @StartTime_Delete, @EndTime_Delete)) + ' milliseconds';

---##############################
--IMPORT Export
	create database ImportExport


	use ImportExport
	select * from [import_export- data-txt] 

	select * from [dbo].[import_export- datas-csv]

	select * from [dbo].[Sheet1$]

--#########################################
	USE AdventureWorks2022
	
	SELECT BusinessEntityID,FirstName,LastName,ModifiedDate FROM PERSON.PERSON
--where 
-- Comparison Operators
-- Equal ( = )
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID=111
	
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE FirstName='GIGI'
	
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE ModifiedDate ='2009-01-09 00:00:00.000'

-- Not equal (!=   or <> )
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID!=1
	
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE FirstName <> 'TERRI'
-- Greater than or equal to(>=  )

	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID>=20000
	
	
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE ModifiedDate >='2014-01-09 00:00:00.000'

-- Less than or equal to(<= )

	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID<=100
	
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE ModifiedDate <='2007-01-09 00:00:00.000'


--#############################
--Where columnName =value AND columnName =value and columnName =value AND columnName =value ......

	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID=10
	
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE FirstName='Michael'	
	
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID=10 AND  FirstName='Michael'
		
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID=10 AND  FirstName='Michael' AND ModifiedDate='2009-04-26 00:00:00.000'
	
--Where columnName =value or columnName =value or columnName =value or columnName =value ......


	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID=10
	
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE FirstName='Michael'	
	
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID=10 OR  FirstName='Michael'
		
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID=10 AND  FirstName='Michael' AND ModifiedDate='2009-04-26 00:00:00.000'
	
	
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE 
	BusinessEntityID=1  OR
	BusinessEntityID=11 OR
	BusinessEntityID=111 OR
	BusinessEntityID=1111 OR
	BusinessEntityID=11111 OR
	BusinessEntityID=111111 


		 
	select BusinessEntityID,FirstName,LastName,ModifiedDate from Person.Person
	where
	firstname ='Thomas' or
	firstname ='Eugene' or
	firstname ='Andrew' or
	firstname ='Ruth' or
	firstname ='Barry' or
	firstname ='Sidney'

--##########################################
--WHERE COLUMN IN (VALI, VAL2, VAL3 ,....)
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID IN (1,11,111,1111,11111)
		 
	select BusinessEntityID,FirstName,LastName,ModifiedDate from Person.Person
	where firstname  IN('Thomas' ,'Eugene' ,'Andrew' ,'Ruth' ,'Barry' ,'Sidney')



--WHERE COLUMN noT  IN (VALI, VAL2, VAL3 ,....)



	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID  NOT IN (1,2,3,4,5)
		 
	select BusinessEntityID,FirstName,LastName,ModifiedDate from Person.Person
	where firstname NOT IN('Thomas' ,'Eugene' ,'Andrew' ,'Ruth' ,'Barry' ,'Sidney')

--Where is null or is not null
	select BusinessEntityID,FirstName,MIDDLENAME,LastName,ModifiedDate from Person.Person
	where MiddleName IS NULL
		
	select * from Person.Person
	where MiddleName IS NOT NULL


--where  between  range value1 and value2 


	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE BusinessEntityID BETWEEN 1 AND 100

	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE  ModifiedDate BETWEEN '2008-12-22' AND '2009-01-09'



--Where like ( % _)

	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE  FirstName LIKE 'A%'

	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE  FirstName LIKE 'ALE%'
	
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE  BusinessEntityID LIKE '111%'
	
	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE  FirstName LIKE '%ED'

	SELECT BusinessEntityID,FirstName,
	LastName,ModifiedDate FROM PERSON.PERSON
	WHERE  FirstName LIKE '%OM%'
	
	
---#####################################################################################################


--QUESTION TO PRACTICE 
--step 1
	Create database school 
--step 2
	use school
--step 3

--1. Teachers Table:
	--Columns: TeacherID int, Name varchar(20), Age int , Class varchar(20)
	create table Teachers (TeacherID int, Name varchar(20), Age int , Class varchar(20))

--2. Students Table:
	--Columns: StudentID, FirstName, LastName, Age, Class, TeacherID
	
--3. Courses Table:
	--Columns: CourseID, CourseName, Department, TeacherID
	
--4. Departments Table:
	--Columns: DepartmentID, DepartmentName
	
--5. Enrollments Table:
	--Columns: EnrollmentID, StudentID, CourseID, EnrollmentDate
	
--6. Teachers_Departments Table:
	--Columns: TeacherDepartmentID, TeacherID, DepartmentID
	
----*****************************************************************************************
--practice question
 Create database hospital

 Use hospital

-- 1. Doctors Table:
   -- Columns: DoctorID, FirstName, LastName, Specialization, Age
  create table Doctors ( DoctorID int , FirstName varchar(20), LastName varchar(20), Specialization  varchar(20), Age int)
-
-- 2. Patients Table:
   -- Columns: PatientID, FirstName, LastName, Age, AdmissionDate, DischargeDate, DoctorID
   
-- 3. Departments Table:
   -- Columns: DepartmentID, DepartmentName, HeadDoctorID
   
-- 4. Nurses Table:
   -- Columns: NurseID, FirstName, LastName, Age, DepartmentID
   
-- 5. Medications Table:
   -- Columns: MedicationID, MedicationName, Dosage
   
-- 6. Prescriptions Table:
   -- Columns: PrescriptionID, PatientID, DoctorID, MedicationID, PrescribedDate, DosageInstructions
   











































































































































































































































































































































