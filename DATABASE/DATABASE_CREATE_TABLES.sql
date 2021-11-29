-- ! READ IF YOU WANT TO ALTER TABLES
-- If you want to alter the tables be sure to update the queries in the 'modules/URL_PARSER.py' and 'main.py'



create table user_data (
	query_id BIGSERIAL PRIMARY KEY NOT NULL,
	url VARCHAR(150) NOT NULL,
	html_tag VARCHAR(50),
	file_type VARCHAR(10),
	files INT,
	date VARCHAR(150) NOT NULL

);

create table web_data (
	web_id BIGSERIAL PRIMARY KEY NOT NULL,
	url VARCHAR(1000) NOT NULL,
	html_tag VARCHAR(50),
	file_type VARCHAR(100),
	results TEXT,
	date VARCHAR(150) NOT NULL

);