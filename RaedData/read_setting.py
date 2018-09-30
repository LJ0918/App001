import os
import yaml


class ReadSetting():
    def __init__(self, filename):
        self.filepath = os.getcwd()+os.sep+'DataPool'+os.sep+filename
    def read_setting(self):
        with open(self.filepath,'r',encoding='utf-8') as f:
            return yaml.load(f)