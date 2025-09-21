 --PK, FK,SQL SERVER  Crossjoins,EQUI, self join,merge,

--########################################################

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
	(15, 'Wayne', 'Male', 6800, 'Finance') 

	select * from department

---#######################################################
--primary key(unique + not null)// column (or a set of columns)
	--1 primary key  in table 
	--CLUSTERED INDEX (SORT & STORE, SEEK FASTER)

	CREATE TABLE emp
	(
		did INT primary key, --unique + not null --clusered index -- 1ci
		ename VARCHAR(50) ,
		gender VARCHAR(50) ,
		phnum INT unique ,--unique data + non clusered index  999 nci
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

	select * from emp

--composite primary key (column1 ,column,......)

	CREATE TABLE hr
	(
		did INT,
		ename VARCHAR(50) ,
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

	select * from HR

 ---###################################################
--Foreign key -->(Primary key  or unique )
	 --Refrential integrity --> add records (Primary , unique)
	 --Cascading integrity --> delete (foreign key)

	 CREATE TABLE Employees (
		EmployeeID INT primary key  ,
		FirstName NVARCHAR(50),
		LastName NVARCHAR(50)
	)

	CREATE TABLE Users (
		UserID INT primary key    ,
		Email NVARCHAR(100) unique,
		Username NVARCHAR(50) 
	)

	CREATE TABLE Orders (
		OrderID INT primary key  ,
		OrderDate DATE,
		CustomerID INT unique,
		EID INT ,
		Email NVARCHAR(100) ,
		foreign key(eid) references Employees (EmployeeID), 
		foreign key(Email) references Users (Email) 
		 
		)
--REFRENCTIAL INTEGRITY (PK, OR UK)

	INSERT INTO Employees VALUES 
	(1, 'John', 'Doe'),
	(2, 'Jane', 'Smith'),
	(3, 'Michael', 'Johnson'),
	(4, 'Emily', 'Davis'),
	(5, 'Chris', 'Brown')

	INSERT INTO Users VALUES 
	(1, 'john.doe@example.com', 'johndoe'),
	(2, 'jane.smith@example.com', 'janesmith'),
	(3, 'michael.johnson@example.com', 'mikejohnson'),
	(4, 'emily.davis@example.com', 'emilydavis'),
	(5, 'chris.brown@example.com', 'chrisbrown')

	INSERT INTO Orders VALUES 
	(1, '2024-08-15', 1, 1, 'john.doe@example.com'),
	(2, '2024-08-16', 2, 2, 'jane.smith@example.com'),
	(3, '2024-08-17', 3, 3, 'michael.johnson@example.com'),
	(4, '2024-08-18', 4, 4, 'emily.davis@example.com'),
	(5, '2024-08-19', 5, 5, 'chris.brown@example.com'),
	(6, '2024-08-15', 1, 1, 'john.doe@example.com'),
	(7, '2024-08-16', 2, 2, 'jane.smith@example.com'),
	(8, '2024-08-17', 3, 3, 'michael.johnson@example.com')



	SELECT * FROM Employees;
	SELECT * FROM Users;
	SELECT * FROM Orders;

--Cascading integrity (delete , update)
	delete FROM Employees;   
	delete FROM Users 
	delete FROM Orders --- DELETE FROM FK FIRST

--#########################################################################
--SQL SERVER JOINS

Create database Ecommerce
go
Use Ecommerce
go
-- Create Customers table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(50)
);
go

INSERT INTO Customers (CustomerID, CustomerName)
VALUES
    (1, 'John Smith'),
    (2, 'Jane Doe'),
    (3, 'Alice Johnson'),
    (4, 'Bob Williams'),
    (15, 'Emily Brown'),
    (6, 'Michael Davis'),
    (17, 'Olivia Wilson'),
    (8, 'William Taylor'),
    (19, 'Sophia Martinez'),
    (10, 'Liam Anderson');

go
-- Create Orders table
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE
);
go

INSERT INTO Orders (OrderID, CustomerID, OrderDate)
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

go
-- Create Products table
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(50),
    Price DECIMAL(10, 2)
);

go
INSERT INTO Products (ProductID, ProductName, Price)
VALUES
    (501, 'Widget', 10.99),
    (502, 'Gadget', 24.99),
    (503, 'Accessory', 5.99),
    (504, 'Tool', 15.49),
    (515, 'Toy', 7.95),
    (506, 'Device', 49.99),
    (517, 'Appliance', 89.00),
    (508, 'Book', 12.50),
    (519, 'Clothing', 29.95),
    (510, 'Jewelry', 59.00);

