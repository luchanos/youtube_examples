from sanic import Sanic, text
from sanic_openapi import openapi2_blueprint


# DB = {
#     'DB_HOST': 'localhost',
#     'DB_PORT': 5432,
#     'DB_NAME': 'postgres',
#     'DB_USER': 'nnsviridov',
#     'DB_PASS': 'dbuser'
# }

app = Sanic("my application")
app.blueprint(openapi2_blueprint)


@app.on_request
async def increment_foo(request):
    if not hasattr(request.conn_info.ctx, "foo"):
        request.conn_info.ctx.foo = 0
    request.conn_info.ctx.foo += 1


@app.get("/")
async def count_foo(request):
    return text(f"request.conn_info.ctx.foo={request.conn_info.ctx.foo}")


if __name__ == '__main__':
    app.run()
