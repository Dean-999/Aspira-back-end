#!/usr/bin/env python3
"""
Aspira 应用启动脚本
简化的运行入口
"""
import os
import sys
from app import create_app

def main():
    """主函数"""
    # 设置环境变量
    os.environ.setdefault('FLASK_ENV', 'development')
    
    # 创建应用
    app = create_app()
    
    # 获取配置
    host = app.config.get('APP_HOST', '0.0.0.0')
    port = app.config.get('APP_PORT', 5000)
    debug = app.config.get('DEBUG', True)
    
    print("🚀 启动 Aspira 后端服务...")
    print(f"📍 访问地址: http://{host}:{port}")
    print(f"🔧 环境模式: {os.environ.get('FLASK_ENV', 'development')}")
    print(f"🐛 调试模式: {'开启' if debug else '关闭'}")
    print("=" * 50)
    print("API 端点预览:")
    print("  健康检查: GET  /api/health")
    print("  用户注册: POST /api/auth/register")
    print("  用户登录: POST /api/auth/login")
    print("  日记管理: /api/journal/*")
    print("  目标管理: /api/goal/*")
    print("  用户管理: /api/user/*")
    print("=" * 50)
    
    try:
        app.run(host=host, port=port, debug=debug)
    except KeyboardInterrupt:
        print("\n👋 服务已停止")
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
