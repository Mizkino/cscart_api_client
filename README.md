# CS-Cart API Client for Python

Client for CS-Cart. wip


## Usage
```.py
import cscart

client = cscart.Client("https://storeofcscart.com", "admin@cscartstore.com", "APIKEYHOGEHOGE")

res = client.get_orders()
```

## install
```.sh
poetry add cscart_api_client
```
