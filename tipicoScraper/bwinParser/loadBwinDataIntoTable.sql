select * from simple_quota;

LOAD DATA INFILE 'Bundesliga_out.csv' 
INTO TABLE simple_quota
CHARACTER SET 'utf8'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
(country, liga, @playday, playtime, team1, team2, Q1, QX, Q2, matchday)
set playday = STR_TO_DATE(@playday, '%d.%m.%Y'), creation_date=NOW();

commit;

update results set liga = '1. Bundesliga' where 1=1;

select liga from results where 1=1;
