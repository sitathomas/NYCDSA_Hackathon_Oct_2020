import pandas as pd

data_folder = '../data/'

def merge_dfs():
    churn = pd.read_csv(data_folder + 'trunc_churn.csv')
    members = pd.read_csv(data_folder + 'trunc_members.csv')
    transactions = pd.read_csv(data_folder + 'trunc_transaction.csv')
    users = pd.read_csv(data_folder + 'trunc_users.csv')

    data = churn.merge(members, on='msno').merge(transactions, on='msno').merge(users, on='msno')
    data.to_csv(data_folder + 'kkbox_merged.csv', index=False)