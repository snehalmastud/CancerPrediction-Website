/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.5.5-10.1.31-MariaDB : Database - 9cancerdiseaseprediction
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`9cancerdiseaseprediction` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `9cancerdiseaseprediction`;

/*Table structure for table `userdetails` */

DROP TABLE IF EXISTS `userdetails`;

CREATE TABLE `userdetails` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mobile` varchar(15) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `userdetails` */

insert  into `userdetails`(`uid`,`name`,`address`,`email`,`mobile`,`password`) values (4,'Chetan Wagadari','soalpur','abc@gmail.com','8989898989','123');
insert  into `userdetails`(`uid`,`name`,`address`,`email`,`mobile`,`password`) values (5,'Chetan Wagadari','soalpur','abcd@gmail.com','9004670813','123');
insert  into `userdetails`(`uid`,`name`,`address`,`email`,`mobile`,`password`) values (6,'a','soalpur','fgh@fd.j','9763004727','123');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
