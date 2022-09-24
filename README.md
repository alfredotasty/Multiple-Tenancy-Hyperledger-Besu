# Multiple-tenency
This network use Hyperledger besu and Tessera

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
## Following the hyperledger besu private network document 
https://besu.hyperledger.org/en/stable/private-networks/
