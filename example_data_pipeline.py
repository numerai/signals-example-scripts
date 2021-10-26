import os
import pandas as pd
from pathlib import Path

from halo import Halo
from opensignals.data import yahoo
from opensignals.features import RSI, SMA

spinner = Halo(text='', spinner='dots')

db_dir = Path('db')

yahoo.download_data(db_dir)

features_generators = [
    RSI(num_days=5, interval=14, variable='adj_close'),
    RSI(num_days=5, interval=21, variable='adj_close'),
    SMA(num_days=5, interval=14, variable='adj_close'),
    SMA(num_days=5, interval=21, variable='adj_close'),
]

spinner.start('Generating features')

train, test, live, feature_names = yahoo.get_data(db_dir,
                                                  features_generators=features_generators,
                                                  feature_prefix='feature')

# TODO: just doing this for testing
path = '/var/opt/signals'
os.makedirs(path, exist_ok=True)

train.to_csv(f'{path}/example_training_data_yahoo.csv')
tournament_data = pd.concat([test, live])
tournament_data.to_csv(f'{path}/example_tournament_data_yahoo.csv')

spinner.succeed()
