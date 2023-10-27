#Lista produktów z piekarni i warzywniaka
shopping_list = {
    "Piekarnia": ['Chleb', 'Pączek', 'Bułki', 'Drożdzówka' ],
    "Warzywniak": ['Marchew', 'Seler', 'Rukola', 'Sałata']
}
all_products = 0

#Przeiterowanie po słowniku, oraz zmiana nazw na wielkie ltery 
for shop, products in shopping_list.items():
    shop = shop.upper()
    products = [product for product in products]

    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {products}.")

#suma produktów
    all_products += len(products)

print(f"W sumie kupuję {all_products} produktów.")
