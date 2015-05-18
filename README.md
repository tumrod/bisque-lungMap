# bisque-lungMap
[Bisque (Bio-Image Semantic Query User Environment)](http://bioimage.ucsb.edu/bisque)


## Requirements:
- python 2.7
- virtualenv 
- pip
- BeautifulSoup4

###### Using easy_install or pip to install
```
$ easy_install virtualenv
$ easy_install pip
$ easy_install BeautifulSoup4
```

(Note - for installations, you may need to use sudo. New versions of python may have pip already installed.)


## Getting it to work

#### 1. Clone this repository
```
$ git clone https://github.com/tumrod/bisque-lungMap.git
```

#### 2. Create a virtualenv  (you may need to specify the python path with: -p <python path>)
```
$ virtualenv bqapi
$ source bqapi/bin/activate 
```

#### 3. Fetch bqapi with the CAS option
```
(bqapi) $ pip install -i http://biodev.ece.ucsb.edu/py/bisque/dev bqapi[CAS]
```

#### 4. Move necessary packages into site-packages
```
(bqapi) $ sh setup_src.sh
```

#### 5. Run the script file
```
(bqapi) $ python <script_file.py>
```

### Tips: 
- You may need to use sudo at start of other commands if there are permission issues.
- You can deactivate the virtualenv by $ deactivate 

