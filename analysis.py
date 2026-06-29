import pandas as pd
import matplotlib.pyplot as plt

# Nepalko  top 10 cities population data
data = {
    'City': [
        'Kathmandu', 'Pokhara', 'Lalitpur', 'Bharatpur',
        'Biratnagar', 'Birgunj', 'Dharan', 'Butwal',
        'Hetauda', 'Dhangadhi'
    ],
    'Population': [
        1003285, 518452, 284922, 280502,
        242548, 204949, 137705, 118462,
        97996, 90043
    ],
    'Province': [
        'Bagmati', 'Gandaki', 'Bagmati', 'Bagmati',
        'Koshi', 'Madhesh', 'Koshi', 'Lumbini',
        'Bagmati', 'Sudurpashchim'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

print("=== Nepal City Population Data ===")
print(df)
print(f"\nTotal Population (top 10 cities): {df['Population'].sum():,}")
print(f"Average Population: {df['Population'].mean():,.0f}")
print(f"Most Populated: {df.loc[df['Population'].idxmax(), 'City']}")
print(f"Least Populated: {df.loc[df['Population'].idxmin(), 'City']}")

# --- CHART 1: Bar Chart ---
plt.figure(figsize=(12, 5))
colors = ['#ff6b6b' if city == 'Pokhara' else '#00d4ff' for city in df['City']]
bars = plt.bar(df['City'], df['Population'], color=colors, edgecolor='white')
plt.title('Top 10 Cities of Nepal by Population', fontsize=14, fontweight='bold')
plt.xlabel('City')
plt.ylabel('Population')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('chart1_population.png', dpi=150)
plt.show()
print("Chart 1 saved!")

# --- CHART 2: Pie Chart ---
plt.figure(figsize=(8, 8))
plt.pie(
    df['Population'],
    labels=df['City'],
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.Set3.colors
)
plt.title('Population Distribution - Top 10 Nepal Cities', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('chart2_pie.png', dpi=150)
plt.show()
print("Chart 2 saved!")

# --- CHART 3: Province wise total ---
province_data = df.groupby('Province')['Population'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
plt.bar(province_data.index, province_data.values, color='#7c3aed', edgecolor='white')
plt.title('Total Population by Province (Top 10 Cities)', fontsize=14, fontweight='bold')
plt.xlabel('Province')
plt.ylabel('Total Population')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig('chart3_province.png', dpi=150)
plt.show()
print("Chart 3 saved!")

print("\nAll done! 3 charts created successfully!")