#!/usr/bin/env python
# coding:utf-8
import json
import sys

import pandas as pd
import pymysql
from pandas import Timestamp
from sqlalchemy import create_engine


class ParseSqlManager:

    def __init__(self, json_file):
        config = self.readDBJsonConfig(json_file)
        print('read config json: ', config)
        self.host = config['db_info']['host']
        self.port = config['db_info']['port']
        self.username = config['db_info']['user']
        self.password = config['db_info']['password']
        self.dcp_framework_dbName = config['db_info']['dcp_framework-dbName']
        self.save_path = config['save_path']
        self.file_name = config['file_name']
        self.config = config

    def __str__(self):
        print(self.host, self.port, self.username, self.password, self.dcp_framework_dbName)

    def readDBJsonConfig(self, jsonFile):
        with open(jsonFile, 'r', encoding='utf-8') as json_file:
            config = json.load(json_file)
        # global host;
        # host = config['db_info']['host']
        #
        # global port;
        # port = config['db_info']['port']
        #
        # global username;
        # username = config['db_info']['user']
        #
        # global password;
        # password = config['db_info']['password']
        #
        # global dcp_framework_dbName;
        # dcp_framework_dbName = config['db_info']['dcp_framework-dbName']
        return config

    def getDBConnection(self, dbName):
        sql_connection = pymysql.connect(host=self.host, user=self.username, password=self.password, db=dbName,
                                         port=self.port,
                                         autocommit=False, charset='utf8mb4')
        return sql_connection

    def getMysqlEngine(self, dbName):
        # db_URI = "mysql+driver://数据库登陆名:对应的密码@IP:端口号/数据库名字"
        db_url = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(self.username, self.password, self.host,
                                                                           self.port, dbName)
        print("db url : %s" % db_url)
        engine = create_engine(db_url)
        return engine

    def executeQuery(self, dBName, sql):
        # df_sql = pd.read_sql(sql, self.getDBConnection(dBName))
        try:
            DataFrame_sql = pd.read_sql(sql, self.getMysqlEngine(dBName))
        except pymysql.err.ProgrammingError as e:
            print('Error is : %s' % str(e))
            sys.exit()
        # print(DataFrame_sql)
        # print(df_sql.head())
        return DataFrame_sql

    def initInsertSql(self, list_data):
        for i in list_data:
            print(list_data[i])

    def dealColumnStr(self, column_list):
        print("dealColumnStr  size:", len(column_list))
        column_str = ''
        for i in range(len(column_list)):
            if i == len(column_list) - 1:
                column_str += self.joinColumnComma(column_list[i])
            else:
                column_str += self.joinColumnComma(column_list[i]) + ','
        return column_str

    def dealColumnValueStr(self, column_list):
        # print("dealColumnValueStr  size:", len(column_list))
        column_str = ''
        for i in range(len(column_list)):
            if isinstance(column_list[i], Timestamp):
                data = str(column_list[i])
            elif isinstance(column_list[i], int):
                data = str(column_list[i])
            else:
                data = column_list[i]
                # data = str(column_list[i]) if isinstance(column_list[i], Timestamp) else column_list[i]
            if i == len(column_list) - 1:
                column_str += self.joinComma(data)
            else:
                column_str += self.joinComma(data) + ','
        return column_str

    def joinComma(self, sstr):
        return '\'' + sstr + '\''

    def joinColumnComma(self, sstr):
        return '`' + sstr + '`'


