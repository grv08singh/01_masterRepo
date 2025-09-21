-- SQL Case Study 2: Gaurav Singh (grv08singh@gmail.com)


-- Pre-Requisite Tables

CREATE DATABASE case_study2;
USE case_study2;

DROP TABLE LOCATION;
CREATE TABLE LOCATION (
  Location_ID INT PRIMARY KEY,
  City VARCHAR(50)
);

INSERT INTO LOCATION (Location_ID, City)
VALUES (122, 'New York'),
       (123, 'Dallas'),
       (124, 'Chicago'),
       (167, 'Boston');


DROP TABLE DEPARTMENT;
  CREATE TABLE DEPARTMENT (
  Department_Id INT PRIMARY KEY,
  Name VARCHAR(50),
  Location_Id INT,
  FOREIGN KEY (Location_Id) REFERENCES LOCATION(Location_ID)
);


INSERT INTO DEPARTMENT (Department_Id, Name, Location_Id)
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
(7505,'DOYLE','JEAN','K',671,7839,'04-APR-85',2850,NULl,30),
(7506,'DENNIS','LYNN','S',671,7839,'15-MAY-85',2750,NULL,30),
(7507,'BAKER','LESLIE','D',671,7839,'10-JUN-85',2200,NULL,40),
(7521,'WARK','CYNTHIA','D',670,7698,'22-FEB-85',1250,500,30);






-----------------------------------------------------------
-- Simple Queries:
-----------------------------------------------------------
-- 1. List all the employee details.
SELECT * FROM [dbo].[EMPLOYEE];



-- 2. List all the department details.
SELECT * FROM [dbo].[DEPARTMENT];



-- 3. List all job details.
SELECT * FROM [dbo].[JOB];



-- 4. List all the locations.
SELECT * FROM [dbo].[LOCATION];



-- 5. List out the First Name, Last Name, Salary, Commission for all Employees.
SELECT [FIRST_NAME], [LAST_NAME], [SALARY], [COMM] FROM [dbo].[EMPLOYEE];



-- 6. List out the Employee ID, Last Name, Department ID for all employees and
-- alias Employee ID as "ID of the Employee", Last Name as "Name of the
-- Employee", Department ID as "Dep_id".
SELECT 
	[EMPLOYEE_ID] AS [ID of the Employee], 
	[LAST_NAME] AS [Name of the Employee], 
	[DEPARTMENT_ID] AS Dep_id
FROM
	[dbo].[EMPLOYEE];



-- 7. List out the annual salary of the employees with their names only.
SELECT [FIRST_NAME], [LAST_NAME], 12*[SALARY] AS annual_salary FROM [dbo].[EMPLOYEE];



-----------------------------------------------------------
-- WHERE Condition:
-----------------------------------------------------------
-- 1. List the details about "Smith".
SELECT * FROM [dbo].[EMPLOYEE] WHERE [LAST_NAME] = 'Smith';



-- 2. List out the employees who are working in department 20.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [DEPARTMENT_ID] = 20;



-- 3. List out the employees who are earning salary between 2000 and 3000.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [SALARY] BETWEEN 2000 AND 3000;



-- 4. List out the employees who are working in department 10 or 20.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [DEPARTMENT_ID] IN (20,30);



-- 5. Find out the employees who are not working in department 10 or 30.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [DEPARTMENT_ID] NOT IN (10,30);



-- 6. List out the employees whose name starts with 'L'.7. List out the employees whose name starts with 'L' and ends with 'E'.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [FIRST_NAME] LIKE 'L%';
SELECT * FROM [dbo].[EMPLOYEE] WHERE [FIRST_NAME] LIKE 'L%E';



-- 8. List out the employees whose name length is 4 and start with 'J'.
SELECT * FROM [dbo].[EMPLOYEE] WHERE LEN([FIRST_NAME]) = 4 AND [FIRST_NAME] LIKE 'J%';



