from spyne import Application, rpc, ServiceBase, Integer, String, ComplexModel
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

# Define Complex Models
class Contact(ComplexModel):
    id = Integer
    name = String
    phone = String
    email = String  # Tambah field email

class Address(ComplexModel):
    id = Integer
    street = String
    city = String
    country = String  # Tambah field country

# SOAP Service
class ContactAddressService(ServiceBase):
    contacts = {
        1: Contact(id=1, name="Aura Fitrah Shaqinah", phone="0812345", email="aura@gmail.com")  # Data baru
    }
    addresses = []

    @rpc(Integer, _returns=Contact)
    def getContact(ctx, contact_id):
        return ContactAddressService.contacts.get(contact_id)

    @rpc(Address, _returns=String)
    def createAddress(ctx, address):
        ContactAddressService.addresses.append(address)
        return "Address created successfully"

# Setup Application
application = Application([ContactAddressService],
    tns='http://example.com/contact_address',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == '__main__':
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("SOAP server running on http://localhost:8000")
    server.serve_forever()
