This is the requirement engineering file.  

# Guidelines
- Please follow a consistent standard format when you add anything here.  
- Please provide a UID for each requirement discovered.  
- Please synchronize such requirements in Trello.  
- Please regularly update the traceability matric besides version control.  

**Format:**  
**ID**               := REQ-<ins>Int</ins>  
**Type**             := Functional | Non-functional | Constraint  
**Text**             := (description of the requirement)  

**Ps:** 
1. For sake of unitiy of notation, which contributes to better identification and management  
of all requirements (or constraints), constraints will also follow the format given for a  
requirement, continuing the numeric sequence of ID.  
2. The detailed allocation of requirements to people will not be explicitly given in this file,  
but instead provided on our Trello Kanban https://trello.com/b/SvWcKF1S/remaining-time-spp.

# Overview
In the first section, we will go through our (potential) stakeholders and their expectations; then in the second setion, a brief  
introduction to the (quantitative) metrices used for evaluation will be unfolded; next comes a list of grouped functional, non-functional 
requirements, and constraints that will guide the development will be presented in the third part; after that, in the fourth part, concrete  
job allocation to each team member will be documented; before ending up, we will also try to define criteria for success of out project  
and provide a more straight-forward functional model, as well as a traceability matric to track the process.

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
One of the most standard metrices for prediction accuracy (a regression task), and an arithmetic mean simple to calculate.  Since the prediction cases
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
One of the most standard metrics for prediction accuracy (a regression task), especially in the area machine learning. The indicator is scale-dependent,
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

**ID:** REQ-19   
**Type:** Non-functional  
**Text:** A complete, reproducible pipeline that goes from raw event log to trained models, evaluated predictions, and a small prototype for running the predictor shall be implemented. 

**ID:** REQ-20  
**Type:** Non-functional  
**Text:** Code should be structured so that encodings are implemented in reusable functions or classes.

**ID:** REQ-21  
**Type:** Non-functional  
**Text:** Scikit-learn’s API should be used where possible.

**ID:** REQ-22  
**Type:** Non-functional  
**Text:** Hyperparameters should be specified in a configuration file or in an easily editable block of code, not hard-coded throughout the pipeline.

**ID:** REQ-23  
**Type:** Non-functional  
**Text:** At least 3–5 automatic unit tests should be created for core components (e.g. checks correct computation of remaining time labels on a small synthetic 
log).

## Infrastructure and Tooling
**ID:** REQ-24  
**Type:** Constraint  
**Text:** Either pytest or Python’s built-in unittest framework should be used.

**ID:** REQ-25   
**Type:** Contraint  
**Text:** Python, PM4Py, scikit-learn, and standard data science libraries should be used.  

**ID:** REQ-26  
**Type:** Contraint  
**Text:** A Git repository containing all code, tests, and documentation needed to reproduce results shall be established.  

**ID:** REQ-27  
**Type:** Non-functional  
**Text:** The repository should be organized and readable. 

## Reporting and Explainability
**ID:** REQ-28   
**Type:** Functional  
**Text:** The system shall generate a comparison table of all models (baseline and ML models) on test data.

**ID:** REQ-29   
**Type:** Functional  
**Text:** The system shall generate at least two plots visualizing model performance, for example: MAE/RMSE vs. prefix length, distribution of prediction errors, or a scatter plot of predicted vs. actual remaining time.

**ID:** REQ-30  
**Type:** Functional  
**Text:** The system shall provide a prototype script or notebook that accepts new data and prints the predicted remaining time for active cases.

**ID:** REQ-31  
**Type:** Non-functional  
**Text:**  Hyperparameters tuned and what search strategy used should be documented (e.g. simple gridsearch or manual search). 

**ID:** REQ-32  
**Type:** Non-functional  
**Text:** The project shall provide a comprehensive README.md file enabling others to run the code independently. It must include a project and dataset description, setup instructions (Python version, virtual environment, dependency installation), and step-by-step commands to reproduce experiments, run the prototype, and execute the test suite.  

**ID:** REQ-33  
**Type:** Non-functional  
**Text:** Code-level documentation should include: meaningful function and class names, docstrings explaining the purpose and input/output of important functions 
(especially in feature engineering, label construction, and training), and comments where the logic is non-trivial.

