import contextlib
import logging
import random
import time
import uuid

import pymysql

formatStr11 = '%(asctime)s - %(name)s - process_id: %(process)s - thread_id: %(thread)d - %(filename)s - %(levelname)s - %(lineno)d: %(message)s'
logging.basicConfig(format=formatStr11,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)
logger = logging.getLogger()
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logging.Formatter(formatStr11))
logger.addHandler(streamHandler)


class initData():
    def __init__(self, host, port, user, passwd, db, charset='utf8mb4'):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset

    # 定义上下文管理器，连接后自动关闭连接
    @contextlib.contextmanager
    def connect(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd,
                                    charset=self.charset)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    @contextlib.contextmanager
    # 定义上下文管理器，连接后自动关闭连接
    def getMySqlConnection(self):
        self.conn = pymysql.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd,
                                    charset=self.charset)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            yield self.cursor
            self.conn.commit()
        finally:
            self.close()

    def close(self):
        print('关闭流...')
        self.cursor.close()
        self.conn.close()

    def get_all(self, sql):
        res = ()
        try:
            self.connect()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.close()
        return res

    def insert(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self.close()

    def update(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self.close()

    def delete(self, sql):
        try:
            self.connect()
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self.close()

    def queryAll(self, sql, param):
        with self.getMySqlConnection() as cur:
            cur.execute(sql, param)
            data = cur.fetchall()
            return data

    def execute(self, sql):
        try:
            self.connect()
            data = self.cursor.execute(sql)
            self.conn.commit()
            return data
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            self.close()

    def batchInsert(self, sql, dataList):
        try:
            self.connect()
            data = self.cursor.executemany(sql, dataList)
            self.conn.commit()
            return data
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            self.close()

    @classmethod
    def create_activity_info_table(cls):
        create_sql = """
             create table if not exists `t_activity_info_m`  (
              `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
              `name` varchar(50) NOT NULL COMMENT '活动名称',
              `theme` varchar(50) DEFAULT NULL COMMENT '活动主题',
              `code` varchar(50) NOT NULL COMMENT '编码',
              `task_code` varchar(50) NOT NULL COMMENT '任务编码',
              `start_time` datetime NOT NULL COMMENT '開始時間',
              `end_time` datetime NOT NULL COMMENT '结束时间',
              `status` varchar(20) NOT NULL COMMENT '状态(approval-待审批, waitExecute-待执行, execute-执行中,finished-已完成)',
              `address` varchar(500) DEFAULT NULL COMMENT '地址',
              `location` geometry DEFAULT NULL COMMENT '经纬度',
              `remark` text DEFAULT NULL COMMENT '备注',
              `promotion_code` varchar(50) DEFAULT NULL COMMENT '携带促销预热编码',
              `city_code` varchar(50) DEFAULT NULL COMMENT '地市编码',
              `district_code` varchar(50) DEFAULT NULL COMMENT '区县编码',
              `area_code` varchar(50) DEFAULT NULL COMMENT '网格编码',
              `area_name` varchar(50) DEFAULT NULL COMMENT '网格名称',
              `source` varchar(50) NOT NULL COMMENT '来源(stall-摆摊, sandbox-沙箱)',
              `create_way` varchar(10) NOT NULL COMMENT '创建来源(1-手机, 2-web单个新增,3-pc导入)',
              `create_date` datetime NOT NULL COMMENT '创建时间',
              `create_by` varchar(50) NOT NULL COMMENT '创建人',
              `update_date` datetime NOT NULL COMMENT '修改时间',
              `update_by` varchar(50) NOT NULL COMMENT '修改人',
              PRIMARY KEY (`id`),
              UNIQUE KEY `uqx_activity_info_m_code` (`code`),
              KEY `inx_activity_info_status` (`status`),
              KEY `inx_activity_info_area_code` (`area_code`),
              KEY `inx_activity_info_city_code` (`city_code`),
              KEY `inx_activity_info_district_code` (`district_code`),
              KEY `inx_activity_info_create_by` (`create_by`)
            ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='活动信息主表';
            """
        logging.debug('create table sql: %s', create_sql)
        logger.info('创建 活动主表: %s', initDataObj.execute(create_sql))

    @classmethod
    def create_activity_extent_table(cls):
        create_sql = """
             create table if not exists `t_activity_info_e`  (
              `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
              `activity_code` varchar(50) NOT NULL COMMENT '活动编码',
              `setup_start_time` datetime DEFAULT NULL COMMENT '开摊时间',
              `setup_end_time` datetime DEFAULT NULL COMMENT '结摊时间',
              `activity_type` varchar(50) NOT NULL COMMENT '促销类型(sqcx,jtcx)',
              `audit_level` varchar(50) DEFAULT NULL COMMENT '稽核层级(level0,level1,level2)',
              `resource_type` varchar(50) DEFAULT NULL COMMENT '资源类型(uptown, enterprise)',
              `resource_code` varchar(500) DEFAULT NULL COMMENT '资源编码',
              `create_date` datetime NOT NULL COMMENT '创建时间',
              `create_by` varchar(50) NOT NULL COMMENT '创建人',
              `update_date` datetime NOT NULL COMMENT '修改时间',
              `update_by` varchar(50) NOT NULL COMMENT '修改人',
              PRIMARY KEY (`id`),
              UNIQUE KEY `uqx_activity_info_e_activity_code` (`activity_code`),
              KEY `inx_activity_info_e_create_by` (`create_by`)
            ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='活动信息扩展表';
            """
        logging.debug('create table sql: %s', create_sql)
        logger.info('创建 活动信息扩展表: %s', initDataObj.execute(create_sql))

    @classmethod
    def create_activity_relation_table(cls):
        create_sql = """
                create table if not exists `t_activity_relation_m`  (
                  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
                  `activity_code` varchar(50) NOT NULL COMMENT '活动编码',
                  `organization_id` varchar(50) DEFAULT NULL COMMENT '组织id',
                  `organization_code` varchar(50) DEFAULT NULL COMMENT '组织区域编码',
                  `organization_level` int(10) DEFAULT NULL COMMENT '组织区域层级',
                  `organization_name` varchar(50) DEFAULT NULL COMMENT '组织名称',
                  `participant_id` varchar(50) NOT NULL COMMENT '参与人useId',
                  `participant_code` varchar(50) NOT NULL COMMENT '参与人工号',
                  `participant_name` varchar(50) NOT NULL COMMENT '参与人姓名',
                  `charge` bit(1) NOT NULL COMMENT '是否活动负责人(0-否,1-是)',
                  `create_date` datetime NOT NULL COMMENT '创建时间',
                  `create_by` varchar(50) NOT NULL COMMENT '创建人',
                  `update_date` datetime NOT NULL COMMENT '修改时间',
                  `update_by` varchar(50) NOT NULL COMMENT '修改人',
                 PRIMARY KEY (`id`),
                 KEY `inx_t_activity_relation_m_create_by` (`create_by`)
               ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='活动参与人表';
               """
        logging.debug('create table sql: %s', create_sql)
        logger.info('创建 活动参与人表: %s', initDataObj.execute(create_sql))

    @classmethod
    def create_activity_flow_table(cls):
        create_sql = """
                create table if not exists `t_activity_flow_m`  (
                  `id` bigint(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
                  `activity_code` varchar(50) NOT NULL COMMENT '活动编码',
                  `flow_info_id` varchar(50) NOT NULL COMMENT '流程信息ID',
                  `flow_version_id` varchar(50) NOT NULL COMMENT '流程版本ID',
                  `current_node` varchar(50) NOT NULL COMMENT '当前节点名称',
                  `node1_name` varchar(50) DEFAULT NULL COMMENT '一级节点名称',
                  `node2_name` varchar(50) DEFAULT NULL COMMENT '二级节点名称',
                  `node1_approve_user_id` text DEFAULT NULL COMMENT '一级审批人userid',
                  `node2_approve_user_id` text DEFAULT NULL COMMENT '二级审批人userid',
                  `create_date` datetime NOT NULL COMMENT '创建时间',
                  `create_by` varchar(50) NOT NULL COMMENT '创建人',
                  `update_date` datetime NOT NULL COMMENT '修改时间',
                  `update_by` varchar(50) NOT NULL COMMENT '修改人',
                 PRIMARY KEY (`id`),
                 UNIQUE KEY `uqx_activity_flow_m_activity_code` (`activity_code`),
                 KEY `inx_activity_flow_m_create_by` (`create_by`)
               ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='活动审批信息表';
               """
        logging.debug('create table sql: %s', create_sql)
        logger.info('创建 活动审批信息表: %s', initDataObj.execute(create_sql))


if __name__ == '__main__':
    initDataObj = initData('127.0.0.1', 5306, 'root', 'root', "promotion")
    # 初始化表
    # 活动信息主表
    initDataObj.create_activity_info_table()
    # 活动信息扩展表
    initDataObj.create_activity_extent_table()
    # 活动关系人表
    initDataObj.create_activity_relation_table()
    # 活动审批信息表
    initDataObj.create_activity_flow_table()

    insert_baseinfo_sql = 'insert into `t_activity_info_m`(name,code,task_code,start_time,end_time,address,status,source,create_way,area_code,area_name,create_date,create_by,update_date,update_by) value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    insert_baseinfo_extend_sql = 'insert into `t_activity_info_e`(activity_code,activity_type,audit_level, create_date,create_by,update_date,update_by) value (%s,%s,%s,%s,%s,%s,%s)'

    insert_t_activity_relation_m_sql = 'insert into `t_activity_relation_m`(activity_code,participant_id,participant_code,participant_name, charge,create_date,create_by,update_date,update_by) value (%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    status_list = ['approval', 'waitExecute', 'execute', 'finish']
    pageIndex = 100
    pageSize = 10000
    for timeParam in range(pageIndex):
        logger.info('insert %s time', timeParam + 1)
        # 插入数据
        baseinfo_insertData = list()
        baseinfo_extend_insertData = list()
        activity_relation_m_insertData = list()
        for index in range(pageSize):
            # 活动编码
            code = str(uuid.uuid3(uuid.NAMESPACE_DNS, str(timeParam * pageSize + index + 1)))
            # code = str(uuid.uuid1())
            # (pageIndex -1)*pageSize + (index+1)
            # code = str(timeParam * pageSize + index + 1)
            baseinfo_insertData.append(
                ("测试活动", code,
                 code, time.localtime(),
                 time.localtime(),
                 "广东省东莞市",
                 # "ST_GeomFromText({0}, 4326)".format("\'POINT(123.123445 27.456128)\'"),
                 random.sample(status_list, 1)[0], "stall",
                 "1", "DG", "东莞", time.localtime(), "system", time.localtime(), "system"))
            baseinfo_extend_insertData.append(
                (code,
                 "sqcx", "level0",
                 time.localtime(), "system", time.localtime(), "system"))
            for kk in range(3):
                temIndex = str(kk + 1)
                activity_relation_m_insertData.append(
                    (code,
                     code + temIndex, "zhenglirun" + temIndex, "zhenglirun" + temIndex,
                     False,
                     time.localtime(), "system", time.localtime(), "system"))
        logger.debug('baseinfo_insertData: %s', baseinfo_insertData)
        initDataObj.batchInsert(insert_baseinfo_sql, baseinfo_insertData)
        logger.info('baseinfo_insertData size: %s', len(baseinfo_insertData))

        initDataObj.batchInsert(insert_baseinfo_extend_sql, baseinfo_extend_insertData)
        logger.info('baseinfo_extend_insertData size: %s', len(baseinfo_extend_insertData))

        initDataObj.batchInsert(insert_t_activity_relation_m_sql, activity_relation_m_insertData)
        logger.info('activity_relation_m_insertData size: %s', len(activity_relation_m_insertData))
