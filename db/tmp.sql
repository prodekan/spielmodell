#  1 -> x heimsieg -> unentschieden

(
select season, playday, flag_team1, count(*) from results
group by  season, playday, flag_team1
order by season, playday
);

select distinct playday from results where season = '1964/1965';

select count(*) from results
where 
season = '2003/2004'
and playday in ('1. Spieltag')
and flag_team1 = '1';

select count(*) from results
where 
season = '2003/2004'
and playday in ('1. Spieltag')
and flag_team1 = 'x';

select count(*) from results
where 
season = '2003/2004'
and playday in ('1. Spieltag')
and flag_team2 = '2';

select * from results
where 
season = '2003/2004'
and playday in ('2. Spieltag') and team2 like '%Bayern%';

desc results;