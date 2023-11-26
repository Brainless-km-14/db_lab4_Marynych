INSERT INTO Champion(ID,Name, represented_country)
VALUES
	(1, 'Chris Bumstead', 'Canada'),
    (2, 'Breon Ansley', 'United States'),
    (3, 'Danny Hester', 'United States');

INSERT INTO Venue(city_id, City, Country)
VALUES
	(1, 'Las Vegas', 'United States'),
	(2, 'Orlano', 'United States');

INSERT INTO Year(Year,Award$,city_id,ID)
VALUES
	(2016,12500,1, 3),
	(2017, 20000,1, 2),
	(2018, 20000,1, 2),
	(2019,30000,1, 1),
	(2020,30000,2, 1),
	(2021,50000,2, 1),
	(2022,50000,1, 1),
	(2023,50000,2, 1);



