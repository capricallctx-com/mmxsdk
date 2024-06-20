import requests

# Define the base URL of your API
base_url = "http://localhost:11380/"  # replace with your actual API base URL

# Define the endpoints based on the variable sub_path in WebAPI::http_request_async
endpoints = [
    "/config/get",
    "/config/set",
    "/exit",
    "/node/exit",
    "/node/info",
    "/node/log",
    "/node/graph/blocks",
    "/header",
    "/headers",
    "/block",
    "/blocks",
    "/transaction",
    "/transactions",
    "/address",
    "/balance",
    "/contract",
    "/swap/list",
    "/swap/info",
    "/swap/user_info",
    "/swap/history",
    "/swap/trade_estimate",
    "/offer/trade_estimate",
    "/farmers",
    "/farmer",
    "/address/history",
    "/contract/exec_history",
    "/wallet/keys",
    "/wallet/seed",
    "/wallet/balance",
    "/wallet/contracts",
    "/wallet/plots",
    "/wallet/address",
    "/wallet/address_info",
    "/wallet/tokens",
    "/wallet/history",
    "/wallet/history/memo",
    "/wallet/tx_history",
    "/wallet/offers",
    "/wallet/send",
    "/wallet/send_many",
    "/wallet/deploy",
    "/wallet/execute",
    "/wallet/offer",
    "/wallet/cancel_offer",
    "/wallet/offer_withdraw",
    "/wallet/offer_trade",
    "/wallet/accept_offer",
    "/wallet/swap/liquid",
    "/wallet/swap/trade",
    "/wallet/swap/add_liquid",
    "/wallet/swap/rem_liquid",
    "/wallet/swap/payout",
    "/wallet/swap/switch_pool",
    "/wallet/swap/rem_all_liquid",
    "/farmer/info",
    "/farmer/blocks",
    "/farmer/proofs",
    "/node/offers",
    "/node/offer",
    "/node/trade_history",
    "/contract/storage",
    "/contract/storage/field",
    "/contract/storage/entry",
]

# Define a function to test each endpoint
def test_endpoint(endpoint):
    # Define the full URL
    url = base_url + endpoint

    # Send a GET request
    response = requests.get(url)

    # Print the response
    print(f"GET {url}: {response.status_code}, {response.text[:100]}")

    # Send a POST request
    # Note: You may need to adjust the data payload according to your API's requirements
    data = {}  # replace with your actual data
    response = requests.post(url, data=data)

    # Print the response
    print(f"POST {url}: {response.status_code}, {response.text[:100]}")

# Test all endpoints
for endpoint in endpoints:
    test_endpoint(endpoint)