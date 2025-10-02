-- 健康任務地圖 MySQL 資料庫初始化
CREATE TABLE users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE buildings (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    points_required INT NOT NULL,
    latitude DOUBLE,
    longitude DOUBLE
);

CREATE TABLE user_progress (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    date DATE,
    steps INT,
    exercise_minutes INT,
    water_ml INT,
    points_earned INT,
    unlocked_building_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (unlocked_building_id) REFERENCES buildings(id)
);

CREATE TABLE challenges (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    description TEXT,
    start_date DATE,
    end_date DATE,
    points_reward INT
);

CREATE TABLE user_challenges (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    challenge_id INT,
    completed BOOLEAN DEFAULT FALSE,
    completed_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (challenge_id) REFERENCES challenges(id)
);

CREATE TABLE teams (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    created_by INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES users(id)
);

CREATE TABLE team_members (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    team_id INT,
    user_id INT,
    joined_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE team_tasks (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    team_id INT,
    title VARCHAR(100),
    description TEXT,
    start_date DATE,
    end_date DATE,
    points_reward INT,
    completed BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (team_id) REFERENCES teams(id)
);

CREATE TABLE team_task_progress (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    team_task_id INT,
    user_id INT,
    completed BOOLEAN DEFAULT FALSE,
    completed_at DATETIME,
    FOREIGN KEY (team_task_id) REFERENCES team_tasks(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
