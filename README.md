
![](/images/hh_logo.jpg)
# <center> Project: Resume analysis for HH.ru </center>
## Contents
1. [Project description](#Project-description)
2. [About Structure](#About%20Structure)
3. [Dependencies](#Dependencies)
4. [Download Project](#Download-Project)
5. [Autors](#Autors)
6. [Findings](Findings)

## Project description

> **HH.ru** - HeadHunter (hh.ru) is the largest Russian online recruitment company developing business in Russia, Belarus, and Kazakhstan. More than 515 thousand companies are HeadHunter clients. The extensive database of applicants on hh.ru contains more than 55 million resumes, and the average daily number of vacancies exceeds 933 thousand. According to SimilarWeb, HeadHunter ranks third in the world in popularity among job search portals and employees[3].


Main stage of Project:
* Formulation of the problem.
* Data structure research.
* Data preparation.
* Exploring data dependencies.
* Data cleaning.




**Purpose of formulation of the problem** — 
By setting the task, we understand the acquaintance with the data and the initial preparation of the data for work.

**Purpose of data structure research** — 
The research of the data structure is understood as the division of some features into several more informative ones. The study of the diversity of features obtained from the database. Suggestion for future work.

**Purpose of data data preparation** — 
Data preparation includes a deeper study of features and their comparison with each other.

**Purpose of exploring data dependencies** — 
The study of dependencies in data refers to the construction of pivot tables and the visualization of graphs to form an understanding of the need for further transformations. Based on the information obtained at this stage, we can get an understanding of the trends in the studied traits, outliers and traits that require detailed study.

**Purpose of data cleaning** — 
Drop "trash", that can interfere with the simulation or distort his result. In many tasks data cleaning - this is main part of stage of preparation data to build a model. 
For that need a lot of time to work.

**Adout Structure:**
* [data](./data) - folder with general and additional data base
* [plotly](./plotly) - folder with picture of diagrams from main file.
* [Project-1. Main-File.ipynb](./Project-1.%20Main-File.ipynb.ipynb) - jupyter-notebook, contained main code of project.


## Data Description
This project uses data from the training task SkillFactory School [SkillFactory School.](https://drive.google.com/file/d/1gahvwyBSM-OxLu7atC9aBoRj0xb1tspz/view?usp=sharing)

 Or you can unarhiv (dst-3.0_16_1_hh_database.csv.zip) file from Data folder.

The requirements of the terms of reference were to build a model that would predict a fair salary, based on the parameters indicated by the applicant, as well as the level of education and city of residence.

The initial dataset is a set of data from a table with information about the parameters of various candidates indicated in the resume for a certain period.

 It contains information about 23 features that describe candidates.

## Used Dependencies
* Python (3.9):
    * [numpy (1.20.3)](https://numpy.org)
    * [pandas (1.3.4)](https://pandas.pydata.org)
    * [plotly (5.12)](https://plotly.com/python/)
    * [seaborn (0.11.2)](https://seaborn.pydata.org)

## Download Project

```
git clone https://github.com/dI98Sk/Project_HH
```

## Usage
All infirmation show in  Project-1. Main-File.ipynb.

##  Autor

* [Skakun Dmitrii](https://www.instagram.com/skakun_dr/)

## Findings

In conclusion, we can say that the work done has a positive effect on future modeling, and helps to build a more accurate model.
