# remaining_time

## Intro
A predictive process mining solution that estimates the remaining time of running incidents from event logs. The main value is providing IT helpdesks with early warnings for long-running tickets, enabling proactive resource management and better service delivery.

## The Team  
Linas   Butkus  
Sarp    Aydoslu  
Qifan   Wu      

## Approaches  
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

## Setup Instruction
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
## Dataset
The dataset used is the "BPI Challenge 2013: Incident Management Log", which consists of 7.554 cases and 65533 events. These stem from Volvo IT Belgium's incident and problem management system and directly concern IT incident handling.

The incident process strives to restore normale service when an incident occurs. It entails the entire lifecycle of a case, including escalation across support lines. For this purpose the dataset also records priority-related attributes such as impact and urgency.

### Setup & Download
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
## End-to-end Usage
To easily use our product, please refer to ../src and find main.py. You can simply run this python file and get the models trained with some useful plots directly presented after the training and saving process is done. 
Please follow the last steps form "Setup & Download" and perform the following steps:
1. Run the main.py:
   ```bash
   # On Windows (or inside an active virtual environment):
   python main.py

   # On macOS/Linux (without a virtual environment):
   python3 main.py
   ```
Since the complexity of our code is nearly in $\mathcal{O}(n^3)$, please be patient and wait for a while before the procedure terminates.

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

artifacts: a directory which contains our trained models, metrics and other generated outputs.

figures: a directory which stores two plots regarding the comparison between baseline model and our two more advanced models, together with a short analysis file.

notebooks: a directory which stores jupyter-notebooks that provides information on how to reproduce the training and testing process, along with a notebook on how to perform our model on new data. 

requirement_engineering: a directory which contains the bpmn-models regrading the workfloe of this project and a markdown file which analyses the requirements in this project and discusses their necessity and realisation in this project.

src: one of the most important directories in our project, which stores program files that assist in preprocessing data, training model and evaluating model. For more information, please refer to the directory's archtecture file.

tests: one of the most important directories in our project, which contains program files supporting automatic unit tests on the program files in the remaining_time directory.

ARCHITECTURE.md: a file which contains general information on all of our modules inside of the src directory.

README.md: this file; explains the general information about the team, methodology, instructions on setup, architecture and organizational issues.

requirements.txt: a file which lists all required/used sources/libraries in this project.

## Results

As shown in the outputs/plots, the baseline model performs the worst. However, the trained linear regression model and ridge regression model perform similarly, while according to our super score defined in requirements_engineering.md, the ridge regression model performs slightly better than the linear regression model. 

Regarding the definition of "success" stated in the same markdown file: both of our more advanced models satisfy this standard, and we also expect them to predict relatively accurate remaining times on real-life datasets.

Nevertheless, the linear regression model might also perform better on new data due to the limitation of our used data set for training. Therefore, it is recommanded to try both models once and pick your more preferred result.
