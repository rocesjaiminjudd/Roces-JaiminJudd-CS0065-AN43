# KNIME Workflow README

## Purpose

This folder contains the KNIME workflow for the Group 29 Printing Cost Estimation project.

The workflow compares:

- Linear Regression
- Simple Regression Tree

Simple Regression Tree is used in KNIME as the Decision Tree Regressor equivalent because the project predicts a numerical value.

## Dataset to Use

Use this dataset:

```text
group29_printing_cost_dataset_100.csv
```

If needed, get it from:

```text
../Dataset/group29_printing_cost_dataset_100.csv
```

## Workflow Layout

Build or check the workflow in this order:

```text
CSV Reader
-> Column Filter
-> Missing Value
-> One to Many
-> Table Partitioner
```

Then split into two branches:

```text
Linear Regression Learner
-> Regression Predictor
-> Numeric Scorer
```

and:

```text
Simple Regression Tree Learner
-> Simple Regression Tree Predictor
-> Numeric Scorer
```

## Important Table Partitioner Connections

The Table Partitioner has two outputs:

```text
Top output = First partition = training data
Bottom output = Second partition = testing data
```

Connect the top output to:

```text
Linear Regression Learner
Simple Regression Tree Learner
```

Connect the bottom output to:

```text
Regression Predictor
Simple Regression Tree Predictor
```

## Important Node Settings

### Column Filter

Remove:

```text
job_id
```

Keep:

```text
pages
color_pages
paper_type
copies
binding
delivery_speed
estimated_cost
```

### One to Many

Encode categorical columns:

```text
paper_type
binding
delivery_speed
```

### Table Partitioner

Use:

```text
Relative size: 80
Sampling strategy: Random
Fixed random seed: checked
```

### Linear Regression Learner

Target column:

```text
estimated_cost
```

### Simple Regression Tree Learner

Target column:

```text
estimated_cost
```

### Numeric Scorer

For both Numeric Scorer nodes:

```text
Reference column: estimated_cost
Predicted column: Prediction (estimated_cost)
```

## Important Note About Decision Tree Regressor

The normal KNIME Decision Tree Learner is for classification. It predicts categories, not numerical values.

Because this project predicts the numerical target `estimated_cost`, the workflow uses:

```text
Simple Regression Tree Learner
Simple Regression Tree Predictor
```

This represents the Decision Tree Regressor comparison model in KNIME.

## Screenshots to Capture

Include screenshots of:

- Full KNIME workflow
- Linear Regression Numeric Scorer result
- Simple Regression Tree Numeric Scorer result
