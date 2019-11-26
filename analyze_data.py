import pandas as pd
import matplotlib.pyplot as plt

mod_data = pd.read_csv('unge_lovende.csv',
                    sep=',',
                    index_col=0)


## statistikk
print(mod_data.describe())

grp_userId = mod_data.groupby("userId")['ep'].sum()
grp_ep = mod_data.groupby("ep")['userId'].nunique()

# plotter antall episoder per unik bruker på ti observasjoner
mod_data.groupby("userId")['ep'].count().head(10).plot(kind="bar", label="antall episoder")
plt.xlabel("unike brukere")
plt.legend()
plt.title("Antall episoder per unik bruker på de ti første obs")
plt.show()

# plotter antall unike brukere per episode
mod_data.groupby("ep")['userId'].nunique().plot(kind="bar", label="unike brukere")
plt.xlabel("Episode")
plt.legend()
plt.title("Antall unike brukere per episode")
plt.show()

# plotter fordeling av episoder sett per ukedag
mod_data.groupby("dayStart")['ep'].count().plot(kind="pie")
plt.title("Fordeling av episoder påbegynt per ukedag")
plt.show()
mod_data.groupby("dayEnd")['ep'].count().plot(kind="pie")
plt.title("Fordeling av episoder avsluttet per ukedag")
plt.show()

# lager variabel for hvilket år episoden ble påbegynt og hvilket år den ble avsluttet
mod_data['startYear'] = mod_data['visitStartTime'].apply(lambda x: x[:4]).astype(int)
mod_data['endYear'] = mod_data['visitEndTime'].apply(lambda x: x[:4]).astype(int)

# lager to nye variabel for å koble måned og år
# for å se hvilken måned (i hvilket år) episoden ble påbegynt og hvilken måned (i hvilket år) avsluttetstart
# lager kopi av endYear og startYear
new = mod_data.startYear.astype(str).copy()
new2 = mod_data.endYear.astype(str).copy()

# concatenating year with month (burde vært year-month)
mod_data["startMonthYear"]= mod_data["monthStart"].str.cat(new, sep ="-")
mod_data["endMonthYear"]= mod_data["monthEnd"].str.cat(new2, sep ="-")


## henter ut alle brukerid som har sett samtlige episoder
all_ep  = mod_data[mod_data["ep"] == 6].copy()
print(all_ep["userId"].head(10))


# plotter antall brukere som påbegynte en episode i ulike måneder
all_ep.groupby("startMonthYear")['userId'].count().plot(kind="bar", label="brukerid")
plt.xlabel("Måned episode start")
plt.legend()
plt.title("Antall brukere som har påstartet en episod per måned")
plt.show()

# plotter antall brukere som avsluttet episoden i ulike måneder
all_ep.groupby("endMonthYear")['userId'].count().plot(kind="bar", label="brukerid")
plt.xlabel("Måned episode slutt")
plt.legend()
plt.title("Antall brukere som har avsluttet en episod per måned")
plt.show()

#lager tilsvarende fiurer (måned for påbeygnt og avsluttet episode), nå som pie chart
# måned for påbeygnt episode
all_ep.groupby("startMonthYear")['userId'].count().plot(kind="pie", label="brukerid")
plt.xlabel("Måned episode start")
plt.legend()
plt.title("Måned for påbegynt episode")
plt.show()

#  måned for avsluttet episode
all_ep.groupby("endMonthYear")['userId'].count().plot(kind="pie", label="brukerid")
plt.xlabel("Måned episode slutt")
plt.legend()
plt.title("Måned for avsluttet episode")
plt.show()


# lager et uttrekk med data for brukere som har sett alle epsiodene
data_allEp = mod_data[mod_data["userId"].isin(all_ep.userId)].copy()

# plotter hvilke måneder som flest brukere har avsluttet episodene
data_allEp.groupby("endMonthYear")['userId'].count().plot(kind="bar", label="Brukere som har sett alle episoder")
plt.xlabel("Måned episode avsluttet")
plt.legend()
plt.show()


# concatenating endMonthYear with ep
new3 = data_allEp.ep.astype(str).copy()
data_allEp["endMonthYear-ep"] = data_allEp["endMonthYear"].str.cat(new3, sep ="-")

#lager datasett for antall brukere som så ferdig ep 6 i desember
lastEp_des15  = data_allEp[data_allEp["endMonthYear-ep"] == "December-2015-6"].copy()
#lager datasett for antall brukere som så ferdig ep 1 i desember
firstEp_des15  = data_allEp[data_allEp["endMonthYear-ep"] == "December-2015-1"].copy()


#antall brukere som så ferdig første episode (ep 1) i desember 2015
firstEp_des15.groupby("endMonthYear")['userId'].nunique().plot(kind="bar", label="Brukere som har sett alle episoder")
plt.xlabel("Måned episode avsluttet")
plt.legend()
plt.title("Antall unike brukere som så ferdig ep 1 ila des 2015")
plt.show()

#antall brukere som så ferdig siste episode (ep 6) i desember 2015
lastEp_des15.groupby("endMonthYear")['userId'].nunique().plot(kind="bar", label="Brukere som har sett alle episoder")
plt.xlabel("Måned episode avsluttet")
plt.legend()
plt.title("Antall unike brukere som så ferdig ep 6 ila des 2015")
plt.show()

# lagrer data for brukere som har sett alle episodene i en ny datafil
with open("user_allEp.csv", "w") as file:
    csv =  data_allEp.to_csv()
    file.write(csv)
