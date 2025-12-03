#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Telescope Data Center 启动脚本
"""

import sys
import os
import asyncio

# 添加项目根目录到Python路径
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def main():
    """启动服务器"""
    try:
        # 导入WebSocket服务器模块
        from server.websocket_server import WebSocketServer
        
        # 创建并启动WebSocket服务器
        server = WebSocketServer(host='localhost', port=8000)
        print("Telescope Data Center 服务器已启动")
        print(f"WebSocket地址: ws://{server.host}:{server.port}")
        print("按 Ctrl+C 停止服务器")
        
        # 启动服务器
        asyncio.run(server.start_server())
        
    except KeyboardInterrupt:
        print("\n服务器已停止")
    except ImportError as e:
        print(f"导入模块失败: {e}")
        print("请确保所有依赖项都已安装")
    except Exception as e:
        print(f"启动服务器失败: {e}")

if __name__ == "__main__":
    main()