**ID:** REQ-34  
**Type:** Non-functional  
**Text:**  Architecture overview should be provided, as: a short text (can be in README or a separate ARCHITECTURE.md) that explains the project structure, and mention how configuration is handled.  

**ID:** REQ-35  
**Type:** Non-functional  
**Text:**  A requirements.txt or pyproject.toml specifying the Python dependencies (e.g. PM4Py, scikit-learn, pandas, matplotlib) should be provided.

**ID:** REQ-36  
**Type:** Non-functional  
**Text:** Instructions or scripts to download / place the dataset should be provided.  

# Definition of Success
The definition of success regarding this project should be viewed from two perspectives: quantitative and qualitative. They are both important components standing behind the project value. 

## Quantitative Criteria  
Accuracy is seen as the dominate criterion, which is also a baseline according to the assignment. However, the thresholds of indictors introduced in this project for a "good" prediction model could hardly be  
precisely defined, because they are strongly context-dependent to the use cases. For instance, tolerance to quality of industrial water is often greater than to household water.  

However, we can apply the following two approaches:  

### Comparative Evaluation
Inspired by [1], we will try to apply a more naive method to compare model quality (binary relation*):  

We assume that, if the prefix length holds same: MAE, RMSE, MedAE, and R^2 Score are equally weighed, i.e. each counts for 25% of the final scoring. However, given that MAE, RMSE, MedAE are often not percentage values, we have to first convert them into (relative) percentage values to combine with R^2 Score and be presented in a more intuitive form.  

Let $\mathcal{B}$ be the current "best" model, and $\mathcal{T}$ be the candidate model for comparison. We define the set of unique prefix lengths as $L$ and the absolute frequency of cases for a given length $l \in L$ as $freq(l)$.

Let $\xi_{i}(M, l)$ denote the performance of model $M$ at prefix length $l$ for the $i$-th metric, where $i \in \{1, 2, 3, 4\}$ corresponds sequentially to:
1. **MAE** 
2. **RMSE** 
3. **MedAE** 
4. **$R^2$ Score**

The indicator function $\text{Super}(\mathcal{B}, \mathcal{T})$ is defined as the weighted average of the relative improvement across all metrics and prefix lengths:

$$ \text{Super}(\mathcal{B}, \mathcal{T}) = \sum_{l \in L} freq(l) \cdot \left( \frac{1}{4} \sum_{i=1}^{4} \frac{\xi_i(\mathcal{B}, l) - \xi_i(\mathcal{T}, l)}{\xi_i(\mathcal{B}, l)} \right) $$

**Interpretation of Relative Difference:**
-   If $\xi_i(\mathcal{T}, l) \le \xi_i(\mathcal{B}, l)$, the term $\frac{\xi_i(\mathcal{B}, l) - \xi_i(\mathcal{T}, l)}{\xi_i(\mathcal{B}, l)}$ falls within the range $[0, 1]$.
-   If $\xi_i(\mathcal{T}, l) > \xi_i(\mathcal{B}, l)$, the value is negative (indicating performance regression), which is tolerated locally within the summation.

We evaluate the relationship using a significance level of $0.05$:

| Condition | Relation | Meaning |
| :--- | :---: | :--- |
| $\text{Super}(\mathcal{B}, \mathcal{T}) < -0.05$ | $\mathcal{T} \prec \mathcal{B}$ | Model $\mathcal{T}$ performs worse than model $\mathcal{B}$ |
| $-0.05 \le \text{Super}(\mathcal{B}, \mathcal{T}) \le 0.05$ | $\mathcal{T} \approx \mathcal{B}$ | Model $\mathcal{T}$ performs equally to model $\mathcal{B}$ |
| $\text{Super}(\mathcal{B}, \mathcal{T}) > 0.05$ | $\mathcal{T} \succ \mathcal{B}$ | Model $\mathcal{T}$ performs better than model $\mathcal{B}$ |


-   **If $\mathcal{T} \approx \mathcal{B}$**: Save both models. Compare subsequent models against both. If a new model $\mathcal{N}$ emerges such that $\mathcal{N} \succ \mathcal{T}$ or $\mathcal{N} \succ \mathcal{B}$, the dominated model is substituted.
-   **If $\mathcal{T} \succ \mathcal{B}$**: Update the best model state to $\mathcal{T}$ and discard $\mathcal{B}$.
-   **If $\mathcal{T} \prec \mathcal{B}$**: Discard $\mathcal{T}$ and retain $\mathcal{B}$.

