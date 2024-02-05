import pandas as pd

spolki = ['bos', 'pko', 'pkn', 'pzu']
data_pocz = '20100101'
data_kon = '20221231'
interwaly = ['d', 'w', 'm', 'y']

for spolka in spolki:
    for interwal in interwaly:
        url = "https://stooq.pl/q/d/l/?s="+spolka+"&d1="+data_pocz+"&d2="+data_kon+"&i="+interwal
        dane_gieldowe = pd.read_csv(url)
        print("Notowanie:"+spolka)
        print(dane_gieldowe.head())