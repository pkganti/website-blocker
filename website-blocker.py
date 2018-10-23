import os
import time
from datetime import datetime as dt

host_file_path = '/etc/hosts'
redirect_url = '127.0.0.1' # Redirect URL when you try to access blocked website
blocked_sites = ['www.facebook.com', 'facebook.com', 'www.instagram.com', 'instagram.com', 'www.yahoo.com']

while True:
    # Check the time is between 8 AM to 6 PM which is when we want to block the sites
    if 8 < dt.now().time().hour < 18:
        with open(host_file_path, 'r+') as f:
            content = f.read()
            for site in blocked_sites:
                if site in content:
                    pass
                else:
                    f.write(redirect_url+" "+site+"\n")

    else:
        with open(host_file_path, 'r+') as f:
            content = f.readlines()
            f.seek(0) # To set the pointer back to the initial position of the file
            for line in content:
                if not any(site in line for site in blocked_sites):
                    f.write(line)
            f.truncate()
            print content

    # Just to make sure this script initiates every 5 seconds without the need to run it through Cron
    time.sleep(5)
