# Homework 1 - Analysis with datasets

### Задания 1:
**Teacher dataset:** Australian AIDS Survival Data

Questions:
1. Прочитайте данные из файла Aids2.csv и загрузите их в датафрейм.
Для этого сделайте импорт библиотеки pandas (import pandas as pd) и воспользуйтесь методом read_csv.
2. Узнайте информацию о размере датасета и типах хранящихся в нем данных.
3. Основываясь на информации из датасета, выяснить, кого больше в процентном
соотношении: мужчин или женщин, – заразившихся СПИДом.
4. Выяснить, каков процент мужчин до 45 лет, успешно прошедших курс лечения,
по отношению к общему количеству заболевших мужчин.
5. Показать, как соотносятся возраст и смертность у пациентов старше 14 лет.
Постройте график функции.
    5.1. при помощи метода plot.line
    5.2. при помощи библиотеки plotly
6. Построить круговую диаграмму, отражающую процентное соотношение
умерших пациентов в возрасте до 30 лет, проведя распределение по регионам
Австралии.
7. Подсчитать средний возраст умерших в представленный в датасете период от
СПИДа пациентов для каждого региона и для Австралии в целом. Результат
представьте гистограммой с группировкой.
8. Определить возраст самого молодого и самого старого умерших пациентов в
каждом регионе. В каких регионах среди инфицированных было больше
пожилых людей (от 55)? В каких преобладает молодежь (до 30)? В каких
больше всего людей среднего возраста (от 31 до 54)?
9. Какими способами происходило заражение СПИДом по регионам? Результат в
виде количества случаев заражения визуализируйте гистограммой.
10.В какой возрастной группе (до 30, от 31 до 54, от 55) процент выживших
пациентов больше, чем умерших? Если таких групп несколько, перечислите
все.

### Задания 2:
**My dataset:** Google play store apps data

Questions:
0. Size, Shape and dtypes
1. Which is the percentage of free and paid applications? how this percentage is related to the category they belong to?
2. Which is the average price and installs of apps by content rating
3. Which is the most popular Genre and which are its top 10 apps
4. which is the year with more application last updates, represent the number of updates over time
5. Find the worst app, means that is not free, was last updated before 2016, have a rating lower than 2 and is the less installed
6. which is the minimum version of android of the categories of the top 100 apps that its content rating is for Everyone
7. how many apps are in each: super light (<2MB) light (2MB;30MB) bulky(30MB>) and 'varies with device'