-- 9. List out the employees who are working in department 30 and draw the
-- salaries more than 2500.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [DEPARTMENT_ID] = 30 AND [SALARY] > 2500;



-- 10. List out the employees who are not receiving commission.
SELECT * FROM [dbo].[EMPLOYEE] WHERE [COMM] IS NULL ;




-----------------------------------------------------------
-- ORDER BY Clause:
-----------------------------------------------------------
-- 1. List out the Employee ID and Last Name in ascending order based on the
-- Employee ID.
SELECT [EMPLOYEE_ID], [LAST_NAME] FROM [dbo].[EMPLOYEE] ORDER BY [EMPLOYEE_ID] ASC;



-- 2. List out the Employee ID and Name in descending order based on salary.
SELECT [EMPLOYEE_ID], [LAST_NAME] FROM [dbo].[EMPLOYEE] ORDER BY [SALARY] DESC;



-- 3. List out the employee details according to their Last Name in ascending-order.
SELECT * FROM [dbo].[EMPLOYEE] ORDER BY [LAST_NAME] ASC;



-- 4. List out the employee details according to their Last Name in ascending
-- order and then Department ID in descending order.
SELECT * FROM [dbo].[EMPLOYEE] ORDER BY [LAST_NAME] ASC, [DEPARTMENT_ID] DESC;



-----------------------------------------------------------
-- GROUP BY and HAVING Clause:
-----------------------------------------------------------
-- 1. List out the department wise maximum salary, minimum salary and
-- average salary of the employees.
SELECT 
	[DEPARTMENT_ID], 
	MAX([SALARY]) AS max_salary, 
	MIN([SALARY]) AS min_salary, 
	AVG([SALARY]) AS avg_salary
FROM [dbo].[EMPLOYEE]
GROUP BY [DEPARTMENT_ID];



-- 2. List out the job wise maximum salary, minimum salary and average
-- salary of the employees.
SELECT 
	[JOB_ID], 
	MAX([SALARY]) AS max_salary, 
	MIN([SALARY]) AS min_salary, 
	AVG([SALARY]) AS avg_salary
FROM [dbo].[EMPLOYEE]
GROUP BY [JOB_ID];



-- 3. List out the number of employees who joined each month in ascending order.
SELECT 
	DATEPART(MONTH, [HIRE_DATE]) AS mnth_num, 
	DATENAME(MONTH, [HIRE_DATE]) AS mnth_name, 
	COUNT([EMPLOYEE_ID]) AS emp_joined
FROM [dbo].[EMPLOYEE]
GROUP BY 
	DATEPART(MONTH, [HIRE_DATE]),
	DATENAME(MONTH, [HIRE_DATE]) 
ORDER BY 
	DATEPART(MONTH, [HIRE_DATE]);



-- 4. List out the number of employees for each month and year in
-- ascending order based on the year and month.
SELECT 
	DATEPART(YEAR, [HIRE_DATE]) AS yr,
	DATEPART(MONTH, [HIRE_DATE]) AS mnth_num, 
	DATENAME(MONTH, [HIRE_DATE]) AS mnth_name, 
	COUNT([EMPLOYEE_ID]) AS emp_joined
FROM [dbo].[EMPLOYEE]
GROUP BY 
	DATEPART(YEAR, [HIRE_DATE]),
	DATEPART(MONTH, [HIRE_DATE]),
	DATENAME(MONTH, [HIRE_DATE]) 
ORDER BY 
	DATEPART(YEAR, [HIRE_DATE]),
	DATEPART(MONTH, [HIRE_DATE]);




-- 5. List out the Department ID having at least four employees.
SELECT 
	[DEPARTMENT_ID], 
	COUNT([EMPLOYEE_ID]) AS emp_count
FROM [dbo].[EMPLOYEE]
GROUP BY [DEPARTMENT_ID]
HAVING COUNT([EMPLOYEE_ID]) >= 4;



