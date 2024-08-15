SELECT  email, COUNT(*) as count FROM Person HAVING count > 1

SELECT email from Person
group by email
having count(email) > 1;