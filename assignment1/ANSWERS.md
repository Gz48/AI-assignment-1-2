# Assignment 1: International Football Results Analysis

This report documents the analysis performed on the Kaggle International Football Results dataset (1872–2024) as part of the Football Analysis Exercise.

---

## Step 1: Load the CSV

We begin by importing the necessary pandas library and loading the dataset from the CSV file.

```python
import pandas as pd

df = pd.read_csv("results.csv")
df.head()
```

---

## Basic Exploration

### 1. How many matches are in the dataset?
**Logic**: We use the `df.shape` attribute which returns the dimensions of the dataframe. The first element (index 0) represents the total number of rows (matches).

```python
print(f"Total Matches: {df.shape[0]}")
# Result: ~49,000 matches
```

### 2. What is the earliest and latest year in the data?
**Logic**: We convert the 'date' column to a datetime format using `pd.to_datetime`. We then use `.min()` and `.max()` on the year component to find the timeline.

```python
df['date'] = pd.to_datetime(df['date'])
print(f"Earliest Year: {df['date'].dt.year.min()}")
print(f"Latest Year: {df['date'].dt.year.max()}")
# Result: 1872 to 2024
```

### 3. How many unique countries are there?
**Logic**: We collect all unique team names from both the 'home_team' and 'away_team' columns using a Set to ensure no duplicates, then count the total.

```python
unique_countries = set(df['home_team'].unique()).union(set(df['away_team'].unique()))
print(f"Unique Countries: {len(unique_countries)}")
# Result: 333 unique countries/teams
```

### 4. Which team appears most frequently as home team?
**Logic**: We use the `.value_counts()` method on the 'home_team' column and take the top result.

```python
print(df['home_team'].value_counts().head(1))
# Result: Sweden (515 appearances)
```

---

## Goals Analysis

**Create total goals:**
```python
df["total_goals"] = df["home_score"] + df["away_score"]
```

### 5. What is the average number of goals per match?
**Logic**: We calculate the arithmetic mean of the 'total_goals' column.

```python
print(f"Average Goals Per Match: {df['total_goals'].mean():.2f}")
# Result: 2.94
```

### 6. What is the highest scoring match?
**Logic**: We find the maximum value in 'total_goals' and filter the dataframe to identify the specific match.

```python
max_goals = df["total_goals"].max()
print(df[df["total_goals"] == max_goals][['date', 'home_team', 'away_team', 'home_score', 'away_score']])
# Result: Australia vs American Samoa (31-0)
```

### 7. Are more goals scored at home or away?
**Logic**: We sum the total goals scored in the 'home_score' and 'away_score' columns separately and compare them.

```python
home_sum = df["home_score"].sum()
away_sum = df["away_score"].sum()
print(f"Home: {home_sum}, Away: {away_sum}")
# Result: Home goals are significantly higher.
```

### 8. What is the most common total goals value?
**Logic**: We use the `.mode()` function to find the most frequent value in the 'total_goals' column.

```python
print(f"Most Common Total Goals: {df['total_goals'].mode()[0]}")
# Result: 2 goals
```

---

## Match Results

**Create match outcome:**
```python
def match_result(row):
    if row["home_score"] > row["away_score"]:
        return "Home Win"
    elif row["home_score"] < row["away_score"]:
        return "Away Win"
    else:
        return "Draw"

df["result"] = df.apply(match_result, axis=1)
```

### 9. What percentage of matches are home wins?
**Logic**: We use `value_counts(normalize=True)` to convert the counts of each result into a percentage of the total.

```python
print(df["result"].value_counts(normalize=True) * 100)
# Result: ~48.91%
```

### 10. Does home advantage exist?
**Logic**: We compare the percentage of 'Home Win' results against 'Away Win' results. Since Home Wins are significantly more frequent, a home advantage is confirmed.

```python
# Home Win (~49%) vs Away Win (~28%)
```

### 11. Which country has the most wins historically?
**Logic**: We identify all winners from both home and away scenarios, concatenate them, and find the most frequent winner using `value_counts()`.

```python
home_wins = df[df['result'] == 'Home Win']['home_team']
away_wins = df[df['result'] == 'Away Win']['away_team']
total_wins = pd.concat([home_wins, away_wins])
print(total_wins.value_counts().head(1))
# Result: Brazil
```

---

## Visualization

### Histogram of goals
**Logic**: Visualizing the distribution of total goals using `plt.hist()`.

```python
import matplotlib.pyplot as plt
df["total_goals"].hist(bins=15)
plt.title("Distribution of Goals Per Match")
plt.show()
```

### Bar chart of match outcomes
**Logic**: Using a bar chart to compare the frequency of Home Wins, Away Wins, and Draws.

```python
df['result'].value_counts().plot(kind='bar')
plt.title("Match Outcomes")
plt.show()
```

### Top 10 teams by total wins
**Logic**: Plotting the top 10 countries by their total number of historical wins.

```python
total_wins.value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Teams by Total Wins")
plt.show()
```
