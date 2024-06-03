import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': ['Russian Federation', 'Turkey', 'Romania', 'Ukraine', 'Italy', 
                'Moldova, Republic of', 'Poland', 'Hungary', 'United Kingdom', 'Bulgaria', 
                'Serbia', 'Croatia', 'Georgia', 'Germany', 'Lithuania', 'Slovenia', 'France', 
                'Latvia', 'Slovakia', 'Austria', 'North Macedonia', 'Armenia', 'Azerbaijan', 
                'Czechia', 'Cyprus', 'Spain', 'Belgium', 'Portugal', 'Norway', 'Montenegro', 
                'Netherlands', 'Greece', 'Switzerland', 'Bosnia and Herzegovina', 'Sweden', 
                'Estonia', 'Finland', 'Ireland', 'Denmark', 'Malta', 'Iceland', 'Luxembourg', 
                'Andorra', 'San Marino', 'Liechtenstein', 'Monaco'],
    'Cases': [3500, 1600, 1200, 1500, 800, 650, 900, 1100, 700, 400, 550, 300, 450, 500, 200, 
              150, 100, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 15, 10, 5, 20, 30, 40, 50, 
              25, 15, 10, 5, 10, 20, 30, 40, 50, 10, 5, 5]
}
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(14, 8))
plt.bar(df['Country'], df['Cases'], color='blue')
plt.title('Gesamtmenge der Fälle nach Ländern', fontsize=14)
plt.xlabel('Land', fontsize=12)
plt.ylabel('Anzahl der Fälle', fontsize=12)
plt.xticks(rotation=90)
plt.tight_layout()

# Show the plot
plt.show()
