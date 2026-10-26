import xmlrpc.client

SERVER_URL = "http://127.0.0.1:8009"
print("Available products: laptop, mouse, keyboard, headphones")
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))

with xmlrpc.client.ServerProxy(SERVER_URL) as server:
    bill = server.calculate_bill(product, quantity)

if "error" in bill:
    print(bill["error"])
    if "available_products" in bill:
        print("Available products:", ", ".join(bill["available_products"]))
else:
    print("Product:", bill["product"])
    print("Quantity:", bill["quantity"])
    print("Unit price: Rs.", bill["unit_price"])
    print("Subtotal: Rs.", bill["subtotal"])
    print("Discount:", str(bill["discount_percent"]) + "%")
    print("Discount amount: Rs.", bill["discount_amount"])
    print("Final amount: Rs.", bill["final_amount"])
