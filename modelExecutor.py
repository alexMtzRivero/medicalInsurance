import joblib
import numpy as np

# age                 52.00
# is_female            0.00
# bmi                 47.74
# is_smoker            0.00
# children_0           0.00
# children_1           1.00
# children_2           0.00
# children_3           0.00
# children_4           0.00
# children_5           0.00
# region_northeast     0.00
# region_northwest     0.00
# region_southeast     1.00
# region_southwest     0.00


def getCost(age, sex, bmi, children, smoker, region):
    model = joblib.load("model.pkl")
    np_array = np.array(
        [
            [
                52.00,
                0.00,
                47.74,
                0.00,
                0.00,
                1.00,
                0.00,
                0.00,
                0.00,
                0.00,
                0.00,
                0.00,
                1.00,
                0.00,
            ]
        ]
    )
    return model.predict(np_array)[0]
