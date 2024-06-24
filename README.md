# Software-Engineering-backend
The backend of our Software-Engineering homework

content tree:

```
/Software-Engineering-backend
|-- app/                        # 应用主模块       
|   |-- main.py                 # 应用的入口点，包括路由和中间件
|   |-- config.py               # 配置文件，如环境变量
|   |-- api/                    # API 特定文件
|   |   |-- __init__.py         # 初始化API模块
|   |-- crud/                   # 业务逻辑层 CRUD 操作
|   |   |-- user.py             # 用户相关的CRUD操作
|   |-- models/                 # 数据模型目录
|   |   |-- database.py         # 设置y管理数据库连接
|   |   |-- user.py             # 用户数据模型
|   |-- schemas/                # Pydantic 模型（用于请求和响应）
|   |   |-- schemas.py          # 具体的Pydantic模型定义
|   |-- services/               # 服务层，包含业务逻辑的主要操作
|   |   |-- user.py             # 用户相关的服务，如登录和用户创建
|   |-- utils/                  # 工具函数和类，例如安全和数据库操作
|   |   |-- security.py         # 安全相关的工具，如密码验证和JWT生成
|   |   |-- database.py         # 数据库操作相关的工具
|-- tests/                      # 测试目录，包含所有的单元测试和集成测试
|-- requirements.txt            # 项目依赖文件，
```

----------------------
Modeified README.md to test Project-Management R2
# Software-Engineering-project-management-test
NKU-SoftwareEngineering2024 Individual Task Project Management 2
