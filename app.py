import responder


api = responder.API()


@api.route('/')
async def hello_world(req, resp):
    resp.content = api.template('hello.html')


if __name__ == '__main__':
    api.run()