go
-- Create OrderDetails table
CREATE TABLE OrderDetails (
    DetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT
);
go
INSERT INTO OrderDetails (DetailID, OrderID, ProductID, Quantity)
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



Select top 1 * from Customers
Select top 1 * from Orders
Select top 1  * from OrderDetails
Select top 1 * from products

--###############################################
--Relationship 
	--Customers		-->Orders		=	 CustomerID
	--Orders		-->OrderDetails	=	 OrderID 
	--OrderDetails	-->products		=	 ProductID
	--Customers		-->products		=	 CustomerID-->OrderID-->ProductID

--####################
/*SYNTAX Joins:
	SELECT columns
	FROM table1  JOIN table2 	ON table1.column = table2.column
	JOIN table3 	ON table1.column = table3.column
	JOIN table4 	ON table2.column = table4.column
*/
--###############################################


Select top 1 * from Customers
Select top 1 * from Orders
Select top 1  * from OrderDetails
Select top 1 * from products

--CustomerID-->OrderID-->ProductID

	Select  * from Customers INNER JOIN Orders ON Customers.CustomerID=Orders.CustomerID
	
	Select  * from Customers c INNER JOIN Orders O ON C.CustomerID=O.CustomerID
		
	Select  * from Customers AS c INNER JOIN Orders AS O ON C.CustomerID=O.CustomerID
	INNER JOIN OrderDetails  AS od ON O.OrderID=OD.OrderID

	Select  * from Customers AS c INNER JOIN Orders AS O ON C.CustomerID=O.CustomerID
	INNER JOIN OrderDetails  AS od ON O.OrderID=OD.OrderID
	INNER JOIN products AS p ON OD.ProductID=P.ProductID

--Query designer 
--cNTRL+SHIFT +q
	SELECT c.CustomerName, O.OrderDate, od.Quantity, p.ProductName, p.Price
	FROM  Customers AS c INNER JOIN
	Orders AS O ON c.CustomerID = O.CustomerID INNER JOIN
	OrderDetails AS od ON O.OrderID = od.OrderID INNER JOIN
	Products AS p ON od.ProductID = p.ProductID

	Select  C.*,P.* from Customers AS c INNER JOIN Orders AS O ON C.CustomerID=O.CustomerID
	INNER JOIN OrderDetails  AS od ON O.OrderID=OD.OrderID
	INNER JOIN products AS p ON OD.ProductID=P.ProductID

--###############################################
--Left outer join 

	Select  * from Customers Left outer  JOIN Orders ON Customers.CustomerID=Orders.CustomerID
	
	Select  * from Customers c Left    JOIN Orders O ON C.CustomerID=O.CustomerID
		
	Select  * from Customers AS c Left JOIN Orders AS O ON C.CustomerID=O.CustomerID
	Left JOIN OrderDetails  AS od ON O.OrderID=OD.OrderID

	Select  * from Customers AS c Left JOIN Orders AS O ON C.CustomerID=O.CustomerID
	Left JOIN OrderDetails  AS od ON O.OrderID=OD.OrderID
	Left JOIN products AS p ON OD.ProductID=P.ProductID

--Display the records of customers without order

	Select  * from Customers c Left JOIN Orders O ON C.CustomerID=O.CustomerID
	WHERE O.OrderID IS NULL
	
--###############################################
--Right outer join 

	Select  * from Customers Right outer  JOIN Orders ON Customers.CustomerID=Orders.CustomerID
	
	Select  * from Customers c Right    JOIN Orders O ON C.CustomerID=O.CustomerID
		
	Select  * from Customers AS c Right JOIN Orders AS O ON C.CustomerID=O.CustomerID
	Right JOIN OrderDetails  AS od ON O.OrderID=OD.OrderID

	Select  * from Customers AS c Right JOIN Orders AS O ON C.CustomerID=O.CustomerID
	Right JOIN OrderDetails  AS od ON O.OrderID=OD.OrderID
	Right JOIN products AS p ON OD.ProductID=P.ProductID

--Display the records of order MISSING  customers INFO

	Select  * from Customers c Right JOIN Orders O ON C.CustomerID=O.CustomerID
	WHERE  C.CustomerID IS NULL

--###############################################
--Full outer join 

	Select  * from Customers Full outer  JOIN Orders ON Customers.CustomerID=Orders.CustomerID
	
	Select  * from Customers c Full    JOIN Orders O ON C.CustomerID=O.CustomerID
		
	Select  * from Customers AS c Full JOIN Orders AS O ON C.CustomerID=O.CustomerID
	Full JOIN OrderDetails  AS od ON O.OrderID=OD.OrderID

	Select  * from Customers AS c Full JOIN Orders AS O ON C.CustomerID=O.CustomerID
	Full JOIN OrderDetails  AS od ON O.OrderID=OD.OrderID
	Full JOIN products AS p ON OD.ProductID=P.ProductID


