# Multiple-tenency
This network use Hyperledger besu and Tessera


## Blueprint
![privateUserTransaction drawio](https://user-images.githubusercontent.com/73258014/195950258-c310653c-91ed-4182-8d8d-a1ed500b45f8.png)


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
## Following the hyperledger besu private network document 
https://besu.hyperledger.org/en/stable/private-networks/
