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
**Type:**  
**Text:**

## Modelling and Evaluation
**ID:** REQ-xx  
**Type:**  
**Text:**

## Infrastructure and Tooling
**ID:** REQ-xx  
**Type:**  
**Text:**

## Reporting and Explainability
**ID:** REQ-xx  
**Type:**  
**Text:**

# Module Responsibility  
Sarp: REQ-xx, REQ-xx, ...
Linas: 
Qifan: 

# Functional Model

**Traceability Matric**
