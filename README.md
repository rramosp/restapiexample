# example REST service with Flask

First, build your container

    docker build -t api .

Then, run the container

    docker run -it -p 5001:5000 api

Finally, on a separate shell run the client to make requests

    python client.py

