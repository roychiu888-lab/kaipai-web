@echo off
REM KaiPai Web - 一键启动脚本 (Windows)

echo 🚀 启动 KaiPai Web 项目...
echo.

REM 检查 Node.js
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Node.js 未找到！请先安装 Node.js
    echo 访问: https://nodejs.org/
    pause
    exit /b 1
)

REM 检查 Python
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python 未找到！请先安装 Python 3.9+
    echo 访问: https://www.python.org/
    pause
    exit /b 1
)

echo ✅ Node.js 版本: 
node -v
echo ✅ Python 版本: 
python --version
echo.

REM 启动后端
echo 📦 启动后端服务...
cd backend

REM 检查虚拟环境
if not exist "venv" (
    echo 创建虚拟环境...
    python -m venv venv
)

REM 激活虚拟环境
call venv\Scripts\activate.bat

REM 检查依赖
python -c "import fastapi" >nul 2>nul
if %errorlevel% neq 0 (
    echo 安装 Python 依赖...
    pip install -r requirements.txt -q
)

echo 后端启动在: http://localhost:8000
echo API 文档: http://localhost:8000/docs
start cmd /k "python main.py"

REM 等待后端启动
timeout /t 3 /nobreak

cd ..

REM 启动前端
echo.
echo 🎨 启动前端服务...

REM 检查 node_modules
if not exist "node_modules" (
    echo 安装 NPM 依赖...
    call npm install -q
)

echo 前端启动在: http://localhost:5173
echo.
echo ✅ 两个服务都已启动！
echo 🔗 打开浏览器访问: http://localhost:5173
echo.
echo 提示: 关闭命令行窗口即可停止服务
echo.

call npm run dev

pause
