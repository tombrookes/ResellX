import requests

EBAY_FINDING_ENDPOINT = "https://svcs.ebay.com/services/search/FindingService/v1"
EBAY_BROWSE_ENDPOINT = "https://api.ebay.com/buy/browse/v1/item_summary/search"
HEADERS = {
    "X-EBAY-API-APP-ID": "<YOUR_APP_ID>",
    "Content-Type": "application/json"
}

def get_sold_listings(query, category_id):
    params = {
        "keywords": query,
        "categoryId": category_id,
        "outputSelector": "SellerInfo",
        "itemFilter": [
            {"name": "SoldItemsOnly", "value": True}
        ]
    }
    response = requests.get(EBAY_FINDING_ENDPOINT, params=params, headers=HEADERS)
    return response.json()

def get_active_listings(query, category_id):
    params = {
        "q": query,
        "category_ids": category_id,
        "filter": "buyingOptions:{FIXED_PRICE}"
    }
    response = requests.get(EBAY_BROWSE_ENDPOINT, params=params, headers=HEADERS)
    return response.json()