-- SQL Mandatory Assignment 1: Gaurav Singh (grv08singh@gmail.com)

CREATE DATABASE assignment1;
USE assignment1;

--Creating Pre-requisite tables and inserting data as per assignment
DROP TABLE Salesman;

CREATE TABLE Salesman (SalesmanId INT,Name VARCHAR(255),Commission DECIMAL(10, 2),City VARCHAR(255),Age INT);
INSERT INTO Salesman (SalesmanId, Name, Commission, City, Age) VALUES
(101, 'Joe', 50, 'California', 17),
(102, 'Simon', 75, 'Texas', 25),
(103, 'Jessie', 105, 'Florida', 35),
(104, 'Danny', 100, 'Texas', 22),
(105, 'Lia', 65, 'New Jersey', 30);

DROP TABLE Customer;

CREATE TABLE Customer (SalesmanId INT,CustomerId INT,CustomerName VARCHAR(255),PurchaseAmount INT);
INSERT INTO Customer (SalesmanId, CustomerId, CustomerName, PurchaseAmount)VALUES
(101, 2345, 'Andrew', 550),
(103, 1575, 'Lucky', 4500),
(104, 2345, 'Andrew', 4000),
(107, 3747, 'Remona', 2700),
(110, 4004, 'Julia', 4545);

DROP TABLE Orders;

CREATE TABLE Orders (OrderId int, CustomerId int, SalesmanId int, Orderdate Date, Amount money);
INSERT INTO Orders VALUES
(5001,2345,101,'2021-07-01',550),
(5003,1234,105,'2022-02-15',1500);

-- Fetching Raw Data
SELECT * FROM Salesman;
SELECT * FROM Customer;
SELECT * FROM Orders;

-- Tasks to be performed



-- Task 1) Insert a new record in your Orders table.
INSERT INTO Orders VALUES (5005,3747,104,'2023-09-05',337);




-- Task 2) 
-- 2.1) Add Primary key constraint for SalesmanId column in Salesman table. 
-- Adding NOT NULL constraint before making the PRIMARY KEY
ALTER TABLE Salesman ALTER COLUMN SalesmanId INT NOT NULL;

-- Making PRIMARY KEY: two ways
ALTER TABLE Salesman ADD CONSTRAINT PK_SalesmanId PRIMARY KEY(SalesmanId);
-- OR
ALTER TABLE Salesman ADD PRIMARY KEY(SalesmanId);

-- 2.2) Add default constraint for City column in Salesman table.
ALTER TABLE Salesman ADD CONSTRAINT DF_city DEFAULT 'No_City' FOR city;

-- 2.3) Add Foreign key constraint for SalesmanId column in Customer table.
-- Adding data for referential integrity
INSERT INTO Salesman (SalesmanId, Name, Commission, City, Age) VALUES
(107, 'Max', 33, 'NYC', 24),
(110, 'Stallion', 25, 'WDC', 27);

-- Creating Foreign key
ALTER TABLE Customer ADD FOREIGN KEY (SalesmanId) REFERENCES Salesman(SalesmanId);
-- OR
ALTER TABLE Orders ADD CONSTRAINT FK_SalesmanId FOREIGN KEY (SalesmanId) REFERENCES Salesman(SalesmanId);

-- 2.4) Add not null constraint in Customer_name column for the Customer table.
ALTER TABLE Customer ALTER COLUMN CustomerName VARCHAR(255) NOT NULL;





-- Task 3) Fetch the data where the Customer’s name is ending with ‘N’ also get the purchase amount value greater than 500.
SELECT * FROM Customer WHERE CustomerName LIKE '%n';
SELECT * FROM Customer WHERE PurchaseAmount > 500;
SELECT * FROM Customer WHERE CustomerName LIKE '%n' AND PurchaseAmount > 500;




-- Task 4) 
-- 4.1) Using SET operators, retrieve the first result with unique SalesmanId values from two tables
SELECT DISTINCT SalesmanId FROM Customer
UNION
SELECT DISTINCT SalesmanId FROM Salesman;

-- 4.2) Using SET operators, retrieve the 2nd result containing SalesmanId with duplicates from two tables.
SELECT DISTINCT SalesmanId FROM Customer
UNION ALL
SELECT DISTINCT SalesmanId FROM Salesman;





-- Task 5) Display the below columns which has the matching data.
--         Orderdate, Salesman Name, Customer Name, Commission, and 
--         City which has the range of Purchase Amount between 500 to 1500.
SELECT Distinct(o.OrderId),o.Orderdate, s.Name AS salesman_name, c.CustomerName, s.Commission, s.City
	FROM Orders o
	INNER JOIN Salesman s ON o.SalesmanId = s.SalesmanId
	INNER JOIN Customer c ON o.CustomerId = c.CustomerId
	WHERE o.Amount >= 500 AND o.Amount <= 1500;





-- Task 6) Using right join fetch all the results from Salesman and Orders table.
SELECT * FROM Salesman s
	RIGHT JOIN Orders o
	ON s.SalesmanId = o.SalesmanId;