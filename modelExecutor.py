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

model = joblib.load("model.pkl")


def inputs_to_2d_list(age, sex, bmi, children, smoker, region):
    sex = 1 if sex == "f" else 0
    smoker = 1 if smoker == "yes" else 0
    result = [age, sex, bmi, smoker]

    children_encoded = [0] * 6
    children_encoded[children] = 1

    region_encodings = {
        "northeast": [1, 0, 0, 0],
        "northwest": [0, 1, 0, 0],
        "southeast": [0, 0, 1, 0],
        "southwest": [0, 0, 0, 1],
    }
    region_array = region_encodings[region]

    result.extend(children_encoded)
    result.extend(region_array)
    return [result]


def getCost(age, sex, bmi, children, smoker, region):
    inputs_as_list = inputs_to_2d_list(age, sex, bmi, children, smoker, region)
    np_array = np.array(inputs_as_list)
    return model.predict(np_array)[0]
