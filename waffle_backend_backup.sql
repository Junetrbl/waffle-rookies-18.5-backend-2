-- MySQL dump 10.13  Distrib 8.0.22, for osx10.15 (x86_64)
--
-- Host: localhost    Database: waffle_backend_assignment_2
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Token',7,'add_token'),(26,'Can change Token',7,'change_token'),(27,'Can delete Token',7,'delete_token'),(28,'Can view Token',7,'view_token'),(29,'Can add operating system',8,'add_operatingsystem'),(30,'Can change operating system',8,'change_operatingsystem'),(31,'Can delete operating system',8,'delete_operatingsystem'),(32,'Can view operating system',8,'view_operatingsystem'),(33,'Can add survey result',9,'add_surveyresult'),(34,'Can change survey result',9,'change_surveyresult'),(35,'Can delete survey result',9,'delete_surveyresult'),(36,'Can view survey result',9,'view_surveyresult'),(37,'Can add user auth',10,'add_userauth'),(38,'Can change user auth',10,'change_userauth'),(39,'Can delete user auth',10,'delete_userauth'),(40,'Can view user auth',10,'view_userauth'),(41,'Can add participant profile',11,'add_participantprofile'),(42,'Can change participant profile',11,'change_participantprofile'),(43,'Can delete participant profile',11,'delete_participantprofile'),(44,'Can view participant profile',11,'view_participantprofile'),(45,'Can add instructor profile',12,'add_instructorprofile'),(46,'Can change instructor profile',12,'change_instructorprofile'),(47,'Can delete instructor profile',12,'delete_instructorprofile'),(48,'Can view instructor profile',12,'view_instructorprofile'),(49,'Can add seminar',13,'add_seminar'),(50,'Can change seminar',13,'change_seminar'),(51,'Can delete seminar',13,'delete_seminar'),(52,'Can view seminar',13,'view_seminar'),(53,'Can add user seminar',14,'add_userseminar'),(54,'Can change user seminar',14,'change_userseminar'),(55,'Can delete user seminar',14,'delete_userseminar'),(56,'Can view user seminar',14,'view_userseminar'),(57,'Can add token',15,'add_tokenproxy'),(58,'Can change token',15,'change_tokenproxy'),(59,'Can delete token',15,'delete_tokenproxy'),(60,'Can view token',15,'view_tokenproxy');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (5,'pbkdf2_sha256$216000$khSBJHyGXCnH$P7+UwoCDB5DWjwVsa34d6bzHHdf1e7bqW9asqGwMFOw=',NULL,0,'June1','Yoonsoo','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 16:16:02.654307'),(6,'pbkdf2_sha256$216000$hDrA3dekj8sr$H05FoGTjSj2KUwc3DFUABRX0Fm3T6V5jlj3xrhxZ4A4=',NULL,0,'June2','Yoonsoo','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 16:16:07.102684'),(7,'pbkdf2_sha256$216000$wy0wptjGMEb4$ias4oNesQmmJrYn4nTZ9A9GKtP5WEfxFzvZhhRmxuDU=',NULL,0,'June3','Yoonsoo','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 16:16:10.984462'),(8,'pbkdf2_sha256$216000$S6EjzecCvYjJ$PtoX6k7H5H0GCHVZBzCAUYYbuy07qWgupSlkBNzldtQ=',NULL,0,'Junepark','Yoonsoo','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 16:16:19.202367'),(9,'pbkdf2_sha256$216000$rJrATWYVjRy0$HLldZRsIVBoCLXMhZegjc6UOysneQoiUphg1uyWwuIg=',NULL,0,'June1211','Yoonsoo','Park','junepark12111@snu.ac.kr',0,1,'2020-09-27 16:16:59.839035'),(10,'pbkdf2_sha256$216000$aXOv30p6n6Or$/ZXu3w030iVQdGkV8hIAeJN8I0vcX4YT6Gng2ikmekg=',NULL,0,'June10','Yoonsoo','Park','junepark12111@snu.ac.kr',0,1,'2020-09-27 16:17:53.410253'),(11,'pbkdf2_sha256$216000$Yf8FG3VN4Gi9$dXw6g3MmWPXktBHTshUzedizmF9n1PDz5+HD7tCt3MY=',NULL,0,'June11','Yoonsoo','Park','junepark12111@snu.ac.kr',0,1,'2020-09-27 16:19:54.693052'),(12,'pbkdf2_sha256$216000$UpnDmec1k25h$NarsmZ0lDPzgQwF3eE1Y9tdGNnXhIwzYEXWOS+HwDNc=',NULL,0,'June12','Yoonsoo','Park','junepark12111@snu.ac.kr',0,1,'2020-09-27 16:22:36.067406'),(13,'pbkdf2_sha256$216000$rj0IVF3j24jq$Uh06rm/eR+OiXUXnnZkW/FVyGTFmCFj3gg/jX/HPISE=',NULL,0,'June13','Yoonsoo','Park','junepark12111@snu.ac.kr',0,1,'2020-09-27 16:41:21.705639'),(14,'pbkdf2_sha256$216000$v0LpGDc5xY3U$W0IetyywrsV7ur9n9ZOvUYLu/uGsRlauwMMMZZr2uYE=',NULL,0,'June15','Yoonsoo','Park','junepark12111@snu.ac.kr',0,1,'2020-09-27 17:06:42.719472'),(15,'pbkdf2_sha256$216000$KdmEdFlgwMsZ$fK+vbAiXnu/WozTsGqNFdypLUyLdx21Xn9UU8ONlTzc=',NULL,0,'June16','Yoonsoo','Park','junepark12111@snu.ac.kr',0,1,'2020-09-27 17:07:16.554604'),(16,'pbkdf2_sha256$216000$y9nBs8mt2tk0$KjDMyatepsbwMdigOcHxFCzom7zn6fmQyTUYaDaFY+w=','2020-09-27 17:08:06.334184',0,'June17','Yoonsoo','Park','junepark12111@snu.ac.kr',0,1,'2020-09-27 17:08:06.323376'),(17,'pbkdf2_sha256$216000$WRKl5JIyJPMT$MN2jZdWM0TMlDrH0SkaGF3HFGipoGC4WiJUZfE55DRo=','2020-09-27 17:14:44.376975',0,'June18','Yoonsoo','Park','junepark12111@snu.ac.kr',0,1,'2020-09-27 17:14:44.364473'),(18,'pbkdf2_sha256$216000$af2UPkw6r7WI$BBIEh3NL5xfk4RDgex8nbXZ6gOkH1v3jjPe6qVkRcBw=','2020-09-27 17:14:59.609239',0,'June19','Yoonsoo','Park','junepark12111@snu.ac.kr',0,1,'2020-09-27 17:14:59.602730'),(19,'pbkdf2_sha256$216000$r4uxZxsp5e9D$DrOuYUGCg9BTYxo5HHC0zu2eXMz34lo0hTUlv6RgrnA=','2020-09-27 17:16:29.055314',0,'June20','Yoonsoo','Park','junepark12111@snu.ac.kr',0,1,'2020-09-27 17:16:29.047745'),(20,'pbkdf2_sha256$216000$04BHVfF1Xhdn$kdSWD31GYsxQW2CJqO220+qZrIDOh/dgX81FvNT5e/I=',NULL,0,'June21','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:22:56.349679'),(21,'pbkdf2_sha256$216000$AA7oV5sdrKmA$c7t4Mkb0ZGMvW5PuyVMlIQmIQSEAmp7fMsh4QHyZvA8=',NULL,0,'June22','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:23:19.611106'),(22,'pbkdf2_sha256$216000$6Poj5nBvQakd$EMNB+pUq44XM440PTLUIZsUBXeTktEphlMQTm7FBGSM=',NULL,0,'June23','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:23:41.600394'),(23,'pbkdf2_sha256$216000$nAlce5Cqu8Sa$vCU4cgMByyFp/uNqyrMEvQ8QmcaHvSkXcCONDRGUh5w=',NULL,0,'June24','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:34:32.365348'),(24,'pbkdf2_sha256$216000$Swy4jRrs9p28$ebxh+OIBVhLXL3P0siGyFqTciaCZNnfePhPeEqxwGKM=',NULL,0,'June25','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:35:52.572924'),(25,'pbkdf2_sha256$216000$lprTLN7fqn80$la56IIEOZfPZMitDP9AfQvY/CpzfUN8ylvT3fQUaVxg=','2020-09-27 18:41:56.698878',0,'June26','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:41:56.680113'),(26,'pbkdf2_sha256$216000$MZ7CROBeOC1i$pfzu2nWeUJ78DMIAf8luijNDXPK4sxOweaeUfmsSq7Q=','2020-09-27 18:43:53.153245',0,'June28','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:43:53.138440'),(27,'pbkdf2_sha256$216000$nhSzotpysjLy$IEDDu599MfbdDDTWhggiHuodI8HxVhBYqXIht2b68cc=','2020-09-27 18:44:29.038417',0,'June29','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:44:29.025821'),(28,'pbkdf2_sha256$216000$uvYGh93bWsbI$J8EBmh6uPPJJ5et/dr1l907+VKVEZ69PgskkXOO+/Rg=','2020-09-27 18:52:24.050881',0,'June30','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:52:24.037696'),(29,'pbkdf2_sha256$216000$WWzfjyZTmYQg$F5uZ6s4Z8jwch3ffKCnLWg+mFpACZc2KpFq9u0HfpEs=','2020-09-27 18:52:34.908486',0,'June31','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:52:34.901161'),(30,'pbkdf2_sha256$216000$Mft822AVNyVp$RiWoupow0qWMAxy/fqTbq7Y+zi6GsUWfLobJZnMwl+c=','2020-09-27 18:53:05.416570',0,'June312','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:53:05.402757'),(31,'pbkdf2_sha256$216000$j1ptktMrnMNW$iGv9AMVeHiHFgk9Ms768+nzQIm3I/8GWUYYQPUfWbQ4=','2020-09-27 18:53:17.208839',0,'June32','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:53:17.198978'),(32,'pbkdf2_sha256$216000$H349TLCxpnuT$GrNC0G5tK15nqQCMlLuNcq/JgZX/2WsUNbJup6kw89E=','2020-09-27 18:53:28.855915',0,'June33','June','Park','junepark1211@snu.ac.kr',0,1,'2020-09-27 18:53:28.846959'),(33,'pbkdf2_sha256$216000$zpiZvfXaeG86$LtOEYMkkwTUdmZ9BLcq9YTypO1wR0kzlaH3GDI54+6A=',NULL,0,'June40','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 06:59:41.129937'),(34,'pbkdf2_sha256$216000$GacEK6Y9Jna8$jiYNHWIPEXWijbS7GMf1CCU0wyK0KuSPwxf3Ypdakrg=',NULL,0,'June41','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 06:59:59.268167'),(35,'pbkdf2_sha256$216000$xlvO5SNbZ2yG$av6ISI8DVSmX7F+ijaxmB3cqvMhxqDlyXjIoKUEPOBM=','2020-09-29 08:11:20.830204',0,'June42','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:02:30.577382'),(36,'pbkdf2_sha256$216000$R7PSQFFAO7RU$/9DEcMWw78m/ZSsLHFLktV65p7CLa5QiEhv68o8lRAo=','2020-09-28 07:12:32.858159',0,'June43','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:12:32.846876'),(37,'pbkdf2_sha256$216000$9Rs4nL4mD85y$5+v0C5dxvsbSHJjjpgblB6zawxBo1YjwYPBTGhCxRnw=','2020-09-28 07:13:11.734351',0,'June44','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:13:11.726421'),(38,'pbkdf2_sha256$216000$5YMx1Zsc1goG$TJ5s/lcjteyCn9xtsZ57Bb0mmxGeYGBP2kbH+2QQh+8=','2020-09-28 07:14:44.437397',0,'June45','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:14:44.426864'),(39,'pbkdf2_sha256$216000$uc4Y5LhNqHzB$ZfwiWWyrbYCZXEPBXhXyoQMaQlBxM34GXGjL/021YsM=','2020-09-28 07:20:12.667327',0,'June46','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:20:12.658345'),(40,'pbkdf2_sha256$216000$r32T0JD1C1mc$rPx/27RWkDwiHN29kDr5qvsk3d4ubrpqhkKM5HuJvoY=','2020-09-28 07:21:52.291121',0,'June47','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:21:52.283561'),(41,'pbkdf2_sha256$216000$72qUr3sZUqFy$rs7LmPqnlipVIyW3EyBLj0XtpmBruB4CF3idBvisWBc=','2020-09-28 07:22:16.229001',0,'June48','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:22:16.221602'),(42,'pbkdf2_sha256$216000$xRKlvKo2p4Fo$cGdq1B7y0nLp7HG7GyLXhU9CWxX2wrc7cHzP+YKSK44=','2020-09-28 07:24:27.139648',0,'June49','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:24:27.129734'),(43,'pbkdf2_sha256$216000$PyzcIT9TLq9n$0e4icSHoqlbwypz5KIrAyT5T9a2GcZhOJrTAIHxRqwk=','2020-09-28 07:25:01.600588',0,'June50','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:25:01.592304'),(44,'pbkdf2_sha256$216000$PjxqFsSkuYSw$gxyHom52lbR/B78RqnmXro+XcEj4+cJe5E5WDMeQs+Y=','2020-09-28 07:25:54.767023',0,'June51','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:25:54.759108'),(45,'pbkdf2_sha256$216000$dhQ217ujqF3l$8B3ew7xzIrl6OJUXaMo22hfxMyWU5c7cK/its0KCj94=','2020-09-28 07:26:54.279485',0,'June52','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:26:54.271281'),(46,'pbkdf2_sha256$216000$T5DeRhB3yyDi$sSvWpd1FEskTyDDbM1NHZxWSXHwk8+S4Nsw3vgSUU4Y=','2020-09-28 07:28:31.758113',0,'June57','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:28:31.749789'),(47,'pbkdf2_sha256$216000$tzG7UL4xoM31$y8gRaPISwuN61CbFapr9e/A8GO8J4bjhj0eJ3+qM3WQ=','2020-09-28 07:28:45.314755',0,'June59','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:28:45.307167'),(48,'pbkdf2_sha256$216000$XxROHLhbwf7s$Sk4XUtptvaKbIeDwmnhNIQoPFi0BdsCpfInmUDvHiuw=','2020-09-28 07:30:47.471363',0,'June60','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:30:47.463137'),(49,'pbkdf2_sha256$216000$7dJLGDb1yGma$1PbH62V1KRhWjeTBnSkPd89cc5bJF3xV3tSJ+GCgk6Y=','2020-09-28 07:35:14.525028',0,'June61','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:35:14.514336'),(50,'pbkdf2_sha256$216000$Hpc2HXBGr1p9$lTs0tLmH6uswnapiOxdkTCgeNhP3jwtDMFxAujja16U=','2020-09-28 07:38:05.732931',0,'June62','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:38:05.722096'),(51,'pbkdf2_sha256$216000$LwgJy0clKUE7$0IRtruKIZDSrBBlm5nsh4V+8RZMPFOyPQ7xP1jbfpjA=',NULL,0,'June63','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:40:27.667028'),(52,'pbkdf2_sha256$216000$UEVA4YbPCHIS$MyrX9krOPiAPmABhfGlg3xy4JYUqodANdARB8d2tc48=',NULL,0,'June64','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:40:51.087717'),(53,'pbkdf2_sha256$216000$qHCKsHy6mtqS$BHvYSNVedcufbgHeQoIMrwk+oB+DmeGqsOYEcSxUKtI=','2020-09-28 07:41:16.310861',0,'June65','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:41:16.303787'),(54,'pbkdf2_sha256$216000$8m5k4W8sfsWv$m1B85XpxGn0uxEZKbj4ev2lcf2WZCfaqInSxfGhkmZU=','2020-09-28 07:41:45.614921',0,'June66','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:41:45.607128'),(55,'pbkdf2_sha256$216000$AOjZcjvgjXYr$GaHI9CKWVZK9lw3a/RaHXsjHa4DvtoXxOFO9a7HobFc=','2020-09-28 07:41:57.939501',0,'June67','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:41:57.931507'),(56,'pbkdf2_sha256$216000$aznoyyOLbRV2$q+fipsRPhlT4QYDXoOZ861pJKeYWR9E2jsY70dQNHY8=','2020-09-28 07:44:56.179947',0,'June678','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 07:44:56.172103'),(57,'pbkdf2_sha256$216000$I2m3aWzdQyM1$kjcsFq2a+Ex/SVw97RbcHP9UWMuvAsMvjArygDeKiqY=','2020-09-28 09:10:08.615082',0,'June68','','','junepark@snu.ac.kr',0,1,'2020-09-28 09:10:08.602243'),(58,'pbkdf2_sha256$216000$SdyZlIKPMnMP$DIe2tGAw0HPwF+vHwmRQ/HsYQ0WkQZEmCUNhhNVidKw=','2020-09-28 11:01:07.591648',0,'June69','Yoonsoo','Park','junepark@snu.ac.kr',0,1,'2020-09-28 11:01:07.575034'),(59,'pbkdf2_sha256$216000$q5LvHzls0RG2$qhb5PAYDoiDHixjt4pj8Rn/O/Y6j7VvTwtUP6JavOxc=','2020-09-28 14:31:30.588390',0,'June70','','','junepark1211@snu.ac.kr',0,1,'2020-09-28 11:05:32.396088'),(62,'pbkdf2_sha256$216000$pCi5UKOrgKbo$MUWL2G8A/8cO5W+JB5t9kDy+vXO46w6UEWOerQ6w2FQ=','2020-10-02 09:20:17.006973',0,'davin111','Davin','Byeon','bdv111@snu.ac.kr',0,1,'2020-10-02 09:20:16.988378'),(63,'pbkdf2_sha256$216000$MwCCoEzdGn3e$ALTNimbvWGqWx1YOGTAemX7u9tCYXe6hpK31B1BVJSo=','2020-10-02 10:47:58.544849',0,'inst123','Dabin','Byeon','bdv111@naver.com',0,1,'2020-10-02 10:47:58.533553'),(64,'pbkdf2_sha256$216000$IPkSYMFcxbtE$E9mW3THJAeFovdC+nF8umc3dvbF9b7J2DRpTm/b3ZZ0=','2020-10-03 18:51:04.522432',0,'inst124','Dabin','Byeon','bdv111@naver.com',0,1,'2020-10-02 11:00:36.611104'),(65,'pbkdf2_sha256$216000$kXRMRQyIhrRm$wIVoTl4lSKb8IMMjUa89YiQOWtZ5lyZ81Bh9nWyB+Ow=','2020-10-05 04:49:52.055325',0,'June','Yoonsoo','Park','junepark1211@snu.ac.kr',0,1,'2020-10-05 04:49:41.113470'),(66,'pbkdf2_sha256$216000$RsIYoDk5vzgx$m0btJYxH9yu9pF4p6XiUQaQKvN0D3HE5hBwapFencmo=','2020-11-11 15:40:02.133914',0,'yoonsoo','Teacher','Lee','iteachwell@gmail.com',0,1,'2020-11-11 15:40:02.113122');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
INSERT INTO `authtoken_token` VALUES ('04e1d4e3e3e85bf9c5bb3d412b247627e306dfe4','2020-09-27 18:43:53.143797',26),('05324b7f0aa80a83815979097e02d9075252939a','2020-09-28 07:41:57.935528',55),('0b8b27190cd9bef13c0f57b5952b92ff92499127','2020-09-28 07:41:45.611529',54),('1da917312c435aabd67a9af656253788c06af2b0','2020-09-28 07:12:32.853346',36),('2cb3c6aeeb59fdda37632d283d57790418747311','2020-09-28 07:25:54.763929',44),('366d771b2693996b8f9bd44ac7f9c6d838fc8528','2020-09-27 18:53:28.850358',32),('3bf2fbb17b04512cbe3d2960c8aabeb6a5f7b2e1','2020-09-28 07:35:14.520434',49),('43570e553d501b118ba10fb488287b1c12039d8c','2020-09-28 09:10:08.610864',57),('459d78176a5236097f4956f8d7dffed9b4ca25a4','2020-09-27 18:53:17.203209',31),('45b0f9b2d45bf69bbfdc33fa74a90f07c79361bb','2020-09-27 18:52:34.903705',29),('49f68a9f5de93466a7a5e4eade78570dfc421f98','2020-09-27 18:53:05.408611',30),('4a4b96f2bf87aed3813298d66583abad1962cba1','2020-09-28 07:14:44.432678',38),('4b7017b3ca4cc914234cf9b04c06e6741a66a35e','2020-09-28 07:13:11.730842',37),('4e56caa35838df11504a789002ce5a0108a533fc','2020-09-27 17:08:06.326007',16),('6299cc4b196fa3a4b7a86c7856302366bd4736e7','2020-09-27 18:52:24.045429',28),('64f349c13698e588032b22c3b8deee359eadfc5b','2020-09-28 07:38:05.728845',50),('6687e22cf6fb1ed9cbebe4b6afbeac8e75247769','2020-10-02 10:47:58.539900',63),('676a7ae3e292029a6d16b5e0cbbc01a3ac17b8dd','2020-09-28 07:41:16.307210',53),('6bfeed13e6f148e3ee8c86f86ecd785d2d78c02c','2020-09-28 07:22:16.225677',41),('70b202ee681c0256ea698b31b7cd171aec4f9d30','2020-09-27 18:41:56.687072',25),('75065f3c46984a3b36707c770b96c4b2afb0a46a','2020-10-05 04:49:41.170306',65),('77f2a58234fb4978d074f44e28739f5be4f75b56','2020-11-11 15:40:02.128033',66),('78dec94e29312a676a2b2c732e688a2aab9fdb06','2020-09-28 07:30:47.467223',48),('7edad9f374b475beb80c97f94f8e90131578c196','2020-09-27 17:16:29.049960',19),('8120cbef7841a0bdd7feea794abc23e86f8fef93','2020-09-27 18:44:29.029777',27),('87a879d14f133edde6ed84a7672c06a22b632992','2020-09-28 07:25:01.596876',43),('8d8901e16db37cf15bd0220b6f8d6a32550defcb','2020-09-28 07:28:45.310978',47),('97e534f88921f1bed9fc5d31bf02d18ce001ffbc','2020-09-28 07:26:54.275650',45),('9889d1a632fc65cd7ed7b27a0d72eb43f542a6ca','2020-09-28 11:05:32.403042',59),('9a611e67b7bb09610552a6f7d264d0c36ffb2d0f','2020-10-02 11:00:36.621073',64),('ba411645d2fbf1fda5718ef43de0aa1891036f7d','2020-09-28 07:21:52.287697',40),('c37c2a01ad01c33109b63998a86d2c12ec1cfd9c','2020-09-28 07:02:30.584245',35),('c8b588b58a9757e110e5f51590a11f1cbf0c06fa','2020-09-28 07:20:12.662757',39),('c92cefaf79e5ee882e785fa321b584b1ddd0c47d','2020-09-27 17:14:44.368926',17),('e16a334877bac40b973a64694c2e51e67ad44738','2020-10-02 09:20:16.999886',62),('e70203699ffc17ffd092d4d4ffe3ed5b3745d223','2020-09-28 11:01:07.585113',58),('e7f0106cb4a902b384571a71854874a1d9ac93bc','2020-09-28 07:28:31.754014',46),('f49adf2599bfff5eadb408642729200a99654bf2','2020-09-27 17:14:59.604921',18),('fa590761f0d736041db6eb990e4c5f19bd0e086d','2020-09-28 07:44:56.176130',56),('ff86e40a95bcd264d5f3662206cc08c7fdcafbee','2020-09-28 07:24:27.136091',42);
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(7,'authtoken','token'),(15,'authtoken','tokenproxy'),(5,'contenttypes','contenttype'),(13,'seminar','seminar'),(14,'seminar','userseminar'),(6,'sessions','session'),(8,'survey','operatingsystem'),(9,'survey','surveyresult'),(12,'user','instructorprofile'),(11,'user','participantprofile'),(10,'user','userauth');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-09-27 13:37:03.706151'),(2,'auth','0001_initial','2020-09-27 13:37:03.763578'),(3,'admin','0001_initial','2020-09-27 13:37:03.878019'),(4,'admin','0002_logentry_remove_auto_add','2020-09-27 13:37:03.922538'),(5,'admin','0003_logentry_add_action_flag_choices','2020-09-27 13:37:03.928950'),(6,'contenttypes','0002_remove_content_type_name','2020-09-27 13:37:03.964286'),(7,'auth','0002_alter_permission_name_max_length','2020-09-27 13:37:03.985269'),(8,'auth','0003_alter_user_email_max_length','2020-09-27 13:37:04.000389'),(9,'auth','0004_alter_user_username_opts','2020-09-27 13:37:04.007029'),(10,'auth','0005_alter_user_last_login_null','2020-09-27 13:37:04.028808'),(11,'auth','0006_require_contenttypes_0002','2020-09-27 13:37:04.030255'),(12,'auth','0007_alter_validators_add_error_messages','2020-09-27 13:37:04.036301'),(13,'auth','0008_alter_user_username_max_length','2020-09-27 13:37:04.061220'),(14,'auth','0009_alter_user_last_name_max_length','2020-09-27 13:37:04.085750'),(15,'auth','0010_alter_group_name_max_length','2020-09-27 13:37:04.098619'),(16,'auth','0011_update_proxy_permissions','2020-09-27 13:37:04.104946'),(17,'auth','0012_alter_user_first_name_max_length','2020-09-27 13:37:04.129793'),(18,'authtoken','0001_initial','2020-09-27 13:37:04.143437'),(19,'authtoken','0002_auto_20160226_1747','2020-09-27 13:37:04.198216'),(20,'sessions','0001_initial','2020-09-27 13:37:04.205639'),(21,'survey','0001_survey_initial','2020-09-27 13:37:04.231383'),(22,'survey','0002_auto_20200912_0149','2020-09-27 13:37:04.298214'),(23,'user','0001_initial','2020-09-27 13:37:04.353405'),(24,'user','0002_auto_20200927_1316','2020-09-27 13:37:04.465852'),(25,'user','0003_auto_20200927_1336','2020-09-27 13:37:04.535552'),(26,'user','0004_auto_20200927_1543','2020-09-27 15:43:37.674534'),(27,'user','0005_auto_20200928_0701','2020-09-28 07:02:07.413245'),(28,'user','0006_auto_20200928_0734','2020-09-28 07:34:58.353309'),(29,'user','0007_auto_20200928_1445','2020-09-28 14:45:59.615662'),(30,'user','0008_auto_20200929_0714','2020-09-29 07:16:05.959414'),(31,'seminar','0001_initial','2020-09-29 07:20:14.767368'),(32,'seminar','0002_auto_20200929_1000','2020-09-29 10:00:24.134471'),(33,'seminar','0003_userseminar_role','2020-09-29 11:21:41.908159'),(34,'seminar','0004_auto_20200929_1934','2020-09-29 19:35:02.089023'),(35,'seminar','0005_auto_20200930_0515','2020-09-30 05:15:07.463038'),(36,'seminar','0006_auto_20200930_0538','2020-09-30 05:38:31.953024'),(37,'seminar','0007_auto_20201003_1511','2020-10-03 15:11:23.434074'),(38,'user','0009_auto_20201003_1511','2020-10-03 15:11:23.617655'),(39,'authtoken','0003_tokenproxy','2020-11-11 15:30:45.948493');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('05hoicnviyzl5jva17wenlhcrnktj013','e30:1kMX8Z:HpKwtQVBceYjXKJ0Q2jcBiBxQ-k6-CR_I9X8yYgu7nU','2020-10-11 13:54:47.093244'),('1jk5jwx0ks4rtjtfp0qf6sjg7ayf7jxr','e30:1kMaHl:B04vHozJ8LgdRczPATe2-aFRy02L5BRn1TQxZmb_1lo','2020-10-11 17:16:29.053749'),('7ork6y80g9i6j7il3kwhsiqxn434zqo0','e30:1kMu76:uHJTjZrAOHtCBGmnrHjX-U5bQJtCBZaef40-GQhdPkA','2020-10-12 14:26:48.690745'),('7uaanb2iz8nk5463l3qxdba8chnht14u','e30:1kMX78:Xo3BpNs_cuiJ4fXPe5TWHNiH7FpFSp_A4u1tanZJ9Z0','2020-10-11 13:53:18.212184'),('8cs3euvtg4ypj1vkclv2cp68kjyriwsz','e30:1kMsuy:5VIzKwXhBS_hwmd-6CEg0yOiaoUY3g9jU1nmiCsqs4o','2020-10-12 13:10:12.513803'),('8l2d5x9zu9pmy7805kcrr070ymr05v2h','e30:1kMsuB:Trmlfwep3sxJEuIkMBjNyEy079UKL1nyNLcsaC9iz4E','2020-10-12 13:09:23.502275'),('atpdz5obci7zpwmd532e9xj4222ol44o','e30:1kMssS:yxhLrQY6GEyZ9lk0-4DhXDsIWIX_rwkKQlUUtjOgStc','2020-10-12 13:07:36.402215'),('b4jg3v2jry3fhgj4x4f1hvfgkzzz8rck','e30:1kMa9e:1ziM6PXEEeNexmiAi9cReG5BCId0YHkXsr0OkkodLhM','2020-10-11 17:08:06.332140'),('f5wbayhguoty7n9jq57n5ptwpqx5etoj','e30:1kMaG4:aElmo_NtQxr5c6dwgFbuXzyGl1eWWMExYwg0tV_ibX8','2020-10-11 17:14:44.374498'),('if84s7j9tt31o76p6zpu35evcp0mvl0n','e30:1kMu53:zFybKPmsmVCiH3sc3e4VdGilh9w2Td33ERvMkjNINpY','2020-10-12 14:24:41.180877'),('mbmi9hxomrxkgg9v8njg6mv5zgv9u5th','e30:1kMstY:ISYYqB9bEbhfNGAlw7Iki6Pt5HDDY69OpYdi-yROdJQ','2020-10-12 13:08:44.909340'),('ofkhdxx1e5s1p54wsuja2qabt4pmjplh','.eJxVjMEOwiAQRP-FsyGFwgIevfcbml1gpWpoUtqT8d9tkx40mdO8N_MWI25rGbeWl3FK4ioAxOW3JIzPXA-SHljvs4xzXZeJ5KHIkzY5zCm_bqf7d1CwlX3tdIRorU_eGN2D66hjRgrJpKAIiBwbMF1vWTuGgI7ZKK96p7Tag-LzBfxGN00:1kcsE6:Ow8er2VTXobu6O43FNEbWY1-NZ9S1dt5KaQSBn7BKwk','2020-11-25 15:40:02.145181'),('unxzvpfsz03c216olxshopm1tiju6s7d','.eJxVjEEOwiAQRe_C2pCWAh1cuvcMZJgZbNVAUtqV8e7apAvd_vfef6mI2zrFrckSZ1Zn5a06_Y4J6SFlJ3zHcquaalmXOeld0Qdt-lpZnpfD_TuYsE3fGrJj4A4N0CicApIJxg6htyN7oN4YRkrZEEvuBkng3Jh6D5lDB-K8en8AJSA4rA:1kOmca:TNHY4YRnXXaqE0b-dujjHZ3ezbhDHeYQnENezpGmKHA','2020-10-17 18:51:04.536417'),('wces22j0ei9xp3cijs2mpxird2248qen','e30:1kMaGJ:LtOuzMrRGqys33M_29AGSdrhgGc7Rvcpola4R6YOvEw','2020-10-11 17:14:59.607641'),('wrjf70pj82xtb4vd3kiwaffaq2f9mzoh','e30:1kMuCo:MuFsVlYSpaY39-zHvRkYt9WA23CO4Aq6BX7uTqmKEoI','2020-10-12 14:32:42.355695'),('yfjvsoehhxs1ngc9rgny7nxuftq2v5gl','.eJxVjDsOwjAQBe_iGlmJvf5R0nMGa9de4wBypDipEHeHSCmgfTPzXiLitta4dV7ilMVZWCNOvyNhenDbSb5ju80yzW1dJpK7Ig_a5XXO_Lwc7t9BxV6_NWodsnJeg2JFbMDbcaSQFBXrGExBH5QDSLkMiRh8Cs4F7TzaUMpgxfsD_EA30g:1kPIRc:FA1ddMvleAlCn70JXnSv_ey65t3i0u6C9pbIte3vpJ0','2020-10-19 04:49:52.070526');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seminar_seminar`
--

