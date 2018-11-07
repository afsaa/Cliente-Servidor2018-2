from suds.client import Client
c = Client('http://localhost:8000/?wsdl')
c.service.say_hello('punk', 5)
string=[
      "Hello, punk",
      "Hello, punk",
      "Hello, punk",
      "Hello, punk",
      "Hello, punk"]
