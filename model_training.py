import pandas as pd
from pycaret.classification import setup, compare_models, finalize_model, save_model


splits = {'train': 'train.csv', 'test': 'test.csv'}
df_train = pd.read_csv("hf://datasets/winvoker/turkish-sentiment-analysis-dataset/" + splits["train"])
df_test = pd.read_csv("hf://datasets/winvoker/turkish-sentiment-analysis-dataset/" + splits["test"])

df = pd.concat([df_train, df_test]).reset_index()
del df["index"]
del df["dataset"]

# PyCaret sessions start
clf = setup(data=df, target='label', session_id=123, log_experiment=True, experiment_name="sentiment_mlflow")

# best model selection
best_model = compare_models()

# Model finalize
final_model = finalize_model(best_model)

# Model save
save_model(final_model, 'sentiment_model')
