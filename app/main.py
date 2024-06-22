import uvicorn
from fastapi import FastAPI

# Import all the Routers
app = FastAPI(root_path='/api/v1')

from routers.systemManager import (systemManager)
from routers.user import (user)
from fastapi.middleware.cors import CORSMiddleware

app.include_router(systemManager, prefix="/systemManager", tags=["Manager for our System"])
app.include_router(user, prefix='/register', tags=["Register function for our system"])

# 这里添加 CORS 中间件，允许所有来源（在生产环境中应更加严格）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域名，对于生产环境应该更加具体
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法，包括 OPTIONS
    allow_headers=["*"],  # 允许所有头部
)

# @app.get("/api/v1")
# def read_root():
#     return {"Hello": "World"}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


