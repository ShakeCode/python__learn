from paramiko import (SSHClient, SFTPClient, AutoAddPolicy)
import argparse

class Args(argparse.ArgumentParser):

    def __init__(self, help_info: str = "remote host login  args"):
        """
        使用 python xx.py -h 查看参数传递帮助
        :param help_info:
        """
        super(Args, self).__init__(description=help_info)

    def __call__(self, *args, **kwargs):
        """
        :param args:
        :param kwargs:
        :return: 返回参数对象,可通过 args.xxx 获取参数
        """
        self.add_argument("--ip", help="remote host ip address")
        self.add_argument("--username", help="SSH login username", default="")
        self.add_argument("--password", help="SSH login password", default="")
        self.add_argument("--port", help="remote host port", default=22)
        return self.parse_args()


class SSH(object):
    def __init__(self, ip_address: str, username: str, password: str, port: int = 22):
        """
        :param ip_address:远程ip地址
        :param username:用户名
        :param password:密码
        :param port:端口号,默认22
        """
        self.ip = ip_address
        self.username = username
        self.password = password
        self.port = port
        self.__client = SSHClient()

    def connect(self) -> None:
        """
        打开连接
        :return:None
        """
        self.__client.set_missing_host_key_policy(AutoAddPolicy())
        self.__client.connect(self.ip, self.port, self.username, self.password)

    def execute(self, command: str) -> None:
        """
        执行命令，stderr未启用
        :param command: windows命令
        :return: None
        """
        std_in, stdout, stderr = self.__client.exec_command(command=command)
        print(stdout.read().decode("utf-8"))

    def upload_file(self, local_file_path: str, remote_file_path: str) -> None:
        """
        打开sftp会话，用于将本地文件上传到远程设备
        :param local_file_path: 本地文件绝对路径
        :param remote_file_path: 远程文件路径:命名方式:path+filename
        :return:
        """
        sftp: SFTPClient = self.__client.open_sftp()
        try:
            sftp.put(localpath=local_file_path, remotepath=remote_file_path)
            print(f"file:{local_file_path} upload success！")
        except Exception as e:
            print(f"upload file file,please check whether the file path is correct!\nerror massage：{e} ")

    def download_file(self, remote_file_path: str, local_save_path) -> None:
        """
        打开sftp会话，用于将远程设备文件拉取到本地
        :param remote_file_path: 远程设备绝对路径
        :param local_save_path: 本地文件保存路径 命名方式:file +filename 注意需要指定文件名，否则报错
        :return:
        """
        sftp: SFTPClient = self.__client.open_sftp()
        try:
            sftp.get(remotepath=remote_file_path, localpath=local_save_path)
            print(f"file:{remote_file_path} download success!")
        except Exception as e:
            print(f"download_file error,please check whether the file path is correct!\nerror massage：{e} ")

    def get_shell(self) -> None:
        """
        获取shell
        :return:
        """
        while True:
            command = input(f"{self.ip}@{self.username}$:")
            if command.__eq__("quit"):
                break
            self.execute(command=command)

    def __del__(self):
        print("Disconnected!")
        self.__client.close()