# Write your MySQL query statement below
SELECT DISTINCT salary AS SecondHighestSalary 
FROM Employee
UNION ALL
    SELECT NULL as SecondHighestSalary
UNION ALL
    SELECT NULL as SecondHighestSalary
ORDER BY SecondHighestSalary DESC
LIMIT 1 
OFFSET 1
;

-- union all does not act as select distinct
-- union acts as a select distinct and removes duplicates