def display(df):
    print (df.head())

def rate_diff(df):
    groups = df.groupby('Type')
    free_apps_df = groups.get_group('Free')
    paid_apps_df = groups.get_group('Paid')
    # del free_apps_df['Price']
    # del paid_apps_df['Price']
    paid_apps_df.to_csv('paid_apps.csv')
    free_apps_df.to_csv('free_apps.csv')


def content_rating_diff(df):
    
    groups = df.groupby('Content Rating')

    everyone_apps_df = groups.get_group('Everyone')
    everyone_ten_df = groups.get_group('Everyone 10+')
    teen_apps_df = groups.get_group('Teen')
    mature_apps_df = groups.get_group('Mature 17+')
    adults_apps_df = groups.get_group('Adults only 18+')
    unrated_apps_df = groups.get_group('Unrated')

    everyone_apps_df.to_csv('everyone_apps.csv')
    teen_apps_df.to_csv('teen_apps.csv')
    everyone_ten_df.to_csv('everyone_ten.csv')
    mature_apps_df.to_csv('mature_apps.csv')
    adults_apps_df.to_csv('adults_apps.csv')
    unrated_apps_df.to_csv('unrated_apps.csv')


def rating_round_off(df):
    for index,row in df.iterrows():
            df.loc[index, 'Rating Roundoff'] = round(row.Rating, 0)

