# Contracts

Some of these are directly from Max's repo


- liquidity.js - This is the main contract that handles a liquidity pool as a sample.  Use the genesis block one unless you have a really good reason to deviate from it.
- nft.js - This is a non-fungible token contract - the on chain one doesn't contain the needed metadata to do the usual with with an NFT since it's intended for pooling.  This includes code to create a limited addition and to add an IPFS image.

## Installation

From Max's repo:

If the code is not deployed on-chain yet, it needs to be compiled and deployed first:
```
mmx_compile -t -n testnet12 -f example.js -o example.dat
mmx wallet deploy example.dat
```
`mmx_compile` returns the binary address that we need to sepecify when deploying a contract later.
`-n testnet12` can be omitted for mainnet.

Once the binary is confirmed on-chain, we can deploy any number of contracts with the same code. \
This can be done via JSON files:
```
{
	"__type": "mmx.contract.Executable",
	"name": "Example",
	"symbol": "EXMPL",
	"decimals": 6,
	"binary": "mmx1...",
	"init_method": "init",
	"init_args": [...]
}
```
If the contract does not represent a token, `name`, `symbol` and `decimals` can be omitted.
If `init_method` is "init", it can be omitted as well since it's the default.

Now deploying a contract from JSON file:
```
mmx wallet deploy example.json
```
Every contract will have a different address since the wallet generates a random 64-bit transaction nonce by default.

The node keeps track which `sender` deployed a contract, as such you can view all your deployed contracts via: