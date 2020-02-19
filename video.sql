/*
Navicat MySQL Data Transfer

Source Server         : mybase
Source Server Version : 80003
Source Host           : localhost:3306
Source Database       : video

Target Server Type    : MYSQL
Target Server Version : 80003
File Encoding         : 65001

Date: 2020-02-19 15:02:34
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for classify1
-- ----------------------------
DROP TABLE IF EXISTS `classify1`;
CREATE TABLE `classify1` (
  `oneid` int(11) NOT NULL,
  `onename` varchar(10) NOT NULL,
  `intro` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`oneid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of classify1
-- ----------------------------

-- ----------------------------
-- Table structure for college
-- ----------------------------
DROP TABLE IF EXISTS `college`;
CREATE TABLE `college` (
  `coid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `intro` varchar(50) NOT NULL,
  `logo` varchar(60) NOT NULL,
  `co_image` varchar(60) NOT NULL,
  `schoolbadge` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`coid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of college
-- ----------------------------

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course` (
  `vid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `author` varchar(15) DEFAULT NULL,
  `intro` varchar(50) NOT NULL,
  `v_image` varchar(60) NOT NULL,
  `viewnum` int(11) DEFAULT NULL,
  `likenum` int(11) DEFAULT NULL,
  `collectnum` int(11) DEFAULT NULL,
  `courseware` varchar(50) DEFAULT NULL,
  `sum` int(11) DEFAULT NULL,
  `clid` int(11) NOT NULL,
  `coid` int(11) DEFAULT NULL,
  `oneid` int(11) DEFAULT NULL,
  PRIMARY KEY (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of course
-- ----------------------------

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history` (
  `hid` int(11) NOT NULL AUTO_INCREMENT,
  `historytime` varchar(50) NOT NULL,
  `collect` tinyint(1) NOT NULL,
  `uid` int(11) NOT NULL,
  `vid` int(11) NOT NULL,
  PRIMARY KEY (`hid`),
  KEY `uid` (`uid`),
  KEY `vid` (`vid`),
  CONSTRAINT `uid` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`),
  CONSTRAINT `vid` FOREIGN KEY (`vid`) REFERENCES `course` (`vid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of history
-- ----------------------------

-- ----------------------------
-- Table structure for material
-- ----------------------------
DROP TABLE IF EXISTS `material`;
CREATE TABLE `material` (
  `mid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `acthor` varchar(15) DEFAULT NULL,
  `intro` varchar(50) NOT NULL,
  `downloadnum` int(11) DEFAULT NULL,
  `m_image` varchar(60) DEFAULT NULL,
  `oneid` int(11) NOT NULL,
  PRIMARY KEY (`mid`),
  KEY `classifyid` (`oneid`),
  CONSTRAINT `classifyid` FOREIGN KEY (`oneid`) REFERENCES `classify1` (`oneid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of material
-- ----------------------------

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `account` varchar(15) NOT NULL,
  `password` varchar(20) NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `u_image` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------

-- ----------------------------
-- Table structure for video
-- ----------------------------
DROP TABLE IF EXISTS `video`;
CREATE TABLE `video` (
  `vid` int(11) NOT NULL,
  `videoId` varchar(50) NOT NULL,
  `sectionname` varchar(30) DEFAULT NULL,
  `time` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of video
-- ----------------------------
