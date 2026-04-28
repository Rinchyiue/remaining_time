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
should provide a clear and easily operable interface for common end-users.

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
(or sequence of clerks') working efficiency. 

**Clerk** 
Example: customer support team  
Expectation: 
- The software has an interface where it is clear and easy to operate.  
- The output should provide information for workload estimation, as well as other factors that might
improve working efficiency.  

**Customer**  
Example: clients   
Expectation: 
- The software has an interface where it is clear and easy to operate.  
- Information about expected remaining waiting time/processing time can also help customers plan
further activities or decide whether to continue the process.  

# Definition of the Success Metrices
## Summary
There are certain factors that are considered important for evaluation in this project:   
reproducability, robustness, maintainability, fine documentation, explainability, basic functionality, accuracy, and earliness.  

## Content
They are respectively defined as follows:  

**reproducability:**  
The experiments done during the development should be capable of  
- being reproduced from the code and training files/data sets
- coinciding all evaluation results documented in the project.  

**robustness:**  
The code should be capable of passing all designed tests.  

**maintainability:**  
The code should be easy to maintain, which encourages the project to be split in more modules (or submodules)  
where the implementation should be as simple as possible.  

**fine documentation:**  
Basic functionality is fulfilled if and only if all of the following statements are fulfilled: 
- A short description pf the project and its goal is provided;
- Description of the datasets used, with source and basic statics, is provided;
- Setup instructions are provided, e.g. Python version and how to install dependencies;
- The code-level documentations have meaningful function and class names;  
- Description in docstrings of purpose, input and output of important functions is provided;
- Explanation of non-trivial logic is provided. 

**explainabililty:** 
Explainability is fulfilled if and only if all of the following statements are fulfilled:  
- Fine documentation is fulfilled;
- The code (i.e. prototype predictor) and tests should be run by anyone merely depending on the provided documentation.
- An architecture overview is provided.

**basic functionality:**   
Basic functionality is fulfilled if and only if all of the following statements are fulfilled:  
- The code (i.d. prototype predictor) should be capable of being performed on new data;
- The code  

**accuracy:**  

**earliness:**  

Beyond those success metrices defined above, the complexity of code should also be as little as possible,  
i.e. the main algorithm should stay in an asympotic class which is at best linear or even constant.  

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

# Module Responsibility  
Sarp: REQ-xx, REQ-xx, ...  
Linas:  
Qifan:  

# Functional Model

**Traceability Matric**
