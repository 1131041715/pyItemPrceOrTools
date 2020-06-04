from aiohttp import web
from routes import setup_routes ,setup_static_routes ,setup_template_routes

app = web.Application()
setup_routes(app)
setup_static_routes(app)
setup_template_routes(app)
web.run_app(app, host='127.0.0.1', port=8080)

 