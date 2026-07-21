from __future__ import annotations

from sqlalchemy import select

from app.core.extensions import db


class BaseRepository:

    model = None

    @classmethod
    def get_by_id(cls, object_id):
        stmt = select(cls.model).where(
            cls.model.id == object_id
        )

        return db.session.scalar(stmt)

    @classmethod
    def create(cls, **kwargs):
        obj = cls.model(**kwargs)

        db.session.add(obj)

        return obj
      
    @staticmethod
    def commit():
        db.session.commit()
        
    @staticmethod
    def rollback():
        db.session.rollback() 