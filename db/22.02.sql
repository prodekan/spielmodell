select * from league;

update league set code = 'BL1' where id = 1;
update league set code = 'BL2' where id = 2;
update league set code = 'BL3' where id = 3;
update league set code = 'PRL' where id = 4;
update league set code = 'CHS' where id = 5;
update league set code = 'LE1' where id = 6;
update league set code = 'LE2' where id = 7;

desc results;

update results set league = 'BL1';

SET SQL_SAFE_UPDATES = 0;

commit;