# remaining_time

# Intro
A predictive process mining solution that estimates the remaining time of running incidents from event logs. The main value is providing IT helpdesks with early warnings for long-running tickets, enabling proactive resource management and better service delivery.

# The Team  
Linas   Butkus  
Sarp    Aydoslu  
Qifan   Wu      

# Current Roles  
Sarp Aydoslu&nbsp;&nbsp;-  Evaluation & Visualization Lead, Quality & Tooling (Tests, CI)  
Linas Butkus&nbsp;-  Data & Preprocessing Lead, Modelling Lead (Shared)  
Qifan Wu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Project Coordinator, Technical Lead, Experimentation Lead  
  
PS: All of us are responsible for the documentation and reporting.  

# Peer Review  
Linas Butkus&nbsp;&nbsp;-> Sarp Aydoslu  
Sarp Aydoslu&nbsp;-> Qifan Wu  
Qifan Wu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-> Linas Butkus  

# Approaches  
Trello: To manage tasks and track project progress, we use Trello with a Kanban-style.
Tasks are organized into categories such as “Backlog”, “In Progress”, “In Review” and
“Done”. This helps the team coordinate work, assign responsibilities, and monitor deadlines
throughout the project life-cycle. In this way, we become more aware of each other and
strive to work more harmoniously.  

GitHub: GitHub is used as the primary platform for version control and collaborative
development. Each team member works on branches, and changes are integrated through
pull requests followed by code reviews. This workflow enables effective change tracking,
minimizes merge conflicts, and supports a structured and transparent development process.  

PM4Py: In this project, PM4Py is used to load and preprocess event log data. By
presenting the functions necessary for loading and structuring logs, it ensures that each
entry is properly ordered by timestamp. These prefixes are important for calculating the
remaining time and preparing the data for machine learning models. Additionally, since
this system includes features such as filtering, sorting, and feature selection, it will help
us lay the keystones for the project. These steps must be followed to ensure clean and
consistent input data. PM4Py makes it easy to convert raw event logs into structured
representations; this data can then be processed using various tools.  

Pandas: Pandas is a data analysis library used to manipulate and transform structured
data. It can be used to load and process event log data, especially when working with
CSV files. In this project, it allows us to organize the data into a tabular format, perform
efficient operations such as filtering and aggregation, and compute features required for the
prediction task. These include metrics like elapsed time, number of events in a prefix, and
activity-related statistics. Overall, pandas plays a key role in preparing the final dataset
that is used as input for the machine learning models.  

ProM: ProM can be used to validate the quality of event logs by checking important
attributes such as case ID, activity and timestamp. Although it is not part of the main
pipeline, ProM can support exploratory analysis and future project extensions.
Disco: Disco is a process mining tool used for analysis of event log data. In this project,
it can be used to better understand the structure and behavior of the event log, which can
support feature engineering and data validation steps.  

Scikit-Learn: We use scikit-learn to implement and evaluate machine learning models
for predicting remaining time. It provides a consistent interface for training regression
models, such as linear regression and random forest. In this project, scikit-learn is used to
analyse the relationship between prefix-based features and the remaining time of a case.
scikit-learn also supports data splitting, preprocessing and hyperparameter adjustment.  

Matplotlib: Matplotlib is a visualisation library used to create plots and graphical
representations of data. In this project, it can be used mainly during the evaluation
phase to analyse the performance of machine learning models. It allows us to generate
plots. These include predicted vs. actual remaining time. They also include error
distributions. And they allow for performance comparisons across different prefix lengths.
These visualisations help us to see how well the models perform and spot any patterns or
weaknesses in the predictions.  

# Setup Instruction
For Python 3.10 or newer.

### To create a virtual environment

```bash
python -m venv venv
```

### To activate the virtual environment

#### Windows
```bash
venv\Scripts\activate
```

#### macOS / Linux
```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```
# Dataset
The dataset used is the "BPI Challenge 2013: Incident Management Log", which consists of 7.556 incidents and 2.306 closed problems. These stem from Volvo IT Belgium's incident and problem management system and directly concern IT incident handling.

The incident process strives to restore normale service when an incident occurs. It entails the entire lifecycle of a case, including escalation across support lines. For this purpose the dataset also records priority-related attributes such as impact and urgency.

## Setup & Download
To download and place the dataset, a data setup script is provided.
1. Open terminal.
2. Navigate to the root directory of the repository and then to directory remaining_time.
3. Run the data setup script:
   ```bash
   # On Windows (or inside an active virtual environment):
   python data_setup.py

   # On macOS/Linux (without a virtual environment):
   python3 data_setup.py
   ```

## Testing

The project includes an automated test suite implemented with pytest.

To run all tests:

```bash
pytest
```
To run a specific test file:

```bash
pytest tests/test_model_evaluation.py
```

## Prototype and Reproduction

Please refer to the notebooks.

## Architecture

In the main directory, you can find:

notebooks: a directory which stores jupyter-notebooks that provides information on how to reproduce the training and testing process, along with a notebook on how to perform our model on new data. 

outputs: a directory which stores two plots regarding the comparison between baseline model and our two more advanced models, together with a short analysis file.

remaining_time: one of the most important directories in our project, which stores program files that assist in preprocessing data, training model and evaluating model. For more information, please refer to the directory's archtecture file.

requirement_engineering: a directory which contains the bpmn-models regrading the workfloe of this project and a markdown file which analyses the requirements in this project and discusses their necessity and realisation in this project.

reviews: a directory where you can find our milestone 0 files about the project setup and some weekly meeting files.

tests: one of the most important directories in our project, which contains program files supporting automatic unit tests on the program files in the remaining_time directory.

training_data: a directory which contains the used data set for training the model; also used in the reproduction phase.

README.md: this file; explains the general information about the team, methodology, instructions on setup, architecture and organizational issues.

model_metrics.csv: a file of evaluation results of the trained models, based on prefix length, MAE, RMSE, MedAE, and R^2 Score.

model_scores.csv: a file conatining more details on statistical comparison of the trained models against the baseline model, as well as the parameters selected for each model.

reg_ols.pkl: a file which contains our trained linear regression model.

requirements.txt: a file which lists all required/used sources/libraries in this project.

ridge.pkl: a file which contains our trained ridge regression model.

sscaler.pkl: a file which contains the standard scaler used in this project.

# Results

As shown in the outputs/plots, the baseline model performs the worst. However, the trained linear regression model and ridge regression model perform similarly, while according to our super score defined in requirements_engineering.md, the ridge regression model performs slightly better than the linear regression model. 

Regarding the definition of "success" stated in the same markdown file: unfortunately, none of our models satisifies this standard.

Nevertheless, the linear regression model might also perform better on new data due to the limitation of our used data set for training. Therefore, it is recommanded to try both models once and pick your more preferred result.

# Orga  
&nbsp;&nbsp;- regular weekly meeting:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sun. 19:30 - 20:30

