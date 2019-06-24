# Added second comment to code - as per task 4.C
# Added one comment to code - as per task 4.C


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    '''
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or 'all' to apply no month filter
        (str) day - name of the day of week to filter by, or 'all' to apply no day filter
    '''
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('\nWould you like to see data for Chicago, New York or Washington?:\n').lower()
    while city not in ['chicago','new york','washington']:
        city = input('\nPlease type in Chicago, New York or Washington:\n')
        city = city.lower()
        
    # get user input for month (all, january, february, ... , june)

    month = input('\nPlease type in the month you wish to see the data for: January, February, March, April, May or June. Type All for no month filter:\n').lower()
    while month not in ['january','february','march','april','may','june','all']:
        month = input('\nOops! Something went wrong. Please type in the month you wish to see the data for: January, February, March, April, May or June. Type All for no month filter:\n')
            
    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('\nPlease type in the day of the week you wish to see the data for: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday. Type All for no weekday filter:\n').lower()
    while day not in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']:
        day = input('\nOops! Something went wrong. Please type in the month you wish to see the data for: January, February, March, April, May or June. Type All for no month filter:\n')
    
    print('\nYou have selected data for '+city.capitalize()+'\nMonth filters: '+month.capitalize()+'\nWeekday filters: '+day.capitalize())
    print('\nanalyzing the data .. .. .. .. .. .. ..')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    '''
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or 'all' to apply no month filter
        (str) day - name of the day of week to filter by, or 'all' to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    '''

    df = pd.read_csv(CITY_DATA[city])
    
    #convert date columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    #extract month and day of week as new columns
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).dayofweek
    
    #apply month filter, if any
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df['month'] == month,:]
        
    #apply day filter, if any
    if day != 'all':
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = days.index(day)
        df = df.loc[df['day_of_week'] == day,:]
    
    return df


def time_stats(df):
    '''Displays statistics on the most frequent times of travel.'''

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is: {}'.format(str(df['month'].mode().values[0])))

    # display the most common day of week
    print('The most common day of the week is: {}'.format(str(df['day_of_week'].mode().values[0])))

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print('The most common start hour is: {}'.format(str(df['start_hour'].mode().values[0])))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    '''Displays statistics on the most popular stations and trip.'''

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is: {} '.format(df['Start Station'].mode().values[0]))

    # display most commonly used end station
    print('The most commonly used end station is: {}'.format(df['End Station'].mode().values[0]))

    # display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ ' ' + df['End Station']
    print('The most frequent combination of start and end station trip is: {}'.format(df['routes'].mode().values[0]))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    '''Displays statistics on the total and average trip duration.'''

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['duration'] = df['End Time'] - df['Start Time']

    # display total travel time
    print('The total travel time is: {}'.format(str(df['duration'].sum())))

    # display mean travel time
    print('The mean travel time is: {}'.format(str(df['duration'].mean())))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df, city):
    '''Displays statistics on bikeshare users.'''

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nThe various user types are:')
    print(df['User Type'].value_counts())

    if city != 'washington':
        # Display counts of gender
        print('\nThe counts of gender are:')
        print(df['Gender'].value_counts())

        # Display earliest year of birth
        print('\nThe earliest year of birth is: {}'.format(str(int(df['Birth Year'].min()))))
        
        # Display latest year of birth
        print('\nThe latest year of birth is: {}'.format(str(int(df['Birth Year'].max()))))
        
        # Display most common year of birth
        print('\nThe most common year of birth is: {}'.format(str(int(df['Birth Year'].mode().values[0]))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_data(df):
    #display the first five rows of raw data used for analysis, ask user if he wants to display another 5 rows
    
    first_row = 0
    last_row = 5
    show_data = input('\nWould you like to see the first five rows of raw data used for your analysis? Y/N \n').lower()
    while True:
        if show_data == 'n':
            break
            
        if show_data == 'y':
            df['day_of_week'] += 1 #adjust the index of the day of the week for display
            print(df.iloc[first_row:last_row,:])
            first_row += 5
            last_row += 5
            show_data = input('\nWould you like to see the next five rows of raw data used for your analysis? Y/N \n').lower()
            if show_data == 'n':
                break
        else:
            show_data = input('\nOops! Something went wrong. Would you like to see the first five rows of raw data used for your analysis? Y/N \n').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        show_data(df)
        restart = input('\nWould you like to restart? Y/N\n')
        if restart.lower() != 'y':
            print('\nThanks for analyzing the bikeshare data with me. Have a good day!\n')
            break


if __name__ == '__main__':
	main()
