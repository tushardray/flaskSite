use footballgames;
SET SQL_SAFE_UPDATES = 0;

create table matches (
id int NOT NULL AUTO_INCREMENT,
datePlayed date,
home_team varchar(30),
away_team varchar(30),
home_score int,
away_score int,
tournament varchar(30),
city varchar(64),
country varchar(40),
neutral varchar(6),
PRIMARY KEY (id)
);
drop table matches;

select * from matches;
delete from matches;

DELETE FROM matches;

select count(*) from matches;

SHOW GLOBAL VARIABLES LIKE 'local_infile';
SET GLOBAL local_infile = true;

LOAD DATA LOCAL INFILE 'C:/Projects/flaskSite/sqlFiles/results.csv'
INTO TABLE matches
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(datePlayed, home_team, away_team, home_score, away_score, tournament, city, country, neutral)
SET ID = NULL;

SHOW VARIABLES LIKE 'secure_file_priv';

update matches set home_team="Scotland" where id=242380;

UPDATE matches SET datePlayed=2022-06-14, home_team=Afghanistan,
                   away_team=Cambodia, home_score=2, away_score=2,
                   tournament=AFC Asian Cup qualification, city=Kolkota, country=India,
            neutral=TRUE where id=286105

SELECT * from matches WHERE id=351640;

SELECT * FROM matches ORDER BY datePlayed DESC LIMIT 21876;

SELECT count(21876) FROM matches ORDER BY datePlayed DESC;