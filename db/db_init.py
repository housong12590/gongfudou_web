from db.db_helper import SQLHelper

users = """
    CREATE TABLE IF NOT EXISTS users(
      id INT PRIMARY KEY AUTO_INCREMENT,
      nickname VARCHAR(255) ,
      city VARCHAR(255),
      avatar VARCHAR(255) ,
      lng VARCHAR(255) ,
      lat VARCHAR(255),
      origin_id VARCHAR(255) NOT NULL UNIQUE  ,
      created_at TIMESTAMP DEFAULT current_timestamp
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;

"""


def create_table():
    SQLHelper.execute('DROP TABLE IF EXISTS users;')
    SQLHelper.execute(users)


create_table()
