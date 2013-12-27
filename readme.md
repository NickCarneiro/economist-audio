# Download The Economist in Audio

A python script to download the economist mp3s to your pc.

# Warning

This doesn't actually work. The login fails. I believe it's because there are a bunch of javascript cookies that get included with the login post request.

I attempted to use Ghost.py which looks really promising, but the dependencies don't work out of the box on OSX so I'm abandoning this for now.

# Setup

* make a virtualenv if you want
* pip install -r requirements.always
* copy local.py.default to local.py and enter your credentials

# Usage

* run python extract.py
