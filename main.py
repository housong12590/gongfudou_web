from flask import Flask, request, jsonify
from db.db_helper import SQLHelper
from flask_cors import *

"""
全村最靓的崽:
http://proxy.jiankanghao.net:50058/total_count

{
    "status_code": 200,
    "msg": "获取信息成功",
    "data": {
        "users": [
            {
                "user_id": 2285,
                "nickname": "czlyj",
                "avatar": "http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIibBoVgjdjnibUDaZd2TQnibqWnoySMq8lUtJAtHtib5Luic5b7khwm0cDibpGa1CgbFRbW12V0l3fZaBA/132",
                "long": "118.728196",
                "lat": "31.981179",
                "login_time": 1551261097
            },
            {
                "user_id": 2299,
                "nickname": "啥",
                "avatar": "http://shenhuanglive.oss-cn-shanghai.aliyuncs.com/image/test_img/5b90e4f08931a.png",
                "long": "118.7399",
                "lat": "31.98452",
                "login_time": 1551260681
            },
            {
                "user_id": 2305,
                "nickname": "是谁",
                "avatar": "http://shenhuanglive.oss-cn-shanghai.aliyuncs.com/production/Avatar/e10999d9ed71aaf7bc360f8bc28c01c2.jpg",
                "long": "118.7399",
                "lat": "31.98451",
                "login_time": 1551266529
            }
        ],
        "today_count": 3,
        "yesterday_count": 2,
        "total_count": 530
    }
}

全村最靓的崽:
http://proxy.jiankanghao.net:50058/user
{
    "status_code": 200,
    "msg": "获取信息成功",
    "data": [
        {
            "user_id": 2305,
            "nickname": "是谁",
            "avatar": "http://shenhuanglive.oss-cn-shanghai.aliyuncs.com/production/Avatar/e10999d9ed71aaf7bc360f8bc28c01c2.jpg",
            "long": "118.7399",
            "lat": "31.98451",
            "login_time": 1551266529
        }
    ]
}
"""

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/total_count')
def total_count():
    ret = SQLHelper.fetch_one('SELECT count(*) AS count FROM users WHERE lng IS NOT NULL')
    total_count = ret.get('count')
    users = SQLHelper.fetch_all(
        "SELECT id user_id,nickname,avatar,lng ,lat ,DATE_FORMAT(created_at,'%%Y-%%m-%%d %%H:%%m:%%s') login_time FROM users WHERE to_days(created_at) = to_days(now()) AND `lng` IS NOT NULL ORDER BY id DESC LIMIT 50")
    today_count = len(users)
    ret = SQLHelper.fetch_one(
        "SELECT COUNT(*) count FROM users WHERE DATE_FORMAT( created_at,'%%Y-%%m-%%d') = DATE_FORMAT(CURDATE()-1,'%%Y-%%m-%%d') AND lng IS NOT NULL;")
    print(ret)
    yesterday_count = ret.get('count')
    data = {'today_count': today_count, 'total_count': total_count,
            'yesterday_count': yesterday_count, 'users': users}
    return make_resp(data)


@app.route('/user')
def user():
    interval = request.args.get('interval', 3)
    sql = "SELECT id user_id,nickname,avatar,lng ,lat,DATE_FORMAT(created_at,'%%Y-%%m-%%d %%H:%%m:%%s') login_time FROM users WHERE created_at > DATE_sub(NOW(), INTERVAL {} SECOND) AND lng IS NOT NULL".format(
        interval)
    ret_data = SQLHelper.fetch_all(sql)
    return make_resp(ret_data)


@app.route('/all')
def all():
    # sql = 'SELECT any_value (lng) AS lat,any_value (lat) AS lng,count(lat) AS count FROM users WHERE lng IS NOT NULL GROUP BY city'
    sql = 'SELECT lng ,lat AS count FROM users WHERE lng IS NOT NULL '
    ret_data = SQLHelper.fetch_all(sql)
    return make_resp(ret_data)


def make_resp(data):
    return jsonify({'status_code': 200, 'msg': '获取信息成功', 'data': data})


if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0")
