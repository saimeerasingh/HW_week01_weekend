# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop_name):
    return shop_name['name']

def get_total_cash(cash):
    return cash ['admin']['total_cash']

def add_or_remove_cash(cash,money):
    cash['admin']['total_cash'] += money

def get_pets_sold(dict):
    return dict['admin']['pets_sold']

def increase_pets_sold(dict,pets):
    dict['admin']['pets_sold'] += pets

def get_stock_count(dict):
    return len(dict['pets'])

def get_pets_by_breed(pets,breed_name):
    new_list =[]
    for pet in pets['pets']:
        if pet['breed'] == breed_name:
            new_list.append(pet['breed'])
    return new_list

def find_pet_by_name(pets,pet_name):
    for pet in pets['pets']:
        if pet['name'] == pet_name:
            return pet

def remove_pet_by_name(pets,pet_name):
    for pet in pets['pets']:
        if pet['name'] == pet_name:
            pets['pets'].remove(pet)
    
def add_pet_to_stock(pet_shop,new_pet):
    pet_shop['pets'].append('new_pet')
    return pet_shop

def get_customer_cash(customers):
    total_cash =0
    for customer in customers:
        total_cash += customers['cash']
        return total_cash
    
def remove_customer_cash(customer,amount):
    customer['cash'] -= int(amount)
    
def get_customer_pet_count(customer):
    return len(customer['pets'])
    
def add_pet_to_customer(customer,new_pet):
    return customer['pets'].append('new_pet')


def customer_can_afford_pet(customer,new_pet):
    if customer['cash'] >= 100:
        return True
    else:
        return False

def sell_pet_to_customer(pet_shop,pet,customer):
    # for pet in pet_shop['pets']:
    #     if pet['name'] == pet:
    customer['pets'].append(pet)
            # len(customer['pets'])
    pet_shop['admin']['pets_sold'] += 1
    customer['cash'] -= pet['price']
    pet_shop['admin']['total_cash'] += pet['price']


