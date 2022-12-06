'''
可以运行主函数启动应用,也可以运行run_app.py将程序挂在后台运行(终端退出后程序不会退出)
'''
from fastapi import FastAPI
from DianDongChe.Services import \
    HardhareControlService,\
    DataAddService,\
    DataQueryService,\
    PeopleService,\
    BaoJingService
from drivers.db_connection import Base,engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

import threading
from fastapi.staticfiles import StaticFiles
app = FastAPI(docs_url='/')

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc/bundles/redoc.standalone.js",
    )


Base.metadata.create_all(engine)
app.include_router(HardhareControlService.router)
app.include_router(DataAddService.router)
app.include_router(DataQueryService.router)
app.include_router(PeopleService.router)
app.include_router(BaoJingService.router)

#懒得记ip了,全放行
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from DianDongChe.mqtt.Transmit.Receive import run_mqtt
#线程的run方法是阻塞的,start是不阻塞的,妈的之前打错了卡住迷惑了好久s
threading.Thread(target=run_mqtt).start()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app,host='0.0.0.0',port=80)
    # pass












