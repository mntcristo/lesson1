product = {
    "city": "Москва", 
    "temperature": "20"
}
print(product['city'])
product['temperature'] = int(product["temperature"]) - 5
print(product) 
print(product.get('country'))
product['country'] = 'Россия'   
print(product)
product['date'] = '27.05.2019' 
print(len(product))