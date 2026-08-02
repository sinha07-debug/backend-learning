--show all games
select* from games;

-- Show all customers
Select *
from customers;

--show game title and prices
select title,price
from games;

--games cheaper than 30
select* from games
where price<30;

--action genre
select* from games
where genre='Action';

--3 most expensive games
select *from games
order by price desc
limit 3;

-- List all game genres
select distinct genre
from games;

--show every game with its developer name
select games.title,developers.name
from games
join developers
on games.d_id=developers.d_id;

--Show every game along with its developer.
select games.title,developers.name
from games
join developers
on games.developer_id = developers.developer_id;

--Show which games each customer purchased
select c.name,g.g_id,p.price
from customers c
join purchases p
on c.c_id=p.c_id
join games g
on g.g_id=p.g_id

--customers who never bought anything
select c.name
from customers c
left join purchases p
on c.c_id =p.c_id
where p.p_id is NULL

--Average rating per game
SELECT
    g.title,
    AVG(r.rating) AS average_rating
FROM games g
LEFT JOIN reviews r
ON g.g_id = r.g_id
GROUP BY g.title;

--Show only developers with more than one game.
select d.name,count(g.g_id) as total_games
from developers d
join games g
on d.d_id=g.d_id
group by d.name
having count(g.g_id)>1;