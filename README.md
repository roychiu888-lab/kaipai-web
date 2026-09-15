# KaiPai Web - AI-Powered Video Editing Platform

一个对标开拍APP的网页版AI视频编辑平台，专门为竖屏短视频（6:9）设计，支持模板化编辑、智能字幕识别、气口剪辑、特效添加等功能。

## ✨ 核心功能

### 📋 模板系统
- 模板选择与管理
- 统一风格配置
- 字幕样式预设
- 动画效果预设

### 🎬 视频编辑
- **智能字幕**: AI语音识别（Whisper）自动生成字幕
- **气口剪辑**: 自动检测并删除停顿和重复
- **字幕编辑**: 字号、颜色、字体、位置调整
- **文字动画**: 淡入、滑动、缩放等10+种动画效果
- **音效库**: 音乐、音效、转场音
- **贴片添加**: 片头、片尾、水印
- **实时预览**: Canvas实时合成预览

### 🎨 智能包装
- 动态字幕高亮
- 综艺级特效
- AI智能封面生成
- 竖屏专属优化（1080x1920）

### 📤 导出
- 多平台输出规格
- 批量导出
- 云端渲染
- 视频号/抖音直接发布

## 🏗️ 项目结构

```
kaipai-web/
├── src/                    # 前端源代码
│   ├── components/         # React组件
│   ├── pages/              # 页面
│   ├── store/              # Zustand状态管理
│   ├── services/           # API服务
│   ├── types/              # TypeScript类型
│   ├── utils/              # 工具函数
│   ├── hooks/              # 自定义Hooks
│   ├── App.tsx
│   └── main.tsx
├── backend/                # 后端源代码
│   ├── app/
│   │   ├── routes/         # API路由
│   │   ├── models/         # 数据模型
│   │   ├── services/       # 业务逻辑
│   │   └── __init__.py
│   ├── main.py             # FastAPI主应用
│   └── requirements.txt
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.js
├── .env.example
├── .gitignore
└── README.md
```

## 🛠️ 技术栈

### 前端
- **框架**: React 18 + TypeScript
- **样式**: Tailwind CSS + PostCSS
- **状态管理**: Zustand
- **打包**: Vite
- **视频编辑**: 
  - FFmpeg.wasm (本地视频处理)
  - Anime.js (文字动画)
  - Tone.js (音效处理)
  - React Player (视频播放)
- **拖拽**: dnd-kit
- **表单**: React Hook Form + Zod

### 后端
- **框架**: FastAPI (Python)
- **异步**: Async/Await
- **任务队列**: Celery
- **数据库**: PostgreSQL
- **缓存**: Redis
- **视频处理**: 
  - FFmpeg
  - OpenAI Whisper (字幕识别)
  - Librosa (音频分析)
- **存储**: MinIO/S3

## 🚀 快速开始

### 前置要求
- Node.js 16+
- Python 3.9+
- FFmpeg
- PostgreSQL 12+ (可选)
- Redis (可选)

### 前端安装

```bash
# 进入前端目录
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build
```

访问 `http://localhost:5173`

### 后端安装

```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 启动API服务器
python main.py
```

访问 `http://localhost:8000`
API文档: `http://localhost:8000/docs`

## 📚 API文档

| 功能 | 端点 | 方法 |
|------|------|------|
| 获取模板列表 | `/api/templates` | GET |
| 创建模板 | `/api/templates` | POST |
| 获取项目列表 | `/api/projects` | GET |
| 创建项目 | `/api/projects` | POST |
| 上传视频 | `/api/videos/upload` | POST |
| 生成字幕 | `/api/videos/{id}/subtitles/generate` | POST |
| 检测气口 | `/api/videos/{id}/pauses/detect` | POST |
| 生成封面 | `/api/projects/{id}/cover/generate` | POST |
| 导出视频 | `/api/projects/{id}/export` | POST |

## 📋 开发路线

### Phase 1 (MVP)
- ✅ 项目框架搭建
- ⬜ 模板管理系统
- ⬜ 视频上传和预览
- ⬜ 字幕识别和编辑
- ⬜ 基础特效
- ⬜ 视频导出

### Phase 2
- ⬜ 气口自动剪辑
- ⬜ 文字动画库
- ⬜ 音效和贴片
- ⬜ 批量处理

### Phase 3
- ⬜ AI数字人
- ⬜ 高级特效
- ⬜ 性能优化
- ⬜ 移动端适配

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

## 📝 许可证

MIT License
