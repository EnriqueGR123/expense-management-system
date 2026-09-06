from fastapi import APIRouter

router = APIRouter(
    prefix='/transaction',
    tags=['Transactions']
)



@router.get('/')
def get_transactions():
    return {'msg': 'hOLAA'}