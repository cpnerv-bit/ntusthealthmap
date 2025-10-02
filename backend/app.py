
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import hashlib

app = Flask(__name__)
CORS(app)

# MySQL 連線設定
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'health_map'
}

def get_db():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    return '健康任務地圖 API 啟動成功'

# 註冊
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = hashlib.sha256(data.get('password').encode()).hexdigest()
    email = data.get('email')
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        db.commit()
        return jsonify({'message': '註冊成功'}), 201
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 400
    finally:
        cursor.close()
        db.close()

# 登入
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = hashlib.sha256(data.get('password').encode()).hexdigest()
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    db.close()
    if user:
        return jsonify({'message': '登入成功', 'user': user})
    else:
        return jsonify({'error': '帳號或密碼錯誤'}), 401

# 每日數據上傳
@app.route('/upload_data', methods=['POST'])
def upload_data():
    data = request.json
    user_id = data.get('user_id')
    date = data.get('date')
    steps = data.get('steps')
    exercise_minutes = data.get('exercise_minutes')
    water_ml = data.get('water_ml')
    points_earned = data.get('points_earned')
    unlocked_building_id = data.get('unlocked_building_id')
    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO user_progress (user_id, date, steps, exercise_minutes, water_ml, points_earned, unlocked_building_id) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (user_id, date, steps, exercise_minutes, water_ml, points_earned, unlocked_building_id))
    db.commit()
    cursor.close()
    db.close()
    return jsonify({'message': '數據上傳成功'})

# 查詢地圖進度與已解鎖建築物
@app.route('/progress/<int:user_id>', methods=['GET'])
def get_progress(user_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT up.*, b.name AS building_name FROM user_progress up LEFT JOIN buildings b ON up.unlocked_building_id = b.id WHERE up.user_id = %s", (user_id,))
    progress = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify({'progress': progress})


# 建築物列表
@app.route('/buildings', methods=['GET'])
def get_buildings():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM buildings")
    buildings = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify({'buildings': buildings})

# 健康挑戰任務列表
@app.route('/challenges', methods=['GET'])
def get_challenges():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM challenges")
    challenges = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify({'challenges': challenges})

# 團隊列表
@app.route('/teams', methods=['GET'])
def get_teams():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify({'teams': teams})

# 團隊任務列表
@app.route('/team_tasks/<int:team_id>', methods=['GET'])
def get_team_tasks(team_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM team_tasks WHERE team_id = %s", (team_id,))
    tasks = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify({'team_tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
