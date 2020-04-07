from flask import Flask, render_template, request, redirect, escape
from helper import search4letters
from DBcm import UseDatabase

app = Flask(__name__)

# @app.route('/')
# def hello(): 
#     return redirect('/entry');

app.config['dbconfig'] =  { 'host': '127.0.0.1',
                            'user': 'vsearch',
                            'password': 'vsearchpasswd',
                            'database': 'searchlogDB', }


def log_request(req, res):
    """Log the details of the web request and the results."""
    
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
        (phrase, letters, ip, browser_string, results)
        values(%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                    req.form['letters'],
                    req.remote_addr,
                    req.user_agent.browser,
                    res, ))

    

@app.route('/')
@app.route('/entry') # create two url to open same web page
def entry_page():
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/search4', methods=['POST']) # decorator creates and url and which actually has post method in it.
def do_search():
    """function will use the request form phrase and letters process it using search4letters function
    and finally render the result of search4letters function in result.html
    """
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here is your results:'
    result = str(search4letters(phrase, letters)) # search letters in the phrase
    log_request(request, result) # keep the search request in log file
    
    return render_template('result.html',
                            the_phrase = phrase,
                            the_letters = letters,
                            the_title = title,
                            the_result = result,)  # use flask to render the template result.html



# @app.route('/viewlog')
# def view_the_log():
#     """function will display the log store in the search.log file in the browser"""
#     contents = list()
#     with open('search.log') as log:
#         # contents = log.read()
#         for line in log:
#             contents.append([])
#             contents.append([escape(item) for item in line.split('|')])
#             # for item in line.split('|'):
#             #     contents[-1].append(escape(item))
#     titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
#     return render_template('viewlog.html',
#                             the_title='View Log',
#                             the_row_titles=titles,
#                             the_data=contents,)

@app.route('/viewlog')
def view_the_log():
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """ select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html',
                            the_title='View Log',
                            the_row_titles=titles,
                            the_data=contents,)



if __name__ == "__main__":
    app.run(debug=True)