import requests

def fetchUserDataQ8(userIdQ8):
    responseQ8 = requests.get(f"https://api.fake.com/users/{userIdQ8}")
    if responseQ8.status_code == 200:
        return responseQ8.json()
    return {"error": "User not found"}