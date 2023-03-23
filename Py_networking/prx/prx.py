import requests


proxies = {
 "http": "192.168.43.1:8080",
 "https": "192.168.43.1:8080",
}


#get html from site
r = requests.get("http://google.com/", proxies=proxies)

#open empty html file
f = open("TEST.html", "w")
f.write(r.text)
print("open")

#end
input("hit enter to close")
f.close()

#print(r.status_code, r.reason, "\n", r.text)
