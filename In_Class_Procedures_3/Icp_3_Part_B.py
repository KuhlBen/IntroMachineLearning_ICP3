import pandas as pd
#1 Read the provided CSV file ‘data.csv’.
data = ("data.csv")
df = pd.read_csv(data)
print(df)

#2 Show the basic statistical description about the data.

print(df.describe())
table = df.copy()

print(table[10:25])
# Check for null values and replace them with the mean
mean_calories = df["Calories"].mean()
mean_duration = df["Duration"].mean()
mean_pulse = df["Pulse"].mean()
mean_maxPulse = df["Maxpulse"].mean()

df["Calories"].fillna(value=mean_calories, inplace=True)
df["Duration"].fillna(value=mean_duration, inplace=True)
df["Pulse"].fillna(value=mean_pulse, inplace=True)
df["Maxpulse"].fillna(value=mean_maxPulse, inplace=True)
table = df.copy()
print(table[10:25])

# Aggregate data using min, max, count, and mean for selected columns
result = df.groupby("Pulse").agg({"Duration": ['mean', 'min', 'max']})
print(result)

# Filter the dataframe based on calories values between 500 and 1000
filter_cal = df.loc[(df["Calories"] > 500) & (df["Calories"] < 1000)]
print(filter_cal)

# Filter the dataframe based on calories values > 500 and pulse < 100
filter_Cal_pulse = df.loc[(df["Calories"] > 500) & (df["Pulse"] < 100)]
print(filter_Cal_pulse)

# Create a new dataframe without the 'Maxpulse' column
df_modified = df.drop(columns=['Maxpulse'])

# Delete the 'Maxpulse' column from the main dataframe
df.drop(columns=['Maxpulse'], inplace=True)

# Convert the datatype of Calories column to int datatype
df["Calories"] = df["Calories"].astype(int)

# Print the modified dataframe and confirm changes
print(df)
print(df_modified)
