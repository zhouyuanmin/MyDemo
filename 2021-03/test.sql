-- 浏览首页 HOME_PAGE study_dws_home_page
-- 选择课程 CLICK_COURSE study_dws_click_course
-- 立即报名 REGISTER_NOW study_dws_register_now
-- 立即支付 CLICK_PAY study_dws_click_pay
-- 支付成功 PAY_SUCCESS study_dws_pay_success
-- 继续支付 SECOND_PAY study_dws_second_pay
CREATE TABLE `study_dws_home_page` (
	`batch_code` VARCHAR ( 255 ) COLLATE utf8mb4_bin NOT NULL COMMENT '批次编号',
	`nickname` VARCHAR ( 64 ) DEFAULT NULL COMMENT '昵称',
	`avatar` VARCHAR ( 1024 ) DEFAULT NULL COMMENT '用户头像url',
	`userid` INT ( 11 ) DEFAULT NULL COMMENT '用户id',
	`create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY ( `batch_code` ) USING BTREE 
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4 ROW_FORMAT = DYNAMIC COMMENT = '浏览首页';
CREATE TABLE `study_dws_click_course` (
	`batch_code` VARCHAR ( 255 ) COLLATE utf8mb4_bin NOT NULL COMMENT '批次编号',
	`nickname` VARCHAR ( 64 ) DEFAULT NULL COMMENT '昵称',
	`avatar` VARCHAR ( 1024 ) DEFAULT NULL COMMENT '用户头像url',
	`user_id` INT ( 11 ) DEFAULT NULL COMMENT '用户id',
	`goods_id` INT ( 11 ) DEFAULT NULL COMMENT '课程id',
	`create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY ( `batch_code` ) USING BTREE
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4 ROW_FORMAT = DYNAMIC COMMENT = '选择课程';
CREATE TABLE `study_dws_register_now` (
	`batch_code` VARCHAR ( 255 ) COLLATE utf8mb4_bin NOT NULL COMMENT '批次编号',
	`nickname` VARCHAR ( 64 ) DEFAULT NULL COMMENT '昵称',
	`avatar` VARCHAR ( 1024 ) DEFAULT NULL COMMENT '用户头像url',
	`user_id` INT ( 11 ) DEFAULT NULL COMMENT '用户id',
	`goods_id` INT ( 11 ) DEFAULT NULL COMMENT '课程id',
	`create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY ( `batch_code` ) USING BTREE
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4 ROW_FORMAT = DYNAMIC COMMENT = '立即报名';
CREATE TABLE `study_dws_click_pay` (
	`batch_code` VARCHAR ( 255 ) COLLATE utf8mb4_bin NOT NULL COMMENT '批次编号',
	`nickname` VARCHAR ( 64 ) DEFAULT NULL COMMENT '昵称',
	`avatar` VARCHAR ( 1024 ) DEFAULT NULL COMMENT '用户头像url',
	`user_id` INT ( 11 ) DEFAULT NULL COMMENT '用户id',
	`goods_id` INT ( 11 ) DEFAULT NULL COMMENT '课程id',
	`create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY ( `batch_code` ) USING BTREE
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4 ROW_FORMAT = DYNAMIC COMMENT = '立即支付';
CREATE TABLE `study_dws_pay_success` (
	`batch_code` VARCHAR ( 255 ) COLLATE utf8mb4_bin NOT NULL COMMENT '批次编号',
	`nickname` VARCHAR ( 64 ) DEFAULT NULL COMMENT '昵称',
	`avatar` VARCHAR ( 1024 ) DEFAULT NULL COMMENT '用户头像url',
	`user_id` INT ( 11 ) DEFAULT NULL COMMENT '用户id',
	`goods_id` INT ( 11 ) DEFAULT NULL COMMENT '课程id',
	`create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`order_no` VARCHAR ( 255 ) COLLATE utf8mb4_bin NOT NULL COMMENT '订单编号',
	PRIMARY KEY ( `batch_code` ) USING BTREE
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4 ROW_FORMAT = DYNAMIC COMMENT = '支付成功';
CREATE TABLE `study_dws_second_pay` (
	`batch_code` VARCHAR ( 255 ) COLLATE utf8mb4_bin NOT NULL COMMENT '批次编号',
	`nickname` VARCHAR ( 64 ) DEFAULT NULL COMMENT '昵称',
	`avatar` VARCHAR ( 1024 ) DEFAULT NULL COMMENT '用户头像url',
	`user_id` INT ( 11 ) DEFAULT NULL COMMENT '用户id',
	`goods_id` INT ( 11 ) DEFAULT NULL COMMENT '课程id',
	`create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
	`order_no` VARCHAR ( 255 ) COLLATE utf8mb4_bin NOT NULL COMMENT '订单编号',
PRIMARY KEY ( `batch_code` ) USING BTREE
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4 ROW_FORMAT = DYNAMIC COMMENT = '继续支付';