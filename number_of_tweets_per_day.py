import pandas as pd
def number_of_tweets_per_day(df):
    date_count = {}
    col = df['Date']
    for entry in col:
        if entry in date_count.keys():
            date_count[entry] +=1
        else:
            date_count[entry] = 1
    return pd.DataFrame(date_count.items(), columns = ['Date', 'Tweets'])