However, even if a model is deleted from the data store, we will still keep their accuracy data. 

And in case we end up with more than one model considered as equally capable, we will further calculate their Super values for each pair and list them according to the ">" relation, but ignore the significance level and simply refer to whether the Super value is negative or positive to add < or > relation. After that pick the model which is on the left end as the preferred "best" model to predict.  

In the end of the development process, we will provide the accuracy acquired by the best model trained, and provide them as reference for potential stakeholders to determine, whether our software can meet their  
demand and tolerance. Also as stated in the metrices' description, the four indicators that we introduce can be supportive for multi-dimentional fitness analysis regarding stakeholders' use cases. 

\* : Binary relation is sufficient, because we only save the best performing model trained, and each time we only have to compare the current trained model with the saved "best" model.  

### Assumed Thresholds  
We define the global performance goals based on weighted metrics across all prefix lengths. Let $\bar{y}_l$ be the true mean value of the target variable for prefix length $l$, and $w_l$ be the normalized weight based on frequency:

$$ w_l = \frac{freq(l)}{\sum_{k \in L} freq(k)} $$

The weighted performance metric $\bar{\xi}_i$ and the weighted true mean $\bar{Y}$ are defined as:
$$ 
\bar{\xi}_i = \sum_{l \in L} w_l \cdot \xi_i(M, l), \quad \bar{Y} = \sum_{l \in L} w_l \cdot \bar{y}_l 
$$

A model is considered to have "achieved" its performance goal if it satisfies the following criteria:

| Metric | Achievement Criterion | Threshold Logic |
| :--- | :--- | :--- |
| **MAE** | $\bar{\xi}_1 \le 0.40 \cdot \bar{Y}$ | Within $\pm 40\%$ of the weighted true mean [2] |
| **RMSE** | $\bar{\xi}_2 \le 0.50 \cdot \bar{Y}$ | Within $\pm 50\%$ of the weighted true mean |
| **MedAE** | $\bar{\xi}_3 \le 0.40 \cdot \bar{Y}$ | Within $\pm 40\%$ of the weighted true mean |
| **$R^2$ Score** | $\bar{\xi}_4 \ge 0.70$ | Exceeds the $1\sigma$ normal distribution threshold* |

---
\* : The $70\%$ threshold is selected as it represents a performance level slightly above the first standard deviation ($\mu \pm 1\sigma \approx 68.27\%$) of a normal distribution.

## Qualitative Criteria
All of the listed requirements (and constraints) should be fulfilled - this serves as a baseline for our project. Ditto, we can also view them as an influential part of foundation of "success" in our project.  
Beyond those, the execession* in number of concrete implementation / evaluation / explanantion elements than the ones described in requirements can also be viewed as a contributor to "success".  

Moreover, considering the whole development process, success can also be defined from the more aspects, which are mainly:  

- Milestone delivery punctuality
- Credibility of used data / references
- Academic integrity
- Flexibility to adjustment
- Team collaberation
- Experience gained from the project

In a nutshell, from the qualitative criteria listed, success in our project can be partially viewed as requirement fulfillment (excession) + experience and soft skills obtained from the project.  

\* : Emphasis here is on the property of excession, rather than the concrete numeric value.  

# Module Responsibility  
Sarp: REQ-23, REQ-24, REQ-28, REQ-29, REQ-34, REQ-35  
Linas: REQ-01, REQ-02, REQ-03, REQ-04, REQ-05, REQ-06, REQ-07, REQ-08, REQ-09, REQ-10, REQ-11, REQ-12, REQ-36  
Qifan: REQ-13, REQ-14, REQ-15, REQ-16, REQ-17, REQ-18, REQ-19, REQ-22, REQ-30, REQ-31  
All: REQ-20, REQ-21, REQ-25, REQ-26, REQ-27, REQ-32, REQ-33  

# Functional Model

# Traceability Matrix
## Plan for update (both requirements and the matric)
Regular: After the first or second weekly-meeting during a milestone phase.  

Optional: Whenever necessary during the development phases.  

Important is that the updates should always stay in alignment with the Trello Kanban, vice versa.  

## Matric explanation
In total, there will be 5 matrices, which consists one for general view, and each of the rest four for a group of requirements. 

