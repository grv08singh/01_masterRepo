-- SQL PRT1 Solution: 15-Mar-2025, 03:00PM
-- GAURAV SINGH (grv08singh@gmail.com)

CREATE DATABASE prt1_march;
USE prt1_march;

-- 1) Cheating Analysis:
-- - Count how many students cheated and how many did not.
SELECT 
	SUM(CAST(cheated AS INT)) AS cheated, 
	COUNT([student_id])-SUM(CAST(cheated AS INT)) AS not_cheated 
FROM [dbo].[student_cheating_dataset];




-- 
-- 2) Penalty Distribution:
-- - Retrieve the average, minimum, and maximum penalty points given to students.
SELECT 
	AVG([penalty_points]) AS avg_pen_points,
	MIN([penalty_points]) AS min_pen_points,
	MAX([penalty_points]) AS max_pen_points
FROM [dbo].[student_cheating_dataset];



-- 
-- 3) Behavior and Cheating:
-- - Find the most common behavior among students who were caught cheating.
WITH cte AS
(SELECT [student_behavior], COUNT([student_behavior]) AS beh_count
FROM [dbo].[student_cheating_dataset]
WHERE [caught_cheating] = 1
GROUP BY [student_behavior])
SELECT [student_behavior] AS most_common_behaviour
FROM cte
WHERE beh_count = 
	(SELECT MAX(beh_count) FROM cte);




-- 
-- 4) Proctor Impact:
-- - Count how many students cheated in exams with a proctor present vs. without a proctor.
WITH cte AS
(SELECT * 
FROM [dbo].[student_cheating_dataset]
WHERE [cheated] = 1)
SELECT 
	SUM(CAST([proctor_present] AS INT)) AS proc_present, 
	COUNT([student_id])-SUM(CAST([proctor_present] AS INT)) AS without_proc
FROM cte;


-- 
-- 5) Subject-Wise Cheating Rates:
-- - Calculate the percentage of students who cheated in each subject.
WITH cte1 AS
(SELECT [subject], COUNT([student_id]) AS cheated
FROM [dbo].[student_cheating_dataset]
WHERE [cheated] = 1
GROUP BY [subject]),
cte2 AS
(SELECT [subject], COUNT([student_id]) AS total_students
FROM [dbo].[student_cheating_dataset]
GROUP BY [subject])

SELECT 
	cte1.subject, 
	cte1.cheated, 
	cte2.total_students,
	CAST((100*CAST(cte1.cheated AS DECIMAL(5,2))/CAST(cte2.total_students AS DECIMAL(5,2))) AS DECIMAL(5,2)) AS cheated_percentage
FROM cte1
JOIN cte2
ON cte1.subject = cte2.subject;

-----------------------------------------
-- END
-----------------------------------------


