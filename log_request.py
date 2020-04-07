import mysql.connector

def log_request(req, res):
    """Log details of the web request and the results."""
    dbconfig = { 'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'searchlogDB', }
    
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
    (phrase, letters, ip, browser_string, results)
    values(%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                   req.form['letters'],
                   req.remote_addr,
                   req.user_agent.browser,
                   res, ))

    conn.commit()
    cursor.close()
    conn.close()