-- MySQL dump 10.19  Distrib 10.3.29-MariaDB, for debian-linux-gnueabihf (armv7l)
--
-- Host: localhost    Database: SENSOR
-- ------------------------------------------------------
-- Table structure for table `SENSOR_DB`
-- 建立資料庫
create database `SENSOR`;

use SENSOR;

-- 建表
DROP TABLE IF EXISTS `SENSOR_DB`;


CREATE TABLE `SENSOR_DB` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Time` timestamp NOT NULL DEFAULT current_timestamp(),
  `Proj_ID` varchar(20) DEFAULT NULL,
  `STID` varchar(20) DEFAULT NULL,
  `Value1` float DEFAULT -9999,
  `Value2` float DEFAULT -9999,
  `Value3` float DEFAULT -9999,
  `Value4` float DEFAULT -9999,
  `Value5` float DEFAULT -9999,
  `Value6` float DEFAULT -9999,
  `Value7` float DEFAULT -9999,
  `Value8` float DEFAULT -9999,
  `Value9` float DEFAULT -9999,
  `Value10` float DEFAULT -9999,
  `Value11` float DEFAULT -9999,
  `Value12` float DEFAULT -9999,
  `Value13` float DEFAULT -9999,
  `Value14` float DEFAULT -9999,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
-- 插入資料
INSERT INTO `SENSOR_DB` ( `Proj_ID`, `STID`) VALUES ('Chaiyi_EPB','2332623TN001');
--

-- Table structure for table `STANDARD_DB`
--

DROP TABLE IF EXISTS `STANDARD_DB`;

CREATE TABLE `STANDARD_DB` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Value1` float DEFAULT -9999,
  `Value2` float DEFAULT -9999,
  `Value3` float DEFAULT -9999,
  `Value4` float DEFAULT -9999,
  `Value5` float DEFAULT -9999,
  `Value6` float DEFAULT -9999,
  `Value7` float DEFAULT -9999,

  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
-- 插入資料
INSERT INTO `STANDARD_DB` ( `Value1`) VALUES ('-9999');
--
--
-- Table structure for table `T01`
--

DROP TABLE IF EXISTS `T01`;

CREATE TABLE `T01` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Proj_ID` varchar(20) DEFAULT NULL,
  `STID` varchar(20) DEFAULT NULL,
  `Value1` float DEFAULT -9999,
  `Value2` float DEFAULT -9999,
  `Value3` float DEFAULT -9999,
  `Value4` float DEFAULT -9999,
  `Value5` float DEFAULT -9999,
  `Value6` float DEFAULT -9999,
  `Value7` float DEFAULT -9999,
  `Value8` float DEFAULT -9999,
  `Value9` float DEFAULT -9999,
  `Value10` float DEFAULT -9999,
  `Value11` float DEFAULT -9999,
  `Value12` float DEFAULT -9999,
  `Value13` float DEFAULT -9999,
  `Value14` float DEFAULT -9999,
  PRIMARY KEY (`ID`,`Time`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
-- 插入資料
INSERT INTO `T01` ( `Proj_ID`, `STID`) VALUES ('Chaiyi_EPB','2332623TN001');
--

--
-- Table structure for table `T05`
--

DROP TABLE IF EXISTS `T05`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T05` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Proj_ID` varchar(20) DEFAULT NULL,
  `STID` varchar(20) DEFAULT NULL,
  `Value1` float DEFAULT -9999,
  `Value2` float DEFAULT -9999,
  `Value3` float DEFAULT -9999,
  `Value4` float DEFAULT -9999,
  `Value5` float DEFAULT -9999,
  `Value6` float DEFAULT -9999,
  `Value7` float DEFAULT -9999,
  `Value8` float DEFAULT -9999,
  `Value9` float DEFAULT -9999,
  `Value10` float DEFAULT -9999,
  `Value11` float DEFAULT -9999,
  `Value12` float DEFAULT -9999,
  `Value13` float DEFAULT -9999,
  `Value14` float DEFAULT -9999,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
-- 插入資料
INSERT INTO `T05` ( `Proj_ID`, `STID`) VALUES ('Chaiyi_EPB','2332623TN001');
--

--
-- Table structure for table `T60`
--

DROP TABLE IF EXISTS `T60`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `T60` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Proj_ID` varchar(20) DEFAULT NULL,
  `STID` varchar(20) DEFAULT NULL,
  `Value1` float DEFAULT -9999,
  `Value2` float DEFAULT -9999,
  `Value3` float DEFAULT -9999,
  `Value4` float DEFAULT -9999,
  `Value5` float DEFAULT -9999,
  `Value6` float DEFAULT -9999,
  `Value7` float DEFAULT -9999,
  `Value8` float DEFAULT -9999,
  `Value9` float DEFAULT -9999,
  `Value10` float DEFAULT -9999,
  `Value11` float DEFAULT -9999,
  `Value12` float DEFAULT -9999,
  `Value13` float DEFAULT -9999,
  `Value14` float DEFAULT -9999,

  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
