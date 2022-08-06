from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.database.conn import db
from app.database.schema import Users

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session)):
    """

    :param session:
    :return:
    """
    user = Users(status="active", name="helloworld")
    session.add(user)
    session.commit()

    return Response("hello")
