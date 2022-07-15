import pandas as pd
import requests
import os

def get_items(use_cache=True):
    '''
    This function checks for a csv and returns the csv as a df if one exists. 
    If no csv exists, it creates one, saves it, then returns the csv as a df.
    '''

    filename = 'items.csv'
    # check for csv
    if os.path.isfile(filename) and use_cache:
        return pd.read_csv(filename)
    
    else:
        # gather data from the first page and create and empty array to store the information
        domain = 'https://python.zgulde.net'
        endpoint = '/api/v1/items'

        # create empty array to hold items
        items = []
        
        # loop through pages
        while True: 
            url = domain + endpoint
            response = requests.get(url)
            data = response.json()
            items.extend(data['payload']['items'])
            endpoint = data['payload']['next_page']
            if endpoint is None:
                break
        
        df = pd.DataFrame(items)
        df.to_csv('items.csv', index = False)

        return df 

def get_stores(use_cache =True):
   '''
    This function checks for a csv and returns the csv as a df if one exists. 
    If no csv exists, it creates one, saves it, then returns the csv as a df.
    '''
    
    filename = 'stores.csv'
    # check for csv
    if os.path.isfile(filename) and use_cache:
        return pd.read_csv(filename)
    
    else: 
        # gather data from the first page and create and empty array to store the information
        domain = 'https://python.zgulde.net'
        endpoint = '/api/v1/stores'
        stores = []
        
        # loop through pages
        while endpoint is not None:
            url = domain + endpoint
            response = requests.get(url)
            data = response.json()
            stores.extend(data['payload']['stores'])
            endpoint = data['payload']['next_page']

        # cache to csv
        df = pd.DataFrame(stores)
        df.to_csv('stores.csv', index = False)
        
        return df



def get_sales(use_cache = True):
    '''
    This function checks for a csv and returns the csv as a df if one exists. 
    If no csv exists, it creates one, saves it, then returns the csv as a df.
    '''
    filename = 'sales.csv'

    # check for csv
    if os.path.isfile(filename) and use_cache:
        return pd.read_csv(filename)

    else:
        #Gather data
        print('Gathering data using API...')
        domain = 'https://python.zgulde.net'
        endpoint = '/api/v1/sales'
        sales = []
        while endpoint is not None:
            url = domain + endpoint
            response = requests.get(url)
            data = response.json()
            sales.extend(data['payload']['sales'])
            endpoint = data['payload']['next_page']

        # cache to csv
        df = pd.DataFrame(sales)
        df.to_csv('sales.csv', index = False)

        return df


def get_merged_data(use_cache=True):
    '''
    This function checks for a csv and returns the csv as a df if one exists. 
    If no csv exists, it creates one, saves it, then returns the csv as a df.
    '''
    filename = 'merged_data.csv'

    #Check for the csv cache
    if os.path.isfile(filename) and use_cache:
        return pd.read_csv(filename)
    
    else:
        #Get items data
        items = get_items()
        
        #Get stores data
        stores = get_stores()
        
        #Get sales data
        sales = get_sales()
        
        #Merge into a single dataframe
        sales = sales.rename(columns={'store':'store_id', 'item':'item_id'})
        
        #merge stores and sales
        df = pd.merge(sales, stores, how='left', on='store_id')
        #merge items
        df = pd.merge(df, items, how='left', on='item_id')
                             
        # cache to csv
        df.to_csv('merged_data.csv', index = False)
                             
        return df


def get_german_power_data(use_cache=True):
    '''
    This function checks for a csv and returns the csv as a df if one exists. 
    If no csv exists, it creates one, saves it, then returns the csv as a df.
    '''
    
    filename = 'german_power.csv'
    
    if os.path.isfile(filename) and use_cache:
        return pd.read_csv(filename)
    
    else:
        df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
        
        df.to_csv('german_power.csv', index=False)
        
        return df