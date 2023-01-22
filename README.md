
![](/images/logo_traiding.jpg)
# <center> Project: Analysis Traiding on MOEX in 2022  </center>
## Contents
1. [Project description](#Project-description)
2. [About Structure](#About%20Structure)
3. [Dependencies](#Dependencies)
4. [Download Project](#Download-Project)
5. [Autors](#Autors)
6. [Findings](Findings)

## Project description
///
> **Target** - The purpose of this project is to research the dynamics of the balance of traders over the trading period. Identify errors in trading operations and visualize the dependencies between them.
Provide suggestions and advice for future trading.

Main stage of Project:
* Data preparaition to needed format.
* Data structure research.
* Exploring data dependencies.
* Data cleaning.




**Purpose of preparation data** — 
Data preparation includes a deeper study of features and their comparison with each other.

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
* [main.ipynb](./main.ipynb) - jupyter-notebook, contained main code of project for first traider.
* [s_main.ipynb](./s_main.ipynb) - jupyter-notebook, contained main code of project for second traider.
* [crypto.ipynb](./crypto.ipynb) - jupyter-notebook, contained main code of project for second traider.

## Data Description

This project used data This project uses self-collected data.
For one year, a small group of 2 traders entered manually, without using any API, the results of their trading operations to control their transactions.
Trading was carried out with the help of several stock brokers and crypto exchanges, such as: Finam Trading, BKS Trading, and Binance, ByBit, respectively.

## Used Dependencies
* Python (3.9):
    * [numpy (1.20.3)](https://numpy.org)
    * [pandas (1.3.4)](https://pandas.pydata.org)
    * [plotly (5.12)](https://plotly.com/python/)
    * [seaborn (0.11.2)](https://seaborn.pydata.org)

## Download Project

```
git clone https://github.com/dI98Sk/Traiding_Analyse
```

## Usage
All infirmation show in these jupyter files:
* main.ipynb
* s_main.ipynb
* crypto.ipynb


##  Autor

* [Skakun Dmitrii](https://www.instagram.com/skakun_dr/)

## Findings

In conclusion, we can say that the work done has a positive effect on future modeling, and helps to build a more accurate model.
This work allows you to analyze the results of trading for the year, identify weaknesses, and points that require attention in the implementation of future transactions.
