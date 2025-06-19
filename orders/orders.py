# orders/orders.py

orders_list = []

def add_order(order_id, product_name):
    orders_list.append({"order_id": order_id, "product": product_name})

def list_orders():
    return orders_list
