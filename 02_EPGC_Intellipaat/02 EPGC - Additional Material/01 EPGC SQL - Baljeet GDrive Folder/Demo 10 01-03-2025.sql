--SQl server DML trigger , exception handling , cases,
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
	  SELECT * FROM Department
--#######################################################
--Trigger in SQL server (event  --> Action  is performed)

--DML(Insert, Update , delete)	--> Data --> table


--Two logical trigger in DML trigger 
		--Inserted (add a new records,new info will be records)
		--Deleted (removal old record,old info  will be records )
	/*
		Syntax:
			Create trigger TriggerName 
			on tablename 
			for insert, update, delete
			as 
			begin 
				--sql logic 
			end
	*/


-- freeze chnages 	--02-03-2025 (i, u, d)
	create trigger TG_freeze 
	on department  
	for insert, update, delete
	as 
		begin 
			if getdate()<'03-03-2025'
			begin 
				print 'all changes have been freezed'
				rollback
			end 
		end


	INSERT INTO Department  VALUES
	  (1, 'David', 'Male', 5000, 'Sales'),
	  (5, 'Shane', 'Female', 5500, 'Finance')

	delete FROM Department
	  
 
	  SELECT * FROM Department

-- Enable/ disable a trigger
	--Enable TRIGGER trigger_name ON table_name;
	--DISABLE TRIGGER trigger_name ON table_name;
	Enable TRIGGER TG_freeze ON Department;
	DISABLE TRIGGER TG_freeze ON Department;

---##############################################
--Trigger copy data from 1 table to another table
	SELECT * FROM Department

	CREATE TABLE Depthist
	(
		sno int identity(1,1),
		timestamps datetime default  getdate(),
		loginname varchar(20) default suser_name(),
		DMLOPS varchar(20),

		new_did INT,
		new_ename VARCHAR(50) ,
		new_gender VARCHAR(50) ,
		new_salary INT ,
		new_dept VARCHAR(50) ,
		
		old_did INT,
		old_ename VARCHAR(50) ,
		old_gender VARCHAR(50) ,
		old_salary INT ,
		old_dept VARCHAR(50) 
	)



--create trigger insert 
	create trigger TG_Insert 
	on department  
	for insert 
	as 
		begin 
			insert into Depthist(DMLOPS,new_did,new_ename,new_gender,new_salary,new_dept,old_did,old_ename,old_gender,old_salary,old_dept)
			select 'Insert',did,ename,gender,salary,dept, null, null, null, null, null from inserted
		end


--Perform insert
	INSERT INTO Department  VALUES
	  (1, 'David', 'Male', 5000, 'Sales'),
	  (5, 'Shane', 'Female', 5500, 'Finance'),
	  (6, 'Shed', 'Male', 8000, 'Sales'),
	  (7, 'Vik', 'Male', 7200, 'HR'),
	  (2, 'Jim', 'Female', 6000, 'HR')





--create trigger Delete 
	create trigger TG_Delete
	on department  
	for Delete 
	as 
		begin 
			insert into Depthist(DMLOPS,new_did,new_ename,new_gender,new_salary,new_dept,old_did,old_ename,old_gender,old_salary,old_dept)
			select 'Delete', null, null, null, null, null,did,ename,gender,salary,dept from deleted
		end

	SELECT * FROM Department

	SELECT * FROM  Depthist

delete FROM DEPARTMENT where gender='male'





--create trigger update 
	create trigger TG_Update
	on department  
	for Update 
	as 
		begin 
			insert into Depthist(DMLOPS,new_did,new_ename,new_gender,new_salary,new_dept,old_did,old_ename,old_gender,old_salary,old_dept)
			select 'Update', i.did, i.ename, i.gender, i.salary, i.dept,d.did,d.ename,d.gender,d.salary,d.dept 
			from deleted d inner join inserted i on i.did=d.did
		end

UPDATE DEPARTMENT SET SALARY =11111111 , DEPT='unknown'

--##########################################################
--DDL trigger (create_table, alter_table, drop_table)

--XML datatype in SQL server --EVENTDATA()

	/*
	Syntax:
		Create trigger TriggerName 
		on database 
		for create_table, alter_table, drop_table
		as 
		--sql logic 
	*/

	--sql logic 

--CREATE TABLE DDL LOGS 

--CREATE TABLE 
	CREATE TABLE DDLLOGS (sno int identity, eventss xml )


	Create trigger TG_monddl 
	on database 
	for create_table, alter_table, drop_table
	as 
	begin 
		insert into DDLLOGS values(EVENTDATA())
	end 


--################################
--Perform DDL operation
--create table
	create table test	(id int , age int, ph int)

--alter table 
	alter table test drop column id

--drop table 
	drop table test

select * from DDLLOGS




