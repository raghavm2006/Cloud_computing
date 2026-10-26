from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

HOST = "127.0.0.1"
PORT = 8009

PRODUCTS = {
    "laptop": 55000.0,
    "mouse": 700.0,
    "keyboard": 1500.0,
    "headphones": 2200.0
}

def calculate_bill(product_name, quantity):
    name = product_name.strip().lower()
    if name not in PRODUCTS:
        return {"error": "Product not found", "available_products": list(PRODUCTS)}
    if not isinstance(quantity, int) or quantity <= 0:
        return {"error": "Quantity must be a positive whole number."}

    unit_price = PRODUCTS[name]
    subtotal = unit_price * quantity
    discount_rate = 0.10 if subtotal >= 10000 else 0.05 if subtotal >= 3000 else 0.0
    discount = subtotal * discount_rate
    final_amount = subtotal - discount
    return {
        "product": name,
        "quantity": quantity,
        "unit_price": unit_price,
        "subtotal": round(subtotal, 2),
        "discount_percent": int(discount_rate * 100),
        "discount_amount": round(discount, 2),
        "final_amount": round(final_amount, 2)
    }

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)

with SimpleXMLRPCServer((HOST, PORT), requestHandler=RequestHandler, allow_none=True) as server:
    server.register_function(calculate_bill, "calculate_bill")
    print(f"Shopping RPC server listening on http://{HOST}:{PORT}")
    print("Products:", PRODUCTS)
    server.serve_forever()
