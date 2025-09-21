create database new_assign1;

use new_assign1;
--------------------------------------------------------------------------------------------

-----------Assignment-1
--1. Install MS SQL Server







--2. Give the difference between Char and Varchar data type. 

--char(10) - abcde_____
--fixed length characters
--n bytes
--consistent

--varchar(10) - aaa(7 empty)
--variable length charaters
--actual length + 2 bytes
--non consistent




--3. Explain the types of SQL Commands. 

--DDL - defination
--create -- create a database object
--alter -- alter modify an existing database object
--drop -- deletes databasebase object permentately
--truncate --deletes all the records and leaves the structure of the table
--DML - manipulation
--insert -- add records to table
--update --modifies the records in the table 
--delete --removes specific records

--DQL -- Query
--select -- display /retrieve the data from the database object

--TCL -- Transaction control
--commit --save the changes in a transaction
--rollback -- undo the transaction
--savepoint -- creates checkpoint in transaction
--DCL --Control
--Grant- gives permission
--revoke removes persission





--4. Explain NVarchar and Nchar

--accept unicode language
--nchar n*2 bytes
--nvarchar actual length *2 +2 bytes


--------------------------------------------------------------------------------------------
---------Assignment-2
--1. Create a customer table which comprises of these columns: ‘customer_id’,
--‘first_name’, ‘last_name’, ‘email’, ‘address’, ‘city’,’state’,’zip’ 

create table customer(
customer_id int,
first_name varchar(30),
last_name varchar(20),
email varchar(20),
address varchar(50),
city varchar(20),
zip char(6)
);

select * from customer;

--2. Insert 5 new records into the table

insert into customer values
(106, 'Jhon','Smith','smith@email.com','address1','San Jose','345671'),
(107, 'Emma','Jackson','emma@gmail.com','address1','Bangalore','345671'),
(108, 'Alex','Brown','smith@email.com','address1','Chennai','345671'),
(109, 'Ria','Davis','ria@gmail.com','address1','Hydrabad','345671'),
(110, 'Gia','Miller','smith@email.com','address1','Kolkata','345671');



select * from customer;

--3. Select only the ‘first_name’ and ‘last_name’ columns fromthe customer
--table
select first_name, last_name from customer;

--4. Select those records where ‘first_name’ starts with “G” and city is ‘SanJose’. 

select * from customer
where first_name LIKE 'g%' and
city = 'San Jose';

select * from customer;

select * from customer
where first_name LIKE '%a%';





--5. Select those records where Email has only ‘gmail’. 

select * from customer;


select * from customer
where email LIKE '%@gmail%';


--6. Select those records where the ‘first_name’ doesn't end with “A”.


select * from customer;


select * from customerwhere first_name not like '%a';


--------------------------------------------------------------------------------------------
----------Assignment-3
--1. Create an ‘Orders’ table which comprises of these columns: ‘order_id’,
--‘order_date’, ‘amount’, ‘customer_id’. 


create table Orders(
order_id int,
order_date date,
amount money, --decimal(10,2)
customer_id int
);

select * from orders;

--2. Insert 5 new records. 

insert into orders values
(1001, '2025-02-12', 50000,101),
(1002, '2024-02-12', 65000,102),
(1003, '2023-08-13', 34000,103),
(1004, '2022-04-18', 67000,104),
(1005, '2024-07-22', 23000,105);

insert into orders values
(1006, '2025-02-12', 1000,107);

select * from Orders;
select * from customer;
--3. Make an inner join on ‘Customer’ and ‘Orders’ tables on the ‘customer_id’ column.

select * from Orders;
select * from customer;

select * from Orders o
inner join
Customer c
ON o.customer_id = c.customer_id;

select c.customer_id, amount from Orders o
inner join
Customer c
ON o.customer_id = c.customer_id;

--Types of Joins
--inner -- only common in both the table 

--full outer --all the records from both the table 
--it will NULL values when no matching data available

--left--all the records from the left table 
--and only the matching records from the right table 
--NULL in the right table when there is no matching 

--right --all the records from the right table 
--and only the matching records from the left table 
--NULL in the left table when there is no matching 

--cross --all the records as a combination of two tables
select * from orders;
select * from customer;

select * from orders
cross join
customer;

select * from customer;

select * into customer_2 from customer;

select * from customer_2;

--self --1 --need a two columns having simlar data so that 

drop table new_table;

create table new_table(
id int,
name1 varchar(20),
name2 varchar(20));

insert into new_Table values
(1,'hima','shiv'),
(2,'hima','arpita'),
(3,'shiv','arpita');

select * from new_table;

select a.id, a.name1, a.name2 from new_table a
join
new_table b
ON a.id =b.id

alter table customer_2
drop column first_name;

alter table customer_2
add first_name varchar(20);

select * from customer_2;

--4. Make left and right joins on ‘Customer’ and ‘Orders’ tables on the‘customer_id’ column. 
select * from Orders o
left join
Customer c
ON o.customer_id = c.customer_id;

select c.customer_id, amount from Orders o
right join
Customer c
ON o.customer_id = c.customer_id;

--5. Make a full outer join on ‘Customer’ and ‘Orders’ table on the ‘customer_id’ column.


select * from Orders o
full outer join
Customer c
ON o.customer_id = c.customer_id;



--6. Update the ‘Orders’ table and set the amount to be 100where‘customer_id’ is 103

select * from Orders;

update Orders
set amount = 100
where customer_id =103; 



--------------------------------------------------------------------------------------------
-----------Assignment-4


--1. Use the inbuilt functions and find the minimum, 
--maximumand average amount from the orders table

select * from Orders;

select min(amount) AS Min_,
max(amount) AS Max_,
avg(amount) AS Avg_ 
from Orders

--inbuilt
---aggregate
---string
---date
----window

--user defined
----scalar value returning - single
----table value returning - table


--2. Create a user-defined function which will multiply the given number with 10

create function multiply_10(@num int)
returns decimal(10,2)
AS
begin
return @num * 10
end;

select dbo.multiply_10(25) AS reult;






--3. Use the case statement to check if 100 is less than 200, greater than200or 
--equal to 200 and print the corresponding value. 

select 
CASE
when 100 > 200 then '100 is greater'
when 200 > 100 then '200 is greater'
else 'Unknown'
end AS condition;








--4. Using a case statement, find the status of the amount. Set the status 
--of theamount as high amount, low amount or medium amount based upon the condition. 


select * from Orders;

select amount,
CASE
when amount >=50000  then 'max'
when amount >=1000  then 'min'
else 'Invalid'
end as amt_Condition
from Orders;


--5. Create a user-defined function, to fetch the amount greater thanthengiveninput.

select * from Orders;

create function amtgreater(@amt money)
returns table
AS
return
(
select * from Orders
where amount > @amt
);

select * from amtgreater(1000);



-------------------------------------------------

--1. Arrange the ‘Orders’ dataset in decreasing order of amount

select * from Orders
order by amount desc;


---Create a table with the name ‘Employee_details1’ consistingof thesecolumns: 
--‘Emp_id’, ‘Emp_name’, ‘Emp_salary’. Create another tablewiththe name ‘Employee_details2’ 
--consisting of the same columns asthefirst
--table.

select * from Customer;

select * into customer_3 from customer;

--. Apply the UNION operator on these two tables
------------------------------------------------------------------------
--set opertaors
--Union -- all the combined data is executed 
--union all -- all the combined data is executed (includes duplicates)
--intersect
--except

select * from Customer_2;
select * from Customer
Except
select * from Customer_3;



select * from customer_3
Union all
select * from Customer;
