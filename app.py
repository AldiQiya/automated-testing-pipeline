import requests

def login(username, password):
    """Fungsi untuk simulasi login"""
    if username == "admin" and password == "12345":
        return True
    return False

def tambah(a, b):
    """Fungsi penjumlahan"""
    return a + b

def get_users():
    """Fungsi untuk mengambil data dari API"""
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response