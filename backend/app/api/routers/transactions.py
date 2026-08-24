
'''
GET    /transactions
GET    /transactions/{id}
POST   /transactions
PUT    /transactions/{id}
DELETE /transactions/{id}
'''

@app.get('/transactions')
def get_transactions():
    pass

@app.get('/transactions/{id}')
def get_transactions_by_id():
    pass

@app.post('/transactions')
def post_transactions():
    pass

@app.put('/transactions/{id}')
def get_transactions_by_id():
    pass

@app.delete('/transactions/{id}')
def get_transactions_by_id():
    pass