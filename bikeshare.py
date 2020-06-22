import time
import pandas as pd
import numpy as np
#Adding comment for completion
# Importing CSV data 
CITY_DATA = { 'chicago' : 'chicago.csv',
              'new york' : 'new_york_city.csv',
              'washington' :  'washington.csv' }

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
    # Prompts user to select what city they want to pull data from and accounts for all user inputs
    while True:
               city = input("Which cities data would you like to see? Chicago, New York, Washington? \n").lower()

               if city == 'chicago':
                print("You've selected Chicago's bike data to review.")
                break
               elif city == 'new york':
                print ("You've selected New York's bike data to review.")
                break
               elif city == 'washington':
                print ("You've selected Washington's bike data to review.")
                break
               else:
                print('\nInvalid input\n')


    # TO DO: get user input for month (all, january, february, ... , june)
    # Prompts user to select what month they want to pull data from and accounts for all user inputs
    while True:
        month = input("\nWhich months data would you like to use? Choose between January - June, or all.\n").lower()

        if month == "all" or month =="january" or month =="february" or month =="march" or month =="april" or month =="may" or month =="june":
            print("Let's look the data from {}.".format((month).title()))
            break
        else:
            print("\nInvalid input.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # Prompts user to select what day they want to pull data from and accounts for all user inputs
    while True:
        day = input("\nWhich day do you want to review? Or type 'all' for the whole week.\n ").lower()

        if day == "monday" or day =="tuesday" or day =="wednesday" or day =="thursday" or day =="friday" or day =="saturday" or day =="sunday" or day =="all":
            print("Let's look the data from {}.".format((day).title()))
            break
        else:
            print("\nInvalid input.\n")

    print('-'*40)
    #Returns user input to function
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
    #Importing data into dataframe
    #Utilizing dt functions to grab month number and name for weekday
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['weekday']=df['Start Time'].dt.weekday_name.str.lower()

    # Prompts user if they would like to recieve additional raw data.
    #Nested in order to back out if need be.
    while True:
        raw = input("\n *Would you like to take a look under the hood? (See the raw data) (Yes or No)*\n").lower()
        if raw == 'yes':
            print(df.head())
            while True:
                    raw2= input("\nYou sure you're ready go deeper into the rabbithole? (Yes or No)\n").lower()
                    # Google desciptive functions https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html
                    if raw2 == 'yes':
                        print('\n',df.info())
                        print('\n',df.describe())
                        while True:
                                raw3= input("\nEVEN MORE RAW DATA??? (Yes or No)\n").lower()
                                if raw3 == 'yes':
                                    print("\nSorry the rest is classified :). Continuing queue.\n")
                                    break
                                elif raw3 == 'no':
                                    break
                                else:
                                    print("Invalid Input")

                        break
                    elif raw2 == 'no':
                        break
                    else:
                        print("Invalid Input")
            break
        elif raw == 'no':
            break
        else:
            print("Invalid Input")

    #Selects specific month number plus 1 since array begins at 0
    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['weekday'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # Selects the most common month using mode function for most repeated
    common_month = df['month'].mode()[0]
    print('{} is the most common month.'.format(common_month))

    # TO DO: display the most common day of week
    #Picks the most selected weekday and capitilizes it.
    common_dow = df['weekday'].mode()[0]
    print('{} is the most common day.'.format(str(common_dow).title()))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour #need to update
    common_hour = df['hour'].mode()[0]
    print('{} is the most common hour.'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('{} is the most commonly used start station.'.format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('{} is the most commonly used end station.'.format(common_end))

    # TO DO: display most frequent combination of start station and end station trip
    print('\nThe most frequent combination of start and end station is', common_start, " and ", common_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_tt = sum(df['Trip Duration'])
    print('Total travel time is', total_tt)

    # TO DO: display mean travel time

    mean_tt = df['Trip Duration'].mean()
    print('Mean travel time is ', mean_tt)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #value_count shows some sets of data will include 'dependent'
    cust = df['User Type'].str.count('Customer').sum()
    subs = df['User Type'].str.count('Subscriber').sum()
    dept = df['User Type'].str.count('Dependent').sum()
    print('There are {} customers, {} subscribers, and {} dependents.'.format(int(cust),int(subs),int(dept)))
    # TO DO: Display counts of gender
    #https://stackoverflow.com/questions/16154032/catch-keyerror-in-python
    #https://knowledge.udacity.com/questions/58317
    while True:
        try:
            print(df['Gender'].value_counts())
            break
        except KeyError:
            print('Gender data unavailable')
            break

    # TO DO: Display earliest, most recent, and most common year of birth
    #Scans data for greatest, least, and most repeated data for the column.
    while True:
        try:
            early_yr = df['Birth Year'].min()
            recent_yr = df['Birth Year'].max()
            common_by = df['Birth Year'].mode()
            print('The earliest birth year is {} - The most recent birth rear is {} - The most common birth year is {}.'.format(int(early_yr), int(recent_yr), int(common_by)))
            break
        except KeyError:
            print('Birth Year data unavailable')
            break

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


if __name__ == "__main__":
    main()
