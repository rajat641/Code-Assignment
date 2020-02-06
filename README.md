# Code-Assignment
## Problem statement
Please write a web service that takes in a string and returns a boolean to indicate 
whether a word is a pyramid word. A word is a ‘pyramid’ word if you can arrange the letters in increasing 
frequency, starting with 1 and continuing without gaps and without duplicates.
Examples:
banana is a pyramid word because you have 1 'b', 2 'n's, and 3 'a's.
bandana is not a pyramid word because you have 1 'b' and 1 'd'.

## Installation/Set-Up Steps for Linux User
 ``It is assumed that the testing machine has python3 and pip already installed in it.``

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
GET Request - ``` http://127.0.0.1:5000/?query=<INPUT_STRING>```
The snapshor for the same is below -

![WhatsApp Image 2020-02-05 at 8 37 09 PM](https://user-images.githubusercontent.com/8374949/73907463-9b23d380-4863-11ea-8351-88ad156598b5.jpeg)

