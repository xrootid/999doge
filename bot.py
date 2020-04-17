import cloudscraper
import json
#Data
 #Bet Set
base_bet = input('Base Bet :')
bid = base_bet
if_win = input('On Win = ')
if_lose = input('On Lose =')
chance = input('Chance =')
low = int(1000000) - (int(chance) * int(10000))
dbet = {
"a":"PlaceBet",
"s":"4b0e122438114b6aa8550df1d4ace992",
"PayIn": bid,
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
def play():
    play = scr.post(url_login, data=dbet, headers=headers).json()
    bet_int = int(bid)
    profit = play['PayOut'] - bet_int
    if play['PayOut'] > 0:
         balance = play['StartingBalance'] + play['PayOut']
         print("WIN",play['PayOut'], "Balance :",balance,"Profit: ",profit)
         bid = int(base_bet)
         start()
    else:
         balance = play['StartingBalance'] - bet_int
         print("LOSE",play['PayOut'], "Balance :",balance,"Profit: ",profit)
         bid = int(base_bet) * int(if_lose) #not work
         start()
def start():
	play()
login()
total_profit = int(0)
i = 10
while i < 5: #not work
	if i == 3:
		break
	i += 1
	start()
	total = total_profit + profit
	print("\nTotal =",total) #not work
