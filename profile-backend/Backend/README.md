# XMeme

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

XMeme is a Web app in which the user can post the memes using name, meme caption and URL of the meme.

- My Repo Contains :- 
  - Frontend
  - Backend 
  - Dockerize file

# Front End
    I have made front end using Reactjs. The interface is user friendly and used 
    axios for sending the API request to backend server. 
    
    Features :-
        - The user can Post the memes and latest 100 memes are displayed in 
          window.
        - The user can later update and make changes in the URL and Caption
          of the meme and the name is unchangeable.
        - By default the frontEnd part is exposed on port 3000.

# Back End
    I have made backend End using Django rest framework and used MySQL for
    storing data for sending the API request to backend server.
    
    Features :-
        - The user can Post the memes using POST mehtod.
        - The user can retrieve the memes using PATCH method.
        - All the memes are retrieve using GET method.
        - By default the BackEnd part is exposed on port 8080. 


### Installation


Install the dependencies and devDependencies and start the server.

$ node app
$ npm install 
$ node start
$ django 
$ python manage.py runserver 8080.

ENDPOINTS :-
    -localhost:3000 for reactjs
    -localhost:8080/memes for GET and POST method
    -localhost:8080/memes/<id> for PATCH and GET method
```
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version} .
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```
   [git-repo-url]: <https://github.com/