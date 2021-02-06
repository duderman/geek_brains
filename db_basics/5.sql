-- 1. Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
UPDATE users SET created_at=NOW(), updated_AT=NOW() WHERE created_at IS NULL AND updated_at IS NULL;

-- 2. Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате 20.10.2017 8:10. Необходимо преобразовать поля к типу DATETIME, сохранив введённые ранее значения.
ALTER TABLE users ADD COLUMN created_at_dt DATETIME;
ALTER TABLE users ADD COLUMN updated_at_dt DATETIME;

UPDATE users SET created_at_dt=STR_TO_DATE(created_at, '%d.%m.%Y %h:%i');
UPDATE users SET updated_at_dt=STR_TO_DATE(updated_at, '%d.%m.%Y %h:%i');

ALTER TABLE users DROP COLUMN created_at;
ALTER TABLE users DROP COLUMN updated_at;

ALTER TABLE users RENAME COLUMN created_at_dt TO created_at;
ALTER TABLE users RENAME COLUMN updated_at_dt TO updated_at;

-- 3. В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, если товар закончился и выше нуля, если на складе имеются запасы. Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value. Однако нулевые запасы должны выводиться в конце, после всех записей.
SELECT * FROM storehouses_products ORDER BY FIELD(`value`, 0), `value`;

-- 1. Подсчитайте средний возраст пользователей в таблице users.
SELECT AVG(TIMESTAMPDIFF(YEAR, dob, CURDATE())) FROM users;

-- 2. Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. Следует учесть, что необходимы дни недели текущего года, а не года рождения.
SELECT WEEKDAY(DATE_FORMAT(DATE_ADD(dob, INTERVAL (YEAR(CURRENT_DATE()) - YEAR(created_at)) YEAR), '%Y-%m-%d')) AS weekday, COUNT(*)
FROM users
GROUP BY weekday;
