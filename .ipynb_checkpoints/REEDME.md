
![](./images/data_cleaning.png)
# <center> Research result of traiding on MOEX market and Cryptocurency </center>
## Contents
1. [Project description](#Project-description)
2. [Описание данных](#Описание-данных)
3. [Зависимости](#Зависимости)
4. [Установка проекта](#Установка-проекта)
5. [Использование проекта](#Использование-проекта)
6. [Авторы](#Авторы)
7. [Выводы](Использование-проекта)

## Project description

> **MOEX** - is the largest exchange in Russia, operating trading markets in equities, bonds, derivatives, the foreign exchange market, money markets, and precious metals. The exchange was formed in 2011 in a merger of the Moscow Interbank Currency Exchange and the Russian Trading System.


Main stage of work on project:
* Preparate data to usefull format.
* Research traiding sistem.
* Drop noninformative signs and records.
* Give recomendation for next trading year.

**Purpose preparate data** — 
Prepare data for create charts, creating informative features to combine data into groups.

**This project** is aimed at analyzing data for the year, identifying errors and formulating recommendations for improving performance.

**About structure of project:**
* [data](./data) - folder with date of project
* [images](./images) - folder with images, nessesary to project
* [outliers_lib](./outliers_lib) - папка со вспомогательными модулями для обработки выбросов 
* [main.ipynb](./main.ipynb) - jupyter-notebook, containig main project code, which preparate date and reserch signs (for market data from first traider)
* [crypto.ipynb](./main.ipynb) - jupyter-notebook, containig main project code, which preparate date and reserch signs (for cryptocerrency data from first traider)
* [s_main.ipynb](./main.ipynb) - jupyter-notebook, containig main project code, which preparate date and reserch signs (for market data from second traider)

## Contents Data
For this project was used data from privat traiders since 07th Nov 2021.


The request from the data provider was to structure and visualize outlier cleanup indicators and prepare recommendations.

The initial dataset is a set of data from a table with the history of trading for a certain period.


## Used methods
* Python (3.9):
    * [numpy (1.20.3)](https://numpy.org)
    * [pandas (1.3.4)](https://pandas.pydata.org)
    * [matplotlib (3.4.3)](https://matplotlib.org)
    * [seaborn (0.11.2)](https://seaborn.pydata.org)


## Autor

* [Skakun_Dmitrii](https://www.instagram.com/skakun_dr/)

## Sumary

According to the results of the work done, we can talk about ready-made data recommendations based on the analysis of the history of traiding.