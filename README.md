*Mattermost on Predix*

1) Create the following services (if you change the name of the service, alter manifest.yml too)
```
cf create-service predix-blobstore Tiered dmblob1
cf create-service postgres shared-nr dmsql1
```

2) Push the app to CF, visit URL to create admin account



