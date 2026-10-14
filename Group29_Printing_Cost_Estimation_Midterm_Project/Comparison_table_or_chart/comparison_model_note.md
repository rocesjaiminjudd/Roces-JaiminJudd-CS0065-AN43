# Comparison Model Note

The Python implementation uses `DecisionTreeRegressor` as the comparison algorithm.

The KNIME workflow uses **Simple Regression Tree Learner** and **Simple Regression Tree Predictor** as the Decision Tree Regressor equivalent because the target value, `estimated_cost`, is numerical. KNIME's regular Decision Tree Learner is used for classification, not numerical regression.

Because of this, the KNIME Simple Regression Tree results are treated as the Decision Tree Regressor comparison results.
