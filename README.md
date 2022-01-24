# Visual-Map-COVID19

![dpc-logo-covid19](https://user-images.githubusercontent.com/43711362/150822069-0c6e4df8-af51-4411-ba1e-a1e5efb0161a.png)

A very simple Dashboard python script to visualize Italian data about the SARS-COV-2 pandemic (data provided by https://www.protezionecivile.it/attivita-rischi/rischio-sanitario/emergenze/coronavirus )

The 'regioni.py' script returns the (little choropleth) map of Italian regions with different colors (unfortunately it needs to be zoomed a bit). 
Each region is colored according to the parameter that is given by the user (like the total amount of infected people or the total amount of death, and other). The color intensity meaning can be understood reading the side color-scale.

The 'graph.py' script returns a linechart based on the parameter that is given by the user (like the amount of total lab-tested covid cases or the total amount of hospitalized people, and other).

Both the previous mentioned scripts needs a csv file from which to read the data.

IMPORTAN DISCLAIMER: this dashboard is NOT official and should NOT be used to retrieve any data or to make any formal conclusion about the covid_19 pandemic. This dashboard has been made as a purely personal project with the goal to improve python skills and the use of its libraries: Dash, Plotly and Pandas dataframe.
Always refer to official information source such as https://www.salute.gov.it/portale/nuovocoronavirus/dettaglioContenutiNuovoCoronavirus.jsp?area=nuovoCoronavirus&id=5351&lingua=italiano&menu=vuoto (for Italy).
