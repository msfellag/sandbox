import requests

BASE = "http://127.0.0.1:5000/"

#response = requests.get(BASE + "helloworld")
print("1 - getApplicationPerUser")
print("2 - getApplicationPerJob")

while True:
    choice = input()
    if choice == "1":
        endpoint = "getApplicationPerUser/"
        break
    elif choice == "2":
        endpoint = "getApplicationPerJob/"
        break
    else:
        print("error chose again")

userId = input("\nid : ")

response = requests.get(BASE + endpoint + str(userId))
print(response.json())