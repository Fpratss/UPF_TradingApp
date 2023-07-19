# Trading App

This project is a trading application that allows users to set risk parameters, track trade orders, and receive real-time trade information.

## Architecture

The architecture of the trading app is as follows:


```
|---------------------------------------------------|
|                 Front-end (Web Browser)           |
|                                                   |
|  +---------------------------------------------+  |
|  |                  HTML/CSS/JS                |  |
|  |  +---------------------------------------+  |  |
|  |  |        WebSocket Connection           |  |  |
|  |  |                                       |  |  |
|  |  |      +------------------------+       |  |  |
|  |  |      |    Azure Functions      |      |  |  |
|  |  |      |       (API)             |      |  |  |
|  |  |      |                         |      |  |  |
|  |  |      |  +--------------------+ |      |  |  |
|  |  |      |  |     MetaTrader     | |      |  |  |
|  |  |      |  |        API         | |      |  |  |
|  |  |      |  +--------------------+ |      |  |  |
|  |  |      |                         |      |  |  |
|  |  +------+-------------------------+------+  |  |
|  |                                             |  |
|  +---------------------------------------------+  |
|                                                   |
|---------------------------------------------------|

```


- **Front-end (Web Browser):** The user interface of the trading app, built using HTML, CSS, and JavaScript. It interacts with the back-end via WebSocket connections.

- **WebSocket Connection:** Enables real-time communication between the front-end and the back-end for receiving trade information.

- **Azure Functions (API):** The back-end of the trading app built using Azure Functions. It provides API endpoints for the front-end to interact with, handles WebSocket communication, and hosts the trading strategies.

- **MetaTrader API:** The API provided by MetaTrader that allows the back-end to establish a connection with the MetaTrader platform for executing trades and retrieving market data.

## Usage

1. Clone the repository.
2. Set up the front-end by hosting the HTML, CSS, and JavaScript files on a web server.
3. Set up the Azure Functions back-end by deploying the API to Azure Functions.
4. Configure the MetaTrader API connection settings in the back-end code.
5. Access the front-end in a web browser to use the trading app.

## License

This project is licensed under the [MIT License](LICENSE).
