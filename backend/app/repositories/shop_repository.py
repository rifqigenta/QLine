from sqlalchemy import select

from app.core.extensions import db
from app.models.shop import Shop

from .base_repository import BaseRepository


class ShopRepository(BaseRepository):

    model = Shop

    @classmethod
    def get_by_username(
        cls,
        username: str,
    ) -> Shop | None:

        stmt = select(Shop).where(
            Shop.username == username
        )

        return db.session.scalar(stmt)
    
    @classmethod
    def get_by_public_code(
        cls,
        public_code: str,
    ) -> Shop | None:

        stmt = select(Shop).where(
            Shop.public_code == public_code
        )

        return db.session.scalar(stmt)