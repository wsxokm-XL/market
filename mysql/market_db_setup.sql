drop database if exists test_market;
create database test_market;
use test_market;

drop table if exists users;
drop table if exists users;
drop table if exists key_words;
drop table if exists shopping_records;

create table users
(
    id bigint not null auto_increment,
    username varchar(150) not null unique,
    password varchar(128) not null,
    money varchar(7) default '9999999' check (money>=0),
    primary key (id)
);

create table shops
(
    shops_id int not null auto_increment,
    name varchar(40) not null,
    stock int not null check (stock>=0),
    price int not null check (price>0),
    primary key (shops_id)
);

alter table shops auto_increment=10000;

create table key_words
(
    shops_id int not null,
    key_word varchar(20) not null,
    primary key (shops_id,key_word),
    foreign key (shops_id) references shops(shops_id) on delete cascade
);

create table shopping_records
(
    shopping_id int auto_increment,
    id bigint not null,
    shops_id int not null,
    nums int check(nums>0),
    total int check (total>0 and total<=9999999),
    primary key (shopping_id),
    foreign key (id) references users(id) on delete cascade,
    foreign key (shops_id) references shops(shops_id) on delete cascade
);

alter table shopping_records auto_increment=10000000;

delimiter ||

create trigger shopping after insert on shopping_records for each row
    begin
        update users set users.money=users.money-new.total where users.id=new.id;
        update shops set shops.stock=shops.stock-new.nums where shops_id=new.shops_id;
        end
    ||

delimiter ;


using test_market;
insert into shops(name,stock,price) value ('test1','100','100');
insert into shops(name,stock,price) value ('test2','200','50');
insert into shops(name,stock,price) value ('test3','300','80');
insert into shops(name,stock,price) value ('test4','400','100');
insert into shops(name,stock,price) value ('test5','500','1');
insert into shops(name,stock,price) value ('test6','100','9');
insert into shops(name,stock,price) value ('test7','100','100');
insert into shops(name,stock,price) value ('test8','100','56');
insert into shops(name,stock,price) value ('test9','100','100');

insert into users(username, password) value (
'mytest0','pbkdf2_sha256$260000$s3wYVj7b0rCCcQTxOxsgi6$ifJMu+IUso8udKeCbvgumlyle+HEzjvnH4uIkMtjC4I=');

insert into shopping_records(id, shops_id, nums, total) value (
    '1','10006','6','54'
);

