import cloudscraper, json, sys, importlib, random
from warna import *
choice = input("Use Your Current Custom Config? Y/N")
if choice == 'Y':
    from config import *
    ch = random.randint(chance1, chance2)
else :
    print("You will use ultimate config please see this base bet before")
    print("[1] Balance 100 DOGE+ = 0.001")
    print("[2] Balance 200 DOGE+ = 0.002")
    print("[3] Balance 300 DOGE+ = 0.003")
    print("[4] Balance 400 DOGE+ = 0.004")
    print("[5] Balance 500 DOGE+ = 0.005")
    print("[6] Balance 600 DOGE+ = 0.006")
    print("[7] Balance 700 DOGE+ = 0.007")
    base_bet = float(input("Base Bet :"))
    Username = input("Username :")
    Password = input("Password :")
    if_lose = int(3)
    chance1 = int(65) ##isi sama jika chance tidak random
    chance2 = int(65) ##isi sama jika chance tidak random
    target_profit = float(input("Target Profit :"))
ch = random.randint(chance1, chance2)
low = int(1000000) - (ch) * int(10000)
num_for = "{:.0f}".format
if base_bet > 0:
    bid = (0 + base_bet) * float(100000000)
else:
    bid = (0 + base_bet) / float(100000000)
dbet = {
"a":"PlaceBet",
"s":"4b0e122438114b6aa8550df1d4ace992",
"PayIn": int(bid),
"Low": low,
"High":"999999",
"ClientSeed":"5664556",
"Currency":"doge",
"ProtocolVersion":"2"
}

headers = {
"user-agent": "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.93 Mobile Safari/537.36",
"content-type": "application/x-www-form-urlencoded",
"accept": "*/*",
"x-requested-with": "com.reland.relandicebot",
"sec-fetch-site": "cross-site",
"sec-fetch-mode": "cors",
"accept-encoding": "gzip, deflate",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
"cookie": "lang=id"
}
url_login = 'https://www.999doge.com/api/web.aspx'
dlogin = 'a=Login&Key=258aed99b1924356909fd825d695a9ac&Username='+Username+'&Password='+Password+'&Totp='
dseed = 'a=GetServerSeedHash&s=4b0e122438114b6aa8550df1d4ace992'
total_profit = int(0)
scr = cloudscraper.create_scraper()
def login():
    login = scr.post(url_login, data=dlogin, headers=headers)

login()
total = 0
play = scr.post(url_login, data=dbet, headers=headers).json()
num_format = "{:.8f}".format
while total < target_profit:
    ch = random.randint(chance1, chance2)
    low = int(1000000) - (ch) * int(10000)
    profit = (play['PayOut'] - bid) / float(100000000)
    bidshow = (0 + bid) / 100000000
    total += profit
    if play['PayOut'] > 0:
        balance = (play['StartingBalance'] + play['PayOut']) / float(100000000)
        print(hijau,"[W]",putih, hijau,"Profit: ",num_format(profit),putih, "Bet :",num_format(bidshow))
        if base_bet > 0:
            bid = (0 + base_bet) * float(100000000)
        else:
            bid = (0 + base_bet) / float(100000000)
        bid = int(bid)
        print(birutua,"Total =",num_format(total),putih, "Balance :",num_format(balance), end="\r") 
        play = scr.post(url_login, data={"a":"PlaceBet","s":"4b0e122438114b6aa8550df1d4ace992","PayIn": bid,"Low": low,"High":"999999","ClientSeed":"5664556","Currency":"doge","ProtocolVersion":"2"}, headers=headers).json()
    else:
        balance = (play['StartingBalance'] - base_bet) / float(100000000)
        print(merah,"[L]",putih, merah,"Profit: ",num_format(profit),putih, "Bet :",num_format(bidshow))
        bid = int(bid) * int(if_lose)
        print(birutua,"Total =",num_format(total),putih, "Balance :",num_format(balance), end="\r") 
        play = scr.post(url_login, data={"a":"PlaceBet","s":"4b0e122438114b6aa8550df1d4ace992","PayIn": bid,"Low": low,"High":"999999","ClientSeed":"5664556","Currency":"doge","ProtocolVersion":"2"}, headers=headers).json()
else:
    print(kuning,"Yay sudah mencapai target profit : ",num_format(total))