-- 6. How many employees joined in February month.
SELECT COUNT([EMPLOYEE_ID]) AS feb_count 
FROM [dbo].[EMPLOYEE] 
WHERE DATEPART(MONTH,[HIRE_DATE]) = 2;



-- 7. How many employees joined in May or June month.
SELECT COUNT([EMPLOYEE_ID]) AS may_jun_count 
FROM [dbo].[EMPLOYEE] 
WHERE DATEPART(MONTH,[HIRE_DATE]) IN (5,6);



-- 8. How many employees joined in 1985?
SELECT COUNT([EMPLOYEE_ID]) AS yr_1985_count 
FROM [dbo].[EMPLOYEE] 
WHERE DATEPART(YEAR,[HIRE_DATE]) = 1985;



-- 9. How many employees joined each month in 1985?
SELECT DATENAME(MONTH,[HIRE_DATE]) AS mnth, COUNT([EMPLOYEE_ID]) AS monthly_count 
FROM [dbo].[EMPLOYEE]
GROUP BY DATEPART(YEAR,[HIRE_DATE]), DATENAME(MONTH,[HIRE_DATE])
HAVING DATEPART(YEAR,[HIRE_DATE]) = 1985;



-- 10. How many employees were joined in April 1985?
SELECT COUNT([EMPLOYEE_ID]) AS Apr_1985_count 
FROM [dbo].[EMPLOYEE] 
WHERE DATEPART(YEAR,[HIRE_DATE]) = 1985 AND DATEPART(MONTH,[HIRE_DATE]) = 4;



-- 11. Which is the Department ID having greater than or equal to 3 employees
-- joining in April 1985?Joins:
SELECT 
	[DEPARTMENT_ID]
FROM [dbo].[EMPLOYEE]
WHERE
	DATEPART(YEAR,[HIRE_DATE]) = 1985 AND
	DATEPART(MONTH,[HIRE_DATE]) = 4
GROUP BY
	[DEPARTMENT_ID]
HAVING COUNT([EMPLOYEE_ID]) >= 3;




-----------------------------------------------------------
-- Joins:
-----------------------------------------------------------

-- 1. List out employees with their department names.
SELECT e.[FIRST_NAME], e.[LAST_NAME], d.[Name] AS dept_nm
FROM [dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id];



-- 2. Display employees with their designations.
SELECT e.[FIRST_NAME], e.[LAST_NAME], j.[DESIGNATION]
FROM [dbo].[EMPLOYEE] e
INNER JOIN [dbo].[JOB] j
ON e.[JOB_ID] = j.[JOB_ID];



-- 3. Display the employees with their department names and city.
SELECT 
	e.[FIRST_NAME], 
	e.[LAST_NAME], 
	d.[Name] AS department, 
	loc.[City]
FROM
	[dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id]
INNER JOIN [dbo].[LOCATION] loc
ON d.[Location_Id] = loc.[Location_ID];
	


-- 4. How many employees are working in different departments? 
-- Display with department names.
SELECT 
	d.[Name] AS department, 
	COUNT(e.[EMPLOYEE_ID]) AS num_of_employees
FROM [dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id]
GROUP BY d.[Name];




-- 5. How many employees are working in the sales department?
SELECT 
	COUNT(e.[EMPLOYEE_ID]) AS sales_employees
FROM [dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id]
WHERE d.[Name] = 'sales'
GROUP BY d.[Name];




-- 6. Which is the department having greater than or equal to 3
-- employees and display the department names in ascending order.
SELECT 
	d.[Name] AS department, 
	COUNT(e.[EMPLOYEE_ID]) AS num_of_employees
FROM [dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id]
GROUP BY d.[Name]
HAVING COUNT(e.[EMPLOYEE_ID]) >= 3
ORDER BY d.[Name];





-- 7. How many employees are working in 'Dallas'?
SELECT 
	COUNT(e.[EMPLOYEE_ID]) AS dallas_employees
