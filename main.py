import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    bol = True
    while bol:
        city = input('enter a city (chicago, new york city, washington): ').lower()

        if city in CITY_DATA:
            bol = False
        else:
            print("invalid entry")
            print("try again")

            # TO DO: get user input for month (all, january, february, ... , june)
    bol = True
    while bol:
        month = input("choose a month (all, january, february, ... , june): ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            bol = False
        else:
            print("invalid month, try again")

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    bol = True
    while bol:
        day = input("choose a day: ").lower()
        if day in ['all', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'monday', 'tuesday']:
            bol = False
        else:
            print('invalid input, try again')

    print('-' * 40)
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

    # loading
    df = pd.read_csv(CITY_DATA[city])

    # convert to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        mths = ['january', 'february', 'march', 'april', 'may', 'june']
        month = mths.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('most common month ', common_month)

    # TO DO: display the most common day of week

    common_day_of_week = df['day_week'].mode()[0]
    print('most common day of week ', common_day_of_week)

    # TO DO: display the most common start hour
    common_hr = df['hour'].mode()[0]
    print('most common hour ', common_hr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print('most common start station ', common_start_station)

    # TO DO: display most commonly used end station

    common_end_station = df['End Station'].mode()[0]
    print('most common end station ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common = df['Start Station'] + " - " + df['End Station']
    print("Most Common Combination: ", common.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print("total travel time is ", travel_time)

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print("average time is ", avg_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('counts of user types is ', user_counts)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\nCounts of Gender: ', df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = int(df['Birth Year'].min())
        print('\nEarliest Year of Birth: ', earliest)
        recent = int(df['Birth Year'].max())
        print('\nMost Recent Year of Birth: ', recent)
        common = int(df['Birth Year'].mode()[0])
        print('\nMost Common Year of Birth: ', common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display(df):
    n = 0
    option = input('\nEnter \'yes\' or \'no\' if you want to display 5 rows of data: ').lower()

    bol = True
    while bol:
        if option == 'yes' and n < df.shape[0]:
            print(df.iloc[n:n + 5, :])
            n += 5
            option = input('\nDo you want to display another 5 rows of data? ').lower()

        if option == 'no' or n > df.shape[0]:
            bol = False
        elif option not in ['yes', 'no']:
            option = input("invalid input, try again: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display(df)

        print('\nwould you like to restart the process?')
        restart = input('Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
