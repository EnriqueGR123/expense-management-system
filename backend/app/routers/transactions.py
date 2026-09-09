from fastapi import APIRouter, Depends
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