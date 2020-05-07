/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 50638
 Source Host           : localhost:3306
 Source Schema         : yoga

 Target Server Type    : MySQL
 Target Server Version : 50638
 File Encoding         : 65001

 Date: 07/05/2020 23:50:07
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 45 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add result', 7, 'add_result');
INSERT INTO `auth_permission` VALUES (26, 'Can change result', 7, 'change_result');
INSERT INTO `auth_permission` VALUES (27, 'Can delete result', 7, 'delete_result');
INSERT INTO `auth_permission` VALUES (28, 'Can view result', 7, 'view_result');
INSERT INTO `auth_permission` VALUES (29, 'Can add user', 8, 'add_user');
INSERT INTO `auth_permission` VALUES (30, 'Can change user', 8, 'change_user');
INSERT INTO `auth_permission` VALUES (31, 'Can delete user', 8, 'delete_user');
INSERT INTO `auth_permission` VALUES (32, 'Can view user', 8, 'view_user');
INSERT INTO `auth_permission` VALUES (33, 'Can add yoga image', 9, 'add_yogaimage');
INSERT INTO `auth_permission` VALUES (34, 'Can change yoga image', 9, 'change_yogaimage');
INSERT INTO `auth_permission` VALUES (35, 'Can delete yoga image', 9, 'delete_yogaimage');
INSERT INTO `auth_permission` VALUES (36, 'Can view yoga image', 9, 'view_yogaimage');
INSERT INTO `auth_permission` VALUES (37, 'Can add study record', 10, 'add_studyrecord');
INSERT INTO `auth_permission` VALUES (38, 'Can change study record', 10, 'change_studyrecord');
INSERT INTO `auth_permission` VALUES (39, 'Can delete study record', 10, 'delete_studyrecord');
INSERT INTO `auth_permission` VALUES (40, 'Can view study record', 10, 'view_studyrecord');
INSERT INTO `auth_permission` VALUES (41, 'Can add favorites', 11, 'add_favorites');
INSERT INTO `auth_permission` VALUES (42, 'Can change favorites', 11, 'change_favorites');
INSERT INTO `auth_permission` VALUES (43, 'Can delete favorites', 11, 'delete_favorites');
INSERT INTO `auth_permission` VALUES (44, 'Can view favorites', 11, 'view_favorites');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (11, 'yogaMaster', 'favorites');
INSERT INTO `django_content_type` VALUES (7, 'yogaMaster', 'result');
INSERT INTO `django_content_type` VALUES (10, 'yogaMaster', 'studyrecord');
INSERT INTO `django_content_type` VALUES (8, 'yogaMaster', 'user');
INSERT INTO `django_content_type` VALUES (9, 'yogaMaster', 'yogaimage');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 23 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2020-04-23 06:28:05.827485');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2020-04-23 06:28:05.932296');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2020-04-23 06:28:06.267895');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2020-04-23 06:28:06.349707');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2020-04-23 06:28:06.366636');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2020-04-23 06:28:06.448074');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2020-04-23 06:28:06.487931');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2020-04-23 06:28:06.521842');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2020-04-23 06:28:06.530812');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2020-04-23 06:28:06.560733');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2020-04-23 06:28:06.564722');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2020-04-23 06:28:06.575693');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2020-04-23 06:28:06.607608');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2020-04-23 06:28:06.645506');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2020-04-23 06:28:06.683408');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2020-04-23 06:28:06.693382');
INSERT INTO `django_migrations` VALUES (17, 'sessions', '0001_initial', '2020-04-23 06:28:06.711331');
INSERT INTO `django_migrations` VALUES (22, 'yogaMaster', '0001_initial', '2020-05-07 12:50:07.132765');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for favorites
-- ----------------------------
DROP TABLE IF EXISTS `favorites`;
CREATE TABLE `favorites`  (
  `favoritesId` int(11) NOT NULL AUTO_INCREMENT,
  `imgid_id` int(11) NOT NULL,
  `usrid_id` int(11) NOT NULL,
  PRIMARY KEY (`favoritesId`) USING BTREE,
  INDEX `favorites_imgid_id_7299b963_fk_yogaImage_imgid`(`imgid_id`) USING BTREE,
  INDEX `favorites_usrid_id_ba15ae55_fk_user_usrid`(`usrid_id`) USING BTREE,
  CONSTRAINT `favorites_imgid_id_7299b963_fk_yogaImage_imgid` FOREIGN KEY (`imgid_id`) REFERENCES `yogaimage` (`imgid`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `favorites_usrid_id_ba15ae55_fk_user_usrid` FOREIGN KEY (`usrid_id`) REFERENCES `user` (`usrid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 27 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of favorites
-- ----------------------------
INSERT INTO `favorites` VALUES (0, 4, 1);
INSERT INTO `favorites` VALUES (4, 7, 1);
INSERT INTO `favorites` VALUES (5, 5, 1);
INSERT INTO `favorites` VALUES (6, 3, 3);
INSERT INTO `favorites` VALUES (7, 2, 4);
INSERT INTO `favorites` VALUES (10, 10, 5);
INSERT INTO `favorites` VALUES (11, 9, 5);
INSERT INTO `favorites` VALUES (12, 14, 7);
INSERT INTO `favorites` VALUES (13, 11, 7);
INSERT INTO `favorites` VALUES (14, 15, 8);
INSERT INTO `favorites` VALUES (17, 1, 2);
INSERT INTO `favorites` VALUES (20, 4, 2);
INSERT INTO `favorites` VALUES (21, 5, 2);
INSERT INTO `favorites` VALUES (23, 17, 2);
INSERT INTO `favorites` VALUES (24, 19, 2);
INSERT INTO `favorites` VALUES (26, 8, 2);

-- ----------------------------
-- Table structure for result
-- ----------------------------
DROP TABLE IF EXISTS `result`;
CREATE TABLE `result`  (
  `resultId` int(11) NOT NULL AUTO_INCREMENT,
  `uploadImg` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `compareImg` varchar(48) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `compareTime` date NOT NULL,
  `imgid_id` int(11) NOT NULL,
  PRIMARY KEY (`resultId`) USING BTREE,
  INDEX `result_imgid_id_3a6b9718_fk_yogaImage_imgid`(`imgid_id`) USING BTREE,
  CONSTRAINT `result_imgid_id_3a6b9718_fk_yogaImage_imgid` FOREIGN KEY (`imgid_id`) REFERENCES `yogaimage` (`imgid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 36 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of result
-- ----------------------------
INSERT INTO `result` VALUES (4, 'upload/wx16f1030d1e971035.o6zAJs8R4Ot4IuytVtjKLaWu67aE.e0FNYsqdveBRabf08d3ceeaf4fc4ece54_oMrjjA7.jpg', 'result/wx16f1030d1e971035.o6zAJs8R4Ot4IuytVtjKLa', 'some difference', '2020-05-06', 1);
INSERT INTO `result` VALUES (5, 'upload/wx16f1030d1e971035.o6zAJs8R4Ot4IuytVtjKLaWu67aE.PKrydnsuSkT3bc8bea18f623cac1e91b0_yYO2mBi.png', 'result/wx16f1030d1e971035.o6zAJs8R4Ot4IuytVtjKLa', 'some difference', '2020-05-07', 7);
INSERT INTO `result` VALUES (29, 'upload/wx16f1030d1e971035.o6zAJs8R4Ot4IuytVtjKLaWu67aE.XMgBWIqnxx478d3c61c3239ab94d57215_25JMkym.png', 'result/yoga.jpg', 'Exercise could be improved:Exercise string not recognized.', '2020-05-07', 21);
INSERT INTO `result` VALUES (30, 'upload/wx16f1030d1e971035.o6zAJs8R4Ot4IuytVtjKLaWu67aE.YO5xfN44tx2jb7d74df3fae51b47b45ba_RtzQ6Yy.png', 'result/buttocks.jpg', 'Exercise could be improved:Exercise string not recognized.', '2020-05-07', 1);
INSERT INTO `result` VALUES (34, 'upload/wx16f1030d1e971035.o6zAJs8R4Ot4IuytVtjKLaWu67aE.8K8uNUlMCjD4b7d74df3fae51b47b45ba_qKGPiCI.png', 'result/half_moon1.jpg', 'Exercise could be improved:Your legs may not be straight. Maybe you can do as many warm-up exercises or leg exercises as you can, but be careful not to strain your legs.\n', '2020-05-07', 20);
INSERT INTO `result` VALUES (35, 'upload/wx16f1030d1e971035.o6zAJs8R4Ot4IuytVtjKLaWu67aE.ryHleH88CQ0A04940aff1b85d9ca3c807_wKArqAP.jpg', 'result/boat.jpg', 'Exercise could be improved:Exercise string not recognized.', '2020-05-07', 8);

-- ----------------------------
-- Table structure for studyrecord
-- ----------------------------
DROP TABLE IF EXISTS `studyrecord`;
CREATE TABLE `studyrecord`  (
  `studyRecordId` int(11) NOT NULL AUTO_INCREMENT,
  `resultid_id` int(11) NOT NULL,
  `usrid_id` int(11) NOT NULL,
  PRIMARY KEY (`studyRecordId`) USING BTREE,
  INDEX `studyRecord_resultid_id_b6d3ccbe_fk_result_resultId`(`resultid_id`) USING BTREE,
  INDEX `studyRecord_usrid_id_eb2d7afa_fk_user_usrid`(`usrid_id`) USING BTREE,
  CONSTRAINT `studyRecord_resultid_id_b6d3ccbe_fk_result_resultId` FOREIGN KEY (`resultid_id`) REFERENCES `result` (`resultId`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `studyRecord_usrid_id_eb2d7afa_fk_user_usrid` FOREIGN KEY (`usrid_id`) REFERENCES `user` (`usrid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 12 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of studyrecord
-- ----------------------------
INSERT INTO `studyrecord` VALUES (5, 30, 1);
INSERT INTO `studyrecord` VALUES (6, 29, 1);
INSERT INTO `studyrecord` VALUES (10, 34, 2);
INSERT INTO `studyrecord` VALUES (11, 35, 2);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `usrid` int(11) NOT NULL AUTO_INCREMENT,
  `nickname` varchar(48) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `avatarUrl` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `city` varchar(48) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `country` varchar(48) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `province` varchar(48) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` int(11) NOT NULL,
  `language` varchar(48) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `lastLoginTime` date NOT NULL,
  PRIMARY KEY (`usrid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'yy', 'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJfB1ibeMtSmJsQWOFuicG2G9gDDmH0syly1BpRqhm0mI7OSKK2aicibia5seyNsZYoURaA3RYUwUcE8fg/132', '', 'China', '', 2, 'zh_CN', '2020-05-06');
INSERT INTO `user` VALUES (2, '杨非軟', 'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJfB1ibeMtSmJsQWOFuicG2G9gDDmH0syly1BpRqhm0mI7OSKK2aicibia5seyNsZYoURaA3RYUwUcE8fg/132', '', 'China', '', 2, 'zh_CN', '2020-05-06');
INSERT INTO `user` VALUES (3, 'hhh', 'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJfB1ibeMtSmJsQWOFuicG2G9gDDmH0syly1BpRqhm0mI7OSKK2aicibia5seyNsZYoURaA3RYUwUcE8fg/132', '', 'China', '', 2, 'zh_CN', '2020-05-01');
INSERT INTO `user` VALUES (4, 'cccc', 'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJfB1ibeMtSmJsQWOFuicG2G9gDDmH0syly1BpRqhm0mI7OSKK2aicibia5seyNsZYoURaA3RYUwUcE8fg/132', '', 'China', '', 2, 'zh_CN', '2020-05-01');
INSERT INTO `user` VALUES (5, 'auser', 'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJfB1ibeMtSmJsQWOFuicG2G9gDDmH0syly1BpRqhm0mI7OSKK2aicibia5seyNsZYoURaA3RYUwUcE8fg/132', '', 'China', '', 1, 'zh_CN', '2020-05-03');
INSERT INTO `user` VALUES (6, 'bbbbb', 'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJfB1ibeMtSmJsQWOFuicG2G9gDDmH0syly1BpRqhm0mI7OSKK2aicibia5seyNsZYoURaA3RYUwUcE8fg/132', '', 'China', '', 2, 'zh_CN', '2020-05-04');
INSERT INTO `user` VALUES (7, 'ooooowww', 'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJfB1ibeMtSmJsQWOFuicG2G9gDDmH0syly1BpRqhm0mI7OSKK2aicibia5seyNsZYoURaA3RYUwUcE8fg/132', '', 'China', '', 2, 'zh_CN', '2020-05-04');
INSERT INTO `user` VALUES (8, 'kkkk', 'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJfB1ibeMtSmJsQWOFuicG2G9gDDmH0syly1BpRqhm0mI7OSKK2aicibia5seyNsZYoURaA3RYUwUcE8fg/132', '', 'China', '', 1, 'zh_CN', '2020-05-04');
INSERT INTO `user` VALUES (9, 'pppp', 'https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTJfB1ibeMtSmJsQWOFuicG2G9gDDmH0syly1BpRqhm0mI7OSKK2aicibia5seyNsZYoURaA3RYUwUcE8fg/132', '', 'China', '', 2, 'zh_CN', '2020-05-04');

-- ----------------------------
-- Table structure for yogaimage
-- ----------------------------
DROP TABLE IF EXISTS `yogaimage`;
CREATE TABLE `yogaimage`  (
  `imgid` int(11) NOT NULL AUTO_INCREMENT,
  `yogaName` varchar(48) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `level` int(11) NOT NULL,
  `imgDescription` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `image` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`imgid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of yogaimage
-- ----------------------------
INSERT INTO `yogaimage` VALUES (1, 'buttocks', 1, 'buttocks', 'yoga/buttocks.jpg');
INSERT INTO `yogaimage` VALUES (2, 'door', 1, 'door', 'yoga/door.jpg');
INSERT INTO `yogaimage` VALUES (3, 'down_dog', 1, 'down_dog', 'yoga/down_dog.jpg');
INSERT INTO `yogaimage` VALUES (4, 'crocodile', 1, 'crocodile', 'yoga/crocodile.jpg');
INSERT INTO `yogaimage` VALUES (5, 'forward _bending', 1, 'forward _bending', 'yoga/forward _bending.jpg');
INSERT INTO `yogaimage` VALUES (7, 'monkey', 3, 'monkey', 'yoga/monkey.jpg');
INSERT INTO `yogaimage` VALUES (8, 'boat', 3, 'boat', 'yoga/boat.jpg');
INSERT INTO `yogaimage` VALUES (9, 'wheel', 3, 'wheel', 'yoga/wheel.jpg');
INSERT INTO `yogaimage` VALUES (10, 'desk', 3, 'desk', 'yoga/desk.jpg');
INSERT INTO `yogaimage` VALUES (11, 'dance', 3, 'dance', 'yoga/dance.jpg');
INSERT INTO `yogaimage` VALUES (14, 'up_dog', 3, 'updog', 'yoga/up_dog.jpg');
INSERT INTO `yogaimage` VALUES (15, 'warrior', 3, 'warrior', 'yoga/warrior_back.jpg');
INSERT INTO `yogaimage` VALUES (17, 'walkingstick', 2, 'walkingstick', 'yoga/walking_stick.jpg');
INSERT INTO `yogaimage` VALUES (18, 'treebywind', 2, 'treebywind', 'yoga/treebywind.jpg');
INSERT INTO `yogaimage` VALUES (19, 'mountain', 2, 'mountain', 'yoga/mountain.jpg');
INSERT INTO `yogaimage` VALUES (20, 'half_moon1', 2, 'halfmoon', 'yoga/half_moon1_RhPVOMw.png');
INSERT INTO `yogaimage` VALUES (21, 'yoga', 2, 'yoga', 'yoga/yoga.png');
INSERT INTO `yogaimage` VALUES (22, 'upside', 3, 'upside', 'yoga/upside_angle.jpg');
INSERT INTO `yogaimage` VALUES (23, 'vblance', 3, 'VB', 'yoga/Vbalance.jpg');
INSERT INTO `yogaimage` VALUES (24, 'aingle', 3, 'single', 'yoga/single_bridge.jpg');

SET FOREIGN_KEY_CHECKS = 1;
