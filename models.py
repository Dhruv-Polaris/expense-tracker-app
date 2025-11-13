from sqlalchemy import Column, Integer, String, Date, DateTime, func, Float
from database import Base

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String)
    category = Column(String, nullable=False)
    amount = Column(Float, nullable=False, default=0)
    spent_on = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f"<Expense(title='{self.title}', description='{self.description}', category='{self.category}', amount='{self.amount}', spent_on='{self.spent_on}')>"
