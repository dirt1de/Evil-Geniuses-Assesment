import pandas as pd
import numpy as np
from process_game_state import ProcessGameState
from matplotlib import path
import seaborn as sns
from matplotlib import pyplot as plt


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

    # Q2(a)
    # Rounds of Team 2 on T side and enters the region / Rounds of Team 2 on T side
    team_2_on_t_side_in_region_rounds = df.loc[(
        df['is_in_region'] == True) & (df['side'] == 'T') & (df['team'] == 'Team2')]['round_num'].drop_duplicates()
    team_2_on_t_side = df.loc[(df['side'] == 'T') & (
        df['team'] == 'Team2')]['round_num'].drop_duplicates()

    ratio = len(team_2_on_t_side_in_region_rounds) / len(team_2_on_t_side)
    print(ratio)

    # Q2(c)
    CT_condition = (df['area_name'] == 'BombsiteB') & (
        df['side'] == 'CT') & (df['team'] == 'Team2')
    ax = sns.kdeplot(data=df.loc[CT_condition], x='x', y='y', fill=True,
                     thresh=0, levels=100, cmap="Blues")
    plt.show()
    fig = ax.get_figure()

    return


if __name__ == '__main__':

    main()
