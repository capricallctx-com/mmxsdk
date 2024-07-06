# SPDX-License-Identifier: MIT
# Copyright (c) 2023-2024, Caprica LLC

import json
import os
import time
from dotenv import load_dotenv
import chain
import context
import server
import wallet
import well_known

"""
this is a simple airdrop script that sends a specified amount of tokens to a list of addresses
we'll send to the first 1111 farmers in the chain
"""

load_dotenv() # get secrets
session = server.login(password=os.getenv("PASSWORD"))
if session is None:
    print("Login failed")
    exit(1)
# we could do this in memory too - but this is an example
some_miners = []
f = chain.farmers(session.hsid, limit=1111)
for farmer in f:
    info = chain.farmer(session.hsid, farmer["farmer_key"])
    print(info['rewards'])
    for reward in info['rewards']:
        some_miners.append(reward)
with open("addresses.json", "w") as f:
    json.dump(some_miners, f)
with open("addresses.json", "r") as f:
    addresses = json.load(f)
i = 1
for address in addresses:
    to_address = address["address"]
    to_value = address["value"]
    memo = f"this is an airdrop! {to_value} to {to_address}"
    print(f"Sending {to_value} to {to_address}!")
    # replace tn12_goldstar with the token you want
    print(wallet.send(session.hsid, well_known.tn12_goldstar, to_value, to_address, context.default_wallet, memo))
    print(f"Sent {i}/{len(addresses)}")
    i += 1
    time.sleep(1)
