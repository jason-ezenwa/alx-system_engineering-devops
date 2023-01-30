# My first postmortem

__Issue Summary__

  The outage lasted for one hour, from 6:15pm when it began to 7:15pm (WAT) when the issue was resolved.
  Users were unable to get any service at port 80. 100% of the users attempting to establish connection at port 80 were unable to. The root cause of this outage was the absence of any listening directive on port 80 for the sites enabled.

__Timeline__
-	6:13pm: sites-enabled Nginx configuration implemented
-	6:15pm: Outage begins
-	6:15pm: Pagers alerted teams
-	6:23pm: Server block with port 80 listening directive added to sites-enabled.
-	6:25pm: Nginx is restarted.
-	6:25pm: Connections to port 80 are permitted again.

__Root Cause__

  At 6:13pm, some Nginx sites-enabled configurations were done on the server, with a listening directive for port 80 omitted. Since the configurations of sites-enabled are included in the nginx.conf http block, this caused errors and refusals when users attempted to connect on port 80. At first, ‘curl’ commands to port 80 were done, which resulted in connection refusals. ‘lsof’ was also done to see if any service was listening on port 80, but it was then discovered that there was nothing listening on port 80 which should not be, so checks were done and it was discovered that the sites-enabled default file did not contain a listening directive for port 80.

The issue was resolved by insistedly creating a symbolic link between sites-available default file, which had a port 80 listening directive and the sites-enabled default file, this created the listening directive in the sites-enabled default file. The Nginx service was restarted to implement all reconfigurations.

__Corrective and preventative measures__
-	Ensure that changes are reviewed and approved before being implemented in production
-	Configurations in the configuration files should be double checked in order to make sure nothing is omitted. 
-	Automated checks will be implemented.