-- 插入資料
INSERT INTO `T60` ( `Proj_ID`, `STID`) VALUES ('Chaiyi_EPB','2332623TN001');
--

-- Dump completed on 2022-05-26 15:52:14


-- 建立資料庫
create database `REVISE`;

use REVISE;
--

DROP TABLE IF EXISTS `INITIAL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `INITIAL` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Proj_ID` varchar(20) NOT NULL,
  `STID` varchar(20) DEFAULT NULL,
  `Address` varchar(30) NOT NULL,
  `Lng` varchar(20) NOT NULL,
  `Lat` varchar(20) NOT NULL,
  `IP` varchar(20) NOT NULL,
  `PORT` varchar(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
-- 插入資料
INSERT INTO `INITIAL` ( `Proj_ID`, `STID`, `Address`,`Lng`,`Lat`,`IP`,`PORT`) 
VALUES ('Chaiyi_EPB','2332623TN001','嘉義市東區忠孝路307號','22.488493','120.4529439','192.168.3.107','4000');
--

--
-- Table structure for table `LABEL`
--

DROP TABLE IF EXISTS `LABEL`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LABEL` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Label` varchar(10) DEFAULT NULL,
  `Name` varchar(10) DEFAULT NULL,
  `IsShow` varchar(5) DEFAULT 'True',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
-- 插入資料
INSERT INTO `LABEL` ( `Label`, `Name`, `IsShow`) VALUES ('Value1','Value1','True');
INSERT INTO `LABEL` ( `Label`, `Name`, `IsShow`) VALUES ('Value2','Value2','True');
INSERT INTO `LABEL` ( `Label`, `Name`, `IsShow`) VALUES ('Value3','Value3','True');
INSERT INTO `LABEL` ( `Label`, `Name`, `IsShow`) VALUES ('Value4','Value4','True');
INSERT INTO `LABEL` ( `Label`, `Name`, `IsShow`) VALUES ('Value5','Value5','True');
INSERT INTO `LABEL` ( `Label`, `Name`, `IsShow`) VALUES ('Value6','Value6','True');
INSERT INTO `LABEL` ( `Label`, `Name`, `IsShow`) VALUES ('Value7','Value7','True');

--

--
-- Table structure for table `RE_VALUE`
--

DROP TABLE IF EXISTS `RE_VALUE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `RE_VALUE` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Va_Name` varchar(10) NOT NULL DEFAULT 'NO_Name',
  `Value_zero` float DEFAULT 1,
  `Value_span` float DEFAULT 0,
  `Count_zero` float DEFAULT 1,
  `Count_span` float DEFAULT 0,
  `a` float DEFAULT 1,
  `b` float DEFAULT 0,
  `offset` float DEFAULT 0,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
-- 插入資料
INSERT INTO `RE_VALUE` ( `Va_Name`) VALUES ('Value1');
INSERT INTO `RE_VALUE` ( `Va_Name`) VALUES ('Value2');
INSERT INTO `RE_VALUE` ( `Va_Name`) VALUES ('Value3');
INSERT INTO `RE_VALUE` ( `Va_Name`) VALUES ('Value4');
INSERT INTO `RE_VALUE` ( `Va_Name`) VALUES ('Value5');
INSERT INTO `RE_VALUE` ( `Va_Name`) VALUES ('Value6');
INSERT INTO `RE_VALUE` ( `Va_Name`) VALUES ('Value7');

--

--
-- Table structure for table `ST_VALUE`
--

DROP TABLE IF EXISTS `ST_VALUE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ST_VALUE` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Va_Name` varchar(10) NOT NULL,
  `Value_zero` float DEFAULT 1,
  `Value_span` float DEFAULT 0,
  `Count_zero` float DEFAULT 1,
  `Count_span` float DEFAULT 0,
  `a` float DEFAULT 1,
  `b` float DEFAULT 0,
  `offset` float DEFAULT 0,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;
-- 插入資料
INSERT INTO `ST_VALUE` ( `Va_Name`) VALUES ('Value1');
INSERT INTO `ST_VALUE` ( `Va_Name`) VALUES ('Value2');
INSERT INTO `ST_VALUE` ( `Va_Name`) VALUES ('Value3');
INSERT INTO `ST_VALUE` ( `Va_Name`) VALUES ('Value4');
INSERT INTO `ST_VALUE` ( `Va_Name`) VALUES ('Value5');
INSERT INTO `ST_VALUE` ( `Va_Name`) VALUES ('Value6');
INSERT INTO `ST_VALUE` ( `Va_Name`) VALUES ('Value7');
--

-- Dump completed on 2022-05-26 15:52:33
