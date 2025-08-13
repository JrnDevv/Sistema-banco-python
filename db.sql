create database contatos_db;
use contatos_db;

create table contatos (
 id int auto_increment primary key,
 nome varchar(100),
 telefone varchar(20),
 email varchar(100)
 );