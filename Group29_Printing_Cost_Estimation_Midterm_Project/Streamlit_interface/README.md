# Streamlit Interface README

## Purpose

This folder contains the Streamlit interface for the Group 29 Printing Cost Estimation project.

The app allows a user to enter print job details and receive an estimated printing cost.

## Required Files

This folder should contain:

```text
streamlit_app.py
requirements.txt
printing_cost_pipeline.joblib
```

The file `printing_cost_pipeline.joblib` is created by running the Python implementation.

If it is missing, run the Python implementation first, then copy the model file into this folder.

## Step 1: Open Terminal

Open PowerShell or the VS Code terminal.

Go to this folder:

```powershell
cd "C:\Users\Msi\Documents\School\CS elective\Group29_Printing_Cost_Estimation_Midterm_Project\Streamlit_interface"
```

## Step 2: Install Requirements

Run:

```powershell
python -m pip install -r requirements.txt
```

## Step 3: Run the Streamlit App

Run:

```powershell
python -m streamlit run streamlit_app.py
```

A browser window should open automatically.

If it does not open, copy the local URL shown in the terminal. It usually looks like:

```text
http://localhost:8501
```

## App Inputs

The app collects:

```text
pages
color_pages
paper_type
copies
binding
delivery_speed
```

## App Output

The app displays:

```text
Estimated printing cost
```

## Validation

The app checks that color pages are not greater than total pages.

It also warns the user if the input is outside the main dataset range, because the prediction may be less reliable.

## Troubleshooting

If the app says the model file is missing, make sure this file is in the same folder as `streamlit_app.py`:

```text
printing_cost_pipeline.joblib
```

If Streamlit is not recognized, run:

```powershell
python -m pip install streamlit
```

Then run the app again:

```powershell
python -m streamlit run streamlit_app.py
```
