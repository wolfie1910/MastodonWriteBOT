from six.moves import urllib
from datetime import datetime
from subprocess import call
from mastodon import Mastodon
import time
import threading
import csv
import os
import json
import time
import signal
import sys
import os.path        # For checking whether secrets file exists
import requests       # For doing the web stuff, dummy!

###############################################################################
# INITIALISATION
###############################################################################

do_upload = True
# Run without uploading, if specified
if '--no-upload' in sys.argv:
    do_upload = False

# Check mastostats.csv exists, if not, create it
if not os.path.isfile("mastostats.csv"):    
        print("mastostats.csv does not exist, creating it...")

        # Create CSV header row
        with open("mastostats.csv", "w") as myfile:
            myfile.write("timestamp,usercount,tootscount\n")
        myfile.close()

# Returns the parameter from the specified file
def get_parameter( parameter, file_path ):
    # Check if secrets file exists
    if not os.path.isfile(file_path):    
        print("File %s not found, exiting."%file_path)
        sys.exit(0)

    # Find parameter in file
    with open( file_path ) as f:
        for line in f:
            if line.startswith( parameter ):
                return line.replace(parameter + ":", "").strip()

    # Cannot find parameter, exit
    print(file_path + "  Missing parameter %s "%parameter)
    sys.exit(0)

# Load secrets from secrets file
secrets_filepath = "secrets/secrets.txt"
uc_client_id     = get_parameter("uc_client_id",     secrets_filepath)
uc_client_secret = get_parameter("uc_client_secret", secrets_filepath)
uc_access_token  = get_parameter("uc_access_token",  secrets_filepath)


# Initialise Mastodon API (change mastodon_hostname to your mastodon instance)
mastodon = Mastodon(
    client_id = uc_client_id,
    client_secret = uc_client_secret,
    access_token = uc_access_token,
    api_base_url = 'https://mastodon_hostname',
)

# Initialise access headers
headers={ 'Authorization': 'Bearer %s'%uc_access_token }

#Writing a post: status is the variable for the toot 
Mastodon.status_post(status='I love to sp@m with my t00ts... *__*', in_reply_to_id=None, media_ids=None, sensitive=False, visibility='public', spoiler_text=None)
