## vzcards 
An application to connect two users, using their mobile numbers. Used for passing messages between two users.

### Installation
instructions:

    git clone https://github.com/poojapauskar/vzcards-api
    cd vzcards-api

### Deployment to Heroku
steps:

    Add a postgres and pgbackups (free tier) to your dyno.
    Add heroku remote to your git. git remote add heroku git://heroku.com/app.git
    Add this buildpack (heroku config:set BUILDPACK_URL='git://github.com/heroku/heroku-buildpack-python.git'). This is very important as heroku will read package.json file and consider it a node.js app.
    Just do your changes and push code to heroku remote like: git push heroku HEAD:master

### Issues and Pull Requests:
Feel free to log any issues here https://github.com/poojapauskar/vzcards-api/issues. If you wish to contribute, fork and send a pull request.

