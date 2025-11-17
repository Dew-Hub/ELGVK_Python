import  requests

api="https://api.exchangerate-api.com/v4/latest/usd"
response = requests.get(api)
data = response.json()
print(f"Güncel Dolar/TL kuru {data["rates"]["TRY"]}")


