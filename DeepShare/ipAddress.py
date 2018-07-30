import urllib.request, json 
with urllib.request.urlopen("http://localhost:8080/json/") as url:
    data = json.loads(url.read().decode())
    #print(data)
    #print(data["url"])
    #print(data["workers"])
    ip_address = "10.200.172.246" 
    worker = data["workers"]
    for x in worker:
        if x["host"] == ip_address :
            print("ip address of worker machine :" + x["host"])
            print("Total cores of worker machine:"+ str(x["cores"]))
            print("Total memory of worker machine:"+ str(x["memory"]))
