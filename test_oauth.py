import requests

# Configuración
TOKEN_URL = 'http://127.0.0.1:8000/o/token/'
API_URL = 'http://127.0.0.1:8000/api/libros/'

CLIENT_ID = 's92gkQhUhVc9lS0b1huEwewEUA0SMIdWn5Abq5K1'
CLIENT_SECRET = '3hqctlLmXovlXnUjVr6f0XySyb4rZVO0s0d85qm82U2i4RTdgmqy2Y8lqBDsSBfIqiMS2PSnMEXWW01JH3ZMv79bQ1vXAKugndTutnNUHyVx1IkrDSZ7reUGfukc9A4s'
USERNAME = 'admin'
PASSWORD = 'admin123'

print("=== Obteniendo Token OAuth 2.0 ===")

# Obtener token
response = requests.post(TOKEN_URL, data={
    'grant_type': 'password',
    'username': USERNAME,
    'password': PASSWORD,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'scope': 'read write'
})

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data['access_token']
    
    print(f"✅ Token obtenido: {access_token[:50]}...")
    
    # Usar token para acceder a API
    headers = {'Authorization': f'Bearer {access_token}'}
    api_response = requests.get(API_URL, headers=headers)
    
    print(f"Status Code: {api_response.status_code}")
    print(f"Data: {api_response.json()}")
else:
    print(f"❌ Error: {response.status_code}")
    print(response.json())