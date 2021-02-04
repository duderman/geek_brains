USE vk;

DROP TABLE IF EXISTS `support_requests_assigns`;
DROP TABLE IF EXISTS `support_operators`;
DROP TABLE IF EXISTS `support_requests`;

CREATE TABLE `support_operators` (
	id SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED NOT NULL,
	`level` ENUM('junior', 'middle', 'senior') NOT NULL,
	started_at DATETIME DEFAULT NOW() NOT NULL,
	
	INDEX operators_level_idx(`level`),
	FOREIGN KEY (user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `support_requests` (
	id SERIAL PRIMARY KEY,
	from_user_id BIGINT UNSIGNED NOT NULL,
	status ENUM('created','processing','resolved'),
	created_at DATETIME DEFAULT NOW(),

    FOREIGN KEY (from_user_id) REFERENCES users(id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `support_requests_assigns` (
	id SERIAL PRIMARY KEY,
	support_request_id BIGINT UNSIGNED NOT NULL,
	support_operator_id BIGINT UNSIGNED NOT NULL,

    FOREIGN KEY (support_request_id) REFERENCES support_requests(id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (support_operator_id) REFERENCES support_operators(id) ON UPDATE CASCADE ON DELETE CASCADE
);