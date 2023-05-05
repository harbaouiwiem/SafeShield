# SafeShield 
#ELK
Once the Kibana interface opens , you should be able to access the dashbords and all the graphics areas .

Next we need to load the dashboard config we make in this prototype , in order to do so, go to the left menu and scroll down to the management icon , then under Kibana section , click on "Saved Objects".

On the top right corner of the interface , click on the "Import" Button.

The import widget will open up , then click on import again , you'll be asked to choose a file go to the project directory (~/Workspace/Siem/ELK/docker-elk/elasticsearch/config/) and choose "export.ndjson". Make sure the "automatically overwrite all saved objects" option is enabled , and then click on the bottom left blue "Import" Button

Now that we have the dashboards configured , go ahead and click on the "Dashboard" option in the left menu and choose "SafeShield Dashboard", then choose a filter and apply it .

