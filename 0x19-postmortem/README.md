# My first postmortem

__Issue Summary__
The outage lasted for one hour, from 6:15pm when it began to 7:15pm (WAT) when the issue was resolved.
Users were unable to get any service at port 80. 100% of the users attempting to establish connection at port 80 were unable to. The root cause of this putage was the absence of any listening directive on port 80 for the sites enabled.
