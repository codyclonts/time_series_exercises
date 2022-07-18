### prepare.py file#####
import acquire
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
### store data####


def prepare_sales(df):
    """
        This function takes in sales df and prepares it
    """

    #Convert sales_date to datetime format
    df.sale_date = pd.to_datetime(df.sale_date)

    #Add a month and day of week column
    df['month'] = df.sale_date.dt.month
    df['day_of_week'] = df.sale_date.dt.day_name()

    #Remove the time portion of the date
    df.sale_date = df.sale_date.dt.date

    #Set the index to be the date and sort it
    df = df.set_index('sale_date').sort_index()

    #Add a sales_total column
    df['sales_total'] = df.sale_amount * df.item_price

    return df




def prep_opsd(df):
    df.columns = [column.replace('+','_').lower() for column in df]
    #convert to datetime
    df.date = pd.to_datetime(df.date)
    #set index to date
    df = df.set_index('date').sort_index()
    
    #create month and year columns
    df['month'] = df.index.month_name()
    df['year'] = df.index.year

    #fill na values with 0
    df = df.fillna(0)
    return df


def sales_date_index(df):
    # Reassign the sale_date column to be a datetime type
    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y %H:%M:%S %Z')
    # Set the index as that date and then sort index (by the date)
    df = df.set_index("sale_date").sort_index()
    return df


def sales_new_columns(df):
    # Add a 'month' and 'day of week' column to your dataframe.
    df['month'] = df.index.strftime('%m') + ' ' + df.index.strftime('%b')
    df['day_of_week'] = df.index.strftime('%w') + ' ' + df.index.strftime('%a')
    # Add a column to your dataframe, sales_total, which is a derived from sale_amount (total items) and item_price.
    df['sales_total'] = df.sale_amount * df.item_price
    return df