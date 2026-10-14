import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor

DATA_PATH = "group29_printing_cost_dataset_100.csv"
TARGET = "estimated_cost"

NUMERIC_FEATURES = ["pages", "color_pages", "copies"]
CATEGORICAL_FEATURES = ["paper_type", "binding", "delivery_speed"]
FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES


def rmse(y_true, y_pred):
    return mean_squared_error(y_true, y_pred) ** 0.5


def build_pipeline(model):
    preprocessor = ColumnTransformer(
        transformers=[
            ("categorical", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_FEATURES),
            ("numeric", "passthrough", NUMERIC_FEATURES),
        ]
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model),
        ]
    )

    return pipeline


df = pd.read_csv(DATA_PATH)

print("Dataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nInvalid category check:")
for column in CATEGORICAL_FEATURES:
    print(f"{column}: {sorted(df[column].dropna().unique())}")

print("\nTarget summary:")
print(df[TARGET].describe())

X = df[FEATURES]
y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=29
)

models = {
    "Linear Regression": build_pipeline(LinearRegression()),
    "Decision Tree Regressor": build_pipeline(
        DecisionTreeRegressor(random_state=29, max_depth=5)
    ),
}

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    results.append(
        {
            "Model": name,
            "MAE": mean_absolute_error(y_test, predictions),
            "RMSE": rmse(y_test, predictions),
            "R-squared": r2_score(y_test, predictions),
        }
    )

results_df = pd.DataFrame(results)

print("\nModel Comparison:")
print(results_df)

results_df.to_csv("model_comparison_results.csv", index=False)

selected_model = models["Linear Regression"]
selected_model.fit(X, y)

joblib.dump(selected_model, "printing_cost_pipeline.joblib")

print("\nSaved model as printing_cost_pipeline.joblib")
print("Saved comparison as model_comparison_results.csv")