from app import login, tambah, get_users

def test_login_valid():
    """Test login dengan kredensial valid"""
    assert login("admin", "12345") == True

def test_login_invalid():
    """Test login dengan kredensial invalid"""
    assert login("user", "salah") == False

def test_tambah_positif():
    """Test penjumlahan bilangan positif"""
    assert tambah(2, 3) == 5

def test_tambah_negatif():
    """Test penjumlahan bilangan negatif"""
    assert tambah(-1, -4) == -5

def test_get_users_status_code():
    """Test status code API"""
    response = get_users()
    assert response.status_code == 200

def test_get_users_data_not_empty():
    """Test data API tidak kosong"""
    response = get_users()
    assert len(response.json()) > 0