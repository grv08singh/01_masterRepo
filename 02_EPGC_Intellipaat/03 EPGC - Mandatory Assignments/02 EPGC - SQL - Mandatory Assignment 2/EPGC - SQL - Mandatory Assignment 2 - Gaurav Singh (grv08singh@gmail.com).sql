-- SQL Mandatory Assignment 2: Gaurav Singh (grv08singh@gmail.com)

CREATE DATABASE assignment2;
USE assignment2;


-- Dataset: Jomato
-- About the dataset:
-- You work for a data analytics company, and your client is a food delivery platform similar to
-- Jomato. They have provided you with a dataset containing information about various
-- restaurants in a city. Your task is to analyze this dataset using SQL queries to extract valuable
-- insights and generate reports for your client.
-- 
-- Tasks to be performed:
-- Importing the csv FLAT FILE Jomato
SELECT * FROM [dbo].[Jomato];




-- Task 1. Create a user-defined functions to stuff the Chicken into ‘Quick Bites’. 
-- Eg: ‘Quick Chicken Bites’.
DROP FUNCTION stuff_word;

CREATE FUNCTION stuff_word(@phrase VARCHAR(255), @word VARCHAR(50))
RETURNS VARCHAR(255)
AS
BEGIN
	RETURN STUFF(@phrase,CHARINDEX(' ',@phrase,1),0,CONCAT(' ', @word))
END;


SELECT dbo.stuff_word('Quick Bites','Chicken');
SELECT dbo.stuff_word('Once a time','upon');





-- Task 2. Use the function to display the restaurant name and cuisine type which has the
-- maximum number of rating.

SELECT TOP 1 [RestaurantName], [CuisinesType]  FROM Jomato ORDER BY [No_of_Rating] DESC;





-- Task 3. Create a Rating Status column to display the rating as ‘Excellent’ if it has more the 4
-- start rating, ‘Good’ if it has above 3.5 and below 5 star rating, ‘Average’ if it is above 3
-- and below 3.5 and ‘Bad’ if it is below 3 star rating.


ALTER TABLE Jomato ADD Rating_Status VARCHAR(20);
UPDATE Jomato SET Rating_Status = 
	CASE 
		WHEN [Rating] >= 4 THEN 'Excellent'
		WHEN [Rating] >= 3.5 THEN 'Good'
		WHEN [Rating] >= 3 THEN 'Average'
		ELSE 'Bad'
	END;



-- Task 4. Find the Ceil, floor and absolute values of the rating column and display the current date
-- and separately display the year, month_name and day.
SELECT Rating, CEILING(Rating) AS CEIL, FLOOR(Rating) AS FLOOR, ABS(Rating) ABSOLUT FROM Jomato;

SELECT GETDATE() AS DATE, YEAR(GETDATE()) AS YEAR, DATENAME(MONTH,GETDATE()) AS MONTH, DAY(GETDATE()) AS DAY ;
OR
SELECT GETDATE() AS DATE, DATEPART(YEAR,GETDATE()) AS YEAR, DATENAME(MONTH,GETDATE()) AS MONTH, DATEPART(DAY,GETDATE()) AS DAY ;



-- Task 5. Display the restaurant type and total average cost using rollup.
SELECT COALESCE(RestaurantType, 'Overall Average'), AVG(AverageCost) FROM Jomato
	GROUP BY ROLLUP(RestaurantType) ;
