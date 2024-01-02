from sqlalchemy.orm import Session

from app import models, schemas


def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(value=item.value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
