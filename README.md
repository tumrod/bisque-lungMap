# bisque-lungMap

Requirements:
python 2.7
virtualenv - $ easy_install virtualenv
pip - $  easy_install pip
BeautifulSoup4 - $ easy_install BeautifulSoup4

(Note - for installations, you may need to use sudo. New versions of python may have pip already installed.)

=============================================================
Clone:
git clone https://github.com/tumrod/bisque-lungMap.git
=============================================================

1. Create a virtualenv  (you may need to specify the python path with: -p <python path>)
$ virtualenv bqapi
$ source bqapi/bin/activate 

2. Fetch bqapi with the CAS option
(bqapi) $ pip install -i http://biodev.ece.ucsb.edu/py/bisque/dev bqapi[CAS]

3. Move necessary packages into site-packages
(bqapi) $ sh setup_src.sh

4. Run the script file
(bqapi) $ python <script_file.py>


==============================================================

Tips: 
You may need to use sudo at start of other commands if there are permission issues.
You can deactivate the virtualenv by $ deactivate 

