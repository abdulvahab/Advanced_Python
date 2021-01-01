from aiohttp import web
from aiohttp.streams import StreamReader
import json
import asyncio
loop = asyncio.get_event_loop()
import nest_asyncio
nest_asyncio.apply()


async def home(request):
    message = json.dumps({"message":"Hello world"})
    return web.Response(text=message)


async def read_all(stream_reader: StreamReader) -> bytes:
    content = list()
    print("running read_all")
    while not stream_reader.is_eof():
        line = await stream_reader.readline()
        print("line is: ", line)
        content.append(line)
    print("end of while loop")
    return b"".join(content)


async def subscribe(request):
    print(request.content)
    response = []
    async for line in request.content:
        print(json.loads(line))
        response.append(line)
    data = b"".join(response)
    request_str = data.decode("utf-8")
        
        
    # data = await read_all(request.content)
    # print(data.decode("utf-8"))
    return web.Response(text=request_str, headers={"Content-Type": "json"})


async def main():
    app = web.Application()
    print(app)
    app.add_routes(
        [
            web.get("/", home),
            web.post("/events", subscribe),
    #             web.get("/events/subscriptions/channels/{uuid}", stream_channel_decorated),
    #             web.get("/predictions", predictions_handler_decorated),
    #             web.get("/test", test_prediction_decorated),
        ]
    )
    await web.run_app(app)

    # app_runner = web.AppRunner(app)
    # await app_runner.setup()
    # site = web.TCPSite(app_runner, host='localhost', port=1786)
    # await site.start()

if __name__ == "__main__":
    asyncio.run(main(), debug=True)
    
# from aiohttp import web

# async def hello(request):
#     return web.Response(text="Hello, world")

# app = web.Application()
# app.add_routes([web.get('/', hello)])
# web.run_app(app)