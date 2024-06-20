
import context
import server
import wallet
from node import node_info

session = server.login(password='85341BD4A38868A9D8E1E93BFDDED7111C62F9FC63517A4B54D082B066CF3057')
if session is None:
    print("Login failed")
    exit(1)
#print(session.hsid)
#print(node_info(session.hsid))
print(wallet.get_balances(session.hsid))
#print(wallet.get_token_list(session.hsid))
print(wallet.send(session.hsid, context.mmx_contract, 0.01, "mmx1885sdnjf2tvsj44lh66696y3quqxv5x2p32utzkxv4arrhu6dgws9gpyc8"))

