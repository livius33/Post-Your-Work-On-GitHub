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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("enter the city: ").lower()
    while city not in["chicago", "new york city", "washington"]:
        city = input ("please choose between chicago, new york city or washington: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input ("enter the month: ").lower()
    while month not in["all", "january", "februar", "march", "april", "may", "june"]:
        month = input ("enter the month: january, februar, ..., june: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ("enter a day: ").lower()
    while day not in["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        day = input ("enter the day: monday, ..., friday: ").lower()

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
    df = pd.read_csv("{}.csv".format(city))
    
    #convert the columns of "Start Time" and "End Time" into the format of "yyyy-mm-dd"
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #extract month data from "Start Time" and put it into a new column called month
    df['month'] = df['Start Time'].dt.month

    #filter it by the month
    if month != 'all':
        # use the index of the months list to get the right output
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by each month to create a new df
        df = df[df['month'] == month]

    # extract each day from "Start Time" and put it into a new column called month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by eacg day of a week
    if day != 'all':
        # filter by day to create a new df
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is: ", df['month'].value_counts().idxmax())

    # TO DO: display the most common day of week
    print("The most common day of the week is: ", df['day_of_week'].value_counts().idxmax())

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is: ", df['hour'].value_counts().idxmax())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: ", df ['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print("The most common end station is: ", df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip")
    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum() / 3600.0
    print("The total travel time in hours is: ", total_duration)

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean() / 3600.0
    print("The mean travel time in hours is: ", mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #TODO Display counts of user types
    
    try:
        print(df['User Type'].value_counts())
    except:
        print('The column is not here')
        
    #TODO: Display counts of gender
    
    try:
        print(df['Gender'].value_counts())
    except:
        print('The column is not here')

    #TODO: Display earliest, most recent, and most common year of birth
     
    try:
        birth_year=df['Birth Year']

        earliest_year = birth_year.min()
        
        print('The most earliest birth year is: {}'.format(earliest_year))
        
        print('The column is not here')
        
        birth_year=df['Birth Year']
        most_recent_birthday=birth_year.max()
        print('The most recent birth year is: {}'.format(most_recent_birthday))
        
        most_common_year =birth_year.value_counts().idxmax()
        print("The most common birth year is: {}".format(most_common_year))
    
    except:
        print('This data is not available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(city):
    """Display the data; 5 rows at a time"""
    print('\n Raw data is available to check. \n')
    display_data =input( 'Do you want to have a look on the raw data? yes or no:  ')
    while display_data == 'yes':
        try: 
            for chunk in pd.read_csv(CITY_DATA[city],chunksize=6):
                print(chunk)
                display_raw = input('\nDo you like to see another 5 rows of the raw data? yes or no: .\n')
               
                if display_raw != 'yes':
                    print('Thank you!')
                    break
            break
        except KeyboardInterrupt:
                        print('Thank You!')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
