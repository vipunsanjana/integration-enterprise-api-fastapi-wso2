from app.db.fake_db import orders_db
from datetime import datetime

def create_order(order):
    order_dict = order.dict()
    order_dict["id"] = len(orders_db) + 1
    order_dict["created_at"] = datetime.utcnow()
    orders_db.append(order_dict)
    return order_dict

def get_orders():
    return orders_db
