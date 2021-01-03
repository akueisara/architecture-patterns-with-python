from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship

import model

metadata = MetaData()

order_lines = Table(
    'order_lines', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255)),
    Column('qty', Integer, nullable=False),
    Column('orderid', String(255)),
)

batches = Table(
    'batches', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('reference', String(255)),
    Column('sku', String(255)),
    Column('_purchased_quantity', Integer, nullable=False),
    Column('eta', Date, nullable=True),
)

allocations = Table(
    'allocations', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('orderline_id', ForeignKey('order_lines.id')),
    Column('batch_id', ForeignKey('batches.id')),
)


def start_mappers():
    lines_mapper = mapper(model.OrderLine, order_lines)
    mapper(model.Batch, batches, properties={
        '_allocations': relationship(
            lines_mapper,
            secondary=allocations,
            collection_class=set,
        )
    })


# Base = declarative_base()

# class Order(Base):
#     id = Column(Integer, primary_key=True)
#
#
# class OrderLine(Base):
#     id = Column(Integer, primary_key=True)
#     sku = Column(String(250))
#     qty = Column(Integer, nullable=False)
#     order_id = Column(Integer, ForeignKey('order.id'))
#     order = relationship(Order)
#
#
# class Allocation(Base):
#     ...


# Django ORM example

# class Order(models.Model):
#     pass
#
# class OrderLine(models.Model):
#     sku = models.CharField(max_length=255)
#     qty = models.IntegerField()
#     order = models.ForeignKey(Order)
#
# class Allocation(models.Model):
#     ...
