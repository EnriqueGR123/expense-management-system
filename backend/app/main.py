from fastapi import FastAPI
from app.routers.transactions import router as transactions_router




app = FastAPI(title="Expense Manager API", version="1.0.0")
app.include_router(transactions_router)


@app.get('/')
def root():
    return {'msg': "Expense Manager API"}
