from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.models.transaction import Transaction
from app.schemas.transactions import TransactionCreate, TransactionResponse


router = APIRouter(
    prefix='/transactions',
    tags=['Transactions']
)


# Eso es Dependency Injection.
@router.get('/', response_model=list[TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return transactions

@router.post('/', response_model=TransactionResponse)     #recibe el JSON y Pydantic lo valida.
def post_transactions(transaction:TransactionCreate, db:Session=Depends(get_db)):
    new_transaction =  Transaction(  amount=transaction.amount, 
                                    description= transaction.description,
                                    type= transaction.type.value)
    #creamos el objeto de SQLAlchemy.
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction


@router.get('/{transaction_id}')
def get_transaction_by_id(transaction_id:int, db:Session=Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail='ERROR, ID NOT FOUND')
    return transaction



@router.put('/{transaction_id}', response_model=TransactionResponse)
def update_transaction(transaction_id:int, transaction:TransactionCreate, db:Session = Depends(get_db)):
    #buscar > comprobar > modificar > commit > refresh > return
    transaction_get = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction_get is None:
        raise HTTPException(status_code=404, detail='ERROR, ID NOT FOUND')
    transaction_get.amount = transaction.amount
    transaction_get.description = transaction.description
    transaction_get.type = transaction.type.value
    db.commit()
    db.refresh(transaction_get)
    return transaction_get


@router.delete('/{transaction_id}')
def delete_transaction(transactionID: int, db:Session= Depends(get_db))->str:
    transaction = db.query(Transaction).filter(Transaction.id == transactionID).first()
    if transaction is None:
        raise HTTPException(status_code=404, detail='ERROR, transaction not Found')
    db.delete(transaction)
    db.commit()
    return 'Transaction was deleted '

# Busque la transacción.
# Si no existe error 404.
# La elimine.
# Haga commit().
# Devuelva un mensaje confirmando la eliminación.


# GET /transactions?type=income
# GET /transactions?type=expense
@router.get('/}')
def get_transaction_income(transaction_type :str, order:str, db:Session = Depends(get_db)):
    transactions = db.query(Transaction).filter(Transaction.type == transaction_type).all()
    if not transactions:
        raise 'Transactions not found'
    elif order == 'asc':
        transactions = db.query(Transaction).order_by(Transaction.amount.asc())
    elif order == 'desc':
        transactions = db.query(Transaction).order_by(Transaction.amount.desc())
    return transactions

# Filtrar por expense.
# Ordenar por amount.
# Si order=desc → mayor a menor.
# Si order=asc → menor a mayor.