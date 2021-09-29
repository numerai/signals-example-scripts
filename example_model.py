
import pandas as pd
from halo import Halo
from sklearn.ensemble import GradientBoostingRegressor

TARGET_NAME = 'target_20d'
PREDICTION_NAME = 'signal'

spinner = Halo(text='', spinner='dots')


def main():
    """Creates example_signal_yahoo.csv to upload for validation and live data submission"""

    spinner.start('Reading data')
    train = pd.read_csv('example_training_data_yahoo.csv')
    tournament = pd.read_csv('example_tournament_data_yahoo.csv')
    spinner.succeed()

    feature_names = train.filter(like='feature_').columns.to_list()

    spinner.start('Training model')
    model = GradientBoostingRegressor(subsample=0.1)
    model.fit(train[feature_names], train[TARGET_NAME])
    spinner.succeed()

    spinner.start('Predicting test and live data')
    # predict test and live data
    tournament[PREDICTION_NAME] = model.predict(tournament[feature_names])
    spinner.succeed()

    # prepare and writeout example file
    spinner.start('Writing signal upload file')
    diagnostic_df = tournament.copy()
    diagnostic_df['data_type'] = diagnostic_df.data_type.fillna('live')
    diagnostic_df[['bloomberg_ticker', 'friday_date', 'data_type', 'signal']].reset_index(drop=True).to_csv('example_signal_yahoo.csv', index=False)
    spinner.succeed()


if __name__ == '__main__':
    main()
