insert into app_users values('alainricor@gmail.com', 'Alain', 'Rico', '2004-05-31', '1234');
insert into app_users values('test@gmail.com', 'test', 'test', '1970-01-01', '1234');

insert into app_mails values(1, 'alainricor@gmail.com', 'test@gmail.com', 'premier mail envoyee', 'Ca marche bien', '2023-07-23', 0, 0);
insert into app_mails values(2, 'test@gmail.com', 'alainricor@gmail.com', 'premier reponse envoyee', 'message recu', '2023-07-24', 0, 0);

commmit;