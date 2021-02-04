mysqldump example > example_dump.sql
mysql -e "CREATE DATABASE sample;"
mysql sample < example_dump.sql
mysqldump --where "1 LIMIT 100" mysql help_keyword > limit_dump.sql
