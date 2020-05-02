-- Create Database [stockengine]
CREATE database IF NOT EXISTS STOCK_ENGINE
DEFAULT CHARACTER SET utf8;

SET default_storage_engine = InnoDB;

-- Specify Database [movierecommender]
USE STOCK_ENGINE;

-- Create Table [user]
DROP TABLE IF EXISTS `STOCK_ENGINE`.`user`;
CREATE TABLE `STOCK_ENGINE`.`user` (
  `id` varchar(255) NOT NULL, -- email address 
  `name` varchar(255),
  `password` varchar(255),
  PRIMARY KEY (`id`)
); 

-- Create Table [user_profile]
DROP TABLE IF EXISTS `STOCK_ENGINE`.`user_profile`;
CREATE TABLE `STOCK_ENGINE`.`user_profile` (
  `user_id` varchar(255) NOT NULL, 
  `profile_id` int NOT NULL, -- can not be set as auto_increment 
  `stk_id` varchar(255) NOT NULL,
  `share_price` decimal(15,2) NOT NULL,
  `investment` decimal(15,2) NOT NULL,
  `timestamp` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`,`profile_id`,`stk_id`)
); 

-- Example of inserting data to [user_profile]
SET @time := CURRENT_TIMESTAMP; -- For unifying the timestamp for multiple data
INSERT INTO `STOCK_ENGINE`.`user_profile` (`user_id`, `profile_id`, `stk_id`, `share_price`, `investment`,`timestamp`) 
VALUES ('breehope@me.com', '3', 'IXUS', '1', '1', @time);

INSERT INTO `STOCK_ENGINE`.`user_profile` (`user_id`, `profile_id`, `stk_id`, `share_price`, `investment`,`timestamp`) 
VALUES ('breehope@me.com', '3', 'ILTB', '1', '1', @time);