import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = {}
    for race in df["race"].unique():
      races[race] = len(df[df["race"] == race])
    race_count = pd.Series(races)

    # What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(len(df[df["education"] == "Bachelors"]) / len(df) * 100, 1)

    with_degree = df[(df["education"] == "Doctorate") | (df["education"] == "Masters") | (df["education"] == "Bachelors")]
    not_with_degree = df[(df["education"] != "Doctorate") & (df["education"] != "Masters") & (df["education"] != "Bachelors")]
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round(len(with_degree) / len(df) * 100, 1)
    lower_education = 100 - higher_education

    # percentage with salary >50K
    higher_education_rich = round(len(with_degree[with_degree["salary"] == ">50K"]) / len(with_degree) * 100, 1)
    lower_education_rich = round(len(not_with_degree[not_with_degree["salary"] == ">50K"]) / len(not_with_degree) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df["hours-per-week"] == min_work_hours])

    rich_percentage = round(len(df[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")]) / len(df[df["hours-per-week"] == min_work_hours]) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    countries = df["native-country"].unique()
    countries_rich_percentage = {}
    for country in countries:
      df_t = df[df["native-country"] == country]
      countries_rich_percentage[country] = round(len(df_t[df_t["salary"] == ">50K"]) / len(df_t) * 100, 1)

    highest_earning_country = max(countries_rich_percentage, key=countries_rich_percentage.get)
    
    highest_earning_country_percentage = countries_rich_percentage[highest_earning_country]

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"].describe().top

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
