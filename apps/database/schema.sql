drop table if exists logging;
create table logging (
  id integer primary key autoincrement,
  req text not null
);
