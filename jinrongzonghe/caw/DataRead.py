'''
读写文件的类
'''
import configparser
import os
import yaml
class DataRead:
        def get_project_path(self):

            current_file_path=os.path.realpath(__file__)
            dir_name=os.path.dirname(current_file_path)
            dir_name=os.path.dirname(dir_name)
            dir_name = os.path.dirname(dir_name)
            return  dir_name+"\\"

        def read_ini(self,file_path,key):
            real_file_path=self.get_project_path()+file_path
            print(real_file_path)
            config= configparser.ConfigParser()
            config.read(real_file_path)
            value=config.get('env', key)
            return value

        def read_yaml(self,file_path):
            real_file_path=self.get_project_path()+file_path
            with open(real_file_path,"r",encoding='utf-8')as f:
                file_content = f.read()

            content = yaml.load(file_content,Loader=yaml.FullLoader)
            return content


         #
         # config = configparser.ConfigParser()
         # config.read(file_path)
         # value = config.get("env",key)
         # return value


if __name__ == '__main__':
    value=DataRead().read_ini(r"jinrongzonghe/data_env\env.ini","url")
    print(value)
    print(DataRead().get_project_path())
    print(DataRead().read_yaml(r"jinrongzonghe/data_case/register_fail(1).yaml"))