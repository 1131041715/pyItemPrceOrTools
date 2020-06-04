# load config from yaml file in current dir

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))      # 项目路径
STATIC_DIR = os.path.join(BASE_DIR, 'static')       # 静态文件路径
TEMPLATE_DIR = os.path.join(BASE_DIR, 'template')   # 模版HTML路径