-- CREATE DATABASE `SE`;
SHOW DATABASES;
SHOW TABLES;
USE `SE`;
DROP TABLE seller;
DROP TABLE customer;

CREATE TABLE seller (
    `id` INT PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `description` TEXT,
    `price` INT NOT NULL
);

INSERT INTO seller (`name`, `description`, `price`) VALUES
('Novel 1', 'Wonderful Story', 500),
('Comics 1', 'Interesting Plot', 300),
('Novel 2', 'Profound theme', 600),
('Comics 2', 'Exquisite painting style', 400),
('Novel 3', 'Thriller and Suspense', 550);

SELECT * FROM seller;



CREATE TABLE customer (
    `c_id` INT PRIMARY KEY,
    `c_name` VARCHAR(255),
    `one_price` INT NOT NULL,
    `unit_quantity` INT NOT NULL,
    FOREIGN KEY (`c_id`) REFERENCES `seller`(`id`)
);

SELECT * FROM customer; 



-- ∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪
-- ★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆★☆
-- ∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪∩∪









CREATE TABLE `settlement`(
	`quantity` INT NOT NULL,
	`price` DECIMAL(10) NOT NULL
);



