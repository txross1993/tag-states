from aiohttp import web
from time import sleep



streams = []
def addToStreams(stream_id):
    streams.append(stream_id)

async def theStreams(request):
    return web.Response(text=str(streams))

async def handle(request):
    stream_id = request.match_info.get('id', "Anonymous")
    addToStreams(stream_id)
    return web.Response(text=stream_id)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/stream_{id}', handle),
                web.get('/streams', theStreams)])

web.run_app(app, host='127.0.0.1', port=8080)