import json
import os
import random
import time
from time import sleep

from dotenv import load_dotenv

import chain
import config
import context
import contract
import node
import schema
import server
import swap
import wallet
import well_known
from node import node_info

TEST_SERVER = "mmx104u6jct6mfy4h307qgawsgkdcmgsdsqg889u25mk3f5d802krp0sz3guuw"

SWAP_DEPLOY = """
{
	"__type": "mmx.contract.Executable",
	"name": "Fish vs Star",
	"symbol": "FISH",
	"decimals": 6,
	"binary": "mmx1gpu8spcn0kwv63ymds8xawfslcwrgh4jsvzr3p64rcq5cf5uf0lszexlms",
	"init_method": "init",
	"init_args": ["mmx1ed5390pu9xkmh5x9nzsejacr9c0kmch3e59w92auxycjtdrx5teql0apz4", "mmx1nt847tctug5gknle96flxy7e3qz2herjh6gwd4tll9rmnct32ayq5md9vn"]
}
"""


load_dotenv()
session = server.login(password=os.getenv("PASSWORD"))
if session is None:
    print("Login failed")
    exit(1)
#print(chain.contract(session.hsid, "mmx1cxx5r6u2z0k4kc640wzkdpdvxekfvnl4x53tfug84fpu2pe5z0eqenckdx"))
#print(wallet.seed(hsid=session.hsid))
"""
addreses = []
f = chain.farmers(session.hsid, limit=1111)
for farmer in f:
    info = chain.farmer(session.hsid, farmer["farmer_key"])
    print(info['rewards'])
    for reward in info['rewards']:
        addreses.append(reward)
with open("addresses.json", "w") as f:
    json.dump(addreses, f)
"""
"""
with open("addresses.json", "r") as f:
    addresses = json.load(f)
i = 1
for address in addresses:
    to_address = address["address"]
    to_value = address["value"]
    memo = f"good job!  you earned {to_value} MMX so far - gold star!"
    print(f"Sending {to_value} to {to_address} - gold star!")
    print(wallet.send(session.hsid, well_known.tn12_goldstar, to_value, to_address, context.default_wallet, memo))
    print(f"Sent {i}/{len(addresses)}")
    i += 1
    time.sleep(1)
"""
#print(chain.farmer(session.hsid, "02F1378090DD09256B47C526677FEC5839BA27D158F27A470EBA494A40AB770F75"))
#print(wallet.offer(session.hsid, well_known.tn12_goldstar, 1, well_known.tn12_tux, 1000))
#print(wallet.offer(session.hsid, well_known.tn12_tux, 1, well_known.tn12_goldstar, 1000))
#print(chain.block(session.hsid, height=22))
#print(swap.list(session.hsid))
print(wallet.deploy(session.hsid, SWAP_DEPLOY))
#print(session.hsid)
#print(node_info(session.hsid))
#print(wallet.get_balances(session.hsid))
#print(wallet.get_token_list(session.hsid))
#print(wallet.send(session.hsid, well_known.tn12_clippy, 123.34, "mmx1ldcka0yun5w0pe9p8a50680mh2lw65f63a3c2fhknfsyszn08wxsqccgck"))
#o = node.node_offers(session.hsid)
#for oo in o:
#    print(oo)
#print(len(o))

"""
for i in range(25):
    print(wallet.offer(session.hsid, context.mmx_contract, .0001, context.moose_contract, .01))
MAX_RANGE = 6000
for loop in range(MAX_RANGE):
    print(f"Loop {loop}/{MAX_RANGE}")
    list_offers = node.node_offers(session.hsid)
    for offer in list_offers:
        offer_info = schema.OfferData(json.dumps(offer))
        if offer_info.owner == TEST_SERVER:
            if random.randint(0, 100) < 5:
                print("Randomly cancelling offer")
                print("Cancelling offer")
                print(wallet.cancel_offer(session.hsid, offer_info.address, None))
            elif random.randint(0, 100) < 5:
                print("Randomly accepting offer")
                print(wallet.accept_offer(session.hsid, offer_info.address, None))
    if random.randint(0, 100) < 10:
        print("Creating new Moose offer")
        print(wallet.offer(session.hsid, context.mmx_contract, .001, context.moose_contract, 50))
    sleep_time = random.randint(0, 19)
    print(f"Sleeping for {sleep_time} seconds")
    sleep(sleep_time)
"""

#print(swap.list(session.hsid))
#print(swap.info(session.hsid, "mmx13wqz8dr8r763m6v2h7m7prlucsnj03q5d3y2uwk690eqm7r2l3sq5p0c7c"))
#print(wallet.cancel_offer(session.hsid, "mmx1v4m5tkflhvmr27l3xr5p8tg8m0hz60pke4vqrc0p9erzvuzf2llqsf5wva", None))

#list_offers = node.node_offers(session.hsid)
#print(list_offers)