create database `images`;
use `images`;

create table `persons` (
	`id` int auto_increment primary key,
    `name` varchar(255)
);

create table `person_faces` (
	`id` int auto_increment primary key,
    `person_id` int,
    `image_path` text
);

insert into persons values (default, 'zen');
insert into person_faces values (default, 1, 'unknown.jpg');
