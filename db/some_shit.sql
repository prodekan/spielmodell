UPDATE results
    SET flag='x' 
    where g1 = g2;

commit;

select * from results where flag not in ('1', '2', 'x');

select count(*), saison from results where flag = '1' group by saison order by saison;

SET SQL_SAFE_UPDATES = 0;