DROP TABLE IF EXISTS `seminar_seminar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seminar_seminar` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `capacity` smallint unsigned NOT NULL,
  `count` smallint unsigned NOT NULL,
  `time` time(6) NOT NULL,
  `online` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `seminar_seminar_capacity_5a3e09b6_check` CHECK ((`capacity` >= 0)),
  CONSTRAINT `seminar_seminar_count_750a674d_check` CHECK ((`count` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=183 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seminar_seminar`
--

LOCK TABLES `seminar_seminar` WRITE;
/*!40000 ALTER TABLE `seminar_seminar` DISABLE KEYS */;
INSERT INTO `seminar_seminar` VALUES (178,'seminar1',1,1,'22:00:00.000000',0,'2020-09-29 20:03:12.012973','2020-09-29 20:03:12.012998'),(180,'seminar100',10,100,'17:40:00.000000',1,'2020-09-29 20:04:07.708853','2020-10-02 17:35:59.016515'),(181,'seminar101',100,100,'12:00:00.000000',1,'2020-09-30 03:44:53.837682','2020-09-30 03:44:53.837704'),(182,'seminar1',100,10,'12:00:00.000000',1,'2020-10-05 04:50:27.955267','2020-10-05 04:50:27.955294');
/*!40000 ALTER TABLE `seminar_seminar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seminar_userseminar`
--

DROP TABLE IF EXISTS `seminar_userseminar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seminar_userseminar` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `seminar_id` int NOT NULL,
  `user_id` int NOT NULL,
  `role` varchar(100) NOT NULL,
  `dropped_at` datetime(6) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `userseminar_unique` (`user_id`,`seminar_id`),
  KEY `seminar_userseminar_seminar_id_a423a58b_fk_seminar_seminar_id` (`seminar_id`),
  KEY `seminar_userseminar_role_bd988dd4` (`role`),
  CONSTRAINT `seminar_userseminar_seminar_id_a423a58b_fk_seminar_seminar_id` FOREIGN KEY (`seminar_id`) REFERENCES `seminar_seminar` (`id`),
  CONSTRAINT `seminar_userseminar_user_id_ae904740_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=135 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seminar_userseminar`
--

LOCK TABLES `seminar_userseminar` WRITE;
/*!40000 ALTER TABLE `seminar_userseminar` DISABLE KEYS */;
INSERT INTO `seminar_userseminar` VALUES (126,'2020-09-29 20:03:12.016904','2020-09-29 20:03:12.016916',178,54,'instructor',NULL,1),(127,'2020-09-29 20:04:07.711759','2020-09-29 20:04:07.711772',180,54,'instructor',NULL,1),(128,'2020-09-30 03:44:53.842674','2020-09-30 03:44:53.842687',181,54,'instructor',NULL,1),(129,'2020-09-30 05:16:56.343510','2020-09-30 05:16:56.343520',180,59,'instructor','2020-09-30 05:16:56.343498',1),(130,'2020-09-30 05:18:12.614837','2020-09-30 05:18:12.614847',180,50,'participant','2020-09-30 06:11:21.187859',0),(131,'2020-09-30 05:18:55.006885','2020-09-30 05:18:55.006898',180,40,'participant','2020-09-30 05:18:55.006870',1),(132,'2020-09-30 05:21:00.174224','2020-09-30 05:21:00.174237',180,57,'participant','2020-09-30 05:21:00.174209',1),(133,'2020-09-30 05:22:24.052174','2020-09-30 05:22:24.052186',180,36,'instructor','2020-09-30 05:22:24.052160',1),(134,'2020-10-05 04:50:27.961658','2020-10-05 04:50:27.961680',182,65,'instructor',NULL,1);
/*!40000 ALTER TABLE `seminar_userseminar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `survey_operatingsystem`
--

DROP TABLE IF EXISTS `survey_operatingsystem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `survey_operatingsystem` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `description` varchar(200) NOT NULL,
  `price` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `survey_operatingsystem_name_6aa585fd` (`name`),
  CONSTRAINT `survey_operatingsystem_chk_1` CHECK ((`price` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey_operatingsystem`
--

LOCK TABLES `survey_operatingsystem` WRITE;
/*!40000 ALTER TABLE `survey_operatingsystem` DISABLE KEYS */;
/*!40000 ALTER TABLE `survey_operatingsystem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `survey_surveyresult`
--

DROP TABLE IF EXISTS `survey_surveyresult`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `survey_surveyresult` (
  `id` int NOT NULL AUTO_INCREMENT,
  `python` smallint unsigned NOT NULL,
  `rdb` smallint unsigned NOT NULL,
  `programming` smallint unsigned NOT NULL,
  `major` varchar(100) NOT NULL,
  `grade` varchar(20) NOT NULL,
  `backend_reason` varchar(500) NOT NULL,
  `waffle_reason` varchar(500) NOT NULL,
  `say_something` varchar(500) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `os_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `survey_surveyresult_os_id_b712c5c1_fk_survey_operatingsystem_id` (`os_id`),
  KEY `survey_surveyresult_user_id_643a7eb1_fk_auth_user_id` (`user_id`),
  CONSTRAINT `survey_surveyresult_os_id_b712c5c1_fk_survey_operatingsystem_id` FOREIGN KEY (`os_id`) REFERENCES `survey_operatingsystem` (`id`),
  CONSTRAINT `survey_surveyresult_user_id_643a7eb1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `survey_surveyresult_chk_1` CHECK ((`python` >= 0)),
  CONSTRAINT `survey_surveyresult_chk_2` CHECK ((`rdb` >= 0)),
  CONSTRAINT `survey_surveyresult_chk_3` CHECK ((`programming` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey_surveyresult`
--

LOCK TABLES `survey_surveyresult` WRITE;
/*!40000 ALTER TABLE `survey_surveyresult` DISABLE KEYS */;
/*!40000 ALTER TABLE `survey_surveyresult` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_instructorprofile`
--

DROP TABLE IF EXISTS `user_instructorprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_instructorprofile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `company` varchar(255) NOT NULL,
  `year` smallint unsigned DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_instructorprofile_user_id_58694357_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `user_instructorprofile_year_0170a704_check` CHECK ((`year` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_instructorprofile`
--

LOCK TABLES `user_instructorprofile` WRITE;
/*!40000 ALTER TABLE `user_instructorprofile` DISABLE KEYS */;
INSERT INTO `user_instructorprofile` VALUES (1,'',NULL,'2020-09-28 07:12:32.851052','2020-09-28 07:12:32.851076',36),(2,'',NULL,'2020-09-28 07:13:11.728608','2020-09-28 07:13:11.728639',37),(3,'',NULL,'2020-09-28 07:14:44.429201','2020-09-28 07:14:44.429248',38),(4,'',NULL,'2020-09-28 07:20:12.660451','2020-09-28 07:20:12.660477',39),(5,'',NULL,'2020-09-28 07:22:16.223827','2020-09-28 07:22:16.223851',41),(6,'',NULL,'2020-09-28 07:24:27.132837','2020-09-28 07:24:27.132893',42),(7,'',NULL,'2020-09-28 07:25:01.594417','2020-09-28 07:25:01.594447',43),(8,'',NULL,'2020-09-28 07:25:54.762128','2020-09-28 07:25:54.762154',44),(9,'kakao',NULL,'2020-09-28 07:26:54.273881','2020-09-28 07:26:54.273909',45),(10,'',4,'2020-09-28 07:28:31.751559','2020-09-28 07:28:31.751582',46),(11,'kakao',4,'2020-09-28 07:28:45.308854','2020-09-28 07:28:45.308878',47),(12,'kakao',0,'2020-09-28 07:30:47.465320','2020-09-28 07:30:47.465342',48),(13,'kakao',4,'2020-09-28 07:35:14.517562','2020-09-28 07:35:14.517599',49),(14,'kakao',1,'2020-09-28 07:38:05.724603','2020-09-28 07:38:05.724640',50),(15,'kakao',1,'2020-09-28 07:40:27.669410','2020-09-28 07:40:27.669460',51),(16,'kakao',1,'2020-09-28 07:40:51.090334','2020-09-28 07:40:51.090363',52),(17,'kakao',1,'2020-09-28 07:41:16.305531','2020-09-28 07:41:16.305556',53),(18,'kakao',1,'2020-09-28 07:41:45.609061','2020-09-29 10:58:22.703393',54),(19,'',10,'2020-09-28 11:05:32.399364','2020-09-28 14:31:30.706689',59),(20,'매스프레소',2,'2020-10-02 11:00:36.615426','2020-10-02 11:03:43.316926',64),(21,'서울대학교',2,'2020-10-05 04:49:41.137020','2020-10-05 04:49:41.137054',65),(22,'',10,'2020-11-11 15:40:02.118035','2020-11-11 15:40:02.118068',66);
/*!40000 ALTER TABLE `user_instructorprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_participantprofile`
--

DROP TABLE IF EXISTS `user_participantprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_participantprofile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `university` varchar(255) NOT NULL,
  `accepted` tinyint(1) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_participantprofile_user_id_f81c8145_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_participantprofile`
--

LOCK TABLES `user_participantprofile` WRITE;
/*!40000 ALTER TABLE `user_participantprofile` DISABLE KEYS */;
INSERT INTO `user_participantprofile` VALUES (1,'snu',1,'2020-09-28 07:02:30.582264','2020-09-28 15:41:03.901338',35),(2,'snu',1,'2020-09-28 07:21:52.285637','2020-09-28 07:21:52.285667',40),(3,'',1,'2020-09-28 07:38:05.726093','2020-09-28 07:38:05.726145',50),(4,'snu',1,'2020-09-28 07:41:57.933190','2020-09-28 07:41:57.933211',55),(5,'snu',1,'2020-09-28 07:44:56.174532','2020-09-28 07:44:56.174553',56),(6,'snu',1,'2020-09-28 09:10:08.608032','2020-09-28 09:10:08.608061',57),(7,'Seoul National Univ',1,'2020-09-28 11:01:07.579940','2020-09-28 11:03:36.188559',58),(32,'',1,'2020-09-28 14:22:03.634294','2020-09-28 14:31:30.593293',59),(38,'서울대학교',0,'2020-10-02 09:20:16.991175','2020-10-02 09:20:16.991200',62),(39,'경북대학교',0,'2020-10-02 10:47:58.535823','2020-10-02 10:52:15.727858',63);
/*!40000 ALTER TABLE `user_participantprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_userauth`
--

DROP TABLE IF EXISTS `user_userauth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_userauth` (
  `id` int NOT NULL AUTO_INCREMENT,
  `role` varchar(100) NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_userauth_user_id_903c6ffe_uniq` (`user_id`),
  CONSTRAINT `user_userauth_user_id_903c6ffe_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_userauth`
--

LOCK TABLES `user_userauth` WRITE;
/*!40000 ALTER TABLE `user_userauth` DISABLE KEYS */;
INSERT INTO `user_userauth` VALUES (1,'',15),(2,'participan',25),(3,'participan',26),(4,'instructor',27),(5,'instructor',28),(6,'instructor',29),(7,'instructor',30),(8,'participan',31),(9,'participan',32),(10,'participant',35),(11,'instructor',36),(12,'instructor',37),(13,'instructor',38),(14,'instructor',39),(15,'participant',40),(16,'instructor',41),(17,'instructor',42),(18,'instructor',43),(19,'instructor',44),(20,'instructor',45),(21,'instructor',46),(22,'instructor',47),(23,'instructor',48),(24,'instructor',49),(25,'instructor',50),(26,'instructor',53),(27,'instructor',54),(28,'participant',55),(29,'participant',56),(30,'participant',57),(31,'participant',58),(32,'instructor',59),(34,'participant',62),(35,'instructor',63),(36,'instructor',64),(37,'instructor',65),(38,'instructor',66);
/*!40000 ALTER TABLE `user_userauth` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-12  6:02:10
