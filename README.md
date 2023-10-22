# "New York Housing Admin"
## Midterm Test for Advanced Programming Class B kelompok 10.
This Midterm Test requires groups of college students to make a Python program that mainly uses one of the following datasets:
1. <a href="https://www.kaggle.com/datasets/aayushmishra1512/faang-complete-stock-data/download?datasetVersionNumber=1" target="_blank">Stock Price</a>
2. <a href="https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data/download?datasetVersionNumber=3" target="_blank">NYC Housing</a>
3. <a href="https://www.kaggle.com/datasets/abecklas/fifa-world-cup/download?datasetVersionNumber=5" target="_blank">FIFA World Cup</a>
4. <a href="https://www.kaggle.com/datasets/volodymyrgavrysh/bank-marketing-campaigns-dataset/download?datasetVersionNumber=1" target="_blank">Bank Marketing</a>
5. <a href="https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data/download?datasetVersionNumber=2" target="_blank">Breast Cancer</a>
6. <a href="https://www.kaggle.com/datasets/fedesoriano/the-boston-houseprice-data/download?datasetVersionNumber=1" target="_blank">Boston Housing</a>
7. <a href="https://drive.google.com/file/d/1mtQC1UzndoJdLx0gZSxp8H3ZOvALiO_q/view?usp=drive_link" target="_blank">Class Attendance</a>

Here, we have chosen the NYC Housing dataset, and we succeeded to make a program titled "New York Housing Admin"
## Features:
Each of the following features are completed with input handling, which means whenever the user enters the wrong or invalid input, the program warns the user and asks to re-enter the input.

### 1. Show housing informations
Here, the user can see a list of housing informations. The user can then choose to sort the list by which column, in ascending or descending order.

### 2. Search for housing informations
The user can search for specific housing information. The user can choose to search by housing id (yields 1 result or none), housing name, price, etc.

### 3. Add housing informations
The user can also add housing information.

### 4. Update housing informations
The user can change the details of the existing information. The user can also choose to not change some details and only change some specific parts.

### 5. Delete housing informations
The user can delete a housing information by id. The user would first be asked to confirm if he really intends to delete the data.

### 6. Saving system using <strong>temporary file</strong>
The changes made by the previous functionalities are not directly written into the actual dataset file, but rather stored in a temporary file.
The user can explicitly commands the program to save the changes made to the dataset. If the user attempts to exit the program and there is unsaved changes, the program asks the user if he wanted to save it.
