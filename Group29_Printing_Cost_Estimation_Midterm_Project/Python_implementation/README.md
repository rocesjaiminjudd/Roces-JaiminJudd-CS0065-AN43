# Python Implementation README

## Purpose

This folder contains the Python implementation for the Group 29 Printing Cost Estimation project.

The Python script trains and compares:

- Linear Regression
- Decision Tree Regressor

The selected model pipeline is saved with joblib.

## Required Files

This folder should contain:

```text
train_model.py
requirements.txt
group29_printing_cost_dataset_100.csv
```

After running the script, it should also contain:

```text
model_comparison_results.csv
printing_cost_pipeline.joblib
```

## Step 1: Open Terminal

Open PowerShell or the VS Code terminal.

Go to this folder:

```powershell
cd "C:\Users\Msi\Documents\School\CS elective\Group29_Printing_Cost_Estimation_Midterm_Project\Python_implementation"
```

## Step 2: Install Requirements

Run:

```powershell
python -m pip install -r requirements.txt
```

This installs the needed libraries, including pandas, scikit-learn, and joblib.

## Step 3: Check the Dataset File

Make sure this file is in the same folder as `train_model.py`:

```text
group29_printing_cost_dataset_100.csv
```

If it is not there, copy it from:

```text
../Dataset/group29_printing_cost_dataset_100.csv
```

PowerShell command:

```powershell
copy "..\Dataset\group29_printing_cost_dataset_100.csv" .
```

## Step 4: Run the Python Script

Run:

```powershell
python train_model.py
```

## What the Script Does

The script will:

1. Load the CSV dataset using pandas.
2. Check the dataset shape.
3. Check missing values.
4. Check duplicate rows.
5. Check categorical values.
6. Prepare `X` input features and `y` target label.
7. Encode categorical features using OneHotEncoder.
8. Train Linear Regression.
9. Train Decision Tree Regressor.
10. Compare MAE, RMSE, and R-squared.
11. Save the comparison table.
12. Save the selected model pipeline.

## Output Files

After running, check for:

```text
model_comparison_results.csv
printing_cost_pipeline.joblib
```

`model_comparison_results.csv` contains the evaluation results.

`printing_cost_pipeline.joblib` is the trained model pipeline used by the Streamlit app.

## Notes

The primary model is Linear Regression.

The comparison model is Decision Tree Regressor.

The target column is:

```text
estimated_cost
```

The input features are:

```text
pages
color_pages
paper_type
copies
binding
delivery_speed
```
