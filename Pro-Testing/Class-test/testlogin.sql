/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50718
Source Host           : 127.0.0.1:3306
Source Database       : question

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2017-08-23 17:42:16
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for testlogin
-- ----------------------------
DROP TABLE IF EXISTS `testlogin`;
CREATE TABLE `testlogin` (
  `id` int(99) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of testlogin
-- ----------------------------
INSERT INTO `testlogin` VALUES ('1', 'Benjamin', '123');
INSERT INTO `testlogin` VALUES ('2', 'Justin', '123');
INSERT INTO `testlogin` VALUES ('3', 'Jessie', '123');
SET FOREIGN_KEY_CHECKS=1;
