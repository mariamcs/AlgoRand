# Accesing a remote API with a custom token key.
# (from contribution to: https://github.com/algorand/py-algorand-sdk)
# In this case, the API is expecting the key "X-API-Key" instead of the
# default "X-Algo-API-Token". This is done by using a dict with our custom
# key, instead of a string, as the token.

from algosdk.v2client import algod
import json

algod_address = "https://testnet-algorand.api.purestake.io/ps2"
algod_token = ""
headers = {
    "X-API-Key": "B3SU4KcVKi94Jap2VXkK83xx38bsv95K5UZm2lab",
}

algod_client = algod.AlgodClient(algod_token, algod_address, headers)

try:
    status = algod_client.status()
    print("Status: " + json.dumps(status, indent=2, sort_keys=True))
except Exception as e:
    print("Failed to get algod status: {}".format(e))

# Retrieve latest block information                                                                                                                                               
last_round = status.get("last-round")
print("####################")
try:
    block = algod_client.block_info(last_round)
    print("Latest block: " + json.dumps(block, indent=2, sort_keys=True))
except Exception as e:
    print("Failed to get algod status: {}".format(e))
