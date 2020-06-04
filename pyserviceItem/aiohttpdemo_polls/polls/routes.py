from views import index

import os
import aiohttp_jinja2
import jinja2

def setup_routes(app):
    app.router.add_route('GET', '/', index)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))      # 项目路径
STATIC_DIR = os.path.join(BASE_DIR, 'static')       # 静态文件路径
TEMPLATE_DIR = os.path.join(BASE_DIR, 'template')   # 模版HTML路径

def setup_static_routes(app):
    app.router.add_static('/static/', path=STATIC_DIR, name='static')


def setup_template_routes(app):
    aiohttp_jinja2.setup(app, filters={'choice_split': choice_split}, loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


def choice_split(choices):
    for i in choices.split(','):
        single = i.split('|')
        yield single