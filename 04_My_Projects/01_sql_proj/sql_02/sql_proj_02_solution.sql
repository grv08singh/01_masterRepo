CREATE DATABASE sql_proj_02;
USE sql_proj_02;

-- Q01. Retrieve all successful bookings:
SELECT * FROM ola_bookings WHERE Booking_Status = 'Success';

-- Q02. Find the average ride distance for each vehicle type:
SELECT Vehicle_Type, AVG(ride_distance) AS avg_ride_distance
FROM ola_bookings
GROUP BY vehicle_type;

-- Q03. Get the total number of cancelled rides by customers:
SELECT COUNT(*) AS Canc_rides_by_cust FROM ola_bookings WHERE Booking_Status = 'Canceled by Customer';

-- Q04. List the top 5 customers who booked the highest number of rides:
SELECT TOP 5 Customer_ID, COUNT(Customer_ID) AS No_of_bookings FROM ola_bookings GROUP BY Customer_ID ORDER BY COUNT(Booking_ID) DESC;

-- Q05. Get the number of rides cancelled by drivers due to personal and car-related issues:
SELECT COUNT(*) AS Canc_by_drvr FROM ola_bookings WHERE Canceled_Rides_by_Driver = 'Personal & Car related issue';

-- Q06. Find the maximum and minimum driver ratings for Prime Sedan bookings:
SELECT MAX(Driver_Ratings) AS Maximum_rating, MIN(Driver_Ratings) AS Minimum_rating FROM ola_bookings WHERE Vehicle_Type = 'Prime Sedan';

-- Q07. Retrieve all rides where payment was made using UPI:
SELECT * FROM ola_bookings WHERE Payment_Method = 'UPI';

-- Q08. Find the average customer rating per vehicle type:
SELECT Vehicle_Type, AVG(Customer_Rating) AS avg_cust_rating
FROM ola_bookings
GROUP BY Vehicle_Type;

-- Q09. Calculate the total booking value of rides completed successfully:
SELECT SUM(Booking_Value) AS total_booking_val
FROM ola_bookings
WHERE Booking_Status = 'Success';

-- Q10. List all incomplete rides along with the reason:
SELECT Booking_ID, Incomplete_Rides_Reason FROM ola_bookings WHERE Incomplete_Rides = 1;
