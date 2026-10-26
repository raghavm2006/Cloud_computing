from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

HOST = "127.0.0.1"
PORT = 8006

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ("/RPC2",)

with SimpleXMLRPCServer((HOST, PORT), requestHandler=RequestHandler, allow_none=True) as server:
    server.register_function(celsius_to_fahrenheit, "celsius_to_fahrenheit")
    print(f"Temperature RPC server listening on http://{HOST}:{PORT}")
    server.serve_forever()
