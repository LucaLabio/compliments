from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database import (
    add_compliment,
    delete_compliment,
    retrieve_compliment,
    retrieve_compliments,
    update_compliment,
)
from server.models.compliment import (
    ErrorResponseModel,
    ResponseModel,
    complimentSchema,
)
router = APIRouter()