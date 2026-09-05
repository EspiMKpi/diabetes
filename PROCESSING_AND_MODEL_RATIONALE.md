# Diabetes: Processing and Model Rationale

## Processing

The dataset contains one row per patient, eight clinical inputs, and the binary `Outcome` target. Duplicate rows are removed. The CSV has no null values, but zero is not physiologically plausible for glucose, blood pressure, skin thickness, insulin, or BMI, so those zeros are converted to missing values. The pipeline fits median imputation on the training split and then standardizes all numeric features. Keeping imputation and scaling inside the pipeline prevents test-set leakage and guarantees the web app uses the same transformation as training.

The notebook visualizes target balance, glucose by outcome, feature correlations, model metrics, and the final confusion matrix. These plots answer data-quality, signal, error, and model-selection questions rather than serving as decoration.

## Algorithms

- Logistic Regression is an interpretable linear baseline: each feature contributes through a learned weight.
- KNN tests local similarity, so it provides a useful experiment about the effect of scaling.
- RBF SVM tests a nonlinear maximum-margin boundary and is appropriate for a small numeric dataset.
- Random Forest captures nonlinear feature interactions and is less dependent on a linear relationship.

The final model is selected by F1 because the application should balance missed diabetic cases and false alarms. Recall is also reported because missing a positive case can be clinically costly. The saved `diabetes_model.sav` contains preprocessing and the selected estimator together.