--Display the records of order without  customers  and customers without order
	Select  * from Customers c Full JOIN Orders O ON C.CustomerID=O.CustomerID
	WHERE  C.CustomerID IS NULL OR O.CustomerID IS NULL

--###########################
--Cross join 
	--Cartesian product of the two tables
	--possible combinations of rows between two or more tables.
	CREATE TABLE Meals(MealName VARCHAR(100))
	CREATE TABLE Drinks(DrinkName VARCHAR(100))

	INSERT INTO Drinks VALUES('Orange Juice'), ('Tea'), ('Cofee')
	INSERT INTO Meals VALUES('Omlet'), ('Fried Egg'), ('Sausage')

	SELECT * FROM Meals
	SELECT * FROM Drinks
	
	SELECT * FROM Meals cross join Drinks







--###########################

	CREATE TABLE emp(
		employee_id INT PRIMARY KEY,
		employee_name VARCHAR(50)	)
	INSERT INTO dep
	VALUES		(1, 'John Smith'),		(2, 'Jane Doe'),		(3, 'Bob Johnson');

	CREATE TABLE dep(
		department_id INT PRIMARY KEY,
		department_name VARCHAR(50)	);

	INSERT INTO emp
	VALUES		(101, 'HR'),		(102, 'Engineering'),		(103, 'Sales');


		SELECT * FROM emp
		SELECT * FROM dep

		
		SELECT * FROM emp cross join dep

--##############################################
--equi join
	Select  * from Customers INNER JOIN Orders ON Customers.CustomerID=Orders.CustomerID

	Select * from Customers c , Orders o where  c.customerid=o.customerid

	SELECT * FROM emp cross join dep

	SELECT * FROM emp , dep



--############################################
CREATE TABLE info (
		EmployeeID int PRIMARY KEY,
		EmployeeName varchar(255),
		ManagerID int
	)

	INSERT INTO info (EmployeeID, EmployeeName, ManagerID) VALUES
	(1, 'Alice Johnson', NULL),
	(2, 'Bob Smith', 1),
	(3, 'Catherine Brown', 1),
	(4, 'Daniel Garcia', 1),
	(5, 'Emma Wilson', 1),
	(6, 'Franklin Moore', 2),
	(7, 'Georgia Taylor', 2),
	(8, 'Henry Anderson', 2),
	(9, 'Isabel Thomas', 3),
	(10, 'Jack Martinez', 3),
	(11, 'Kylie Robinson', 3),
	(12, 'Liam Clark', 4),
	(13, 'Mia Rodriguez', 4),
	(14, 'Noah Lewis', 4),
	(15, 'Olivia Lee', 5),
	(16, 'Parker Walker', 5),
	(17, 'Quinn Hall', 5),
	(18, 'Ryan Allen', 6),
	(19, 'Sophia Young', 6),
	(20, 'Tyler Hernandez', 6);

	select * from info





--employee name and manager name 
	select Emp.employeename, mgr.employeename as Mgrname
	from info emp left join info mgr
	on mgr.employeeid = emp.managerid





CREATE TABLE Prod (
		ProductID INT PRIMARY KEY,
		ProductName NVARCHAR(50),
		ListPrice DECIMAL(10, 2)
	)

	INSERT INTO Prod (ProductID, ProductName, ListPrice)
	VALUES 
	(1, 'Product A', 100.00),
	(2, 'Product B', 150.00),
	(3, 'Product C', 100.00),
	(4, 'Product D', 200.00),
	(5, 'Product E', 150.00);

	INSERT INTO Prod (ProductID, ProductName, ListPrice)
	values(6, 'Product f', 150.00)

	SELECT * FROm PROD

--Product with same price

	SELECT * FROm 
	PROD p1 inner join  PROD p2 
	on p1.listprice=p2.listprice
	where p1.productid>p2.productid













--############################################

/*Merge Syntax
		MERGE  target_table USING source_table ON merge_condition
		WHEN MATCHED THEN
			UPDATE SET column1 = value1, column2 = value2, ...
		WHEN NOT MATCHED BY TARGET THEN
			INSERT (column1, column2, ...) VALUES (value1, value2, ...)
		WHEN NOT MATCHED BY SOURCE THEN
			DELETE;
*/


