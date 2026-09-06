from fastapi import APIRouter



router = APIRouter ( # agrupar endpoints relacionados.
    prefix='/transactions',
    tags=['Transaction'] # hace que Swagger agrupe nuestros endpoints visualmente:
)