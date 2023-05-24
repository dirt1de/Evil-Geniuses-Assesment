import numpy as np
# import math


class ProcessGameState:
    # https://stackoverflow.com/questions/36399381/whats-the-fastest-way-of-checking-if-a-point-is-inside-a-polygon-in-python
    # Check the link above for the benchmark between contains_points() in matplotlib and Ray Tracing algorithm

    def check_is_in_region(df, polygon, z_boundary):
        target_x = df["x"]
        target_y = df["y"]
        target_z = df["z"]

        if (target_z < z_boundary[0]) | (z_boundary[1] < target_z):
            return False

        return polygon.contains_points([(target_x, target_y)])

    # TODO: convert the logic to using 'apply'

    def extract_feature(df, retract_col_name, retract_key_name):
        feature_map_list = []
        for row in range(len(df.index)):
            features = df.loc[:, retract_col_name][row]
            if features is None:
                feature_map_list.append(None)
            else:
                map = {}
                for i in range(len(features)):
                    cur_feature = features[i][retract_key_name]
                    if cur_feature in map:
                        map[cur_feature] += 1
                    else:
                        map[cur_feature] = 1
                feature_map_list.append(map)
        return feature_map_list

    # Angle summation algorithm
    # def get_dist(point1_x, point1_y, point2_x, point2_y):
    #     result = math.sqrt((point2_x - point1_x) ** 2 + (point2_y - point1_y) ** 2)
    #     return result

    # def extract_is_in_region(self, polygon, z_boundary):
    #     self.df['is_in_region'] = self.df.apply(
    #         self.check_is_in_region, args=(polygon, z_boundary), axis=1)

    # def check_is_in_region(df, region, z_boundary):
    #     target_x = df["x"]
    #     target_y = df["y"]
    #     target_z = df["z"]

    #     # if (target_z < z_boundary[0]) | (z_boundary[1] < target_z):
    #     #     return False

    #     degree = 0
    #     for i in range(len(region) - 1):
    #         vertex1 = region[i]
    #         vertex2 = region[i + 1]

    #         # calculate distance of vector
    #         Edge1 = get_dist(vertex1[0], vertex1[1], vertex2[0], vertex2[1])
    #         Edge2 = get_dist(target_x, target_y, vertex1[0], vertex1[1])
    #         Edge3 = get_dist(target_x, target_y, vertex1[0], vertex1[1])

    #         # calculate direction of vector
    #         ta_x = vertex1[0] - target_x
    #         ta_y = vertex1[1] - target_y
    #         tb_x = vertex2[0] - target_x
    #         tb_y = vertex2[1] - target_y

    #         cross_product = tb_y * ta_x - tb_x * ta_y
    #         clockwise = cross_product < 0

    #         # calculate sum of angles
    #         if clockwise:
    #             degree = degree + \
    #                 math.degrees(
    #                     math.acos((Edge2 * Edge2 + Edge3 * Edge3 - Edge1 * Edge1) / (2.0 * Edge2 * Edge3)))
    #         else:
    #             degree = degree - \
    #                 math.degrees(
    #                     math.acos((Edge2 * Edge2 + Edge3 * Edge3 - Edge1 * Edge1) / (2.0 * Edge2 * Edge3)))
    #     # print(degree)
    #     if abs(round(degree) - 360) <= 30:
    #         return True
    #     return False