if __name__ == '__main__':
    manager = ParseSqlManager("promotion-connect-config.json")
    sys_config = manager.config
    stall_module = manager.config['stall']

    for targetTab in stall_module['target-table-list']:
        print(targetTab)
        apiCodeList = targetTab['api-code-list']
        # 列： client_code, tenant_code, datasource_code, code, name, sql, create_by, create_date, modify_by, modify_date
        # column_str = ','.join(targetTab['column_code'])
        column_str = ''
        column_list = targetTab['column_code']
        column_str = manager.dealColumnStr(column_list)

        api_code_str = ''
        apiCodeList = targetTab['api-code-list']
        for i in range(len(apiCodeList)):
            if i == len(apiCodeList) - 1:
                api_code_str += manager.joinComma(apiCodeList[i])
            else:
                api_code_str += manager.joinComma(apiCodeList[i]) + ','
        print("api_code_str：", api_code_str)
        print("列：", column_str)
        where_part = targetTab['where_filter'] \
            .replace('@client_code', manager.joinComma(sys_config['@client_code'])).replace('@tenant_code',
                                                                                            manager.joinComma(
                                                                                                sys_config[
                                                                                                    '@tenant_code'])).replace(
            '@stall_datasource_code', manager.joinComma(sys_config['@stall_datasource_code'])).replace('@api-code-list',
                                                                                                       api_code_str)
        sql = 'select {0} from {1} where {2}'.format(column_str, targetTab['table-name'], where_part)
        DataFrame_sql = manager.executeQuery(manager.dcp_framework_dbName, sql)
        # print(DataFrame_sql)
        # print(DataFrame_sql.to_dict())
        # print(DataFrame_sql.to_json())
        print("結果：", DataFrame_sql.values.tolist())
        DataFrame_sql.to_sql(targetTab['table-name'] + "_temp", manager.getMysqlEngine(manager.dcp_framework_dbName),
                             if_exists='replace', index=False)

        # 生成insert語句
        # tar_table = '`' + manager.dcp_framework_dbName + '`' + '.' + '`'
        tar_table = '`{0}`.`{1}`'.format(manager.dcp_framework_dbName, targetTab['table-name'])
        # 转换list
        dataList = DataFrame_sql.values.tolist()
        insert_sql_list = []
        # 生成删除语句
        delete_sql = 'delete from {0} where {1};'.format(tar_table, where_part)
        insert_sql_list.append(delete_sql)
        for index in range(len(dataList)):
            # 转换每行数据
            dataStr = manager.dealColumnValueStr(dataList[index])
            #  'str' object is not callable 不可命名类型为成员变量名称
            insert_sql = 'insert into {0} ({1}) values ({2});'.format(tar_table, column_str, dataStr)
            print(insert_sql)
            insert_sql_list.append(insert_sql)

        # 替换唯一值的：租户编码、终端编码、数据源编码
        # "@client_code": "8959c6aa-26a5-11ed-a331-3c7c3f602b59",
        # "@tenant_code": "7f24f99d-26a5-11ed-a331-3c7c3f602b59",
        # "@business_datasource_code": "dcp_grid",
        # "@stall_datasource_code": "stall-assistant",
        #
        # "@target_client_code": "8959c6aa-26a5-11ed-a331-3c7c3f602b59",
        # "@target_tenant_code": "7f24f99d-26a5-11ed-a331-3c7c3f602b59",
        # "@target_business_datasource_code": "dcp_grid",
        # "@target_stall_datasource_code": "stall-assistant",
        final_insert_sql_list = []
        for data in insert_sql_list:
            data = data.replace(manager.joinComma(sys_config['@client_code']), '@client_code').replace(
                manager.joinComma(sys_config['@tenant_code']),
                '@tenant_code')
            data = data.replace(manager.joinComma(sys_config['@business_datasource_code']),
                                '@business_datasource_code').replace(
                manager.joinComma(sys_config['@stall_datasource_code']),
                '@stall_datasource_code')
            final_insert_sql_list.append(data)

        # 文件名称
        fileName = sys_config['file_name'] + '.sql'
        with open(fileName, "w", encoding='utf-8') as file:
            for sql_str in final_insert_sql_list:
                file.write(sql_str)
                file.write("\r")

    # dataArray = manager.executeQuery('dcp_framework', 'select * from t_api_m')
    # manager.initInsertSql(dataArray)
