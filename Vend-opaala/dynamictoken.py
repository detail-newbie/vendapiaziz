import psycopg2
import requests
import json

url = "https://sohailtest.vendhq.com/api/1.0/token"

payload = {'code': '4GYI1hpMtzRwTjUO7cBox_adQrdWbf13Dn5Ihvho','client_id': 'uFkMUoUPfPsBGNbNydBD7ssqr1JOJd2C','client_secret': 'kP6ZszgEXm3VQ2ENWlV5XJuuFmmsIXYc','grant_type': 'authorization_code',
'redirect_uri': 'http://example.org/callback'}
files = [

]
headers = {
  
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))

exit() 


