# -*- coding: utf-8 -*-
"""
CSS2024 Project option 1

"""

#load pandas and file had to use absoloute path as relative path did not load

import pandas as pd

file = pd.read_csv("C:/Users/LICTAD/OneDrive - University of the Western Cape/Documents/CSS2024/CSS2024/CSS2024 Project/movie_dataset.csv")
#file = pd.read_csv("movie_dataset.csv") 
   
print(file.info())

print(file.describe())

#df = pd.read_csv("movie_dataset.csv")

df = pd.read_csv("C:/Users/LICTAD/OneDrive - University of the Western Cape/Documents/CSS2024/CSS2024/CSS2024 Project/movie_dataset.csv")

#df.drop(['Index'],inplace=True,axis=1)
"""
Question 1
"""
print(df["Rating"].max())

#max ratingg is 9.0

max_rating_index = df["Rating"].idxmax()
value_matching_max_rating = df.loc[max_rating_index, "Rating"]

#Loc54

max_rating = df["Rating"].max()
result = title_for_max_rating = df.loc[df["Rating"] == max_rating, "Title"].values[0]

print(result)

#Dark Knight
"""
Question 2
"""
#Use average (mean) revenue to replace Nan

#movie_dataset.csv

x = df["Revenue (Millions)"].mean()

df["Revenue (Millions)"].fillna(x, inplace = True) 

column_avg = df["Revenue (Millions)"].mean().mean()
print("Revenue Average:")
print(column_avg)

#Average Revenue = 82 956 637
"""
Question 3
"""
#pick rows that year = 2015 to 2017
#calculate mean
#print(df['Revenue (Millions)'].unique())

#df.dropna(subset=["Revenue (Millions)"], inplace=True)
df["Revenue (Millions)"] = pd.to_numeric(df["Revenue (Millions)"], errors='coerce')

# conversion to datetime
#df["Year"] = pd.to_datetime(df["Year"], errors="coerce")



df['Year'] = pd.to_datetime(df['Year'], format='%Y')


#desired_year = 2015, 2016, 2017
start_year = 2015
end_year = 2027

filtered_df = df[(df["Year"].dt.year >= start_year) & (df["Year"].dt.year <= end_year)]
#print (filtered_df)
#nan_check = df["Revenue (Millions)"].isna().any()
#print(f"NaN values present in the column: {nan_check}")
"""
I was having problems with date format hence all the fiddle below
"""
#df.dropna(subset=["Revenue (Millions)"], inplace=True)

mean_value = filtered_df["Revenue (Millions)"].mean()
mean_value = mean_value*100000
import math
rounded_number = math.ceil(mean_value)
print(f"The average value between 2015-17 is: ${rounded_number}")
"""
Question 4
"""
# Filter the df for entries in the year 2016
entries_2016 = df[df["Year"].dt.year == 2016]

# Count the number of entries for 2016
count_entries_2016 = entries_2016.shape[0]

print(f"the numeber of movies released in 2016: {count_entries_2016}")
"""
Question 5
"""

# Count occurrences of "	Christopher Nolan" in the "Director" column
Christopher_Nolan_count = df["Director"].value_counts().get("Christopher Nolan", 0)

# Display the result
print(f"The name 'Christopher Nolan' appears {Christopher_Nolan_count} times.")
"""
Question 6
"""
# Count number of movies with rating 8 or better
#">8"_count = df["Rating"].value_caounts()

# Assuming your DataFrame is named 'df' and the column is named 'rating'
# Count occurrences where the 'rating' is greater than or equal to 8
count_greater_than_eight = (df['Rating'] >= 8).sum()

# Display the result
print(f"The number of times a rating was 8 or better is: {count_greater_than_eight}")
"""
Question 7
"""
# Replace 'desired_director' with the specific director's name you're interested in
desired_director = 'Christopher Nolan'

# Filter the DataFrame for the specific director
director_df = df[df['Director'] == desired_director]

# Calculate the median rating for the selected director
median_rating = director_df['Rating'].median()

# Display the result
print(f"The median rating for {desired_director} is: {median_rating}")
"""
Question 8
"""
#Find the year with the highest average rating?
#mean of each year and then compare

mean_ratings_per_year = df.groupby('Year')['Rating'].mean()

# Find the year with the highest mean rating
max_mean_year = mean_ratings_per_year.idxmax()
max_mean_rating = mean_ratings_per_year.max()

# Display the results
print(f"Mean ratings per year:\n{mean_ratings_per_year}\n")
print(f"The year with the highest mean rating is {max_mean_year} with a mean rating of {max_mean_rating}")

"""
Question 9
"""
#What is the percentage increase in number of movies made between 2006 and 2016?
entries_2006 = df[df["Year"].dt.year == 2006]
count_entries_2006 = entries_2006.shape[0]
#already have a count of 2016
print(f"Number of movies in 2006 {count_entries_2006}")
print(f"Number of movies in 2016 {count_entries_2016}")
#percentage_increase = ((new_value - old_value) / abs(old_value)) * 100
percentage_increase = ((count_entries_2016) - (count_entries_2006)) / abs(count_entries_2006)* 100

print(f"Percentage increase from 2006 to 2016 in the number of movies: {percentage_increase}%") 

"""
Question 10
"""
#count how many times an actors name appears

