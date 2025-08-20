from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model = Column(String)
    category = Column(String)
    image_url = Column(String)
    avg_sold_price = Column(Float)
    most_popular_size = Column(String)
    sell_through_rate = Column(Float)

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    price = Column(Float)
    sold_date = Column(DateTime)
    product = relationship("Product", back_populates="sales")

Product.sales = relationship("Sale", order_by=Sale.id, back_populates="product")