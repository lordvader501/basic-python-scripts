# IP Address Checker
### Find the external as well as internal IP address of your computer.

It is a python code to make a request to [https://ipv4.icanhazip.com](https://ipv4.icanhazip.com), which in turn send a response back with your External IP address.
This response is in HTML so it also extracts only useful information from it and prints it as an output.

It uses socket module to get internal IP address.

#### Requirements:
* Install requests module.
* run `pip install requests`

#### Usage

* Clone the repo 
* open the `ip-checker` folder
* run `python ip-check.py`
* You just recieved your public and private IP.
