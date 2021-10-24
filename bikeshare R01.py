import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data together!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Enter one of the following cities: Chicago, New York City, Washington: ').lower()
        if city not in CITY_DATA:
            print('please select a city from the list above, city you chose is not in the list')
        else:
            break
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter a month from January through June, or all to view data for all months: ').lower()
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        if month not in months:
            print('That\'s not in the months list. Please enter a month from January through June, or all to view data for all months')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter a day of the week or enter all: ').lower()
        day_of_week = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day not in day_of_week :
            print('Enter a day of the week or all')
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# RF Note: loading city data, time and month into DataFrame.
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month   
# RF Note: Month string to interger conversion
    if month != 'all':
        months =['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most popular month, based on your city of interest, is: ', popular_month)

    # TO DO: display the most common day of week
    popular_weekday= df['day_of_week'] .mode()[0]
    print('The most popular weekday, based on your city and month of interest, is: ', popular_weekday)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour= df['hour'] .mode()[0]
    print('The most popular hour is: ', popular_hour)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most common Start Station is: ', popular_start_station) 

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most common End Station is: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] + ' and ' + df['End Station']
    popular_combo = df['combo'].mode()[0]
    print('popular_combo is', popular_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time is ', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time is ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('Count of user types is ',user_type_count)

    # TO DO: Display counts of gender
    if 'Gender' in df: 
        gender_count = df['Gender'].value_counts()
        print('Gender count for the city is ', gender_count)
    else:
        print('Washington doesn\t track gender data')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest_birth_year= df['Birth_Year'].min()
        print('Earliest Birth Year is ', earliest_birth_year)
        recent_birth_year= df['Birth_Year'].max()
        print('Recent Birth Year is ', recent_birth_year)
        common_birth_year= df['Birth_Year'].mode()[0]
        print('Most common Birth Year is ', common_birth_year)
    else:
        print('Washington doesn\t track birth year data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

#RF Note: request post 1st submission to ask the user if they want to see the first five rows
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while True:
        print(df.iloc[start_loc: start_loc + 5])
        view_display = input("Do you wish to continue?: ").lower()
       
if __name__ == "__main__":
	main()