# Genertae JWT token it's use for verify user 
# in privacy group wich who can request access JSON-RPC api 
# to data that store in network that speard by privacy group id 
# beacuse in front-end event throug you do some private transaction or permission
# another account in you wallet will see it the same but cannot access
# the solution that fix this problem is JWT token. user using it when sign in or auth
# to fetch api data from besu and another user hold another token and they can't see
# each other if they are in dfiffernce privacy group 

from datetime import datetime
import jwt,time


def init1():
    # Private & Public RSA user1
    private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA2nM7w4qSt5sudD0Zn1nHI/EqhIEI+ipe/BkUU248bpuwcghR
K44MRqCeP1H8Jn9qQW0+GYjLUOzLX3lr9I5PTrbxbcj5rbLJI6rZp738LG2jA44S
Tgns5O32doWodiZBOkXFyGT5Hn+pZAzYy42mBTC8X8HhYQJ9qlg9vArCVPYbBX8y
jZZ4tt1BA4ySu72HiY4eofBhRICPmX4lhYnyi/lzOgS0jPIW0EnALtrPeXMwZEfi
psWalx+FKr5mDoxnrcuVmKPl+oxkYbEV5P2caMWY7TsiALtGj6z45oi2JEZrzk+e
rTRzYMi+yxL0nrktO2Z92EH8s+OEA4BKbvoVQQIDAQABAoIBAQCO2IGBGZFdPL2A
xx+FIyjkaORbpyEerSxVf3TaJaCg12/m8WdaqtV+LbOtRkgzSGhMBkpwWhJRhbZr
ZTPhxFk56Mkw+BXErr92cldHqCVJTBwny/ROUZE2FiFvWXFSaSuIFm4B331Do0k6
Imh1mtewVzEnENn3HLDd/jvIReTTtrEfFQ8jUP05mBeidfySl4dN6pd11CqgrRpX
SZi3e83YAEHtFv+GQqKLVcN/vFkL+pT/hTuHzcxvc9aNrBEOt1+ZuTVfMoqRS7F4
yFnHSUC53cZDSd5JLTxiPV37O57tS5cz75vLtQ1E3caV21fsWBi1WJLwEL7jFAJQ
tnuC+xZNAoGBAPrLccaOGySGsYjKmYnOiSaxM5Ydjwl3jEaV2f5bZsqjDWIJB4EJ
lbu/AWO9idbTsXqPqI4pq/rrXKJh7ESVSZN8Ve0NLpYcN/OoPjWL+LumDqg6KbFh
hjYdcsRe2Yb7ChhvM68Y/RYuLSHDJMBdk7pojKImfhEHx7piwnXPlJ5LAoGBAN77
7nols0ZQXFyNw+cYLaWKC8G5XNSE3z1w4ys22JpfLPD0oD9yaBnfGKmjDDXJIPdI
dKj6wOPUHhRNhXd+ykFUtIY5TCSjZf4EEQHKUJTstM0H0jxH2gvwchrpV/feoLvF
AKNRVJZS8udEesn0n7p8lYeziRAL+uBjm8wkrrMjAoGBAJIDmL5NRihB82L88d91
zAwm5y3jD8AnRhhiboTUmkgoHkaRkzjhZ7fjQN/dHj9hCNeehDggsuxn04sHEBPu
BuRDY5OcNR9YVosZzP5H/AzkZWw0UMnhSc5/3q3Nu0AHMJ2BQMoU9mTPhZ8+iksl
MDk7XYWae5NWwEYX8be9n315AoGAZwgttw74eULkineOz5cicF0K9aZ6uE/0/uTM
cslS6HGVyHigGvD4HQwyzx9hovCeZOR70yCaRCtdArCXPRG+ztUe3O5Yuo0tsWOb
oCIlfcqp+BrnD6d7nwypDLpJRWT/DAQJOW15EkSdrDK+MdbwfzDVvvA8IsgGUex0
rq08c9UCgYBYAEUCslsXXwWtYohqd+Ynx2nCjjDD4SpH/ItmO07jXd7Q3TmtEnB4
l60Y210BEB2CRA2ra0+F4iNNv//U2f4oUAAs4p+OSTK5L5TfuMSsjrmgTZIMGecI
+kroeeSxFSCH2GgQNHzPzzstL7Ti12BGK76H8f4oISmJfMq63fm/Gw==
-----END RSA PRIVATE KEY-----
"""
    public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2nM7w4qSt5sudD0Zn1nH
I/EqhIEI+ipe/BkUU248bpuwcghRK44MRqCeP1H8Jn9qQW0+GYjLUOzLX3lr9I5P
Trbxbcj5rbLJI6rZp738LG2jA44STgns5O32doWodiZBOkXFyGT5Hn+pZAzYy42m
BTC8X8HhYQJ9qlg9vArCVPYbBX8yjZZ4tt1BA4ySu72HiY4eofBhRICPmX4lhYny
i/lzOgS0jPIW0EnALtrPeXMwZEfipsWalx+FKr5mDoxnrcuVmKPl+oxkYbEV5P2c
aMWY7TsiALtGj6z45oi2JEZrzk+erTRzYMi+yxL0nrktO2Z92EH8s+OEA4BKbvoV
QQIDAQAB
-----END PUBLIC KEY-----"""

    # tenant node that user need to authenticate 
    privacy_public_key = "keiNgxxEVbW1fzp0b8aNj1n5JxN+n1PwSoITiPruYhU="
    endcoded = jwt.encode({"permissions":["*:*"],"privacyPublicKey":privacy_public_key,"exp": 1600899999002},private_key, algorithm="RS256")
    return endcoded

