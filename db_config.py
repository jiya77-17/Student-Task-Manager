import mysql.connector

def get_database_connection():

    connection = mysql.connector.connect(
        host="gateway01.ap-southeast-1.prod.aws.tidbcloud.com",
        user="24a4BKHzQu88HyD.root",
        password="ou3H8uqViWFl9YDc",
        database="student_task_manager",
        port=4000
    )

    return connection
    