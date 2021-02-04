UPDATE users SET created_at=NOW(), updated_AT=NOW() WHERE created_at IS NULL AND updated_at IS NULL;

ALTER TABLE users ADD COLUMN created_at_dt DATETIME;
ALTER TABLE users ADD COLUMN updated_at_dt DATETIME;

UPDATE users SET created_at_dt=STR_TO_DATE(created_at, '%d.%m.%Y %h:%i');
UPDATE users SET updated_at_dt=STR_TO_DATE(updated_at, '%d.%m.%Y %h:%i');

ALTER TABLE users DROP COLUMN created_at;
ALTER TABLE users DROP COLUMN updated_at;

ALTER TABLE users RENAME COLUMN created_at_dt TO created_at;
ALTER TABLE users RENAME COLUMN updated_at_dt TO updated_at;

SELECT * FROM storehouses_products ORDER BY FIELD(`value`, 0), `value`;

SELECT AVG(TIMESTAMPDIFF(YEAR, dob, CURDATE())) FROM users;

SELECT WEEKDAY(DATE_FORMAT(DATE_ADD(dob, INTERVAL (YEAR(CURRENT_DATE()) - YEAR(created_at)) YEAR), '%Y-%m-%d')) AS weekday, COUNT(*)
FROM users
GROUP BY weekday;
