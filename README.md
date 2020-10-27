# Samsung DNAC client list (prototypes)

## Requirements
 1. docker (https://docs.docker.com/get-docker/)
 2. DNAC dashboard (Should be accessible from the server)

## How to run it.
 1. docker build --tag dnac-client:1.0 .
 2. docker run -p 5000:5000 dnac-client:1.0
 3. check the program running on the port 5000
 4. open the link : http://localhost:5000
