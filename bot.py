  
import cloudscraper
import json
#Data
 #Bet Set
base_bet = float(input('Base Bet :'))
if_win = int(input('On Win = '))
if_lose = int(input('On Lose ='))
chance = int(input('Chance ='))
low = int(1000000) - (chance) * int(10000)
num_for = "{:.0f}".format
if base_bet > 0:
    bid = (0 + base_bet) * float(100000000)
else:
    bid = (0 + base_bet) / float(100000000)
print(num_for(int(bid)))
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
dlogin = 'a=Login&Key=258aed99b1924356909fd825d695a9ac&Username=layscape1&Password=aqmar2012&Totp='
dseed = 'a=GetServerSeedHash&s=4b0e122438114b6aa8550df1d4ace992'
total_profit = int(0)
scr = cloudscraper.create_scraper()
def login():
    login = scr.post(url_login, data=dlogin, headers=headers)
login()
total = 0
play = scr.post(url_login, data=dbet, headers=headers).json()
print(play)
num_format = "{:.8f}".format
while True:
    profit = (play['PayOut'] - bid) / float(100000000)
    total += profit
    if play['PayOut'] > 0:
        balance = (play['StartingBalance'] + play['PayOut']) / float(100000000)
        print("WIN",play['PayOut'], "Balance :",num_format(balance),"Profit: ",num_format(profit), "Bet :",bid)
        if base_bet > 0:
            bid = (0 + base_bet) * float(100000000)
        else:
            bid = (0 + base_bet) / float(100000000)
        bid = int(bid)
        print("Total =",num_format(total), end="\r") 
        play = scr.post(url_login, data=dbet, headers=headers).json()
    else:
        balance = (play['StartingBalance'] - base_bet) / float(100000000)
        print("LOSE",play['PayOut'], "Balance :",num_format(balance),"Profit: ",num_format(profit), "Bet :",bid)
        bid = int(bid) * int(if_lose)
        print("Total =",num_format(total), end="\r") 
        play = scr.post(url_login, data={
"a":"PlaceBet",
"s":"4b0e122438114b6aa8550df1d4ace992",
"PayIn": bid,
"Low": low,
"High":"999999",
"ClientSeed":"5664556",
"Currency":"doge",
"ProtocolVersion":"2"
}, headers=headers).json()
