-- для заполнения базы использовал https://github.com/Percona-Lab/mysql_random_data_load

USE vk;

SELECT DISTINCT firstname FROM users ORDER BY firstname ASC;

UPDATE users SET is_deleted=true ORDER BY id ASC LIMIT 5;

DELETE FROM messages WHERE created_at > NOW();