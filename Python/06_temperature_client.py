import xmlrpc.client

SERVER_URL = "http://127.0.0.1:8006"
celsius = float(input("Enter temperature in Celsius: "))

with xmlrpc.client.ServerProxy(SERVER_URL) as server:
    fahrenheit = server.celsius_to_fahrenheit(celsius)

print(f"{celsius:.2f} Celsius = {fahrenheit:.2f} Fahrenheit")
