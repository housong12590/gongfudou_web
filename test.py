from db.db_helper import SQLHelper

ret = SQLHelper.fetch_one(
    'SELECT count(id) AS count FROM users WHERE TO_DAYS( NOW( ) ) - TO_DAYS( created_at) <= 1')
print(ret)
