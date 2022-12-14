import pandas
''' When going through the assignment, keep in mind that to actually see these variables you need to use python's print() statement to see their values printed out in replit's console 
'''

# Step 1: Use the appropriate pandas method to read the titanic data into your python file
titanic_data = pandas.read_csv("titanic.csv")
print(titanic_data)

# Step 2(a): Use the pandas method that reads the first 25 lines of the dataset
first_25_passengers = titanic_data.head(25)
first_25_pasengers

# Step 2(b): Use the pandas method thats reads the last 25 lines of the dataset
last_25_passengers = titanic_data.tail(25)
last_25_pasengers

# Step 3: Use the pandas method that only tells us the number of rows and columns in our data
first_shape= titanic_data.shape
titanic_shape

# Step 4: Describe the titanic data
titanic_description = titanic_data.descrive
titanic_description

# Step 5(a): How many passengers were between the ages of 0 to 16?
chidren_age_above_0 = (titanic_data['Age'] >= 0.0)
chidren_age_below_16 = (titanic_data['Age'] <= 16.0)
chidren_age = titanic_data[age_above_0 & age_below_16]
chidren_age

# Step 5(b): How many passengers were between the ages of 17 to 25?
young_adults_age_above_17 = (titanic_data['Age'] >= 17.0)
young_adults_age_below_25 = (titanic_data['Age'] <= 25.0)
young_adults_age = titanic_data[age_above_17 & age_below_25]
young_adults_age

# Step 5(c): How many passengers were between the ages of 26 to 40?
adults_age_above_26 = (titanic_data['Age'] >= 26.0)
adults_age_below_40 = (titanic_data['Age'] <= 40.0)
adults = titanic_data[age_above_26 & age_below_40]
adults

# Step 5(d): How many passengers were between the ages of 41 to 59?
mature_adults_age_above_41 = (titanic_data['Age'] >= 41.0)
mature_adults_age_below_59= (titanic_data['Age'] <= 59.0)
mature_adults_age = titanic_data[age_above_41 & age_below_59]
mature_adults_age

# Step 5(e): How many passengers were 60 or older?
seniors_age_above_60 = (titanic_data['Age'] >= 60.0)
seniors_age= titanic_data[age_above_60]
seniors_age

# Step 6: How many values are missing from the "age" column
missing_ages = titanic_data.shape[0] -titanic_data['Age'].count()
missing_ages

# Step 7: List out all the available passengers' ages
age_list =  titanic_data[titanic_data['Ages'] == 'all ages']['Age']
age_list

# Step 8: Filter the DataFrame to find all passengers who boarded the Titanic at Port Cherbourg
cherbourg_paasengers = titanic_data[titanic_data['Embarked'] == 'C']
cherbourg_paasengers

# Step 9(a): Find the average age of all female passengers
avg_fem_age = titanic_data[titanic_data['Sex'] == 'female']['Age']
avg_fem_age

# Step 9(b): Find the average age of all male passengers
avg_male_age =  titanic_data[titanic_data['Sex'] == 'male']['Age']
avg_male_age

# Step 10(a): Find the survival percentage of passengers in group "C"
cherbourg_survival = titanic_data[(titanic_data['Survived'] == 1) & (titanic_data['Embarked'] == "C")]
cherbourg_survival

# Step 10(b): Find the survival percentage of passengers in group "Q"
queenstown_survival = titanic_data[(titanic_data['Survived'] == 1) & (titanic_data['Embarked'] == "Q")]
queenstown_survival

# Step 10(c): Find the survival percentage of passengers in group "S"
south_survival = titanic_data[(titanic_data['Survived'] == 1) & (titanic_data['Embarked'] == "S")]
south_survival