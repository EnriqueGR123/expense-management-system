from fastapi import FastAPI
from app.schemas.transactions import TransactionCreate, TransactionResponse
from datetime import datetime, timezone
from app.db.session import Base, engine
from app.models.transaction import Transaction


app = FastAPI(title="Expense Manager API", version="1.0.0")

Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return {'msg': "Expense Manager API"}


@app.post('/transactions', response_model= TransactionResponse)
#Esta ruta debe devolver una respuesta que cumpla con TransactionResponse
def create_transactions(transaction: TransactionCreate):
    return {
        "id": 1,
        "amount": transaction.amount,
        "description": transaction.description,
        "type": transaction.type,
        "created_at": datetime.now(timezone.utc),
        "secret": "esto no debería salir",

    }