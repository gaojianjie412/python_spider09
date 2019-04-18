
create database u17 default character set=utf8;

use u17;

create table comic (
  id integer auto_increment primary key,
  comic_id varchar(32),
  name varchar(256),
  cover varchar(1024),
  line2 varchar(512)
);

create table comic_chapter (
  id integer auto_increment primary key,
  comic_id varchar(32),
  chapter_id varchar(32),
  chapter_url varchar(1024),
  title varchar(128)

);