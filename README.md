# Pyreact Fastapi
This project developed with react as FE and Fast API for REST APIs

## Back End developed with Fast API
Important Modules
`pip install fastapi`

You will also need an ASGI server, for production such as Uvicorn

`pip install uvicorn`

Elasticsearch modules

`pip install elasticsearch`

`pip install elasticsearch_dsl`

### Important code snippets
Inorder to run the server by running the python file instead of `uvicorn main:app --reload`

You run the API using `python main.py` on your host with port `8000`
```
if __name__ == "__main__":
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True, debug=True)
```

`#type:ignore` -- this comments helps you to ignore the pylance warning for the custom imports
## Front End developed with react
`$ create-react-app reactfe`

You are running `create-react-app` 4.0.1, which is behind the latest release (4.0.2).

We no longer support global installation of Create React App.

Please remove any global installs with one of the following commands:
- npm uninstall -g create-react-app
- yarn global remove create-react-app

The latest instructions for creating a new app can be found here:
https://create-react-app.dev/docs/getting-started/

Let's start using new commands:
yarn create react-app `<appname>`

Success! Created stocksfe at C:/Users/PATH/stocksfe
Inside that directory, you can run several commands:

  `yarn start`
    Starts the development server.

  `yarn build`
    Bundles the app into static files for production.

  `yarn test`
    Starts the test runner.

  `yarn eject`
    Removes this tool and copies build dependencies, configuration files
    and scripts into the app directory. If you do this, you can’t go back!

We suggest that you begin by typing:

  cd stocksfe
  yarn start

Happy hacking!
---------------------------------------------------------------------------------
### Modules and important front end commands
- `yarn add axios`
- `yarn add react-bootstrap`
- `yarn add bootstrap@4.6.0`
- `yarn add react-chartjs-2 chart.js` -- for charts

After the bootstrap and react-bootstrap libraries, Add the sytlesheets and react-bootstrap related javascript files in the `index.html` 

refer: https://react-bootstrap.github.io/getting-started/introduction/