import pandas as pd

# TODO: convert the logic to using 'apply'


def extract_feature(df, retract_col_name, retract_key_name):
    feature_map_list = []
    for row in range(len(df.index)):
        # print(row)
        features = df.loc[:, retract_col_name][row]
        # print(weapons)
        map = {}
        for i in range(len(features)):
            cur_feature = features[i][retract_key_name]
            if cur_feature in map:
                map[cur_feature] += 1
            else:
                map[cur_feature] = 1
        feature_map_list.append(map)
    df['extracted_feature_map'] = feature_map_list


def main():
    # Convert from parquet to df
    df = pd.read_parquet('game_state_frame_data.parquet', engine='pyarrow')

    retract_col_name = "inventory"
    retract_key_name = 'weapon_class'

    extract_feature(df.iloc[:6], retract_col_name, retract_key_name)

    return


if __name__ == '__main__':

    main()