def init2():
    # Private & Public RSA user2
    private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAxPxVUUDdg5Ij3xfDFNkDMimcem8OnLsAJL5oFaRcsGWR0pis
r9T4z3Z820s03blGUTURWBTV6kEGnqcg/7/ebWOSy4obopQixPYelT4RyDmKPg48
lOSqQl6WG4LIYKrT6MDFpvjtK9mpnG4T8HL3C00VFHyWTNPYEDUyMix9UJd9nOB9
vrBFKDLGVskh7JQqpZqBo/LMWYS4MfgnFwGT6imfuyvr2yUEyz65aj06S+mql4H/
TZYjuvvcpEksdiyF+Zv2oFBucm6jYqj0r9MJrHBFqbOI/y7lpVq4Yd36x82aEaON
4Rqwxz52NL/+PyadERtgOFhMBSgt2ptO+eheRwIDAQABAoIBAE+XZSGfg+FVewj5
IOmbhZ8PERqnJNBO/o/aH1QfRRRA9dqRtbSV6LJqvagdiw7LfY3yUz+zq3srKvGP
tdWgQM8SHI4BD4lxMVtD1reWjLjKBwFr3y6J9gE7FounHC9y1oyE11fP3ISLPezm
zUeqLAd07b+JV3FTZ0mlNNLxBvE4jeKt2Be0m/btbz96aQPxVwB4IP7EVsv7Z0NN
FEhLA/4Zm0MdwWdyl8toZ7y5cVj7Z2p8QRjpAH92b99470ZEN2W4PeeSktb4+dML
ZKgd7AYE7AId5ujTgKX6jnpRQrh5N8ngq68mFE+J1S4fBmTt/mHjy3fDZFFvk7bZ
9NLhEYECgYEA/GUWq7qnAR/Lg0mxlePy93QqfRMKf8pjZqXehhuaf24akh7oqZyM
8tz98WPkLnz3UMFD76ffzEonaakREUKj40DGKFINsjrZiVKr33+AQ/AFMOJnp4f1
dA3hmv+tkDxzfod4MwKlg2SR31dBfUii8LpUfSEE75DBh8P9shrQXuUCgYEAx8yi
bUN87tiD+SSCqPmuFmeVvwv7vDypt6aCRphpl0ITcs37wGpUorure2hAKSy3Qh0N
OVyat5JUOTo+nXOxfpW5xfRip2W35dFyQgNJJF0f4r93afxOO/rTaAxXu/fS6YwZ
NAubqOw0goZd+gqUqAJMjvyTl6bKNvbGBtwZCbsCgYA0hrk0HhE5e6t39DNAFYNw
Gj3pb7gEplMPfr+Tu1To5jojZMlY2xq+RF2ZCgfn4Nv7c203CAHcWyZep+/EXtEK
r2VN6N2u1O6G1KyuQ7Om7+G0rbmStQnRED5+am1tkhcbIwhR3WAiuyBckaUwdJhs
buq8a83CKacNIS3ADjKFPQKBgQC1TmYKvtZNK58+47nJuqEWZbNGpYovu+DK7ceE
ZmRTRTu+z1rntdXNwn2PRAANHS3DSfepGPaxJJFXSRpu6QClfRsSnn0zqKNjYlfL
vY2O+Q6pRdQIElOwLCHRZnnq8a2sD10DlJERjh7sXyBCeX2CpGtyyZLpaApSLEdx
DCOQZwKBgQCMEp57JSRRR/VybHNhsfdbS+6NClJNbreos/APEnV+LQu2cAZiIywn
uHELbPtv5ULKLQT6+Bizc15rrkQQHJNSr1VaIhj35NyH4poXyKj5OmUQtRR0gSOc
r4KFJZk7BhlT2cqeFi9eqY7kaNVX3P/eKgcmRsRkb6hxUlzaHy689Q==
-----END RSA PRIVATE KEY-----
"""
    public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxPxVUUDdg5Ij3xfDFNkD
Mimcem8OnLsAJL5oFaRcsGWR0pisr9T4z3Z820s03blGUTURWBTV6kEGnqcg/7/e
bWOSy4obopQixPYelT4RyDmKPg48lOSqQl6WG4LIYKrT6MDFpvjtK9mpnG4T8HL3
C00VFHyWTNPYEDUyMix9UJd9nOB9vrBFKDLGVskh7JQqpZqBo/LMWYS4MfgnFwGT
6imfuyvr2yUEyz65aj06S+mql4H/TZYjuvvcpEksdiyF+Zv2oFBucm6jYqj0r9MJ
rHBFqbOI/y7lpVq4Yd36x82aEaON4Rqwxz52NL/+PyadERtgOFhMBSgt2ptO+ehe
RwIDAQAB
-----END PUBLIC KEY-----"""

    # tenant node that user need to authenticate 
    privacy_public_key = "keiNgxxEVbW1fzp0b8aNj1n5JxN+n1PwSoITiPruYhU="
    endcoded = jwt.encode({"permissions":["*:*"],"privacyPublicKey":privacy_public_key,"exp": 1600899999002},private_key, algorithm="RS256")
    return endcoded

def main():
    timestamp = 1666385737
    times = time.localtime(timestamp)
    timesString = time.strftime("%m/%d/%Y, %H:%M:%S", times)
    strToken1 = init1()
    strToken2 = init2()
    print("Generate JWT Token Success!")
    print("|-------------------------------------------------------------------------------|\n")
    print("[Token1] is :",strToken1,"\n\n\t\t --------Token will expire on",timesString,"--------")
    print("|-------------------------------------------------------------------------------|\n")
    print("[Token2] is :",strToken2,"\n\n\t\t --------Token will expire on",timesString,"--------")

main()