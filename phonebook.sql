CREATE TABLE `phonebook` (
`id` integer primary key AUTOINCREMENT,
`first_name` varchar(255) NOT NULL,
`last_name` varchar(255),
`email` varchar(255),
`thumbnail_path` text,
`phone` varchar(15) NOT NULL
);
