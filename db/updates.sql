SET SQL_SAFE_UPDATES = 0;

UPDATE results SET flag_team1 = 'x', flag_team2 = 'x'  where g1 = g2;

UPDATE results SET flag_team1 = '1', flag_team2 = '0'  where g1 > g2;

UPDATE results SET flag_team1 = '0', flag_team2 = '2' where g1 < g2;

commit;
