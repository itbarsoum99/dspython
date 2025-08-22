import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult_data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_mask = df['education'] == 'Bachelors'
    percentage_bachelors = round((bachelors_mask.sum() / df.shape[0]) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    advanced_degrees = ['Bachelors', 'Masters', 'Doctorate']
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    highered_mask = df['education'].isin(advanced_degrees)
    higher_education = highered_mask.sum()
    lowered_mask = ~highered_mask
    lower_education = lowered_mask.sum()

    # percentage with salary >50K
    higher_education_rich = round(((df[highered_mask]['salary'] == ">50K").sum() / higher_education) * 100, 1)
    lower_education_rich = round(((df[lowered_mask]['salary'] == ">50K").sum() / lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_mask = df['hours-per-week'] == min_work_hours
    num_min_workers = min_mask.sum()

    rich_percentage = ((df[min_mask]['salary'] == ">50K").sum() / num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    salary_mask = df['salary'] == ">50K"
    people_rich = df[salary_mask]['native-country'].value_counts()
    people = df['native-country'].value_counts()
    newdf = pd.concat([people_rich, people], axis=1)
    newdf.columns = ['people_rich', 'people']
    newdf['percentage'] = newdf['people_rich'] / newdf['people']

    highest_earning_country = newdf['percentage'].idxmax()
    highest_earning_country_percentage = round(newdf['percentage'].max() * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_mask = df['native-country'] == "India"
    top_IN_occupation = df[india_mask][salary_mask]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()
