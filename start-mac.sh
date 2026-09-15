#!/bin/bash
# KaiPai Web - 一键启动脚本 (macOS)

echo "🚀 启动 KaiPai Web 项目..."
echo ""

# 检查 Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js 未找到！请先安装 Node.js"
    echo "访问: https://nodejs.org/"
    exit 1
fi

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 未找到！请先安装 Python 3.9+"
    echo "访问: https://www.python.org/"
    exit 1
fi

echo "✅ Node.js 版本: $(node -v)"
echo "✅ Python 版本: $(python3 --version)"
echo ""

# 启动后端
echo "📦 启动后端服务..."
cd backend

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 检查依赖
if ! python3 -c "import fastapi" 2>/dev/null; then
    echo "安装 Python 依赖..."
    pip install -r requirements.txt -q
fi

echo "后端启动在: http://localhost:8000"
echo "API 文档: http://localhost:8000/docs"
python3 main.py &
BACKEND_PID=$!

echo ""
echo "⏳ 等待后端启动..."
sleep 3

cd ..

# 启动前端
echo "🎨 启动前端服务..."

# 检查 node_modules
if [ ! -d "node_modules" ]; then
    echo "安装 NPM 依赖..."
    npm install -q
fi

echo "前端启动在: http://localhost:5173"
echo ""
echo "✅ 两个服务都已启动！"
echo "📂 后端进程 ID: $BACKEND_PID"
echo "🔗 打开浏览器访问: http://localhost:5173"
echo ""
echo "按 Ctrl+C 关闭所有服务"
echo ""

npm run dev

# 清理
kill $BACKEND_PID 2>/dev/null
