# bisque-lungMap

Requirements:
python 2.7
virtualenv - $ easy_install virtualenv
pip - $ pip sudo apt-get install python-pip
BeautifulSoup4 - $ easy_install BeautifulSoup4

=============================================================
Clone:
git clone https://github.com/tumrod/bisque-lungMap.git
=============================================================

1. Create a virtualenv and fetch bqapi with the CAS option
$ virtualenv bqapi
$ source bqapi/bin/activate 
$ pip install -i http://biodev.ece.ucsb.edu/py/bisque/dev bqapi[CAS]

2. Move necessary packages into site-packages
(bqapi) $ sh setup_src.sh

3. To run a python script, make sure that you have activated the virtualenv
[it should look like (bqapi) $ ]

$ source bqapi/bin/activate 

4. Run the script file
(bqapi) $ python <script_file.py>

** You can deactivate the virtualenv by $ deactivate 

==============================================================

Tips: 
For pip, you may need to use: sudo easy_install pip
You may need to use sudo at start of other commands if there are permission issues.
For virtualenv, you may need to specify the python path with: -p <python path>

