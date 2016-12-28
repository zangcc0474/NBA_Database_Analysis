-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: localhost    Database: NBA_Database
-- ------------------------------------------------------
-- Server version	5.7.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app_contract`
--

DROP TABLE IF EXISTS `app_contract`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_contract` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year` date NOT NULL,
  `Salary` bigint(20) NOT NULL,
  `player_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_contract_afe72417` (`player_id`),
  KEY `app_contract_f6a7ca40` (`team_id`),
  CONSTRAINT `app_contract_player_id_6d6d8b0b_fk_app_player_player_id` FOREIGN KEY (`player_id`) REFERENCES `app_player` (`player_id`),
  CONSTRAINT `app_contract_team_id_e84fa9a1_fk_app_team_team_id` FOREIGN KEY (`team_id`) REFERENCES `app_team` (`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_contract`
--

LOCK TABLES `app_contract` WRITE;
/*!40000 ALTER TABLE `app_contract` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_contract` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_game`
--

DROP TABLE IF EXISTS `app_game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_game` (
  `game_id` varchar(100) NOT NULL,
  `game_date` datetime(6) NOT NULL,
  `host` varchar(100) NOT NULL,
  `guest` varchar(100) NOT NULL,
  `host_score` int(11) NOT NULL,
  `guest_score` int(11) NOT NULL,
  `guest_team_id` int(11) NOT NULL,
  `host_team_id` int(11) NOT NULL,
  PRIMARY KEY (`game_id`),
  KEY `app_game_3f0810b4` (`guest_team_id`),
  KEY `app_game_6e4d6377` (`host_team_id`),
  CONSTRAINT `app_game_guest_team_id_abb9fb34_fk_app_team_team_id` FOREIGN KEY (`guest_team_id`) REFERENCES `app_team` (`team_id`),
  CONSTRAINT `app_game_host_team_id_1a1265d8_fk_app_team_team_id` FOREIGN KEY (`host_team_id`) REFERENCES `app_team` (`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_game`
--

LOCK TABLES `app_game` WRITE;
/*!40000 ALTER TABLE `app_game` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_player`
--

DROP TABLE IF EXISTS `app_player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_player` (
  `player_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_player`
--

LOCK TABLES `app_player` WRITE;
/*!40000 ALTER TABLE `app_player` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_player_game_adv_stats`
--

DROP TABLE IF EXISTS `app_player_game_adv_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_player_game_adv_stats` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `game_id` varchar(100) NOT NULL,
  `player_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_player_game_adv_stats_game_id_06c5abbd_fk_app_game_game_id` (`game_id`),
  KEY `app_player_game_adv_s_player_id_750418b2_fk_app_player_player_id` (`player_id`),
  CONSTRAINT `app_player_game_adv_s_player_id_750418b2_fk_app_player_player_id` FOREIGN KEY (`player_id`) REFERENCES `app_player` (`player_id`),
  CONSTRAINT `app_player_game_adv_stats_game_id_06c5abbd_fk_app_game_game_id` FOREIGN KEY (`game_id`) REFERENCES `app_game` (`game_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_player_game_adv_stats`
--

LOCK TABLES `app_player_game_adv_stats` WRITE;
/*!40000 ALTER TABLE `app_player_game_adv_stats` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_player_game_adv_stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_player_game_stats`
--

DROP TABLE IF EXISTS `app_player_game_stats`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_player_game_stats` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `assistant` int(11) NOT NULL,
  `block` int(11) NOT NULL,
  `game_id` varchar(100) NOT NULL,
  `player_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_player_game_stats_game_id_69e71d43_fk_app_game_game_id` (`game_id`),
  KEY `app_player_game_stats_player_id_cf6daea0_fk_app_player_player_id` (`player_id`),
  CONSTRAINT `app_player_game_stats_game_id_69e71d43_fk_app_game_game_id` FOREIGN KEY (`game_id`) REFERENCES `app_game` (`game_id`),
  CONSTRAINT `app_player_game_stats_player_id_cf6daea0_fk_app_player_player_id` FOREIGN KEY (`player_id`) REFERENCES `app_player` (`player_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_player_game_stats`
--

LOCK TABLES `app_player_game_stats` WRITE;
/*!40000 ALTER TABLE `app_player_game_stats` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_player_game_stats` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_team`
--

DROP TABLE IF EXISTS `app_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_team` (
  `team_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_team`
--

LOCK TABLES `app_team` WRITE;
/*!40000 ALTER TABLE `app_team` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'app','contract'),(4,'app','game'),(3,'app','player'),(6,'app','player_game_adv_stats'),(1,'app','player_game_stats'),(5,'app','team'),(7,'contenttypes','contenttype'),(8,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'app','0001_initial','2016-12-28 05:37:28.621397'),(2,'contenttypes','0001_initial','2016-12-28 05:37:28.660606'),(3,'contenttypes','0002_remove_content_type_name','2016-12-28 05:37:28.706420'),(4,'sessions','0001_initial','2016-12-28 05:37:28.738069');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'NBA_Database'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-28  0:44:48
