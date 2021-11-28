-- ! READ IF YOU WANT TO ALTER TABLES
-- If you want to alter the tables be sure to update the queries in the 'modules/URL_PARSER.py' and 'main.py'


create table parsed_urls (
    url_id BIGSERIAL PRIMARY KEY NOT NULL,
	URL VARCHAR(1000) NOT NULL,
	text TEXT
);

create table user_info (
	user_query_id BIGSERIAL PRIMARY KEY NOT NULL,
	user_input VARCHAR(150) NOT NULL,
	metachar TEXT
);

create table web_scraped_data (
	web_scraped_id BIGSERIAL PRIMARY KEY NOT NULL,
	URL VARCHAR(1000) NOT NULL,
	file_name VARCHAR(100),
	results TEXT
);