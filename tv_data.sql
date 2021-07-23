-- Creating Sample table and populating with data
drop table if exists tv_watched;

CREATE TABLE tv_watched
(
  	id      SERIAL PRIMARY KEY,
	name	VARCHAR(50),
	hours	NUMERIC
);

insert into tv_watched(name, hours)
Values
	('Han','33'),
	('Christian','12'),
	('Lisa','41'),
	('Jacob','16'),
	('Nick','59'),
	('Ahmed','38'),
	('Peleke','21'),
	('Matt','25');

select * from tv_watched;

-- Creating Sample table and populating with data
drop table if exists tv_watched_geo;

CREATE TABLE tv_watched_geo
(
  	id      SERIAL PRIMARY KEY,
	name	VARCHAR(50),
	hours	numeric,
	lat		numeric,
	lon		numeric
);

insert into tv_watched_geo(name, hours, lat, lon)
Values
	('Han','33', 30.421309, -87.2169149),
	('Christian','12', 43.6166163, -116.20088600000001),
	('Lisa','41', 29.7589382, -95.36769740000001),
	('Jacob','16',	35.996653, -78.90180529999999),
	('Nick','59', 36.1451082, -82.41680550000001),
	('Ahmed','38', 43.6166163, -116.20088600000001),
	('Peleke','21', 43.6166163, -116.20088600000001),
	('Matt','25', 43.6166163, -116.20088600000001);

select * from tv_watched_geo;