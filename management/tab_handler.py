from management.product_handler import get_product_by_id
from menu import products


def calculate_tab(dicionarios):
    subtotal=0
    for dics in dicionarios:
        product =get_product_by_id(dics["_id"])
        subtotal += product["price"]*dics["amount"]
    
    return  {"subtotal": f"${round(subtotal,2)}"}



