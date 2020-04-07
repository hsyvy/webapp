def search4letters(phrase:str, letters:str='aeiou'):
    return set(letters).intersection(set(phrase))

def log_request(req, res):
    with open('search.log', 'a') as log:
            print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
            