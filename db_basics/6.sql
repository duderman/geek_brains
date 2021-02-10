-- Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.

SELECT from_user_id, COUNT(from_user_id) as msgs_count
    FROM messages
    WHERE to_user_id = :user_id
    GROUP BY from_user_id
    ORDER BY msgs_count DESC
    LIMIT 1;

-- Подсчитать общее количество лайков, которые получили пользователи младше 10 лет.

SELECT COUNT(likes.id) AS likes_count
    FROM likes
    JOIN users u on likes.user_id = u.id
    JOIN profiles p on u.id = p.user_id
    WHERE p.birthday > DATE_SUB(NOW(), INTERVAL 10 YEAR);

-- Определить кто больше поставил лайков (всего): мужчины или женщины.

SELECT p.gender, COUNT(likes.id) as likes_count
    FROM likes
    JOIN users u on u.id = likes.user_id
    JOIN profiles p on u.id = p.user_id
    GROUP BY p.gender
    ORDER BY likes_count DESC
    LIMIT 1;