--#############################
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


	CREATE TABLE UpdatedEmployees (
		EmployeeID INT PRIMARY KEY,
		FirstName VARCHAR(50),
		LastName VARCHAR(50),
		Department VARCHAR(50),
		Email VARCHAR(100)
	)

	INSERT INTO UpdatedEmployees (EmployeeID, FirstName, LastName, Department, Email)
	VALUES
		(1, 'John', 'sdf', 'sfsd', 'jsdfsdfe.com'),  -- Updated email
		(2, 'Jane', 'sd', 'sdf', 'sdf.doe@example.com'),
		(3, 'Jim', 'Beam', 'dsdf', 'jim.fsd@sdf.com'),  -- Updated email
		(6, 'Jill', 'Valentine', 'IT', 'jill.valentine@example.com'), -- New employee
		(7, 'Chris', 'Redfield', 'Security', 'chris.redfield@example.com');  -- New employee


	
	SELECT * FROM UpdatedEmployees
	SELECT * FROM Employees
	 
--update
	merge UpdatedEmployees ue using employees ee
	on ue.employeeid =ee.employeeid
	when matched then 
		update set
			ue.FirstName=	ee.FirstName,
			ue.LastName	=ee.LastName	,
			ue.Department	=ee.Department	,
			ue.Email=ee.Email
		;
--Insert
	merge UpdatedEmployees ue using employees ee
	on ue.employeeid =ee.employeeid
	when not matched by target then 
		insert(EmployeeID, FirstName, LastName, Department, Email)
		VALUES(EE.EmployeeID, EE.FirstName, EE.LastName, EE.Department, EE.Email)
;
--DELETE
	merge UpdatedEmployees ue using employees ee
	on ue.employeeid =ee.employeeid
	when not matched by SOURCE then 
	DELETE
;


--update
merge UpdatedEmployees ue using employees ee
on ue.employeeid =ee.employeeid
	when matched then 
		update set
			ue.FirstName=	ee.FirstName,
			ue.LastName	=ee.LastName	,
			ue.Department	=ee.Department	,
			ue.Email=ee.Email 
--Insert 
	when not matched by target then 
		insert(EmployeeID, FirstName, LastName, Department, Email)
		VALUES(EE.EmployeeID, EE.FirstName, EE.LastName, EE.Department, EE.Email)
 
--DELETE 
	when not matched by SOURCE then 
		DELETE
;


	SELECT * FROM UpdatedEmployees
	SELECT * FROM Employees
--#################################################################
--################################################################################################

--FIND COLUMN--FirstName

	SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE COLUMN_NAME ='FirstName'
--FIND TABLE WITHIN A DATABASE

	SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE '%EMPLOYEE%'


--Practice Question for AdventureWorks2022 database 
--1. Inner Join:
	 Question: Write a query to retrieve the `BusinessEntityID`, `JobTitle`, `FirstName`, and `LastName` of 
	all employees by joining the `HumanResources.Employee` and `Person.Person` tables on `BusinessEntityID`.


	select He.BusinessEntityID,JobTitle,FirstName,lastname
	from humanResources.Employee HE Inner Join Person.Person  PP on He.BusinessEntityID=PP.BusinessEntityID

--2. Left Join:
	Question: Write a query to list all persons with their addresses, including those who do not have an 
	address. Use the `Person.Person` table and the `Person.Address` table, joining on `BusinessEntityID`.

--3. Right Join:
	 Question: Write a query to list all product reviews along with the names of the reviewers.
	 Include all reviews even if the reviewer s name is not available. 
	Use the `Production.ProductReview` table and the `Person.Person` table, joining on 	`ReviewerID`.

--4. Full Outer Join:
	Question: Write a query to list all employees and their associated departments. 
	Include employees without departments and departments without employees.
	 Use the `HumanResources.Employee` and `HumanResources.Department` tables, joining on `DepartmentID`.

--5. Join with Aggregates:
	Question: Write a query to find the total sales amount for each sales person.
	 Use the `Sales.SalesOrderHeader` and `Sales.SalesPerson` tables, joining on `SalesPersonID`.

--6. Join with Multiple Tables:
	Question: Write a query to retrieve the `ProductID`, `Name`, `SalesOrderID`, and `OrderDate`
	 for all sales orders. Use the `Sales.SalesOrderDetail`, `Production.Product`, and `Sales.SalesOrderHeader` 
	tables, joining on `ProductID` and `SalesOrderID`.

--7. Join with Subquery:
	Question: Write a query to find the names of employees who have placed an order. 
	Use a subquery to find the `EmployeeID` from the `Sales.SalesOrderHeader` table and join it with the 
	`HumanResources.Employee` and `Person.Person` tables to get the `FirstName` and `LastName`.
	 







































































