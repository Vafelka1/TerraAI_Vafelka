import gradio as gr
import random
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
#import shap
import catboost as cb

matplotlib.use("Agg")
X_train = pd.read_csv('dfc_10.csv')
y_train = X_train.pop('confidence')

cat_features=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
cat_features_names=['race', 'sex', 'age', 'smoke', 'ecog', 'tumor_load', 'kras', 'p53', 'stk11', 'keapi1', 'xlt', 'not_squamous_status', 'pd11_status', 'preference']
rus_labels=['Раса', 'Пол', 'Возраст', 'Статус курения', 'ECOG',
       'Есть опухолевая нагрузка? (симптомная опухоль)', 'Ко-мутации KRAS',
       'Ко-мутации p53.', 'Ко-мутации STK11', 'Ко-мутации KEAP1',
       'Срок от окончания ХЛТ',
       'Молекулярный статус (только для неплоскоклеточного рака)',
       'PD-L1 статус', 'Предпочтение пациента по ответу на терапию'
        ]
model = cb.CatBoostClassifier(loss_function='MultiClass',
#                              task_type = "GPU",
                              eval_metric='Accuracy')

model.load_model('langcancer_10_cb.cbm')

#explainer = shap.TreeExplainer(model)

#grid = {'learning_rate': [0.03, 0.1],
#        'depth': [4, 6, 10],
#        'l2_leaf_reg': [1, 3, 5,],
#        'iterations': [50, 100, 150]}
#
#
#model.grid_search(grid,train_dataset)
#pred = model.predict(X_test)

def predict(*args):
    df = pd.DataFrame([args], columns=cat_features_names)
    print(df.head())
    df = df.astype({col: "category" for col in cat_features_names})
    pos_pred = model.predict(df)
    print(pos_pred)
    return pos_pred[0][0]

cat_features_names=['race', 'sex', 'age', 'smoke', 'ecog', 'tumor_load', 'kras', 'p53', 'stk11', 'keapi1', 'xlt', 'not_squamous_status', 'pd11_status', 'preference']

import json

with open("vocab.json", "r") as fp: 
    unique = json.load(fp)

unique_race = sorted(unique[0][1])
unique_sex = sorted(unique[1][1])
unique_age = sorted(unique[2][1])
unique_smoke = sorted(unique[3][1])
unique_ecog = unique[4][1]
unique_tumor_load = sorted(unique[5][1])
unique_kras = sorted(unique[6][1])
unique_p53 = sorted(unique[7][1])
unique_stk11 = sorted(unique[8][1])
unique_keapi1 = sorted(unique[9][1])
unique_xlt = sorted(unique[10][1])
unique_not_squamous_status = sorted(unique[11][1])
unique_pd11_status = sorted(unique[12][1])
unique_preference = sorted(unique[13][1])

with gr.Blocks() as demo:
    gr.Markdown("""
    **Lung Cancer Classification with gradio and CatBoost 10% data used ** Kobyzev Yuri).
    """)
    with gr.Row():
        with gr.Column():
            race = gr.Dropdown(
                label=rus_labels[0], choices=unique_race, value=lambda: random.choice(unique_race)
            )
            sex = gr.Dropdown(
                label=rus_labels[1], choices=unique_sex, value=lambda: random.choice(unique_sex)
            )
            age = gr.Dropdown(
                label=rus_labels[2],
                choices=unique_age,
                value=lambda: random.choice(unique_age),
            )
            smoke = gr.Dropdown(
                label=rus_labels[3],
                choices=unique_smoke,
                value=lambda: random.choice(unique_smoke),
            )
            ecog = gr.Dropdown(
                label=rus_labels[4],
                choices=unique_ecog,
                value=lambda: random.choice(unique_ecog),
            )
            tumor_load = gr.Dropdown(
                label=rus_labels[5],
                choices=unique_tumor_load,
                value=lambda: random.choice(unique_tumor_load),
            )
            kras = gr.Dropdown(
                label=rus_labels[6],
                choices=unique_kras,
                value=lambda: random.choice(unique_kras),
            )
        with gr.Column():
            p53 = gr.Dropdown(
                label=rus_labels[7],
                choices=unique_tumor_load,
                value=lambda: random.choice(unique_p53),
            )

            stk11 = gr.Dropdown(
                label=rus_labels[8],
                choices=unique_stk11,
                value=lambda: random.choice(unique_stk11),
            )
            keapi1 = gr.Dropdown(
                label=rus_labels[9],
                choices=unique_keapi1,
                value=lambda: random.choice(unique_keapi1),
            )
            xlt = gr.Dropdown(
                label=rus_labels[10],
                choices=unique_xlt,
                value=lambda: random.choice(unique_xlt),
            )
            not_squamous_status = gr.Dropdown(
                label=rus_labels[11],
                choices=unique_not_squamous_status,
                value=lambda: random.choice(unique_not_squamous_status),
            )
            pd11_status = gr.Dropdown(
                label=rus_labels[12],
                choices=unique_pd11_status,
                value=lambda: random.choice(unique_pd11_status),
            )
            preference = gr.Dropdown(
                label=rus_labels[13],
                choices=unique_preference,
                value=lambda: random.choice(unique_preference),
            )

    with gr.Row():
        with gr.Column():
            label = gr.Label()
            predict_btn = gr.Button(value="Предикт")

        predict_btn.click(
            predict,
            inputs=[
                race,
                sex,
                age,
                smoke,
                ecog,
                tumor_load,
                kras,
                p53,
                stk11,
                keapi1,
                xlt,
                not_squamous_status,
                pd11_status,
                preference
            ],
            outputs=[label],
        )

    demo.launch(share=True)












