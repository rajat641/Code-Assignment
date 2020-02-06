# Code-Assignment
## Problem statement
Please write a web service that takes in a string and returns a boolean to indicate 
whether a word is a pyramid word. A word is a ‘pyramid’ word if you can arrange the letters in increasing 
frequency, starting with 1 and continuing without gaps and without duplicates.
Examples:
banana is a pyramid word because you have 1 'b', 2 'n's, and 3 'a's.
bandana is not a pyramid word because you have 1 'b' and 1 'd'.

## Installation Steps for Linux User

```
pip3 install virtualenv
```
```
virtualenv -p /usr/bin/python3 venv
```
```
source venv/bin/activate
```
```
pip3 install flask
```

## Run

```
python3 app.py
```
Once you run the above command, the using postman fire a GET request with input string as a query paramater.
GET Request - ``` http://127.0.0.1:5000/?query=weqqw```
The snapshor for the same is below -
