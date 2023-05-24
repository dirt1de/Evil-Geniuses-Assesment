import pandas as pd
import numpy as np
from process_game_state import ProcessGameState
from matplotlib import path


def main():
    # Convert from parquet to df
    df = pd.read_parquet('game_state_frame_data.parquet', engine='pyarrow')

    retract_col_name = "inventory"
    retract_key_name = 'weapon_class'

    df['extracted_feature_map'] = ProcessGameState.extract_feature(
        df, retract_col_name, retract_key_name)

    polygon = path.Path(
        [(-1735, 250), (-2024, 398), (-2806, 742), (-2472, 1233), (-1565, 580)])
    z_boundary = [285, 421]

    df['is_in_region'] = df.apply(
        ProcessGameState.check_is_in_region, args=(polygon, z_boundary), axis=1)

    # print(len(df.loc[df['is_in_region'] == True]))
    return


if __name__ == '__main__':

    main()
