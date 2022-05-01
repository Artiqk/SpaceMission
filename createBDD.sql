CREATE DATABASE space_missions;

USE space_missions;

CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `first_name` varchar(255),
  `last_name` varchar(255),
  `age` int,
  `mail` varchar(255)
);

CREATE TABLE `missions` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `mission_name` varchar(255),
  `mission_description` varchar(255),
  `user` varchar(255)
);
