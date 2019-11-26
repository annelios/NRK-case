import pandas as pd

def date_utc(s):
     return lambda x: pd.to_datetime(s, utc=True)

data = pd.read_csv('https://storage.googleapis.com/nrk-us/intervjuoppgave/unge-lovende.csv', sep=',', index_col=0)
data['visitEndTime'] = (data.visitStartTime + data.timeWithinVisit)

with open("data.csv", "w") as file:
    csv =  data.to_csv()
    file.write(csv)

unge_lovende = pd.read_csv('data.csv',
                    sep=',',
                    date_parser=date_utc,
                    converters={'visitStartTime': lambda x: pd.Timestamp.utcfromtimestamp(int(x))
                                ,'visitEndTime': lambda x: pd.Timestamp.utcfromtimestamp(int(x))
                    })

unge_lovende['ep'] = unge_lovende.programId.str.extract('([^a-zA-Z]+)', expand=False)
unge_lovende['ep'] = ((unge_lovende['ep'].astype(int)- 20000014)/100).astype(int)

# dropper variabler som ikke lenger brukes
unge_lovende.drop('programId', axis=1, inplace=True)
unge_lovende.drop('timeWithinVisit', axis=1, inplace=True)


## lager time variabel som får object-format (looper ikke, men nå object)
unge_lovende['time'] = pd.to_datetime(unge_lovende['visitEndTime']).dt.time


## lager analysevariabler
unge_lovende['dayStart'] = unge_lovende['visitStartTime'].dt.day_name()
unge_lovende['dayEnd'] = unge_lovende['visitEndTime'].dt.day_name()
unge_lovende['monthStart'] = unge_lovende['visitStartTime'].dt.month_name()
unge_lovende['monthEnd'] = unge_lovende['visitEndTime'].dt.month_name()

with open("unge_lovende.csv", "w") as file:
    csv =  unge_lovende.to_csv()
    file.write(csv)
