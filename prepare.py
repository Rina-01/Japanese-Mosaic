import os

DIR_NAME = os.path.abspath(os.path.dirname(__file__))


if not os.path.exists(DIR_NAME + "\\logs\\"):
    os.makedirs(DIR_NAME + "\\logs\\")
    
if not os.path.exists(DIR_NAME + "\\sol_files\\"):
    os.makedirs(DIR_NAME + "\\sol_files\\")

if not os.path.exists(DIR_NAME + "\\task_files\\"):
    os.makedirs(DIR_NAME + "\\task_files\\")
    
if not os.path.exists(DIR_NAME + "\\tasks\\"):
    os.makedirs(DIR_NAME + "\\tasks\\")
