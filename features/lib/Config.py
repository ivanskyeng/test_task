from ConfigParser import *
import os

parser = SafeConfigParser()


class Config:
  def get_config(self,filename,section,key):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    # path to parent dir of this file  /test_task/features/
    parser.read(base_dir + '/' + filename)
    config_value = parser.get(section,key)
    return config_value

