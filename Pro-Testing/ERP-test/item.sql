/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50718
Source Host           : 127.0.0.1:3306
Source Database       : question

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2017-08-23 17:39:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for item
-- ----------------------------
DROP TABLE IF EXISTS `item`;
CREATE TABLE `item` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `pname` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `pguige` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `pchenbenjia` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `pxiaoshoujia` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `psctime` varchar(255) CHARACTER SET sjis DEFAULT NULL,
  `pyxtime` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `pjhtime` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of item
-- ----------------------------
INSERT INTO `item` VALUES ('1', '杰士邦', '10个/盒', '10元', '20元', '2017-08-23 11:19', '2017-08-23 11:19', '2017-08-23 11:19');
INSERT INTO `item` VALUES ('6', '篮球', '1个', '15元', '50元', '2017-08-23 11:20', '2017-08-23 11:20', '2017-08-23 11:20');
INSERT INTO `item` VALUES ('11', 'NFC模拟器', '10CM*6CM', '60元', '100元', '2017-08-01 13:38', '2017-08-01 13:38', '2017-08-30 13:39');
INSERT INTO `item` VALUES ('15', '罗技鼠标', '白色', '25元', '45元', '2017-08-01 13:53', '2017-08-01 17:06', '2017-08-08 13:53');
INSERT INTO `item` VALUES ('21', '摇头丸', '10粒/瓶', '1000元', '2000元', '2017-08-08 16:14', '2017-08-08 16:14', '2017-08-08 16:14');
SET FOREIGN_KEY_CHECKS=1;
