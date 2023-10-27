print("Lista zakupów")
shopping_list = {
    "Piekarnia": ['Chleb', 'Pączek', 'Bułki'],
    "Warzywniak": ['Marchew', 'Seler', 'Rukola']
}
sum_list = 0

for shop, products in shopping_list.items():
    shop = shop.upper()
    products = [product.upper() for product in products]

    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {products}.")

    sum_list += len(products)

print(f"W sumie kupuję {sum_list} produktów.")