---####################################
-- user not allowed to create a table which has name = temp
	create trigger checktbl
	on database 
	for create_table, alter_table, drop_table 
	as 
		begin 

		declare @tblnme varchar(30)
		set @tblnme=eventdata().value('(/EVENT_INSTANCE/ObjectName)[1]','varchar(20)')
		if @tblnme like '%temp%'
			begin 
				print 'user not allowed to create table as TEMP'
				rollback
			end
		end
--create table
	create table temp	(id int , age int, ph int)

	create table q2131temp312312cas	(id int , age int, ph int)


---############################################################
--Exception /Error handling (Error related function)
select error_message(), error_line(), error_state(), error_Severity(),error_procedure(),error_number()

--Scenasrios Error handling 
	select * from Department 
--Scenasrios Error handling 
	select 1/0
--Scenasrios Error handling 
	create table demo101
	(id int identity , phnum int unique)

	insert into demo101
	values (3467)

	select * from demo101
--Scenasrios Error handling 

	select * from sys.messages where message_id =2627



--Error handling 
	Begin Try
			--SQL stmt
	end Try

	Begin Catch
			--generate Errors
			--Write to table
	end Catch

	

--Error handling 
	Begin Try
		--Scenasrios Error handling 
		select 1/0
	end Try

	Begin Catch
			--generate Errors
			print 'error related to calculations'
	end Catch


--Error handling 
	Begin Try
		--Scenasrios Error handling 
		insert into demo101 	values (3467)

	end Try

	Begin Catch
			--generate Errors
			print 'error related to duplicate entries'
	end Catch


--Error handling 
	Begin Try
		--Scenasrios Error handling 
		select 1/0
	end Try

	Begin Catch
			--generate Errors
			select error_message(), error_line(), error_state(), error_Severity(),error_procedure(),error_number()

	end Catch

--###################################
	create table errorlog
		(	sno int identity(1,1),
			timestamps varchar(100) default getdate(),
			ERRORLINE varchar(200),
			ERRORMESSAGE varchar(200),
			ERRORNUMBER varchar(200), 
			ERRORSTATE varchar(200),
			ERRORSEVERITY varchar(200), 
			ERRORPROCEDURE varchar(200)
			)


--Error handling 
	Begin Try
		--Scenasrios Error handling 
		select 1/0
	end Try

	Begin Catch
			insert into errorlog(ERRORLINE,ERRORMESSAGE,ERRORNUMBER,ERRORSTATE,ERRORSEVERITY,ERRORPROCEDURE) 
			values( ERROR_LINE(),ERROR_MESSAGE(),ERROR_NUMBER(),ERROR_STATE(),ERROR_SEVERITY(),ERROR_PROCEDURE())
			
	end Catch


	select * from errorlog

--Error handling 
	Begin Try
			--Scenasrios Error handling 
		insert into demo101 	values (3467)

	end Try

	Begin Catch
			insert into errorlog(ERRORLINE,ERRORMESSAGE,ERRORNUMBER,ERRORSTATE,ERRORSEVERITY,ERRORPROCEDURE) 
			values( ERROR_LINE(),ERROR_MESSAGE(),ERROR_NUMBER(),ERROR_STATE(),ERROR_SEVERITY(),ERROR_PROCEDURE())
			
	end Catch


--###########################################


--Cases in SQL server
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


	  SELECT did,ename,gender,dept,salary,
	  IIF(SALARY >6500, 'GOOD SAL', 'BAD SAL') AS COMMENTS
	  FROM Department ORDER BY salary ASC



	  SELECT did,ename,gender,dept,salary
	  
	  FROM Department


	  
	  
	  SELECT did,ename,gender,dept,salary,
	  CASE 
		when salary <=5000 then 'Increment 50 %'
		when salary between 5001 and 6500 then 'Increment 40 %'
		when salary between 6501 and 7000 then 'Increment 30 %'
		when salary between 7001 and 7500  then 'Increment 20 %'
		when salary >=7501 then 'Increment 10 %'
		else 'salary =6000'
	  END AS Comments
	  FROM Department ORDER BY salary ASC

	  
	  SELECT did,ename,gender,dept,salary,
	  CASE 
		when salary <=5000 then salary*1.5
		when salary between 5001 and 6500 then salary*1.4
		when salary between 6501 and 7000 then  salary*1.3
		when salary between 7001 and 7500  then salary*1.2
		when salary >=7501 then  salary*1.1
		else  6000
	  END AS Comments
	  FROM Department ORDER BY salary ASC
	   

	  update Department
	  set salary=CASE 
					when salary <=5000 then salary*1.5
					when salary between 5001 and 6500 then salary*1.4
					when salary between 6501 and 7000 then  salary*1.3
					when salary between 7001 and 7500  then salary*1.2
					when salary >=7501 then  salary*1.1
					else  6000
				  END 


				select * from Department





















































































































































































































