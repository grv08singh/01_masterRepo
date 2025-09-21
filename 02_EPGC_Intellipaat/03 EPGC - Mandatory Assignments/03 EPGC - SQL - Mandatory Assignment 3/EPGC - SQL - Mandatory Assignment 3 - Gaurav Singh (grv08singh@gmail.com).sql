-- SQL Mandatory Assignment 3: Gaurav Singh (grv08singh@gmail.com)

CREATE DATABASE assignment3;
USE assignment3;


-- Dataset: Jomato
-- About the dataset:
-- You work for a data analytics company, and your client is a food delivery platform similar to
-- Jomato. They have provided you with a dataset containing information about various
-- restaurants in a city. Your task is to analyze this dataset using SQL queries to extract valuable
-- insights and generate reports for your client
-- 
-- Tasks to be performed:
-- Importing the csv FLAT FILE Jomato
SELECT * FROM [dbo].[Jomato];


-- 1. Create a stored procedure to display the restaurant name, type and cuisine where the
-- table booking is not zero.
CREATE PROCEDURE sp_table_not_zero 
AS
BEGIN
	SELECT [RestaurantName], [RestaurantType], [CuisinesType] FROM [dbo].[Jomato] WHERE [TableBooking] <> 0
END;

EXEC sp_table_not_zero;


-- 2. Create a transaction and update the cuisine type ‘Cafe’ to ‘Cafeteria’. Check the result
-- and rollback it.
BEGIN TRAN
UPDATE [dbo].[Jomato] SET [CuisinesType] = 'Cafeteria' WHERE [CuisinesType] = 'Cafe';
SELECT * FROM [dbo].[Jomato] WHERE [CuisinesType] = 'Cafe';
ROLLBACK



-- 3. Generate a row number column and find the top 5 areas with the highest rating of
-- restaurants.
WITH top_rated AS
(	SELECT [Area], [Rating], 
	ROW_NUMBER() OVER (ORDER BY [Rating] DESC) AS row_num 
	FROM [dbo].[Jomato]
)
SELECT * FROM top_rated WHERE row_num <= 5;



-- 4. Use the while loop to display the 1 to 50.
DECLARE @loop INT = 1;
WHILE @loop <= 50
BEGIN
	WITH top_rated AS
	(	SELECT *, ROW_NUMBER() OVER (ORDER BY [Rating] DESC) AS row_num 
		FROM [dbo].[Jomato]
	)
	SELECT * FROM top_rated WHERE row_num = @loop
    SET @loop = @loop + 1;
END;





-- 5. Write a query to Create a Top rating view to store the generated top 5 highest rating of
-- restaurants.
CREATE VIEW vw_top_rating AS SELECT TOP 5 * FROM [dbo].[Jomato] ORDER BY [Rating] DESC;

SELECT * FROM vw_top_rating;



-- 6. Create a trigger that give an message whenever a new record is inserted.
DROP TRIGGER tg_insert;
CREATE TRIGGER tg_insert ON [dbo].[Jomato] FOR INSERT AS
BEGIN
	PRINT 'Wow!!! A new record is being inserted.'
END;

INSERT INTO [dbo].[Jomato] VALUES(7105,'Avb','cdc',3.5454556,52,123,1,0,'Italian','Delhi','CP',60);


