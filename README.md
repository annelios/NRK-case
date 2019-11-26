# Case NRK

## Innhold
Jeg har laget to filer: modify_dictionary.py og analyze_data.py
Første fil må kjøres først, for at fil nr to skal fungere.

#### modify_dictionary.py:
Filen henter inn data fra spesifisert nettside oppgavetekst og formaterer varibaler i dataframe og da særlig variabler med timestamp formatering. Lager noen ekstra variabler og lagrer et modifisert datagrunnlag som skrives til ny fil i mappetrukturen det kjøres fra.

#### analyze_data.py:
Filen henter inn data fra modifisert datagrunnlag som ble gjort i modify_dictionary.py. Forsøker å analysere variablene i dataframen så godt jeg klarer gitt tiden jeg hadde til rådighet. Jeg har forsøkt å illustrere ulike aspekter ved datagrunnlaget i ulike figurer. Tar blant annet vare på brukerne som har sett all episodene for å finne ut hvor mange som ev har "bingewatchet" episodene.

Skulle gjerne gått dypere inn i materien, hvis jeg hadde hatt mer tid.

## Interessante videre analyser
Dersom det også hadde vært tilgjenglig data om personene som ser på unge lovende hadde det kunne vært spennende å gjøre ytterligere analyser. Interessant dersom følgende informasjon om bruker hadde vært tilgjengelig
  - alder
  - bosted
  - bosituasjon
  - hvilke andre serier/filmer ser denne bruker også på (av NRK sine serier/filmer)