#need to seperate the names in the column
names_list = df["Actors"].str.split(', ')

# Flatten the list of lists into a single list
flat_names_list = [name for sublist in names_list.dropna() for name in sublist]

# Count the occurrences of each individual name
name_counts = pd.Series(flat_names_list).value_counts()

most_common_name = name_counts.idxmax()
print("Most common actor:", most_common_name)

"""
Question 11
"""
#Count genres
"""
I have left in all my attempts at this question
"""
# Split the comma-separated values into a list
#genre_list = df['Genre'].str.split(', ')

# Flatten the list of lists into a single list
#flat_genre_list = [genre for sublist in genre_list.dropna() for genre in sublist]

# Count the occurrences of each individual name
#genre_counts = pd.Series(flat_genre_list).value_counts()

# Display the counts
#print(genre_counts)


#genre_list = df["Genre"].str.split(', ')
#unique_names_count = len(set(genre_list))
#unique_values_df = df[genre_list].drop_duplicates()
#complete_list = unique_values_df[genre_list].tolist()

#df = pd.DataFrame({"Genre": [1, 2, 3, 4, 5, 6]})
#genre_list = df["Genre"].str.split(', ')
#genre_list = df["Genre"].tolist()
#genre_list = df["Genre"].str.split(', ')

#print("Converted list:", genre_list)
 

# Use set() to get unique names and len() to count them
#unique_names_count = len(set(genre_list))

#print("Number of unique names:", unique_names_count)

df["Genre"] = df["Genre"].str.split(',')
df_exploded = df.explode("Genre")
unique_count = df_exploded["Genre"].nunique()

print("The number of diffrent Genres is:", (unique_count))

"""
Question 12

The Directors with the most movies rated over 8
The Directors With the highest average revenue
Plot the common Directors
The Actor with highest average Revenue
The Actor with highet average rating
Genre with highest average rating
Genre with Highest Average Revenue 
Runtime vs Revenue vs Rating
Discription for key words?

"""

import matplotlib.pyplot as plt
# Example: Filtering by Rating above 8 and Runtime greater than 120 minutes
filtered_df = df[(df["Rating"] > 8) & (df["Runtime (Minutes)"] > 120)]


# Assuming 'Rating' and 'Runtime (Minutes)' are columns
plt.scatter(filtered_df["Rating"], filtered_df["Runtime (Minutes)"])
plt.xlabel("Rating")
plt.ylabel("Runtime (Minutes)")
plt.title("Scatter Plot Runtime vs Rating")
plt.show()

#Revenue vs Runtime
plt.scatter(filtered_df["Revenue (Millions)"], filtered_df["Runtime (Minutes)"])
plt.xlabel("Revenue (Millions)")
plt.ylabel("Runtime (Minutes)")
plt.title("Scatter Runtime vs Revenue")
plt.show()

filtered_df = df[(df["Rating"] > 8) & (df["Revenue (Millions)"] > 300)]
plt.scatter(filtered_df["Rating"], filtered_df["Runtime (Minutes)"])
plt.xlabel("Rating")
plt.ylabel("Revenue (Millions)")
plt.title("Scatter Plot of Revenue vs Rating")
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Filter the DataFrame 
filtered_df = df[(df["Revenue (Millions)"] > 300) & (df["Rating"] > 8)]

# Create a scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x="Director", y="Revenue (Millions)", hue="Rating", palette="viridis")

# Adjust plot aesthetics
plt.title("Relationship between Director, Revenue (Millions) > 300, and Rating > 8")
plt.xlabel("Director")
plt.ylabel("Revenue (Millions)")
plt.xticks(rotation=45, ha="right")  

# Rotate x-axis labels for better visibility

# Show the plot
plt.tight_layout()
plt.show()



#df_exploded contains the exploded "Genre" column
genre_mean_revenue = df_exploded.groupby("Genre")["Revenue (Millions)"].mean()
highest_mean_genre = genre_mean_revenue.idxmax()

print(f"The genre with the highest mean revenue is: {highest_mean_genre}")

genre_mean_revenue = df_exploded.groupby("Genre")["Revenue (Millions)"].mean()

import matplotlib.pyplot as plt
sorted_genres = genre_mean_revenue.sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sorted_genres.plot(kind='bar', color='skyblue')
plt.title("Mean Revenue by Genre")
plt.xlabel("Genre")
plt.ylabel("Mean Revenue")
plt.xticks(rotation=45, ha="right") 

# Rotate x-axis labels for better readability
plt.tight_layout()


#The Actors with highest mean Revenue


names_list = df["Actors"].str.split(', ')

# Flatten the list of lists into a single list
flat_names_list = [name for sublist in names_list.dropna() for name in sublist]

# Count the occurrences of each individual name
name_counts = pd.Series(flat_names_list).value_counts()

actor_mean_revenue = df.groupby("Actors")["Revenue (Millions)"].mean()

import matplotlib.pyplot as plt

sorted_actors = actor_mean_revenue.sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sorted_actors.head(10).plot(kind='bar', color='skyblue')
plt.title("Mean Revenue per Actor (Top 10)")
plt.xlabel("Actor")
plt.ylabel("Mean Revenue")
plt.xticks(rotation=45, ha="right") 

# Rotate x-axis labels for better readability
plt.tight_layout()

plt.show()


