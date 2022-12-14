import pandas
import seaborn
import matplotlib.pyplot as plt

''' 
The best way to complete this activity is to copy the code in this file into a jupyter notebook file you create. This will also you to see your visualizations easier. Once you have finished creating your visuals copy your code back into this file and submit it to Replit. Don't forget to also upload your new code to Github! 
'''

# Step 1: Create a heatmap showing the correlation between the following features: survival, pclass, sex, age, and fare 
corr_heatmap_survived = titanic_data[(titanic_data['Survived'] == 1) & (titanic_data['Embarked'] == "S")]
corr_heatmap_survived

passengers_sex_and_age =titanic_data[titanic_data['Sex'] == 'female' or 'male' or 'kid']['Age']
passengers_sex_and_age

passeners_age_ = (titanic_data['Age'] <= 60.0 )
passengers_age= titanic_data[age_below_60]
seniors_age

# Step 2: Create a bar graph that illustrates how many passengers fell into each of these age ranges: 0 - 16, 17 - 25, 26 -40, 41 - 59, 60 or older
age_group_chart_all_ages = chidren_age_above_0 = (titanic_data['Age'] >= 0.0) chidren_age_below_16 = (titanic_data['Age'] <= 16.0)
young_adults_age_above_17 = (titanic_data['Age'] >= 17.0)
young_adults_age_below_25 = (titanic_data['Age'] <= 25.0)
adults_age_above_26 = (titanic_data['Age'] >= 26.0)
adults_age_below_40 = (titanic_data['Age'] <= 40.0)
mature_adults_age_above_41 = (titanic_data['Age'] >= 41.0)
mature_adults_age_below_59= (titanic_data['Age'] <= 59.0)
seniors_age_above_60 = (titanic_data['Age'] >= 60.0)
seniors_age= titanic_data[age_above_60]
age_group_chart_all_ages

# Step 3: Create a line graph showing the average survival percentage of each of the previous age groups
avg_survival_percentage = titanic_data[(titanic_data['Survived'] == 4) & (titanic_data['Embarked'] == "survived")]
avg_survival_percentage

# Step 4: Create a pie chart that shows the percentage of survivors that were male and the percentage of survivors that were female
survivors = 
avg_survival_gender =  titanic_data[titanic_data['Sex'] == 'male']['Age'] or avg_male_age = titanic_data[titanic_data['Sex'] == 'female']['Age']
avg_fem_age
avg_survival_gender

# Step 5: Create a histogram that shows the distribution of passengers between the three embarking locations: C (Cherbourg), Q (Queenstown), S (Southampton)
titanic_description = cherbourg_survival = titanic_data[(titanic_data['Survived'] == 1) & (titanic_data['Embarked'] == "C")]
cherbourg_survival
queenstown_survival = titanic_data[(titanic_data['Survived'] == 1) & (titanic_data['Embarked'] == "Q")]
queenstown_survival
south_survival = titanic_data[(titanic_data['Survived'] == 1) & (titanic_data['Embarked'] == "S")]
south_survival