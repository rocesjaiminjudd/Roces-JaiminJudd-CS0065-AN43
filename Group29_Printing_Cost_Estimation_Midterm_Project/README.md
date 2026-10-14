# Group 29 Printing Cost Estimation Midterm Project

## Project Overview

This project estimates the total cost of a printing service using predictive regression. The system predicts a numerical output called `estimated_cost` from print job details.

Primary algorithm: Linear Regression

Comparison algorithm: Decision Tree Regressor

In KNIME, Simple Regression Tree is used as the Decision Tree Regressor equivalent because the target value is numerical.

## Project Folders

```text
Dataset
Data_dictionary
KNIME_workflow
Python_implementation
Streamlit_interface
Comparison_table_or_chart
Short_interpretation_and_limitations
```

## Recommended Run Order

1. Open the dataset in the `Dataset` folder.
2. Run the Python implementation in `Python_implementation`.
3. Copy or confirm the trained model file is inside `Streamlit_interface`.
4. Run the Streamlit app from `Streamlit_interface`.
5. Open the KNIME workflow in `KNIME_workflow` and execute the nodes.
6. Record or screenshot the model results.
7. Review the report files in `Data_dictionary` and `Short_interpretation_and_limitations`.

## Main Dataset

Use this dataset:

```text
Dataset/group29_printing_cost_dataset_100.csv
```

The dataset has 100 records and these columns:

```text
job_id, pages, color_pages, paper_type, copies, binding, delivery_speed, estimated_cost
```

## Inputs and Output

Input features:

```text
pages
color_pages
paper_type
copies
binding
delivery_speed
```

Target/output:

```text
estimated_cost
```

Reference-only field:

```text
job_id
```

Do not use `job_id` for training.

## Python Implementation

Go to the `Python_implementation` folder and follow its README.

Main command:

```powershell
python train_model.py
```

This creates or updates:

```text
model_comparison_results.csv
printing_cost_pipeline.joblib
```

## Streamlit Interface

Go to the `Streamlit_interface` folder and follow its README.

Main command:

```powershell
python -m streamlit run streamlit_app.py
```

The app lets the user enter printing details and displays the estimated cost.

## KNIME Workflow

Open the workflow inside the `KNIME_workflow` folder using KNIME Analytics Platform.

The workflow uses:

```text
CSV Reader -> Column Filter -> Missing Value -> One to Many -> Table Partitioner
```

Then it splits into:

```text
Linear Regression Learner -> Regression Predictor -> Numeric Scorer
Simple Regression Tree Learner -> Simple Regression Tree Predictor -> Numeric Scorer
```

## Important KNIME Note

The regular KNIME Decision Tree Learner is for classification. Since this project predicts a numerical value, KNIME uses Simple Regression Tree Learner and Simple Regression Tree Predictor as the Decision Tree Regressor equivalent.

## Final Outputs

The project includes:

- 100-record dataset
- Data dictionary
- KNIME workflow
- Python implementation
- Streamlit interface
- Comparison table or chart
- Short interpretation and limitations