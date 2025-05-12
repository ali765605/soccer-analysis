import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create DataFrame with Premier League 2024-25 top scorers data
players_data = {
    'Player': ['Mohamed Salah', 'Alexander Isak', 'Erling Haaland', 'Bryan Mbeumo', 
               'Chris Wood', 'Yoane Wissa', 'Ollie Watkins', 'Cole Palmer', 
               'Matheus Cunha', 'Jean-Philippe Mateta'],
    'Club': ['Liverpool', 'Newcastle', 'Man City', 'Brentford',
             'Nottingham Forest', 'Brentford', 'Aston Villa', 'Chelsea', 
             'Wolves', 'Crystal Palace'],
    'Goals': [28, 23, 21, 18, 18, 16, 15, 14, 14, 13],
    'Penalties': [9, 4, 2, 5, 3, 0, 2, 3, 0, 2]
}

# Create DataFrame
df = pd.DataFrame(players_data)

# Add a column for non-penalty goals
df['Non-Penalty Goals'] = df['Goals'] - df['Penalties']

# Display the data
print(df)

# Group by club and sum goals
goals_by_club = df.groupby('Club')['Goals'].sum().reset_index().sort_values('Goals', ascending=False)

# Plotting with a custom color palette and improved styling
plt.figure(figsize=(12, 8))
sns.set_style("whitegrid")
custom_palette = sns.color_palette("bright", len(goals_by_club))

# Create bar plot
ax = sns.barplot(x='Club', y='Goals', data=goals_by_club, palette=custom_palette)

# Enhance the visual appeal
plt.title('Total Goals by Top Scorers per Club (Premier League 2024-25)', fontsize=16)
plt.xlabel('Club', fontsize=14)
plt.ylabel('Goals', fontsize=14)
plt.xticks(rotation=45, ha='right')

# Add value labels on top of bars
for i, v in enumerate(goals_by_club['Goals']):
    ax.text(i, v+0.5, str(v), ha='center', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()

# Basic statistical analysis
print("\nStatistical Summary of Goals by Top Scorers:")
print(df['Goals'].describe())

# Club with highest-scoring player
top_scorer = df.loc[df['Goals'].idxmax()]
print(f"\nTop Scorer: {top_scorer['Player']} ({top_scorer['Club']}) with {top_scorer['Goals']} goals")

# Club with most goals from penalties
pens_by_club = df.groupby('Club')['Penalties'].sum().reset_index().sort_values('Penalties', ascending=False)
print(f"\nClub with most penalty goals: {pens_by_club.iloc[0]['Club']} with {pens_by_club.iloc[0]['Penalties']} penalties")

