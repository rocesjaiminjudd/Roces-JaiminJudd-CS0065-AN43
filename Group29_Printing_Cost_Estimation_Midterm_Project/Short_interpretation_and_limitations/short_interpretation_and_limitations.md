# Short Interpretation and Limitations

## Project Summary

This project estimates the total printing cost of a print job using predictive regression. The input features include pages, color pages, paper type, number of copies, binding, and delivery speed. The target output is the estimated printing cost.

The primary model used in this project is Linear Regression. The comparison model is Decision Tree Regressor. In KNIME, Simple Regression Tree was used as the Decision Tree Regressor equivalent because it predicts numerical values.

## Best Model

Linear Regression was selected as the final model.

In the Python implementation, Linear Regression achieved a higher R-squared value and a lower RMSE compared with the Decision Tree Regressor. Although the Decision Tree Regressor had a slightly lower MAE, Linear Regression performed more consistently overall.

In the KNIME workflow, Linear Regression also performed better than the Simple Regression Tree. It had a higher R-squared value and lower prediction errors.

Because Linear Regression performed consistently in both tools and is easier to explain, it was chosen as the best model for this project.

## Interpretation of Results

The results show that printing cost has a mostly regular pattern. As the number of pages, color pages, and copies increases, the total printing cost also increases. This type of relationship is suitable for Linear Regression because the model works well when the target value changes in a predictable numerical pattern.

The tree-based model did not perform as consistently. This may be because the dataset is synthetic and still limited in size. A decision tree can be sensitive to how the training and testing data are split, especially when the dataset has only 100 records.

## Limitations

This project has several limitations:

- The dataset is synthetic and may not fully represent real printing shop prices.
- The dataset has only 100 records, which is acceptable for the activity but still small for real machine-learning use.
- The model does not include taxes, discounts, customer membership rates, labor cost, machine maintenance, ink availability, or special design services.
- The prediction may be unreliable for inputs outside the dataset range.
- The model may not handle unusual printing requests accurately.
- KNIME and Python may produce different results because they can use different train-test splits, encoding methods, and model settings.

## Critical Thinking Questions

### 1. Which input should have the strongest influence on the estimated value?

The number of pages and number of copies should have the strongest influence on the estimated printing cost because they directly affect the amount of paper, ink, and printing work needed. Color pages should also strongly affect the cost because color printing is usually more expensive than black-and-white printing.

### 2. How should the system handle an input outside the range represented in the dataset?

The system should still provide an estimate, but it should show a warning that the prediction may be less reliable. For very large, unusual, or expensive print jobs, the price should be checked manually by the printing service.

### 3. What size of prediction error would still be acceptable for this project?

For this prototype, prediction error should be evaluated relative to the total order cost. An error within approximately 10% to 20% may be acceptable for a student demonstration. However, the current model errors are still relatively large, showing that the project would benefit from more records, improved input features, and real printing-shop data. For actual business use, the acceptable error should be considerably smaller.

## Final Conclusion

Linear Regression is the selected model for this project because it performed more consistently overall and is easier to explain. The model is useful for estimating printing cost, but it should be improved with more real-world data before being used in an actual printing business.

## KNIME Comparison Model Note

In Python, the comparison model was implemented using `DecisionTreeRegressor`. In KNIME, the equivalent regression-tree model used was **Simple Regression Tree Learner** and **Simple Regression Tree Predictor** because KNIME's regular Decision Tree Learner is for classification, while this project requires predicting a numerical value, `estimated_cost`.

Therefore, the Simple Regression Tree result in KNIME represents the Decision Tree Regressor comparison model.
