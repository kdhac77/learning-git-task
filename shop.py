print("LISTA NA SOBOTNIE ŚNIADANIE")
shopping_list = {
    "Spożywczy": ['Chleb', 'Masło', 'Ser'],
    "Warzywniak": ['Marchew', 'Pietruszka', 'Rukola', 'Sałata']
}
food_products = 0

#Przeiterowanie po słowniku, oraz zmiana nazw na wielkie ltery 
for shop, products in shopping_list.items():
    shop = shop.upper()
    products = [product.upper() for product in products]

    print(f"Idę do {shop}, kupuję tu następujące rzeczy: {products}.")

#suma produktów
    food_products += len(products)

print(f"W sumie kupuję {food_products} produktów.")
