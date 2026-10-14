# Data Dictionary

## Project Information

Project title: Group 29 Printing Cost Estimation

Project type: Predictive Regression

System question: What numerical value should the system estimate for printing cost estimation?

System output: Estimated printing cost

Dataset file: group29_printing_cost_dataset_100.csv

Number of records: 100

## Dataset Purpose

The dataset is used to train and evaluate regression models that estimate the total printing cost of a print job. The prediction is based on page count, color pages, paper type, number of copies, binding option, and delivery speed.

## Field Classification

Reference-only field:
- job_id

Analytical input features:
- pages
- color_pages
- paper_type
- copies
- binding
- delivery_speed

Target label:
- estimated_cost

Generated output:
- predicted estimated printing cost

## Data Dictionary Table

| Column Name | Description | Data Type | Role | Example Values | Notes |
|---|---|---|---|---|---|
| job_id | Unique identifier for each printing job | Text/String | Reference-only field | P001, P002, P003 | Excluded from model training because it does not affect printing cost |
| pages | Total number of pages per copy | Numeric/Integer | Input feature | 12, 85, 300 | Must be greater than 0 |
| color_pages | Number of pages printed in color | Numeric/Integer | Input feature | 0, 10, 168 | Must be 0 or greater and cannot be greater than pages |
| paper_type | Type of paper used for printing | Categorical/Text | Input feature | standard, recycled, premium, glossy | Encoded before model training |
| copies | Number of copies requested | Numeric/Integer | Input feature | 1, 20, 50 | Must be greater than 0 |
| binding | Binding option selected for the print job | Categorical/Text | Input feature | none, staple, spiral, perfect | Encoded before model training |
| delivery_speed | Delivery option selected by the customer | Categorical/Text | Input feature | standard, rush | Encoded before model training |
| estimated_cost | Total estimated cost of the printing job | Numeric/Float | Target label/output | 680.62, 32135.92, 107480.11 | This is the value the model learns to predict |

## Allowed Categorical Values

### paper_type

| Value | Meaning |
|---|---|
| standard | Regular printing paper |
| recycled | Recycled paper option |
| premium | Higher-quality paper |
| glossy | Glossy paper for higher-quality visual output |

### binding

| Value | Meaning |
|---|---|
| none | No binding requested |
| staple | Stapled output |
| spiral | Spiral binding |
| perfect | Perfect binding |

### delivery_speed

| Value | Meaning |
|---|---|
| standard | Normal delivery speed |
| rush | Faster delivery with added cost |

## Data Preparation Notes

The job_id column is excluded from model training because it is only an identifier.

Categorical fields are encoded before training. In KNIME, this is done using the One to Many node. In Python, this is done using OneHotEncoder.

The dataset should be checked for:
- Missing values
- Duplicate rows
- Invalid categorical values
- Invalid numerical values
- Target column correctness

## Validation Rules

| Field | Validation Rule |
|---|---|
| pages | Must be a positive whole number |
| color_pages | Must be 0 or greater and cannot exceed pages |
| copies | Must be a positive whole number |
| paper_type | Must be one of the allowed paper type values |
| binding | Must be one of the allowed binding values |
| delivery_speed | Must be standard or rush |
| estimated_cost | Must be a positive numerical value |

## Missing Information

The dataset is synthetic and does not include every possible factor that may affect real printing prices. Missing real-world information includes:
- Taxes
- Discounts
- Labor cost
- Machine maintenance cost
- Ink availability
- Customer membership pricing
- Special layout or design services
- Bulk order negotiations

## Privacy Fairness Safety or Accessibility Concern

A safety and reliability concern is that predictions may be inaccurate for print jobs outside the range of the dataset. For example, very large printing orders or unusual combinations of color pages, paper type, and binding may produce less reliable estimates. The system should warn users when their input is outside the dataset range.

A privacy concern is low because the dataset does not include customer names, contact details, addresses, or payment information.

## Model Use Notes

The target label for both KNIME and Python is estimated_cost.

The input features used for model training are:
- pages
- color_pages
- paper_type
- copies
- binding
- delivery_speed

The selected model is Linear Regression because it performed consistently and is easier to explain for printing cost estimation.
