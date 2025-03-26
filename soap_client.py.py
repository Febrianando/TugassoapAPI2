from zeep import Client

# Load WSDL
client = Client('http://localhost:8000/soap_service?wsdl')

# Test getContact
contact = client.service.getContact(1)
print(f"Contact: {contact.name}, No.Telp: {contact.phone}, Email: {contact.email}")  # Tampilkan email

# Test createAddress
address_data = {
    'id': 1,
    'street': 'Jl H Abd Majid No 81',
    'city': 'Lamongan',
    'country': 'Indonesia'  # Tambah field country
}
status = client.service.createAddress(address_data)
print(f"Address: {address_data['street']}, {address_data['city']}, {address_data['country']}")
print(f"Status: {status}")
