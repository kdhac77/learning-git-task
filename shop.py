#Lista produktów z piekarni i warzywniaka
shopping_list = {
    "Piekarnia": ['Chleb', 'Pączek', 'Bułki', 'Drożdzówka' ],
    "Warzywniak": ['Marchew', 'Seler', 'Rukola', 'Sałata']
}
add_list = 0

#Przeiterowanie po słowniku, oraz zmiana nazw na wielkie ltery 
for shop, products in shopping_list.items():
    shop = shop.upper()
    products = [product.upper() for product in products]

    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {products}.")

#suma produktów
    add_list += len(products)

print(f"W sumie kupuję {add_list} produktów.")
