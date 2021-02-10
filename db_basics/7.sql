-- 1. Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.
SELECT users.* FROM users LEFT JOIN orders ON users.id = orders.user_id GROUP BY users.id HAVING COUNT(orders.id) > 0;

-- 2. Выведите список товаров products и разделов catalogs, который соответствует товару.
SELECT p.*, c.name FROM products AS p JOIN catalogs c on p.catalog_id = c.id;