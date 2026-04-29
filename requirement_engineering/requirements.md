This is the requirement engineering file.  

# Guidelines
- Please follow a consistent standard format when you add anything here.  
- Please provide a UID for each requirement discovered.  
- Please synchronize such requirements in Trello.  
- Please regularly update the traceability matric besides version control.  

**Format:**  
**ID**               := REQ-<ins>Int</ins>  
**Type**             := functional requirement | non-functional requirement | constraints  
**Text**             := (description of the requirement)  

**Ps:** 
1. For sake of unitiy of notation, which contributes to better identification and management  
of all requirements (or constraints), constraints will also follow the format given for a  
requirement, continuing the numeric sequence of ID.  
2. The detailed allocation of requirements to people will not be explicitly given in this file,  
but instead provided on our Trello Kanban https://trello.com/b/SvWcKF1S/remaining-time-spp.

# General Summary
TO DO

# Stakeholders
## Summary  
There are various (potential) stakeholders, and according to their professions and roles in the process  
they can be further classified into four groups: academic, leader, clerk and client. Expectations can be  
different given different points of view, but there are also some expectations in common, e.g. the software  
should provide a clear and easily operable interface for common end-users and alert to bottlenecks/violations  
should be given in certain negative cases.

## Content
The advisor: Alessandro Berti  
Potential (end-)users: incident manager/commander, business executives, customer support team,  
or even clients.  

Moreover, we can classify them into groups as follows:  

**Academic**  
Example: the advisor  
Expectation: 
- This software project can fulfill all the constraints given in the assignment file;  
- All deadlines for development can be met;
- The enhancement of functionality can be a bonus (e.g. more training data sets are used to develop, or more  
advanced algorithm is applied for more precise prediction value generation).  

**Leader**  
Example: incident manager/commander, business executives  
Expectation: 
- The software has an interface where it is clear and easy to operate.
- The output should be benefitial for decision making (e.g. whether adjustment should be appiled based on
the expected duration).
- In relationship to the clerk group, it can also be viewed as an indirect assessment on certain clerk's
(or sequence of clerks') working efficiency or indirectly resource utilization.  
- In certain negative cases, alert to bottlenecks/violations should be given. In such cases, the output value
should also support extimating potential losses. 

**Clerk** 
Example: customer support team  
Expectation: 
- The software has an interface where it is clear and easy to operate.  
- The output should provide information for workload estimation, as well as other factors that might
improve working efficiency.
- In certain negative cases, alert to bottlenecks/violations should be given.  

**Customer**  
Example: clients   
Expectation: 
- The software has an interface where it is clear and easy to operate.  
- Information about expected remaining waiting time/processing time can also help customers plan
further activities or decide whether to continue the process.
- In certain negative cases, alert to bottlenecks/violations should be given. In such cases, the output value  
should also support extimating potential losses.  

# Metrices to be used
## Summary
The dominating factor of the quantitative evalution of our project: accuracy based on prefix length  
and model, which can be explained in four indicators: Mean Absolute Error (MAE), Root Mean Squared Error (RMSE),  
Median Absolute Error (MedAE) and R<sup>2</sup> Score. 

More interestingly, all of the indicators can be calculated thanking scikit, https://scikit-learn.org/stable/modules/model_evaluation.html. 

## Content
As for each model, an evaluation should be performed to detect accuracy of the prediction. In this project,  
we select Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), Median Absolute Error (MedAE) and R<sup>2</sup> Score  
as indicators to accuracy. However, to ensure the comparability and finite scalablity, prefix length and model  
should also be paired with the corresponding indicator value.  

**MAE**  
- Definition (Wikipedia):   

```math
\mathrm{MAE} = \frac{1}{n}\sum_{i=1}^{n} |y_i - x_i|
```

where:

$y_i$ is the predicted value  
$x_i$ is the actual value  
$n$ is the number of observations

- Reason:  
One of the most standard metrices for prediction accuracy, and an arithmetic mean simple to calculate.  Since the prediction cases
with same model and prefix length are equally weighed, MAE's incapability in different data scales can be ignored in this context.

**RMSE**  
- Definition (Wikipedia)*:  

```math
\mathrm{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - x_i)^2}
```
where:

$y_i$ is the predicted value  
$x_i$ is the actual value  
$n$ is the number of observations

- Reason:
One of the most standard metrics for prediction accuracy, especially in the area machine learning. The indicator is scale-dependent,
analog to MAE, this property is not violated. Moreover, RMSE is sensitive to outliners, for each error is proportional to the size  
of the squared error, thus large errors can have significant influence on the outcome.

\* : This definition is the regression variant.

**MedAE**  
- Definition (Wikipedia):

```math
\mathrm{MedAE} = \mathrm{median}(|y_i - x_i|)
```

where:

$y_i$ is the predicted value  
$x_i$ is the actual value  
$|y_i - x_i|$ is the absolute error for observation $i$

- Reason:
Median Absolute Error often serves as a population parameter - population can be refered to the group of prediction values carried out from
same background (i.e. a group of prediction cases). This might help discovering a probability distribution. In contrast to RMSE, Median Absolute
Error is more resilient to outliners.

**R<sup>2</sup> Score**  
- Definition (Wikipedia):

