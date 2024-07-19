/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - icds
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`icds` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `icds`;

/*Table structure for table `agency` */

DROP TABLE IF EXISTS `agency`;

CREATE TABLE `agency` (
  `agency_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`agency_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `agency` */

/*Table structure for table `agency_staff` */

DROP TABLE IF EXISTS `agency_staff`;

CREATE TABLE `agency_staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `agency_staff` */

/*Table structure for table `anganavadi` */

DROP TABLE IF EXISTS `anganavadi`;

CREATE TABLE `anganavadi` (
  `angu_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `licence_no` bigint(25) DEFAULT NULL,
  `place` varchar(25) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `post` varchar(15) DEFAULT NULL,
  `pin` bigint(11) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`angu_id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

/*Data for the table `anganavadi` */

insert  into `anganavadi`(`angu_id`,`name`,`licence_no`,`place`,`phone`,`email`,`post`,`pin`,`login_id`) values (27,'nvbnvn',12345,'fghfgh',8593996328,'gjghjgj','hjgjgj',123456,109),(31,'fvdfg',12345,'df',8877665549,'aa@gmail.com','fdg',339900,146),(34,'Secondpath',12345,'calicut',8877665556,'aha@gmail.com','calicut',673600,158),(35,'asdfghjklmn',12345,'df',8877612344,'rrhh@gmail.com','fsdf',673600,161),(43,'Tulipsqueen',22344,'dg',1234567891,'aa@gmail.com','gg',673600,43),(44,'hgvgfgggg',12310,'njkjh',989776675,'sbbnd@gmail.com','Kozhikode',987654,244);

/*Table structure for table `calendar` */

DROP TABLE IF EXISTS `calendar`;

CREATE TABLE `calendar` (
  `calender_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `program` varchar(30) DEFAULT NULL,
  `details` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`calender_id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `calendar` */

insert  into `calendar`(`calender_id`,`date`,`program`,`details`) values (17,'2019-10-18','uuu','hjkjk'),(19,'2019-10-27','nbnb','nmbn'),(20,'2019-10-12','nbnb','gfdgdfgfdgdfgdfg'),(21,'1998-08-07','jh','uyg'),(22,'2019-10-31','njbh','hjghghbnbn');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) DEFAULT NULL,
  `recid` int(11) DEFAULT NULL,
  `message` varchar(35) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time` time DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

insert  into `chat`(`chat_id`,`userid`,`recid`,`message`,`date`,`time`) values (1,245,1,'dgd','2020-02-26','09:53:52'),(2,245,1,'dgddgdg','2020-02-26','09:53:54'),(3,245,1,'dgddgdg','2020-02-26','09:53:55'),(4,245,1,'fgf','2020-02-26','09:54:00'),(5,1,245,'haii','2020-02-26','09:54:00'),(6,245,1,'ghg','2020-02-26','09:55:12'),(7,245,1,'hloo','2020-02-26','09:55:35'),(8,245,1,'hloo','2020-02-26','09:55:36'),(9,245,1,'hloo','2020-02-26','09:55:38'),(10,245,1,'nm','2020-02-26','09:55:44'),(11,245,1,'xgd','2020-02-26','09:58:09'),(12,245,1,'xgd','2020-02-26','09:58:13'),(13,245,1,'xgd','2020-02-26','09:58:13'),(14,245,1,'hooi','2020-02-26','09:58:18'),(15,1,245,'any help','2020-02-26','09:58:18'),(16,1,245,'if you need any help,please contact','2020-02-26','09:58:18'),(17,245,1,'okay','2020-02-26','10:01:55'),(18,245,1,'okay','2020-02-26','10:01:57'),(19,245,1,'thank you','2020-02-26','10:02:05'),(20,245,1,'helw','2020-02-26','10:23:06'),(21,245,1,'excuse me','2020-02-26','10:47:08'),(22,1,0,'\"+ta+\"','2020-02-26',NULL),(23,1,245,'ok','2020-02-26','10:56:58'),(24,1,245,'hello','2020-02-26','16:17:40'),(25,245,1,'mm','2020-02-26','16:18:04'),(26,245,1,'hey','2020-02-26','16:20:39'),(27,1,245,'fine?','2020-02-26','16:20:52'),(28,245,1,'yaa','2020-02-26','16:20:56'),(29,245,1,'we need help','2020-02-26','16:21:21'),(30,1,245,'what','2020-02-26','16:21:37'),(31,1,245,'mm...?','2020-02-26','16:22:12'),(32,245,1,'waitt','2020-02-26','16:22:20'),(33,1,244,'hello','2020-02-26','16:22:50'),(34,245,1,'haii','2020-03-04','20:41:09'),(35,1,245,'how are you','2020-03-04','20:43:34'),(36,1,245,'bb','2020-03-04','20:44:10'),(37,245,1,'gcc','2020-03-04','21:02:51'),(38,245,1,'yaa','2020-03-04','21:06:43'),(39,245,1,'hloo','2020-03-04','22:52:05'),(40,245,1,'hii','2020-03-04','23:17:49'),(41,245,1,'jgdjkf','2020-03-05','15:56:01'),(42,1,245,'helwwwwwwwwwwwwwww','2020-03-05','15:56:33'),(43,245,1,'haii','2020-03-09','09:25:57'),(44,245,1,'h','2020-03-09','17:16:01');

/*Table structure for table `checkup` */

DROP TABLE IF EXISTS `checkup`;

CREATE TABLE `checkup` (
  `checkup_id` int(11) NOT NULL AUTO_INCREMENT,
  `child_mother_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `details` varchar(40) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`checkup_id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=latin1;

/*Data for the table `checkup` */

insert  into `checkup`(`checkup_id`,`child_mother_id`,`date`,`details`,`status`) values (2,0,'0000-00-00','\"+remarks+\"',NULL),(3,0,'2019-09-05','bjbjb',NULL),(7,7,'2019-10-16','fdddgd',NULL),(8,7,'2019-10-09','nmbmb',NULL),(9,7,'2019-10-09','ghfhfh',NULL),(10,1,'2019-10-08','ghfh','child'),(11,11,'2019-10-03','ererre',NULL),(12,11,'2019-10-09','khkhkj',NULL),(13,1,'2019-10-09','hgfhfgh','mother'),(14,9,'2019-10-02','dgdfgdfg',NULL),(15,1,'2019-10-05','p','mother'),(16,1,'2019-10-02','jjk',NULL),(17,1,'2019-10-02','jghjgjh','mother'),(18,2,'2019-10-02','gdfgdfg','mother'),(19,2,'2019-10-02','sdsdsd','mother'),(20,2,'2019-10-31','hgghj','mother'),(21,2,'2019-10-06','cc','child'),(22,31,'2019-10-23','ssy','mother'),(23,2,'2019-10-01','ooooo','child'),(24,1,'0000-00-00','kjkj','mother'),(25,1,'0000-00-00','kjkjkj','mother'),(26,1,'2019-10-18','kjkj','mother'),(27,36,'0000-00-00','','mother'),(28,36,'0000-00-00','','mother'),(29,36,'2019-10-12','ffgfg','mother'),(30,1,'2019-10-04','','child'),(31,1,'2019-10-04','','child'),(32,1,'2019-10-18','jhjg','child'),(33,38,'2019-10-19','dfsdf','mother'),(34,52,'2019-10-17','jghjghj','mother'),(35,46,'2019-10-05','jghjgj','mother'),(36,46,'2019-10-05','jghjgj','mother'),(37,46,'2019-10-05',',jk','mother'),(38,46,'2019-10-05',',jk','mother'),(39,46,'2019-10-19','gghghj','mother'),(40,46,'2019-10-05','jghjgj','mother'),(41,52,'2019-10-26','eeee','mother'),(42,52,'2019-10-12','jkhjk','mother'),(43,38,'2019-10-26','hjghj','mother'),(44,6,'2019-10-31','jklkjlk','child'),(45,6,'2019-10-25','ytrytry','child'),(46,1,'2019-10-17','gfhfgh','child'),(47,46,'2019-10-26','mbnmbnm','mother'),(48,1,'2019-10-19','h','child'),(49,46,'2019-10-19','GHJGJG','mother'),(50,38,'2019-10-31','HGFHH','mother'),(51,6,'2019-10-19','jhghj','child'),(52,47,'2019-10-26','kjk','mother'),(53,2,'2019-10-28','babgfg','mother'),(54,12,'2019-10-26','ssssddd','child'),(55,49,'2019-10-19','bhfhdfghf','mother'),(58,50,'2019-10-21','y','mother'),(61,50,'2019-10-15','kmklm','mother'),(62,50,'2019-10-20','iiuj','mother'),(63,50,'2019-10-19','jhjhj','mother'),(64,13,'2019-10-19','hghghjg','child'),(65,11,'2019-10-18','hjkhkhkhh','child');

/*Table structure for table `child_reg` */

DROP TABLE IF EXISTS `child_reg`;

CREATE TABLE `child_reg` (
  `child_reg_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `bloodgroup` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `weight` varchar(20) DEFAULT NULL,
  `fathername` varchar(20) DEFAULT NULL,
  `mothername` varchar(20) DEFAULT NULL,
  `motheraadharno` bigint(20) DEFAULT NULL,
  `fatheraadharno` bigint(20) DEFAULT NULL,
  `fatherjob` varchar(30) DEFAULT NULL,
  `house` varchar(20) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `dist` varchar(20) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `hospital_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`child_reg_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `child_reg` */

insert  into `child_reg`(`child_reg_id`,`name`,`dob`,`bloodgroup`,`gender`,`weight`,`fathername`,`mothername`,`motheraadharno`,`fatheraadharno`,`fatherjob`,`house`,`post`,`dist`,`state`,`pin`,`email`,`phone`,`hospital_id`) values (1,'achu','2019-10-25','O+ve','male','44','jjjj','minnu',6755443399662,1234567891231,'bcvbc','cvbcvb','cvb','vcbcb','vcbcvb',656657,'vbcvbcb',5567668887,38),(12,'unnikutti','2017-06-06','O+ve','female','12','asok','seena',6789097856342,6876876666444,'artist','punyaa','kakkodi','calicut','kerala',673612,'qqq@gmail.com',8877665544,38),(18,'chikku','2019-12-22','O+ve','female','12','ajit','ammu',6788990088097,6745990088097,'artist','vykashi','calicut','calicut','kerala',673609,'vyaka@gmail.com',9866332211,38);

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaints` varchar(60) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`complaints`,`login_id`,`date`,`status`) values (5,'utyutgjhjhkhjgkgjkgk',43,'2019-10-08','seen'),(17,'hfgfh',43,'2019-10-09','seen'),(18,'help....!',158,'2019-10-09','seen'),(21,'rrrrrrrrr',42,'2019-10-10','pending'),(22,'ayyyo',158,'2019-10-10','seen'),(23,'ha ha ha\r\n',158,'2019-10-10','seen'),(25,'httuuytyu',158,'2019-10-10','pending'),(26,'gfdhfghgh',161,'2019-10-10','seen'),(27,'hggjghj',43,'2019-10-10','seen'),(30,'ghjgjghj',43,'2019-10-11','pending'),(31,'help me..........please!!!!!!!!!!',43,'2019-10-11','seen'),(32,'vvttddoo',43,'2019-10-13','pending'),(37,'howw',210,'2010-01-01','pending'),(38,'jhjhjh',43,'2019-10-21','seen'),(39,'dfgdgfdgf',1,'2019-10-22','pending'),(40,'hdfgdhfgdgf',43,'2019-10-22','pending');

/*Table structure for table `deathcer` */

DROP TABLE IF EXISTS `deathcer`;

CREATE TABLE `deathcer` (
  `d_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `nameoffather` varchar(20) DEFAULT NULL,
  `nameofmother` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `placeofdeath` varchar(20) DEFAULT NULL,
  `postofdeath` varchar(20) DEFAULT NULL,
  `pinofdeath` bigint(20) DEFAULT NULL,
  `infoname` varchar(50) DEFAULT NULL,
  `contact` bigint(20) DEFAULT NULL,
  `sign` varchar(50) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `deathcer` */

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(35) DEFAULT NULL,
  `hospital_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`dept_id`,`name`,`hospital_id`) values (2,'cs',37),(4,'Cardiac sectionmnmn',38),(7,'ff',34),(8,'gdg',40),(16,'neuro',38),(17,'Aayur Vedic type',38);

/*Table structure for table `duty_allocation` */

DROP TABLE IF EXISTS `duty_allocation`;

CREATE TABLE `duty_allocation` (
  `allocation_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `vaccination_date_id` int(11) DEFAULT NULL,
  `angu_id` int(11) DEFAULT NULL,
  `vaccination_id` int(11) DEFAULT NULL,
  `health_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`allocation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;

/*Data for the table `duty_allocation` */

insert  into `duty_allocation`(`allocation_id`,`staff_id`,`vaccination_date_id`,`angu_id`,`vaccination_id`,`health_id`) values (1,3,0,2,0,NULL),(2,3,0,2,0,NULL),(14,16,2,3,0,NULL),(15,16,2,3,7,NULL),(16,16,2,3,7,NULL),(17,7,3,16,2,NULL),(18,4,1,29,3,NULL),(19,13,10,27,3,NULL),(20,0,0,0,0,NULL),(21,0,0,0,0,NULL),(22,0,0,34,0,NULL),(23,0,0,34,0,NULL),(24,0,0,0,0,NULL),(25,0,0,0,0,NULL),(26,0,0,0,0,NULL),(27,0,0,0,0,NULL),(28,0,0,0,0,NULL),(29,0,0,0,0,NULL),(32,17,3,31,2,NULL),(34,30,13,27,7,NULL),(35,32,7,31,2,NULL),(36,32,7,31,2,90),(37,32,3,34,4,90),(39,18,7,43,7,41),(53,7,2,27,1,41),(58,46,4,31,2,41),(60,46,6,43,3,41);

/*Table structure for table `enroll_child` */

DROP TABLE IF EXISTS `enroll_child`;

CREATE TABLE `enroll_child` (
  `child_id` int(11) NOT NULL AUTO_INCREMENT,
  `angu_id` int(11) DEFAULT NULL,
  `hospital_child_reg_id` int(11) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`child_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `enroll_child` */

insert  into `enroll_child`(`child_id`,`angu_id`,`hospital_child_reg_id`,`photo`,`date`) values (1,43,38,'/static/pics/Screenshot (1).png','2019-10-03'),(2,43,2,'/static/pics/th.jpg','2019-10-03'),(3,43,2,'/static/pics/th.jpg','2019-10-04'),(4,43,4,'/static/pics/28su9mp.jpg','2019-10-10'),(5,43,4,'/static/pics/Christmas_bauble_black_and_white.jpg','2019-10-10'),(6,43,4,'/static/pics/download (1).jpg','2019-10-10'),(7,43,3,'/static/pics/Christmas_bauble_black_and_white.jpg','2019-10-10'),(8,43,3,'/static/pics/Christmas_bauble_black_and_white.jpg','2019-10-10'),(9,43,6,'/static/pics/images (3).jpg','2019-10-10'),(10,43,5,'/static/pics/christmas-cake.jpg','2019-10-10'),(11,43,2,'/static/pics/28su9mp.jpg','2019-10-10'),(12,43,2,'/static/pics/28su9mp.jpg','2019-10-10'),(13,43,2,'/static/pics/download (1).jpg','2019-10-10'),(14,43,1,'/static/pics/images.jpg','2019-10-10'),(15,43,8,'/static/pics/download (1).jpg','2019-10-10'),(16,43,7,'/static/pics/christmas-cake.jpg','2019-10-11'),(17,43,7,'/static/pics/christmas-cake.jpg','2019-10-11'),(18,43,12,'/static/pics/28su9mp.jpg','2019-10-11'),(19,43,13,'/static/pics/Screenshot_20190811-212818-01.jpeg','2019-10-13'),(20,1,17,'/static/pics/christmas-cake.jpg','2019-10-22'),(21,NULL,NULL,NULL,NULL),(22,43,17,'/static/pics/IMG_20190516_162038396-01.jpeg','2019-12-05'),(23,43,17,'/static/pics/IMG_20190516_162038396-01.jpeg','2019-12-05'),(24,43,11,'/static/pics/IMG_20170923_080359173.jpg','2019-12-05'),(25,43,11,'/static/pics/IMG_20170923_080359173.jpg','2019-12-05');

/*Table structure for table `enroll_mother` */

DROP TABLE IF EXISTS `enroll_mother`;

CREATE TABLE `enroll_mother` (
  `mother_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `dob` varchar(25) DEFAULT NULL,
  `bloodgroup` varchar(25) DEFAULT NULL,
  `height` varchar(25) DEFAULT NULL,
  `weight` varchar(50) DEFAULT NULL,
  `aadhar_no` varchar(15) DEFAULT NULL,
  `occupation` varchar(11) DEFAULT NULL,
  `hus_name` varchar(20) DEFAULT NULL,
  `hus_aadharno` bigint(20) DEFAULT NULL,
  `hus_occupation` varchar(30) DEFAULT NULL,
  `house` varchar(20) DEFAULT NULL,
  `postoffice` varchar(20) DEFAULT NULL,
  `pin` varchar(20) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  `district` varchar(20) DEFAULT NULL,
  `angu_id` int(11) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`mother_id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1;

/*Data for the table `enroll_mother` */

insert  into `enroll_mother`(`mother_id`,`name`,`dob`,`bloodgroup`,`height`,`weight`,`aadhar_no`,`occupation`,`hus_name`,`hus_aadharno`,`hus_occupation`,`house`,`postoffice`,`pin`,`state`,`email`,`phone`,`photo`,`district`,`angu_id`,`lid`) values (2,'neena','2019-10-02','AB+ve','5646','66','8977669877342','hfghfgh','fghfghfgh',8977669877342,'hsbs','dgdgdg','gdgdg','646456','dfgdgdg','dfgdgdg@gmail.com',8766554434,'/static/pics/2018-03-18-10-04-46-106-01.jpeg','gdgdfg',43,NULL),(49,'minnu','2019-10-19','B+ve','140','43','6755443399662','artit','ajith',6755443399668,'engineer','raroth','panagad','673611','kerala','min@gmail.com',8877665544,'/static/pics/images (3).jpg','calicut',43,244),(50,'nehla','2019-10-19','AB+ve','232','33','3344221133221','cdfdf','dfdfdf',3344221133223,'jhjhjh','bbnj','kokkallur','673612','jhkjh','jhjhj@gmail.com',9988776654,'/static/pics/2019-02-09-13-53-07-714-01.jpeg','jhjhkhj',43,NULL),(51,'jjjj','2019-10-02','AB+ve','150000','45445454','1234567891236','Abbbb','Husb',1234567891237,'Hoccu','Hname','ABcd','987845','Kerala','abcd@gmail.com',4545454554,'/static/pics/IMG_20170923_080359173-01.jpeg','Dist',43,NULL),(52,'Seena','1998-09-12','O-ve','123','67','6789097856342','jhj','kjkk',6789097856348,'jkjkj','kjkjkj','kjkjkj','673609','jkjlkjkj','aa@gmail.com',9087563412,'/static/pics/Screenshot_20190811-212818-01.jpeg','jlkjkjkj',43,245);

/*Table structure for table `healthcentre` */

DROP TABLE IF EXISTS `healthcentre`;

CREATE TABLE `healthcentre` (
  `healthcentre_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `licence_no` bigint(25) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`healthcentre_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

/*Data for the table `healthcentre` */

insert  into `healthcentre`(`healthcentre_id`,`login_id`,`name`,`licence_no`,`place`,`post`,`pin`,`email`,`phone`) values (13,91,'bcc',65454,'fgdfg','fgfdgd',567587,'fgfg@gmail.com',8877665544),(19,117,'fghfh',12332,'dfgdfg','gdgdg',123456,'gdgdg',8866554433),(23,145,'Lollipop',12355,'aa','fsdf',673609,'aa@gmail.com',8877665541),(26,211,'hgjghjghj',92155,'nbmnmbnm','nmbnm',887764,'hgjhj@gmail.com',9988776655),(27,212,'hgjghjghj',90921,'nbmnmbnm','nmbnm',887766,'hgjhj@gmail.com',9988776655),(28,230,'V4U',90080,'calicut','calicut',675800,'dfgdgdg@gmail.com',9078674539),(30,247,'mknjn',78778,'bnbvb','vgvghh',908766,'bbjh@gmail.com',6776766767);

/*Table structure for table `hospital` */

DROP TABLE IF EXISTS `hospital`;

CREATE TABLE `hospital` (
  `hospital_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `Licence_no` bigint(25) DEFAULT NULL,
  `owner_name` varchar(20) DEFAULT NULL,
  `Year_ofestablishment` int(11) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(15) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`hospital_id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=latin1;

/*Data for the table `hospital` */

insert  into `hospital`(`hospital_id`,`name`,`Licence_no`,`owner_name`,`Year_ofestablishment`,`place`,`post`,`pin`,`email`,`phone`,`lid`) values (10,'asd',99977,'gfgfg',1223,'jghjghj','hjgjgj',123456,'raj@gmail.com',8877335544,38),(11,'starcare',4535,'fggf',3434,'gff','fghf',4656,'ghfh',4354,40),(12,'asd',67673,'gfgfg',1223,'jghjghj','hjgjgj',123456,'ghjghj@gmail.com',8877335544,113),(18,'Mother',89090,'joseph',1998,'calicut','calicut',673600,'moms@gmail.com',8877665546,141),(43,'Asoka',90067,'rajan',1996,'calicut','calicut',673600,'jkljlj@gm',9088776654,206),(47,'moulana',90003,'azad',1998,'kolkata','kolkata',672900,'moulana@gmail.com',9745191754,215),(51,'Amrutha',90003,'amrita',1998,'kochi','palarivattam',980078,'amrita@g',9088097865,229),(52,'Abcd Hospital',44545,'Abcd',2015,'Kozhikode','Kozhikode',673601,'abcd@gmail.com',9874561231,237),(53,'hghghgf',56788,'hjhhghg',2019,'hhuyty','calicut',673612,'sd@gmail.com',9877665544,238),(57,'Poppins',90041,'ajj',1998,'hhuyty','ghhghj',908756,'sduv@gmail.com',9078564321,242),(58,'njnjn',88877,'hjhjh',1993,'hbhbh','hbh',990088,'bbh@gmail.com',9099889977,246);

/*Table structure for table `hospital_child` */

DROP TABLE IF EXISTS `hospital_child`;

CREATE TABLE `hospital_child` (
  `child_reg_id` int(11) NOT NULL AUTO_INCREMENT,
  `hospital_id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `bloodgroup` varchar(20) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `fathername` varchar(20) DEFAULT NULL,
  `mothername` varchar(20) DEFAULT NULL,
  `motheraadhar` bigint(20) DEFAULT NULL,
  `fatheraadhar` bigint(20) DEFAULT NULL,
  `house` varchar(30) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  `dist` varchar(30) DEFAULT NULL,
  `state` varchar(30) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` int(11) DEFAULT NULL,
  PRIMARY KEY (`child_reg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `hospital_child` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(30) DEFAULT NULL,
  `password` varchar(25) DEFAULT NULL,
  `type` varchar(35) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=248 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`type`) values (1,'admin','admin','admin'),(34,'ho','88','hospital'),(35,'hg','88','healthcenter'),(36,'hg','88','anganavadi'),(37,'kkjk','8900','hospital'),(38,'raj@gmail.com','9876','hospital'),(39,NULL,NULL,NULL),(40,'ghfh','4354','hospital'),(41,'care247@gmail.com','9876','healthcenter'),(42,'gfdg','454','anganavadi'),(43,'qwerty@gmail.com','9898','anganavadi'),(44,'fdsfs','35435','anganavadi'),(45,'\"+email+\"','\"+phone+\"','staff'),(46,'ll','66','staff'),(47,'hh','77','staff'),(48,'ammugk@gmail.com','8593996328','staff'),(49,'shi@gmail.com','9888766745','staff'),(50,'ii','99','staff'),(51,'vin123@gmail.com','9876675433','staff'),(52,'hh@','9876675433','staff'),(53,'hh','555','staff'),(54,'jhj','9898','hospital'),(55,'gjghj','778','anganavadi'),(56,'ghjgj','76786','hospital'),(57,'tytu','8768','hospital'),(58,'rtyy','786878','hospital'),(59,'ghjhjh','76867','hospital'),(60,'gfh','566446','hospital'),(61,'uu','o','hospital'),(62,'gdgdg','66456','healthcenter'),(63,'fhfh','4545','healthcenter'),(64,'gfhfh','5656','anganavadi'),(65,'tet','324','anganavadi'),(66,'ytutu','54656','anganavadi'),(67,'vv','66','hospital'),(68,'ghfh','88','hospital'),(69,'ghjgj','76786','hospital'),(70,'fhfh','77','hospital'),(71,'ghghj','66','hospital'),(72,'hjhjhk','76786','hospital'),(73,'ghfhf','65564','anganavadi'),(74,'gdgdg','4354','healthcenter'),(75,'tretr','4566','hospital'),(83,'sfgvdxsfg','547657654','anganavadi'),(84,'sfsf','45356434','hospital'),(85,'xczczxvc','45854745','healthcentre'),(86,'gjhj','9789','staff'),(87,'dfgdg','3545','hospital'),(88,'dgdg','656546','healthcenter'),(90,'gdgdfg','4543554','healthcenter'),(91,'fgfg','57676','healthcenter'),(92,'gjgjgj','775','staff'),(93,'hfhfh','97897','staff'),(94,'hgjg','878','staff'),(95,'dgfg','544','staff'),(96,'ffghfgh','7686787','staff'),(97,'fgfgfg','859399632','hospital'),(98,'fgfgfg','859399632','hospital'),(99,'','','healthcenter'),(100,'','','healthcenter'),(101,'','9888766745','healthcenter'),(102,'','9876675433','healthcenter'),(103,'','','anganavadi'),(104,'','','anganavadi'),(105,'','','anganavadi'),(106,'','','anganavadi'),(107,'','','anganavadi'),(108,'','','anganavadi'),(109,'gjghjgj','8593996328','anganavadi'),(110,'gjghjgj','8593996328','anganavadi'),(111,'fhfgh','9888766745','anganavadi'),(112,'oo','8877665544','hospital'),(113,'ghjghj','123456789123','hospital'),(114,'ghjghj','123456789123','hospital'),(115,'hjghj','12345678912','hospital'),(116,'','','healthcenter'),(117,'gdgdg','8866554433','healthcenter'),(118,'gdgdg','8866554433','healthcenter'),(119,'hh','8877665544','healthcenter'),(120,'sdfsd@gmail.com','8877665544','hospital'),(121,'sdfsd@gmail.com','8877665544','hospital'),(122,'aa@gmail.com','8877665544','hospital'),(123,'aa@gmail.com','8877665544','hospital'),(124,'aa@gmail.com','8877665544','hospital'),(125,'aa@gmail.com','8877665544','hospital'),(126,'aa@gmail.com','8877665544','hospital'),(127,'aa@gmail.com','8877665544','hospital'),(128,'aa@gmail.com','8877665544','hospital'),(129,'aa@gmail.com','8877665544','hospital'),(130,'jghj@gmail.com','hj','hospital'),(131,'jghj@gmail.com','hj','hospital'),(132,'aa@gmail.com','j','hospital'),(133,'aa@gmail.com','j','hospital'),(134,'aa@gmail.com','8877665544','hospital'),(135,'aa@gmail.com','3344225511','anganavadi'),(136,'aa@gmail.com','887766554','hospital'),(137,'aa@gmail.com','887766554','hospital'),(138,'aa@gmail.com','887766554','hospital'),(139,'aa@gmail.com','887766554','hospital'),(140,'aa@gmail.com','8877665544','hospital'),(141,'moms@gmail.com','8877665544','hospital'),(143,'hh@gmail.com','1234','healthcenter'),(144,'aa@gmail.com','8877665547','healthcenter'),(145,'aa@gmail.com','8877665544','healthcenter'),(146,'aa@gmail.com','8877665549','anganavadi'),(147,'aa@gmail.com','8877665544','hospital'),(148,'\"+email+\"','\"+phone+\"','hospital'),(150,'\"+email+\"','\"+phone+\"','hospital'),(151,'\"+email+\"','\"+phone+\"','hospital'),(152,'\"+email+\"','\"+phone+\"','hospital'),(153,'\"+email+\"','\"+phone+\"','hospital'),(155,'hh@gmail.com','8877665544','hospital'),(156,'hh@gmail.com','8877665544','healthcenter'),(157,'aa@gmail.com','1234567891','anganavadi'),(158,'aha@gmail.com','8877665556','anganavadi'),(161,'rrhh@gmail.com','8877612344','anganavadi'),(162,'hh@gmail.com','887766554','staff'),(163,'hh@gmail.com','887766554','staff'),(164,'aa@gmail.com','887766554','staff'),(165,'hh@gmail.com','8877665544','staff'),(166,'k@gmail.com','8877665541','staff'),(167,'asw@gmail.com','8877665544','staff'),(168,'qqq@gmail.com','8877665544','staff'),(169,'fghfh@gmail.com','8877665544','staff'),(170,'ghjgj@gmail.com','8678678','staff'),(171,'ghjgj@gmail.com','8877665544','staff'),(172,'ghjgj@gmail.com','8877665544','staff'),(173,'min@gmail.com','8877665544','staff'),(174,'vc@gmail.com','8877665549','staff'),(175,'vnbvbn@gmail.com','8877665544','staff'),(176,'vnbvbn@gmail.com','8877665544','staff'),(177,'aa@gmail.com','8877665544','staff'),(178,'mnb@gmail.com','8877665544','staff'),(179,'ad@gmail.com','8888888888','staff'),(180,'ad@gmail.com','9887797989','staff'),(181,'ad@gmail.com','9887797989','staff'),(182,'ad@gmail.com','8899445566','staff'),(183,'ad@gmail.com','8899445566','staff'),(184,'ad@gmail.com','7766554433','staff'),(185,'ghg@gmail.com','8566443232','staff'),(188,'ss@gmail.com','7755664433','hospital'),(189,'ss@gmail.com','7755664433','hospital'),(190,'nbv@gmail.com','7744996611','hospital'),(191,'jhg@gmail.com','8800991122','hospital'),(192,'ad@gmail.com','7788999056','hospital'),(194,'ad@gmail.com','9988775511','hospital'),(195,'ad@gmail.com','9988775511','hospital'),(196,'ad@gmail.com','8877669900','hospital'),(200,'lk@gmail.com','9077886655','hospital'),(201,'mm@gmail.com','9800776654','hospital'),(202,'mm@gmail.com','9800776654','hospital'),(203,'jhkhjkk@gmail.com','4455667788','staff'),(204,'jhkh@gmail.com','9900887766','hospital'),(205,'jhkh@gmail.com','9900887766','hospital'),(206,'jkljlj@gm','8877665544','hospital'),(207,'hkbg@gmail.com','9988776655','hospital'),(208,'hgjghj@gm','4433224455','hospital'),(209,'hjgj@gmail.com','8877990066','hospital'),(211,'hgjhj@gmail.com','9988776655','healthcenter'),(212,'hgjhj@gmail.com','9988776655','healthcenter'),(213,'jhkhjk@gmail.com','8899776655','staff'),(214,'hgh@gmail.com','9988776655','staff'),(215,'moulana@gmail.com','9745191754','hospital'),(216,'fgf@gmail.com','9077665544','staff'),(217,'jhjhj@gmail.com','9988776655','staff'),(218,'min@gmail.com','9766554433','staff'),(219,'ad@gmail.com','9988776677','staff'),(220,'dd@gmail.com','9904748364','hospital'),(221,'dd@gmail.com','9904748364','hospital'),(222,'ad@gmail.com','9988776677','staff'),(223,'ad@gmail.com','9988776677','staff'),(224,'jhjhj@gmail.com','9988776655','staff'),(225,'vinumols@gmail.com','9766554433','staff'),(226,'dfgdgdg@gmail.com','5675699999','staff'),(227,'dfgdgdg@gmail.com','5675699999','staff'),(228,'dfgdgdg@gmail.com','9900887766','hospital'),(229,'amrita@g','9088097866','hospital'),(230,'dfgdgdg@gmail.com','9078674534','healthcenter'),(232,'dfgdgdg@gmail.com','9088776500','staff'),(233,'dfgdgdg@gmail.com','9088776655','staff'),(234,'dfgdgdg@gmail.com','8977078000','staff'),(235,'ajit@gmail.com','9808','staff'),(236,'sd@gmail.com','112','staff'),(237,'abcd@gmail.com','9874561231','hospital'),(238,'sd@gmail.com','9877665544','hospital'),(242,'sduv@gmail.com','9078564321','hospital'),(244,'op','123','user'),(245,'aa@gmail.com','12345','user'),(246,'bbh@gmail.com','9099889977','hospital'),(247,'bbjh@gmail.com','6776766767','healthcenter');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) DEFAULT NULL,
  `massage` varchar(300) DEFAULT NULL,
  `angu_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`subject`,`massage`,`angu_id`,`date`) values (9,'Disaster','njnnn jhjhhhh.mkjjhj',43,'2019-10-03'),(18,'Peace','mkljkkkkkkk.  mkjkhjh',43,'2019-10-03'),(19,'cbvbcvb','cbvcbcb',43,'2019-10-09'),(22,'fdsfs','fdsfs',1,'2019-10-22'),(23,'abcd','abcd efgh',43,'2019-11-12'),(24,'xyz','xy yxxxxx',44,'2019-11-12'),(25,'qwerty','qwerrtyyyy',44,'2019-11-12'),(26,'bbc','bbccc',43,'2019-11-14'),(27,'kjkjfkjf','mkmkm',43,'2020-03-03'),(28,'mkmkj','vbvb',46,'2020-03-12');

/*Table structure for table `nutrition` */

DROP TABLE IF EXISTS `nutrition`;

CREATE TABLE `nutrition` (
  `nutrition_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `details` varchar(40) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`nutrition_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `nutrition` */

insert  into `nutrition`(`nutrition_id`,`name`,`details`,`type`) values (4,'rerer','fgdgd','fgdgdg'),(5,'oats','its good for health','cerals'),(8,'ceralas','jggj','fgfgdfg'),(11,'fhfh','gfgdgf','gd'),(14,'ookj','jnjnj','kkljk'),(17,'shigu','aah ','ooh'),(19,'ghg','ggg','ooh'),(20,'seemu','okkk ','value'),(21,'opv','nbnbn ','bbjhhv');

/*Table structure for table `nutrtion_entry` */

DROP TABLE IF EXISTS `nutrtion_entry`;

CREATE TABLE `nutrtion_entry` (
  `entry_id` int(11) NOT NULL AUTO_INCREMENT,
  `child_mother_id` int(11) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL COMMENT 'child or mother ',
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`entry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;

/*Data for the table `nutrtion_entry` */

insert  into `nutrtion_entry`(`entry_id`,`child_mother_id`,`quantity`,`date`,`type`,`status`) values (1,1,7,'2019-10-03','5',NULL),(2,1,87,'2019-10-03','5','mother'),(3,1,8,'2019-10-03','5','child'),(4,1,1,'2019-10-03','8','mother'),(5,1,565,'2019-10-03','5','mother'),(9,1,90,'2019-10-03','4','mother'),(10,1,1,'2019-10-03','5','mother'),(11,1,6,'2019-10-03','5','child'),(12,2,2,'2019-10-03','5','child'),(13,2,4,'2019-10-03','5','child'),(14,31,9,'2019-10-04','8','mother'),(15,2,87,'2019-10-04','4','child'),(16,1,0,'2019-10-08','5','child'),(17,1,0,'2019-10-08','5','child'),(18,36,0,'2019-10-09','4','mother'),(19,36,0,'2019-10-09','4','mother'),(20,49,0,'2019-10-09','8','mother'),(21,52,9,'2019-10-10','5','mother'),(22,38,8,'2019-10-10','14','mother'),(23,38,8,'2019-10-10','14','mother'),(24,52,0,'2019-10-10','select','mother'),(25,52,0,'2019-10-10','select','mother'),(26,52,0,'2019-10-10','select','mother'),(27,52,0,'2019-10-10','8','mother'),(28,46,0,'2019-10-10','8','mother'),(29,46,5,'2019-10-10','11','mother'),(30,6,8,'2019-10-11','17','child'),(31,6,9,'2019-10-11','11','child'),(32,6,0,'2019-10-11','4','child'),(33,6,0,'2019-10-11','4','child'),(34,6,9,'2019-10-11','20','child'),(35,46,0,'2019-10-11','17','mother'),(36,46,0,'2019-10-11','17','mother'),(37,38,9,'2019-10-11','8','mother'),(38,6,7,'2019-10-11','4','child'),(39,47,7,'2019-10-11','17','mother'),(40,47,7,'2019-10-11','17','mother'),(41,47,7,'2019-10-11','17','mother'),(42,2,0,'2019-10-13','5','mother'),(43,2,5,'2019-10-13','8','mother'),(44,13,3,'2019-10-13','14','child'),(45,50,8,'2019-10-19','8','mother'),(46,50,2,'2019-10-19','5','mother'),(47,50,8,'2019-10-19','8','mother'),(48,50,9,'2019-10-19','14','mother'),(49,50,1,'2019-10-21','5','mother'),(50,12,6,'2019-10-21','21','child'),(51,2,10,'2019-10-21','8','mother'),(52,17,12,'2019-10-22','17','child'),(53,12,2,'2019-10-29','8','child'),(54,13,78,'2019-10-29','8','child');

/*Table structure for table `nutrtion_stock` */

DROP TABLE IF EXISTS `nutrtion_stock`;

CREATE TABLE `nutrtion_stock` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `nutrition_id` int(11) DEFAULT NULL,
  `angu_id` int(11) DEFAULT NULL,
  `stock` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=latin1;

/*Data for the table `nutrtion_stock` */

insert  into `nutrtion_stock`(`stock_id`,`nutrition_id`,`angu_id`,`stock`) values (1,11,16,'x1'),(2,0,0,'y6'),(3,0,0,'oo'),(4,0,0,'pppp'),(5,8,29,'y6'),(6,5,29,'x'),(7,8,16,'wy'),(8,0,0,'ll'),(9,0,0,''),(10,0,0,''),(11,0,0,''),(12,0,0,''),(13,0,0,''),(14,0,0,''),(15,0,0,'fhd'),(16,0,0,'fhd'),(17,0,0,'iii'),(18,0,0,'w8'),(19,0,0,'ol'),(20,17,16,'88'),(21,17,16,'45'),(24,11,20,'y6'),(25,0,0,'iii'),(26,0,0,'iii'),(27,0,0,'iii'),(28,0,0,'iii'),(29,0,0,'iii'),(30,0,0,'iii'),(31,0,0,'iii'),(32,0,0,'iii'),(33,0,0,'hjmh'),(34,0,0,'hjmh'),(35,0,0,'hjmh'),(36,0,0,'hjmh'),(37,0,0,'o'),(38,0,0,'o'),(48,0,0,'ty'),(49,0,0,'ty'),(50,5,0,'iii'),(51,5,0,'iii'),(52,0,0,'hgh'),(53,0,0,'hgh'),(54,0,0,'c'),(55,0,0,'tt'),(56,0,0,'tt'),(57,0,0,'hj'),(58,0,0,'hj'),(59,0,0,'hgh'),(60,0,0,'hgh'),(61,0,0,'jj'),(62,0,0,'jj'),(63,0,0,'jbgmj'),(64,0,0,'jbgmj'),(65,0,0,'jghj'),(66,0,0,'jghj'),(67,0,0,'hghj'),(68,0,0,'ghj'),(69,0,0,'ghj'),(70,0,0,'ghj'),(71,0,0,'ghj'),(72,0,0,'gjghj'),(73,0,0,'gjghj'),(74,0,0,'fgh'),(75,0,0,'fgh'),(76,0,0,'jhkj'),(77,0,0,'jhkj'),(78,0,0,'jhkj'),(79,0,0,'jhkj'),(80,0,0,'jhkj'),(81,0,0,'jhkj'),(87,17,34,'9'),(88,20,31,'7'),(89,5,45,'89'),(90,4,34,'454');

/*Table structure for table `op` */

DROP TABLE IF EXISTS `op`;

CREATE TABLE `op` (
  `op_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `dates` varchar(50) DEFAULT NULL,
  `from_time` varchar(50) DEFAULT NULL,
  `to_time` varchar(50) DEFAULT NULL,
  `hospital_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`op_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;

/*Data for the table `op` */

insert  into `op`(`op_id`,`staff_id`,`dates`,`from_time`,`to_time`,`hospital_id`) values (1,0,'0000-00-00','00:00:00','00:00:00',NULL),(2,1,'2019-09-04','21:01:00','14:01:00',NULL),(3,1,'2019-09-04','11:02:00','02:02:00',NULL),(5,0,'2019-09-04','12:00:00','07:59:00',NULL),(6,2019,'2019-09-03','07:58:00','08:08:00',NULL),(8,0,'2019-09-03','04:59:00','01:59:00',NULL),(10,2019,'2019-10-30','02:03:00','14:12:00',NULL),(11,0,'2019-09-04','03:59:00','03:59:00',NULL),(12,2019,'2019-09-03','01:59:00','01:59:00',NULL),(29,2019,'2019-10-18','04:45 PM','07:45 PM',NULL),(30,2019,'2019-10-19','04:45 PM','07:45 PM',NULL),(33,4,'2019-10-30','04:45 PM','07:45 PM',NULL),(34,5,'2019-10-01','02:45 PM','07:45 PM',NULL),(35,14,'2019-10-29','09:45 PM','07:45 PM',NULL),(36,5,'2019-10-26','09:45 am','10:45 am',38);

/*Table structure for table `reply` */

DROP TABLE IF EXISTS `reply`;

CREATE TABLE `reply` (
  `reply_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint_id` int(11) DEFAULT NULL,
  `reply` varchar(30) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`reply_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

/*Data for the table `reply` */

insert  into `reply`(`reply_id`,`complaint_id`,`reply`,`date`) values (1,3,'JHGJGJGJ','2019-10-08'),(2,5,'hhhhh','2019-10-08'),(3,8,'NO PRBM','2019-10-08'),(4,13,'ohhhhhhh kk','2019-10-09'),(5,16,'hhhhh','2019-10-09'),(6,16,'hhhhh','2019-10-09'),(7,17,'cbcv','2019-10-09'),(8,15,'aaaaa,okk','2019-10-09'),(9,18,'yes we are here.....!','2019-10-09'),(10,1,'drtdrtdr','2019-10-09'),(11,12,'dtdftdft','2019-10-09'),(12,14,'dftdftdf','2019-10-09'),(13,14,'dfgdfgdg','2019-10-09'),(14,14,'dfgdfgdg','2019-10-09'),(15,14,'dfgdfgdg','2019-10-09'),(16,14,'dfgdfgdg','2019-10-09'),(17,14,'dfgdfgdg','2019-10-09'),(18,14,'dfgdfgdg','2019-10-10'),(19,19,'dfgdfgdg','2019-10-10'),(20,20,'waittttttttttttt','2019-10-10'),(21,20,'waittttttttttttt','2019-10-10'),(22,22,'worry','2019-10-10'),(23,23,'as assssssssss','2019-10-10'),(24,24,'eeeee','2019-10-10'),(26,31,'ghgfhfh','2010-01-01'),(27,35,'mm jaba','2010-01-01'),(28,37,'ya ya','2010-01-01'),(29,27,'dfgdfgd','2019-10-21'),(30,26,'gdfgdfgd','2019-10-21'),(31,38,'dsfdsfsf','2019-10-22'),(32,38,'aaahhhh...kk','2019-10-22');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `hosp_health_id` int(11) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `bloodgroup` varchar(10) DEFAULT NULL,
  `house` varchar(30) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  `dist` varchar(30) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `state` varchar(15) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `qualn` varchar(20) DEFAULT NULL,
  `designation` varchar(20) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`login_id`,`hosp_health_id`,`name`,`dob`,`gender`,`bloodgroup`,`house`,`post`,`dist`,`pin`,`state`,`email`,`phone`,`qualn`,`designation`,`photo`,`type`) values (4,48,38,'ammu','2019-09-18','female','O+ve','ambalaparambil','kokkallur','kozhikode',673612,'Kerala','ammugk@gmail.com',2147483647,'pg','Main nurse','//static//picsth.jpg','nurse'),(5,49,38,'shigha','2019-09-04','female','A+ve','azhinjilam','farook','Malappuram',674412,'Kerala','shi@gmail.com',2147483647,'pg','staffnurse','/static/pics/th.jpg','nurse'),(7,51,41,'tintuu','2001-12-20','male','B-ve','nbm','hgjghjg','fgjjgjgj',554433,'fghfhh','dd@gmail.com',9904748364,'sslc','gfhhfhgfh','/static/picsth.jpg','attender'),(13,166,38,'po','2019-10-12','male','B+ve','fghfgh','fghfgh','fghfh',673612,'ghfhf','k@gmail.com',2147483647,'plustwo','hkjhjk','/static/pics/496443016.jpg','nurse'),(14,167,38,'iuoui','1999-03-25','female','O+ve','ambalathil','kokkallur','calicut',673612,'kerala','asw@gmail.com',2147483647,'degree','junior','/static/pics/xmas-cake.gif','doctor'),(22,177,38,'dgdfgdfg','2000-12-09','male','A+ve','nvbn','erere','dfg',6736,'gffghfh','fgfgh@gmail.com',4564646,'plustwo','dgfgdfgdfg','/static/pics/download (1).jpg','select'),(24,179,38,'hjgjh','2019-10-08','male','O+ve','hgj','hgjghj','ghjgj',555666,'jhkhk','ad@gmail.com',2147483647,'sslc','ujgjhgj','/static/pics/Capture.PNG','select'),(29,184,38,'kljkl','2019-10-19','female','AB+ve','hgj','clt','ghjgj',965874,'jhkhk','ad@gmail.com',9988776677,'sslc','ujgjhgj','/static/pics/DSCF2427.JPG','doctor'),(30,185,41,'tintuu','2001-12-20','male','B-ve','nbm','hgjghjg','fgjjgjgj',554433,'fghfhh','dd@gmail.com',9904748364,'sslc','gfhhfhgfh','/static/pics/DSCF2460.JPG','attender'),(32,213,90,'ghjghj','0000-00-00','male','O+ve','jhkhjk','jhkhj','jhkhk',887766,'hjhjk','jhkhjk@gmail.com',2147483647,'plustwo','doctor','/static/pics/Capture.PNG','nurse'),(33,214,90,'bablu','0000-00-00','male','O+ve','khjk','hjkhjk','jhkhjk',887766,'jhghj','hgh@gmail.com',2147483647,'sslc','jghjhjhj','/static/pics/Desert.jpg','attender'),(37,219,38,'ijijij','2014-10-20','male','O-ve','njnjnjtr','gygygr','hhg',998877,'njnjn','ad@gmail.com',9988776677,'sslc','jnjnjn','/static/pics/wooden-double-swing-door-93843.jpg','doctor'),(38,222,38,'njnjnj','2015-10-19','male','AB+ve','jbnb','jhjh','jhjhkhj',557828,'dd','ad@gmail.com',9988776677,'plustwo','njn','/static/pics/IMG_20190529_150953_346-01-01.jpeg','doctor'),(42,227,41,'Navya','2019-10-18','male','A+ve','bnbnb','hghghg','hghghjg',667788,'hghghg','dfgdgdg@gmail.com',5675699999,'plustwo','jhjhj','/static/pics/IMG_20190608_163013_463-01.jpeg','attender'),(43,232,41,'vimal','1991-01-01','male','A+ve','bmbg','bjgj','jhjghjgh',673602,'hghghg','dfgdgdg@gmail.com',9088776500,'degree','gfdg','/static/pics/IMG_20170923_080438952.jpg','attender'),(46,235,41,'Ajith','1996-10-05','male','B+ve','Vadakumpattu','kokkallur','calicut',673410,'kerrala','va_aji@gmail.com',8907874420,'pg','senior','/static/pics/2019-02-09-13-53-07-714-01.jpeg','doctor'),(47,236,38,'Anitha','1987-10-12','male','B+ve','jhjh','hbhbhjv','calicut',67360,'hghghg','sd@gmail.com',903322115,'plustwo','jkhj','/static/pics/2019-02-09-13-53-07-714-01.jpeg','select');

/*Table structure for table `staff_request` */

DROP TABLE IF EXISTS `staff_request`;

CREATE TABLE `staff_request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `login_id` int(11) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `staff_request` */

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `stud_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `fathername` varchar(30) DEFAULT NULL,
  `fatheraadharno` bigint(20) DEFAULT NULL,
  `house` varchar(30) DEFAULT NULL,
  `post` varchar(30) DEFAULT NULL,
  `dist` varchar(30) DEFAULT NULL,
  `state` varchar(30) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `localgurdian` varchar(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `phone` bigint(15) DEFAULT NULL,
  `angu_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`stud_id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`stud_id`,`name`,`dob`,`gender`,`fathername`,`fatheraadharno`,`house`,`post`,`dist`,`state`,`pin`,`localgurdian`,`email`,`photo`,`phone`,`angu_id`) values (1,'\"+name+\"','0000-00-00','\"+gender+\"','\"+fname+\"',0,'\"+hname+\"','\"+post+\"','\"+dist+\"','\"+state+\"',0,'\"+gurd+\"','\"+email+\"','\"+phone+\"',0,0),(8,'\"+name+\"','0000-00-00','\"+gender+\"','\"+fname+\"',0,'\"+hname+\"','\"+post+\"','\"+dist+\"','\"+state+\"',0,'\"+gurd+\"','\"+email+\"','\"+phone+\"',0,0),(11,'THATHAHA','2019-10-05','FEMALE','vnbvn',3543535,'nvbn','erere','vnbnbnb','vbn',768888,'cvgbhfgh','aa@gmail.com','/static/pics/th.jpg',8877665544,43),(16,'maalu','2019-10-26','FEMALE','ajith',2233445566771,'punyaa','jhkhjkhj','calicut','kerala',673616,'venu','aakkkk@gmail.com','/static/pics/theme-christmas.jpg',8877665549,43),(34,'ghgh','2019-10-25','MALE','ghfh',1234567891234,'gfgh','fghfh','fghfh','fghfh',673612,'venu','hh@gmail.com','/static/pics/151632_Christmas_Traub_Daniel.jpg',8877665547,38),(35,'bablu','2019-10-20','FEMALE','bhbhj',4566778899445,'jkhgj','hghghg','hghghjg','hghghg',554433,'hgjghg','dfgdgdg@gmail.com','/static/pics/20170601_174655.jpg',9988776655,43),(36,'Akhila','2019-11-01','FEMALE','hghgh',9087653412000,'hhghgh','jhg','ghghgh','ghghgh',673609,'bbvb','hhpoppi@gmail.com','/static/pics/20170601_174655.jpg',9066778890,43);

/*Table structure for table `vaccination` */

DROP TABLE IF EXISTS `vaccination`;

CREATE TABLE `vaccination` (
  `vaccination_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) DEFAULT NULL,
  `details` varchar(35) DEFAULT NULL,
  `importance` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`vaccination_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `vaccination` */

insert  into `vaccination`(`vaccination_id`,`name`,`details`,`importance`) values (1,'one','good for health','its important'),(2,'olay','good for skin','skin complexion'),(3,'bs','jkhgjgj','blalalal'),(4,'sm1','kljljl','jkljlk'),(9,'vlc','kljbhbgggf','njbbhbj');

/*Table structure for table `vaccination_date` */

DROP TABLE IF EXISTS `vaccination_date`;

CREATE TABLE `vaccination_date` (
  `date_id` int(11) NOT NULL AUTO_INCREMENT,
  `vaccination_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`date_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

/*Data for the table `vaccination_date` */

insert  into `vaccination_date`(`date_id`,`vaccination_id`,`date`) values (3,7,'2019-10-11'),(4,0,'2019-10-05'),(5,0,'2019-10-05'),(6,0,'2019-10-04'),(7,0,'2019-10-04'),(8,0,'0000-00-00'),(9,0,'0000-00-00'),(11,6,'2019-10-30'),(13,7,'2019-10-25'),(16,3,'2019-10-12'),(17,1,'2019-10-01'),(18,1,'2019-10-01'),(19,1,'2019-10-27'),(20,1,'2019-10-20'),(21,1,'2019-10-20'),(22,1,'2019-10-13'),(23,1,'2019-10-13'),(24,2,'2019-10-27'),(25,4,'2019-09-06'),(26,2,'2019-10-27'),(27,4,'2019-10-27'),(28,4,'2019-10-27'),(29,2,'2020-01-12'),(30,1,'2019-12-28');

/*Table structure for table `vaccination_entry` */

DROP TABLE IF EXISTS `vaccination_entry`;

CREATE TABLE `vaccination_entry` (
  `entry_id` int(11) NOT NULL AUTO_INCREMENT,
  `vaccination_id` int(11) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  `child_id` int(11) DEFAULT NULL,
  `venuid` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`entry_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `vaccination_entry` */

insert  into `vaccination_entry`(`entry_id`,`vaccination_id`,`date`,`child_id`,`venuid`,`staff_id`,`type`) values (1,4,'2019-07-09',1,44,46,'child'),(2,4,'2019-07-09',52,44,46,'mother'),(3,4,'2019-07-10',12,44,46,'child'),(4,2,'2019-07-09',12,31,46,'child'),(5,0,'2019-11-12',1,0,0,'child'),(6,3,'2019-11-12',1,43,46,'child'),(13,3,'2019-11-12',12,43,46,'child'),(14,2,'2020-02-15',1,31,46,'child');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
