"""
Aspira 后端应用程序入口
完整版本，包含所有必要的API端点
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

# 简单的内存存储（生产环境应使用数据库）
user_data_store = {}
goals_data_store = {}
awards_data_store = {}
content_data_store = {}
banner_data_store = {}
stages_data_store = {}
ai_suggestions_store = {}

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Aspira Backend!', 'status': 'success'})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': '2024-01-01T00:00:00Z'})

@app.route('/test')
def test():
    return jsonify({
        'status': 'success',
        'message': 'Backend is working!',
        'endpoints': [
            '/',
            '/health',
            '/api/user-data',
            '/api/goals-data',
            '/api/awards-data',
            '/api/content-data',
            '/api/banner-data',
            '/api/stages-data',
            '/api/ai-suggestions'
        ]
    })

# API 路由 - 用户数据
@app.route('/api/user-data', methods=['POST'])
def save_user_data():
    try:
        data = request.get_json()
        user_id = data.get('userId', 'default_user')
        user_data_store[user_id] = data
        print(f"保存用户数据: {user_id}")
        return jsonify({'status': 'success', 'message': 'User data saved successfully'})
    except Exception as e:
        print(f"保存用户数据失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/user-data/<user_id>', methods=['GET'])
def get_user_data(user_id):
    try:
        data = user_data_store.get(user_id, {})
        print(f"获取用户数据: {user_id}")
        return jsonify({
            'status': 'success', 
            'data': data
        })
    except Exception as e:
        print(f"获取用户数据失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# API 路由 - 目标数据
@app.route('/api/goals-data', methods=['POST'])
def save_goals_data():
    try:
        data = request.get_json()
        user_id = data.get('userId', 'default_user')
        goals_data_store[user_id] = data
        print(f"保存目标数据: {user_id}")
        return jsonify({'status': 'success', 'message': 'Goals data saved successfully'})
    except Exception as e:
        print(f"保存目标数据失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/goals-data/<user_id>', methods=['GET'])
def get_goals_data(user_id):
    try:
        data = goals_data_store.get(user_id, {})
        print(f"获取目标数据: {user_id}")
        return jsonify({
            'status': 'success', 
            'data': data
        })
    except Exception as e:
        print(f"获取目标数据失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# API 路由 - 奖项数据
@app.route('/api/awards-data', methods=['POST'])
def save_awards_data():
    try:
        data = request.get_json()
        user_id = data.get('userId', 'default_user')
        awards_data_store[user_id] = data
        print(f"保存奖项数据: {user_id}")
        return jsonify({'status': 'success', 'message': 'Awards data saved successfully'})
    except Exception as e:
        print(f"保存奖项数据失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/awards-data/<user_id>', methods=['GET'])
def get_awards_data(user_id):
    try:
        data = awards_data_store.get(user_id, {})
        print(f"获取奖项数据: {user_id}")
        return jsonify({
            'status': 'success', 
            'data': data
        })
    except Exception as e:
        print(f"获取奖项数据失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# API 路由 - 内容数据
@app.route('/api/content-data', methods=['POST'])
def save_content_data():
    try:
        data = request.get_json()
        user_id = data.get('userId', 'default_user')
        content_data_store[user_id] = data
        print(f"保存内容数据: {user_id}")
        return jsonify({'status': 'success', 'message': 'Content data saved successfully'})
    except Exception as e:
        print(f"保存内容数据失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/content-data/<user_id>', methods=['GET'])
def get_content_data(user_id):
    try:
        data = content_data_store.get(user_id, {})
        print(f"获取内容数据: {user_id}")
        return jsonify({
            'status': 'success', 
            'data': data
        })
    except Exception as e:
        print(f"获取内容数据失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# API 路由 - 横幅数据
@app.route('/api/banner-data', methods=['POST'])
def save_banner_data():
    try:
        data = request.get_json()
        user_id = data.get('userId', 'default_user')
        banner_data_store[user_id] = data
        print(f"保存横幅数据: {user_id}")
        return jsonify({'status': 'success', 'message': 'Banner data saved successfully'})
    except Exception as e:
        print(f"保存横幅数据失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/banner-data/<user_id>', methods=['GET'])
def get_banner_data(user_id):
    try:
        data = banner_data_store.get(user_id, {})
        print(f"获取横幅数据: {user_id}")
        return jsonify({
            'status': 'success', 
            'data': data
        })
    except Exception as e:
        print(f"获取横幅数据失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# API 路由 - 阶段数据
@app.route('/api/stages-data', methods=['POST'])
def save_stages_data():
    try:
        data = request.get_json()
        user_id = data.get('userId', 'default_user')
        stages_data_store[user_id] = data
        print(f"保存阶段数据: {user_id}")
        return jsonify({'status': 'success', 'message': 'Stages data saved successfully'})
    except Exception as e:
        print(f"保存阶段数据失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/stages-data/<user_id>', methods=['GET'])
def get_stages_data(user_id):
    try:
        data = stages_data_store.get(user_id, {})
        print(f"获取阶段数据: {user_id}")
        return jsonify({
            'status': 'success', 
            'data': data
        })
    except Exception as e:
        print(f"获取阶段数据失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# API 路由 - AI建议
@app.route('/api/ai-suggestions', methods=['POST'])
def save_ai_suggestions():
    try:
        data = request.get_json()
        user_id = data.get('userId', 'default_user')
        ai_suggestions_store[user_id] = data
        print(f"保存AI建议: {user_id}")
        return jsonify({'status': 'success', 'message': 'AI suggestions saved successfully'})
    except Exception as e:
        print(f"保存AI建议失败: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting Aspira Backend on port {port}")
    app.run(debug=False, host='0.0.0.0', port=port)
