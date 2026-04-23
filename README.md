# remaining_time

**#Intro**
A predictive process mining solution that estimates the remaining time of running incidents from event logs. The main value is providing IT helpdesks with early warnings for long-running tickets, enabling proactive resource management and better service delivery. (Linas)

**#The Team** <br>
Linas   Butkus  <br>
Sarp    Aydoslu <br>
Qifan   Wu      <br>

**#Current Roles** <br>
Linas Butkus&nbsp;&nbsp;-  Evaluation & Visualization Lead, Quality & Tooling (Tests, CI) <br>
Sarp Aydoslu&nbsp;-  Data & Preprocessing Lead, Modelling & Experimentation Lead <br>
Qifan Wu&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Project Coordinator, Technical Lead <br>
<br>
PS: All of us are responsible for the documentation and reporting. <br>

**#Approaches** <br>
Trello: To manage tasks and track project progress, we use Trello with a Kanban-style.
Tasks are organized into categories such as “Backlog”, “In Progress”, “In Review” and
“Done”. This helps the team coordinate work, assign responsibilities, and monitor deadlines
throughout the project life-cycle. In this way, we become more aware of each other and
strive to work more harmoniously. <br>

GitHub: GitHub is used as the primary platform for version control and collaborative
development. Each team member works on branches, and changes are integrated through
pull requests followed by code reviews. This workflow enables effective change tracking,
minimizes merge conflicts, and supports a structured and transparent development process. <br>

PM4Py: In this project, PM4Py is used to load and preprocess event log data. By
presenting the functions necessary for loading and structuring logs, it ensures that each
entry is properly ordered by timestamp. These prefixes are important for calculating the
remaining time and preparing the data for machine learning models. Additionally, since
this system includes features such as filtering, sorting, and feature selection, it will help
us lay the keystones for the project. These steps must be followed to ensure clean and
consistent input data. PM4Py makes it easy to convert raw event logs into structured
representations; this data can then be processed using various tools. <br>

Pandas: Pandas is a data analysis library used to manipulate and transform structured
data. It can be used to load and process event log data, especially when working with
CSV files. In this project, it allows us to organize the data into a tabular format, perform
efficient operations such as filtering and aggregation, and compute features required for the
prediction task. These include metrics like elapsed time, number of events in a prefix, and
activity-related statistics. Overall, pandas plays a key role in preparing the final dataset
that is used as input for the machine learning models. <br>

ProM: ProM can be used to validate the quality of event logs by checking important
attributes such as case ID, activity and timestamp. Although it is not part of the main
pipeline, ProM can support exploratory analysis and future project extensions.
Disco: Disco is a process mining tool used for analysis of event log data. In this project,
it can be used to better understand the structure and behavior of the event log, which can
support feature engineering and data validation steps. <br>

Scikit-Learn: We use scikit-learn to implement and evaluate machine learning models
for predicting remaining time. It provides a consistent interface for training regression
models, such as linear regression and random forest. In this project, scikit-learn is used to
analyse the relationship between prefix-based features and the remaining time of a case.
scikit-learn also supports data splitting, preprocessing and hyperparameter adjustment. <br>

Matplotlib: Matplotlib is a visualisation library used to create plots and graphical
representations of data. In this project, it can be used mainly during the evaluation
phase to analyse the performance of machine learning models. It allows us to generate
plots. These include predicted vs. actual remaining time. They also include error
distributions. And they allow for performance comparisons across different prefix lengths.
These visualisations help us to see how well the models perform and spot any patterns or
weaknesses in the predictions. <br>

**#Orga** <br>
&nbsp;&nbsp;- regular weekly meeting: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sun. 19:30 - 20:30
