from menu import products

def get_product_by_id(id):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")
        
    else:
        product_dic = dict()
        for product in products:
            if product['_id'] == id:
                product_dic = product

    return product_dic

def get_products_by_type(type):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")
    product_list= []
    for product in products:
        if product['type'] == type:
            product_list.append(product)
    
    return product_list




def add_product(menu,**newProduct):
    new_id=1
    quant = len(menu)
    if quant>0:
        max_id = max(item["_id"] for item in menu)
        new_id= max_id+1
    
    newItem = {"_id":new_id,**newProduct}

    menu.append(newItem)
    return newItem

def menu_report():
    products_count =len(products)
    soma_total=0
    average_price=float(0)
    most_common_type=0
    lista_precos =[]
    maior=0
    for product in products:
        lista_precos.append(product["price"])

    soma_total = sum(lista_precos)
    average_price = soma_total/products_count  
    types_dicts={

    }
    for product in products:
        if product["type"] not in types_dicts:
             types_dicts[product["type"]]=0

        types_dicts[product["type"]]+=1

    most_type=""
    most_type_count=0
    for key,value in types_dicts.items():
        if value>most_type_count:
            most_type_count=value
            most_type=key
        
   
   

    return f"Products Count: {products_count} - Average Price: ${round(average_price,2)} - Most Common Type: {most_type}"


