# Visual-Map-COVID19
A very simple Dash-based python script to visualize Italian data about the SARS-COV-2 pandemic (data provided by https://www.protezionecivile.it/attivita-rischi/rischio-sanitario/emergenze/coronavirus )

The 'regioni.py' script returns the (little) map of Italian regions with different colors (unfortunately it needs to be zoomed a bit). 
Each region is colored according to the parameter that is given by the user (like the total amount of infected people or the total amount of death, and other). The color intensity meaning can be understood reading the side color-scale.

The 'graph.py' script returns a linechart based on the parameter that is given by the user (like the amount of total lab-tested covid case or the total amount of hospitalized people, and other).
