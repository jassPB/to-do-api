# to-do-api
Elaborated by: Joseph Piñar Baltodano

## Table of contents
- [Description](#description)
- [Features](#features)
- [How use?](#how-use)
- [How contribute?](#how-contribute)
- [What about the license?](#what-about-the-license)


### Description
This is a To-Do API writes in Python using the flask framework

### Features
- Consume all task storaged with the endpoint `/tasks` and method <font color=blue>GET</font>
- Consume one task storaged with the endpoint `/task/<id>` and method <font color=blue>GET</font> **(Work in process)**
- Add new task with the endpoint `/task` and method <font color=green>POST</font> **(Work in process)**
- Update one task storaged with the endpoint `/task/<id>` and method <font color=#AA336A>UPDATE</font> **(Work in process)**
- Delete one task storaged with the endpoint `/task/<id>` and method <font color=red>DELETE</font> **(Work in process)**

### How use?
1. Clone the repository in your computer and go to the directory following this commands in your terminal:
    ```bash
    git clone https://github.com/jassPB/to-do-api.git 
    cd to-do-api
    ```
2. Run the following command in your terminal for install all requirements
   ```bash
   pip3 install -r requirements.txt
   ```    
   If not works try chance `pip3` for `pip`
3. Run the following command in your terminal for start the server
    ```bash
    python3 src/app.py
    ```    
    If not works try chance `python3` for `python`
4. In your browser go to [localhost:4000](http://localhost:4000/tasks)

### How contribute?
1. Create a fork of the repository in GitHub
2. Clone your repository on your computer following this commands:
    ```bash
    git clone https://github.com/<your username>/to-do-api.git 
    cd to-do-api
    ```
3. Create new branch with a descriptive name of the functionality you are going to contribute to
    ```bash
    git checkout -b <feature>
    ```
4. When you commit changes try descrive this changes in one line message
5. When you have all the commits push this changes
    ```bash
    git push origin <branch-name>
    ```
6. Go to GitHub and create PR in this repository and explain all changes with all details and example images

### What about the license?
This API have GNU GPLv3 license, so you can modify the code and distribute it, as long as you do it under the same license
