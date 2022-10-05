import json


class ReadConfig:

    def readDBJsonConfig(self):
        with open("promotion-connect-config.json", 'r') as json_file:
            config = json.load(json_file)
        print(config)
        server = config['db_info']['host']
        print(server)


if '__main__' == __name__:
    config = ReadConfig();
    config.readDBJsonConfig()
