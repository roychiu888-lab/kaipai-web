import { useState } from 'react'
import Sidebar from './components/layout/Sidebar'
import Header from './components/layout/Header'
import JokeGeneratorAdvanced from './components/JokeGeneratorAdvanced'

export default function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true)
  const [currentPage, setCurrentPage] = useState('home')

  return (
    <div className="flex h-screen bg-gray-50">
      <Sidebar isOpen={isSidebarOpen} />
      <div className="flex-1 flex flex-col">
        <Header onToggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)} />
        <main className="flex-1 overflow-auto p-6">
          {currentPage === 'home' && (
            <div>
              <h1 className="text-3xl font-bold mb-4">欢迎来到 KaiPai 视频编辑工作室</h1>
              <p className="text-gray-600 mb-6">选择左侧菜单开始创建您的视频项目</p>
              
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition cursor-pointer" onClick={() => setCurrentPage('jokes')}>
                  <div className="text-4xl mb-3">😂</div>
                  <h3 className="text-xl font-bold mb-2">笑话生成器</h3>
                  <p className="text-gray-600">享受随机笑话</p>
                </div>
              </div>
            </div>
          )}

          {currentPage === 'jokes' && (
            <div>
              <button 
                onClick={() => setCurrentPage('home')}
                className="mb-4 px-4 py-2 bg-gray-300 rounded hover:bg-gray-400"
              >
                ← 返回首页
              </button>
              <JokeGeneratorAdvanced />
            </div>
          )}
        </main>
      </div>
    </div>
  )
}
