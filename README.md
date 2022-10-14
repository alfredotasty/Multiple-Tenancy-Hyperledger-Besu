# Hyperledger besu Multiple-tenency
This network use Hyperledger besu and Tessera for using to send private transaction to the node that want privacy in blockchain network
that mean another node in network can't see private transaction 
and setting privacy transaction to multi-tenant network


## How private transaction work?

send private transaction diagram

![besuAndTesseraDiagram drawio](https://user-images.githubusercontent.com/73258014/195951920-17386857-7483-4293-94a0-7761cdacb8eb.png)

breifly recap!

private transaction on hyperledger besu is integration with tessera. tessera will use the same key pair as besu node and decrypt transaction with signature solution and send to tessera endpoint node that we want to do some private transaction by P2P network. when finished P2P process tessera will return transaction to besu node that return transaction call enclave transaction. besu node will be sending transaction to next process call minning for distribute transaction to all nodes when transaction distributed the only node that can be read data in enclave transaction is endpoint node


example Web3Quorum sending transaction

```sh
const Web3 = require("web3");
const Web3Quorum = require("web3js-quorum");
const web3 = new Web3Quorum(new Web3("http://127.0.0.1")) // besu endpoint network 

const contractOption = {
    data: '0x123',// conrtract byte code 
    privateFrom: "tesseraNode1Publickey", //tesseraNode1Publickey
    privateFor: ["tesseraNode2PublicKey"], //tesseraNode2PublicKey
    privateKey: "besuNode1PrivateKey" //besuNode1PrivateKey
};
web3.priv.generateAndSendRawTransaction(contractOption);

```


## Multiple-tenency Blueprint
<img width="600" alt="multiplewallet" src=https://user-images.githubusercontent.com/73258014/195950258-c310653c-91ed-4182-8d8d-a1ed500b45f8.png>



## Installation

install besu and tessera

```sh
$ brew install besu
$ brew install libsodium
```
Download tessera distribute from https://github.com/ConsenSys/tessera/releases/tag/tessera-22.1.7

```sh
$ tar xvf tessera-[version].tar
$ export PATH=$PATH:tessera-[version]/bin
$ tessera help
```
or move tessera directory to network directory and use 
```sh
$ ../../tessera-22.1.7/bin/tessera help

```
start besu node 
```sh
$ besu --data-path=data --genesis-file=../genesis.json [--option]

```
start tessera node 
```sh
$ tessera -configfile tessera.conf
or 
$ ../../tessera-22.1.7/bin/tessera -configfile tessera.conf

```
## Authentication

payload
```sh
{ "permissions":["*:*"],
  "privacyPublicKey":tesseraNode_publicKey,
  "exp": 1600899999002
 }
```
generate JWT token
```sh
python3 generateJWT.py
```
example out put

<img width="400" alt="jwtExample" src="https://user-images.githubusercontent.com/73258014/195951260-ca169da1-b7a2-445b-9e58-90bc234df9ae.png">


## Following the hyperledger besu private network document 
https://besu.hyperledger.org/en/stable/private-networks/
