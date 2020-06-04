from aiohttp import web
import aiohttp_jinja2

async def index(request):
    # return web.Response(text = 'cloclk.htm')
    return aiohttp_jinja2.render_template('clock.html', request, locals())
    # return {
    #     'template': 'clock.html'
    # }