As for the columns, we select "Requirement ID", "Analysis", "Design", "Implementation", "Documentation", "Test", "Evaluation", "Review", and "Deliverable", which roughly simulates the develop ment process for a single  
requirement with specification in taking "Documentation" out from "Implementation" and "Evaluation" out from "Test". The reason for this seperation is to emphasize explainability in this project which can be a weakness  
of students. 

As for the rows, in the matrix for general view, each of them stands for a submatric; in other submatrices, each of them corresponds to a requirement.  

It is also worth mentioning that the constraints should be followed throughout the development process, therefore, there will not be a matrix tracing them.  

## The Matrix
### Matrix 0: General View
|Requirement ID | Analysis | Design | Implementation | Documentation | Test | Evaluation | Review | Deliverable |
|---|---|---|---|---|---|---|---|---|
|Data and Preprocessing|---|---|---|---|---|---|---|---|
|Modelling and Evaluation|---|---|---|---|---|---|---|---|
|Infrastructure and Tooling|---|---|---|---|---|---|---|---|
|Reporting and Explainablity|---|---|---|---|---|---|---|---|

### Matrix 1: Data and Preprocessing
|Requirement ID | Analysis | Design | Implementation | Documentation | Test | Evaluation | Review | Deliverable |
|---|---|---|---|---|---|---|---|---|
|REQ-01|---|---|---|---|---|---|---|---|
|REQ-02|---|---|---|---|---|---|---|---|
|REQ-03|---|---|---|---|---|---|---|---|
|REQ-04|---|---|---|---|---|---|---|---|
|REQ-05|---|---|---|---|---|---|---|---|
|REQ-06|---|---|---|---|---|---|---|---|
|REQ-07|---|---|---|---|---|---|---|---|
|REQ-08|---|---|---|---|---|---|---|---|
|REQ-09|---|---|---|---|---|---|---|---|
|REQ-10|---|---|---|---|---|---|---|---|
|REQ-11|---|---|---|---|---|---|---|---|

### Matrix 2: Modelling and Evaluation  
|Requirement ID | Analysis | Design | Implementation | Documentation | Test | Evaluation | Review | Deliverable |
|---|---|---|---|---|---|---|---|---|
|REQ-12|---|---|---|---|---|---|---|---|
|REQ-13|---|---|---|---|---|---|---|---|
|REQ-14|---|---|---|---|---|---|---|---|
|REQ-15|---|---|---|---|---|---|---|---|
|REQ-16|---|---|---|---|---|---|---|---|
|REQ-17|---|---|---|---|---|---|---|---|
|REQ-18|---|---|---|---|---|---|---|---|
|REQ-19|---|---|---|---|---|---|---|---|
|REQ-20|---|---|---|---|---|---|---|---|
|REQ-21|---|---|---|---|---|---|---|---|
|REQ-22|---|---|---|---|---|---|---|---|
|REQ-23|---|---|---|---|---|---|---|---|

### Matrix 3: Infrastructure and Tooling  
|Requirement ID | Analysis | Design | Implementation | Documentation | Test | Evaluation | Review | Deliverable |
|---|---|---|---|---|---|---|---|---|
|REQ-27|---|---|---|---|---|---|---|---|

### Matrix 4: Reporting and Explainability
|Requirement ID | Analysis | Design | Implementation | Documentation | Test | Evaluation | Review | Deliverable |
|---|---|---|---|---|---|---|---|---|
|REQ-28|---|---|---|---|---|---|---|---|
|REQ-29|---|---|---|---|---|---|---|---|
|REQ-30|---|---|---|---|---|---|---|---|
|REQ-31|---|---|---|---|---|---|---|---|
|REQ-32|---|---|---|---|---|---|---|---|
|REQ-33|---|---|---|---|---|---|---|---|
|REQ-34|---|---|---|---|---|---|---|---|
|REQ-35|---|---|---|---|---|---|---|---|
|REQ-36|---|---|---|---|---|---|---|---|

# Reference
[1]: Rama-Maneiro, Efrén, Juan C. Vidal, and Manuel Lama. "Deep learning for predictive business process monitoring: Review and benchmark." IEEE Transactions on Services Computing 16.1 (2021): 739-756.
[2]: Verenich, Ilya, et al. "Survey and cross-benchmark comparison of remaining time prediction methods in business process monitoring." ACM Transactions on Intelligent Systems and Technology (TIST) 10.4 (2019): 1-34.
