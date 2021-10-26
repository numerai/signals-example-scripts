import argparse
import os
import pandas as pd
from pathlib import Path

from halo import Halo
from opensignals.data import yahoo
from opensignals.features import RSI, SMA

spinner = Halo(text='', spinner='dots')


def main(output_dir=None):

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

    training_data_output_path = 'example_training_data_yahoo.csv'
    tournament_data_output_path = 'tournament_data_yahoo.csv'

    if output_dir is not None:
        os.makedirs(output_dir, exist_ok=True)
        training_data_output_path = f'{output_dir}/example_training_data_yahoo.csv'
        tournament_data_output_path = f'{output_dir}/example_tournament_data_yahoo.csv'

    train.to_csv(training_data_output_path)
    tournament_data = pd.concat([test, live])
    tournament_data.to_csv(tournament_data_output_path)

    spinner.succeed()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Signals example data pipeline')
    parser.add_argument('--output_dir', default=None)

    args = parser.parse_args()
    main(args.output_dir)
