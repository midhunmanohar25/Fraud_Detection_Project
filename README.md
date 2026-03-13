Career247_Capstone_Project_Pipeline
==============================

Designed and implemented an end-to-end machine learning–based fraud detection system to analyze financial transaction data and identify suspicious activities. The project includes data preprocessing, exploratory data analysis, feature engineering, model training, and a risk analysis interface to help detect fraudulent transactions and reduce financial risk.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── Website                <- Website used for this project
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    |   ├── Pages           <- Pages of the website used in this project    
    │   │   |
    |   |   ├── 1_Fraud Risk Engine.py
    |   |   ├── 2_Risk Analysis Section.py
    |   |   └── 3_Recommendations.py
    |   |
    |   |
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── df.pkl
    │   │   └── pipeline.pkl
    │   │
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
