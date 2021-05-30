
from pydantic import BaseModel, Field


class complimentSchema(BaseModel):
    text: str = Field(...)
    language: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                    "text":"I love you",
                    "language":'ingles',
                }
            }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}