A data set has $n$ values $y_1, \ldots, y_n$ (collectively denoted $y_i$, or as a vector $y = [y_1, \ldots, y_n]^T$), each associated with a fitted  
(or modeled, or predicted) value $f_1, \ldots, f_n$ (denoted $f_i$, or as a vector $f$).

Define the residuals as:
```math
e_i = y_i - f_i
```

Let $\bar{y}$ be mean of the observed data:
```math
\bar{y} = \frac{1}{n}\sum_{i=1}^{n} y_i
```

Residual Sum of Squares (SSres)

```math
SS_{res} = \sum_{i=1}^{n}(y_i - f_i)^2 = \sum_{i=1}^{n} e_i^2
```

Total Sum of Squares (SStot)

```math
SS_{tot} = \sum_{i=1}^{n}(y_i - \bar{y})^2
```

R<sup>2</sup> Score (Coefficient of Determination)

```math
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
```

- Reason:
It can serve as a fitness indicator for our prediction model - if the value is negative, it implies that the model does not fit the data set well.
Moreover, since the desired (and usual) results always range in [0,1], it's more intuitive because of the existence of a counterpart representation in
percentage.

More precisely, the indicator represents the percentage of the variablity of the dependent variable in the data set has been account for; in our project,  
the dependent variable is the prediction value. Therefore, it can be used for completeness check of variability coverage calculating the prediction value.

# Requirements
## Data and Preprocessing
**ID:** REQ-01  
**Type:** Functional  
**Text:** The system shall load the incident management event log using PM4Py or pandas.

**ID:** REQ-02  
**Type:** Functional  
**Text:** The system shall extract and validate the presence of the essential columns within the loaded log, including case identifier, activity name, timestamp, and relevant case attributes (e.g. priority, customer, incident type).

**ID:** REQ-03  
**Type:** Functional  
**Text:** The system shall ensure that events within each case are sorted by timestamp.

**ID:** REQ-04  
**Type:** Functional  
**Text:** The system shall compute the remaining time for each prefix of each case, defined as the difference between the completion timestamp and the timestamp of the last event in the prefix, expressed in a consistent unit.

**ID:** REQ-05  
**Type:** Functional  
**Text:** The system shall implement a logic to either keep or filter out prefixes that are "too short" (e.g., still in an initial trivial state).

**ID:** REQ-06  
**Type:** Functional  
**Text:** The system shall build a prefix-level supervised dataset where each row represents one prefix of one case, containing a feature vector and the corresponding remaining time label.

**ID:** REQ-07  
**Type:** Functional  
**Text:** The system shall split the dataset into training, validation, and test sets using a time-based split (e.g. first 70% of cases by start time for training, next 15% for validation, last 15% for test).

**ID:** REQ-08  
**Type:** Functional  
**Text:** The system shall encode static case attributes (e.g. priority, customer type at creation time) as features.

**ID:** REQ-09  
**Type:** Functional  
**Text:** The system shall encode aggregated dynamic features per prefix, including the number of events so far, elapsed time since case start and activity occurrence counts.

**ID:** REQ-10  
**Type:** Functional  
**Text:** The system shall encode temporal features of the last event in the prefix: day of week and hour of day (e.g. as one-hot or cyclical encoding).

**ID:** REQ-11  
**Type:** Functional  
**Text:** The system shall apply one-hot encoding of categorical features and scaling or normalization of numeric features as required by the chosen models.

## Modelling and Evaluation
**ID:** REQ-12   
**Type:** Functional  
**Text:** The system shall implement a naive baseline predictor for remaining time (e.g. always predicting the mean remaining time of training prefixes, or the mean remaining time conditional on the current activity).

**ID:** REQ-13   
**Type:** Functional  
**Text:** The system shall implement at least two supervised regression models (e.g. Linear/Ridge Regression and a tree-based model such as RandomForestRegressor or GradientBoostingRegressor).

**ID:** REQ-14   
**Type:** Functional  
**Text:** The system shall train all models on the training set and use the validation set to select hyperparameters.

**ID:** REQ-15   
**Type:** Functional  
**Text:** The system shall provide the functionality to evaluate different hyperparameter configurations on the validation set, either via a simple grid search or manual search.

**ID:** REQ-16   
**Type:** Functional  
**Text:** The system shall provide the functionality to retrain the selected best model configuration on the combined training and validation set.

**ID:** REQ-17   
**Type:** Functional  
**Text:** The system shall evaluate all models on the test set and report at least the Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

**ID:** REQ-18   
**Type:** Functional  
**Text:** The system shall evaluate model performance separately across multiple prefix lengths, specifically early, mid, and late prefixes.


## Infrastructure and Tooling
**ID:** REQ-xx  
**Type:**  
**Text:**

## Reporting and Explainability
**ID:** REQ-19   
**Type:** Functional  
**Text:** The system shall generate a comparison table of all models (baseline and ML models) on test data.

**ID:** REQ-20   
**Type:** Functional  
**Text:** The system shall generate at least two plots visualizing model performance, for example: MAE/RMSE vs. prefix length, distribution of prediction errors, or a scatter plot of predicted vs. actual remaining time.

**ID:** REQ-21  
**Type:** Functional  
**Text:** The system shall provide a prototype script or notebook that accepts new data and prints the predicted remaining time for active cases.

# Definition of Success

# Module Responsibility  
Sarp: REQ-xx, REQ-xx, ...  
Linas:  
Qifan:  

# Functional Model

**Traceability Matric**
