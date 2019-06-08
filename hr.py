import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-csv_dir', required=True, type=str, default=None)
parser.add_argument('-session_length', required=True, type=str, default=None)

args = parser.parse_args()

session_file = args.csv_dir
session_length = args.session_length

def find_mean(heart_rate_array, num_seconds):
    can_continue = True
    i = 0
    max_mean = 0
    while can_continue:
        session = heart_rate_array[i:i + num_seconds]
        if session.mean() > max_mean:
            max_mean = session.mean()
        i += 1
        if (i + num_seconds) > len(heart_rate_array):
            can_continue = False
    return max_mean

if os.path.isfile(session_file):
    try:
        df = pd.read_csv(session_file)

        times = df['Sport']
        times = times[2:]
        hr = df['Date']
        hr = hr[2:]

        x = pd.DataFrame()
        x['hr'] = hr
        x['times'] = times
        x.reset_index(inplace=True)
        x.drop('index', axis=1, inplace=True)

        num_seconds = int(float(session_length) * 60)

        heart_rate_array = x['hr'].apply(lambda y: float(y))

        max_mean = find_mean(heart_rate_array, num_seconds)
        print(f'max average hr is {round(max_mean,2)}')
    except:
        print('failed!')
else:
    print('file not found')