FROM
	[dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id]
INNER JOIN [dbo].[LOCATION] loc
ON d.[Location_Id] = loc.[Location_ID]
WHERE loc.[City] = 'Dallas';




-- 8. Display all employees in sales or operations departments.
SELECT 
	e.[FIRST_NAME],
	e.[LAST_NAME],
	d.[Name] AS dept
FROM [dbo].[EMPLOYEE] e
INNER JOIN [dbo].[DEPARTMENT] d
ON e.[DEPARTMENT_ID] = d.[Department_Id]
WHERE d.[Name] IN ('sales','operations');





-----------------------------------------------------------
-- CONDITIONAL STATEMENT
-----------------------------------------------------------
-- 1. Display the employee details with salary grades. Use conditional statement to
-- create a grade column.
SELECT *,
	CASE
		WHEN [SALARY] > 2700 THEN 'A'
		WHEN [SALARY] > 1800 THEN 'B'
		WHEN [SALARY] > 900 THEN 'C'
		WHEN [SALARY] <= 900 THEN 'D'
	END AS grade
FROM [dbo].[EMPLOYEE];




-- 2. List out the number of employees grade wise. Use conditional statement to
-- create a grade column.
WITH grade_wise AS
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
FROM grade_wise
GROUP BY grade;




-- 3. Display the employee salary grades and the number of employees between
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

-- 1. Display the employees list who got the maximum salary.
SELECT * 
FROM [dbo].[EMPLOYEE] 
WHERE [SALARY] = (SELECT MAX([SALARY]) FROM [dbo].[EMPLOYEE]);



-- 2. Display the employees who are working in the sales department.
SELECT * 
FROM [dbo].[EMPLOYEE] 
WHERE [DEPARTMENT_ID] = (SELECT [Department_Id] FROM [dbo].[DEPARTMENT] WHERE [Name] = 'sales');



-- 3. Display the employees who are working as 'Clerk'.
SELECT * 
FROM [dbo].[EMPLOYEE] 
WHERE [JOB_ID] = (SELECT [JOB_ID] FROM [dbo].[JOB] WHERE [DESIGNATION] = 'clerk');



-- 4. Display the list of employees who are living in 'Boston'.
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



-- 5. Find out the number of employees working in the sales department.
SELECT COUNT([EMPLOYEE_ID]) AS sales_emp
FROM [dbo].[EMPLOYEE]
WHERE [DEPARTMENT_ID] = 
	(
		SELECT [Department_Id]
		FROM [dbo].[DEPARTMENT]
		WHERE [Name] = 'sales'
	);




-- 6. Update the salaries of employees who are working as clerks on the basis of 10%.
UPDATE [dbo].[EMPLOYEE]
SET [SALARY] = 1.1*[SALARY]
WHERE [JOB_ID] = 
	(
		SELECT [JOB_ID] 
		FROM [dbo].[JOB] 
		WHERE [DESIGNATION] = 'clerk'
	);




-- 7. Display the second highest salary drawing employee details.
SELECT *
FROM [dbo].[EMPLOYEE]
ORDER BY [SALARY] DESC
OFFSET 1 ROWS
FETCH NEXT 1 ROWS ONLY;



-- 8. List out the employees who earn more than every employee in department 30.
SELECT *
FROM [dbo].[EMPLOYEE]
WHERE [SALARY] > 
	(
		SELECT MAX([SALARY]) AS max_sal_in_dept_30
		FROM [dbo].[EMPLOYEE] 
		WHERE [DEPARTMENT_ID] = 30
	);



-- 9. Find out which department has no employees.
SELECT [Name] 
FROM [dbo].[DEPARTMENT]
WHERE [Department_Id] NOT IN
	(
		SELECT DISTINCT [DEPARTMENT_ID]
		FROM [dbo].[EMPLOYEE]
	);



-- 10. Find out the employees who earn greater than the average salary for
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


