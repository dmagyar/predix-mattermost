#!/usr/bin/python

import json 
import os

data = json.loads(os.getenv("VCAP_SERVICES"))
pblob=data['predix-blobstore'][0]['credentials']
pbucket=pblob['url'][8:pblob['url'].index('.')]
tt=pblob['url'][len(pbucket)+12::]

print("PBLOB_URL=%s" % pblob['url'])
print("PBLOB_BUCKET=%s" % pbucket)
print("PBLOB_REGION=%s" % tt[0:tt.index('.')])
print("PBLOB_API_KEY=%s" % pblob['access_key_id'])
print("PBLOB_SECRET_KEY=%s" % pblob['secret_access_key'])
