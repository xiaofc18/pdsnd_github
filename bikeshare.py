import time
import calendar
import pandas as pd
import numpy as np

# define city name to the input data
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# define filter function
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Hello! Let\'s explore some US bikeshare data!')
    city_list = ['chicago','new york city','washington']
    right_typing = False
    while(right_typing == False):
        city = input("Which city do you want to choose between chicago, new york city and washington: ").lower()

        if city in city_list:
            print(city + ' is chosen.')
            right_typing = True
        else:
            print('please check your typing if the city name is correctly spelled.')

    # get user input for month (all, january, february, ... , june)
    month_list = ['all', 'january', 'february','march', 'april','may', 'june']
    right_typing = False
    while(right_typing == False):
        month = input("Which month do you want to choose between all, january, february, march, april, may and june: ").lower()

        if month in month_list:
            print(month + ' is chosen.')
            right_typing = True
        else:
            print('please check your typing if the month name is correctly spelled.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    weekday_list = ['all', 'monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']
    right_typing = False
    while(right_typing == False):
        day = input("Which month do you want to choose between all, monday, tuesday,wednesday,thursday,friday,saturday, sunday: ").lower()

        if day in weekday_list:
            print(day + ' is chosen.')
            right_typing = True
        else:
            print('please check your typing if the weekday name is correctly spelled.')


    print('-'*40)
    return city, month, day

#####################################
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #show 5 rows each time when the answer is not 'no'.
    furtherDisplay = True
    n = 0
    while(furtherDisplay == True):
        n = n + 1
        moreData = input('\nWould you like to have a look at the raw data? Enter yes or no.\n').lower()
        if moreData != 'no':
            df_select = df.iloc[5*(n-1):(5*n)]
            print(df_select)

        else:
            print('Let us have a look at some statistics.')
            furtherDisplay = False


    return df

#####################################
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('The most common month is ' + calendar.month_name[popular_month] + '.')  ###import the module

	# display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is ' + popular_day_of_week + '.')

	# display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is ' + str(popular_hour) + '.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#####################################
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most common used start station is ' + popular_start_station + '.')

	# display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common used end station is ' + popular_end_station + '.')

	# display most frequent combination of start station and end station trip
    df2 = df.assign(station_combination = df['Start Station']+ ' --> ' +df['End Station'])
    popular_station_combination = df2['station_combination'].mode()[0]
    print('The most frequent combination of start station and end station trip is ' + popular_station_combination + '.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#####################################
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is ' + str(total_travel_time) + ' seconds or around ' + str(int(total_travel_time/60)) + ' minutes.')

	# display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time is ' + str(int(mean_travel_time)) + ' seconds or around ' + str(int(mean_travel_time/60)) + ' minutes.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#####################################
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count summary of different user types: ')
    print(user_types)


    print('-'*10)
	# Display counts of gender  (only available for NYC and Chicago)

    df_col_name = list(df.columns.values)
    if 'Gender' in df_col_name:
        gender_count = df['Gender'].value_counts()
        print('Count summary of both genders: ')
        print(gender_count)
    else:
        print('No available info about Gender for Washington.')

    print('-'*10)
	# Display earliest, most recent, and most common year of birth  (only available for NYC and Chicago)
    if 'Birth Year' in df_col_name:
        birth_year_earliest = df['Birth Year'].min()
        birth_year_latest = df['Birth Year'].max()
        birth_year_common = df['Birth Year'].mode()[0]
        print('The earliest year of birth is ' + str(int(birth_year_earliest)) + '.')
        print('The most recent year of birth is ' + str(int(birth_year_latest)) + '.')
        print('The most common year of birth is ' + str(int(birth_year_common)) + '.')
    else:
        print('No available data for Birth Year in Washington.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#####################################
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

if __name__ == "__main__":
	main()
