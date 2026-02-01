# python ML model dployment with django 

# create a readme.md file of your projet 

# 1. create python env
we will use python env to create python envirament
'''bash
#  create python envirament
python -m venv .venv 
# activate the virtual enirament '''
source .venv/scripts/activate
# 2. install python libraries

'''
# web devlepment 
pip install django
# machil learning 
pip install numpy pandas matplotlib seaborn plotly scikit-learn xgboost

# for saving and loading model 
pip install joblib

# for notebook support 
pip install ipykernel

# 3. train your ML model

step 1 find the data
step 2 preprocess the data
step 3 train the model
step 4 evaluvate the model
step 4 save the model


ihave saved the models as 'xgb_model.pkl' in 'models' directory
> you can see the procedure of ML training  model and saving it in this [jupiter nootbook] (./ml_project/o1.ipynb)


# create a django project 
'''
django-admin startproject tip_prediction
cd tip_prediction
'''

# 5 create a django app
'''
bash 
python manage.py startapp ml_app
'''
# 6 update setting.py
