import hmac
import hashlib

query_string = "timestamp=1578963600000"
secret = "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"


def hashing(query_string):
    return hmac.new(
        secret.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256
    ).hexdigest()


print("hashing the string: ")
print(query_string)
print("and return:")
print(hashing(query_string))
print("\n")

another_string = "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559"

print("hashing the string: ")
print(another_string)
print("and return:")
print(hashing(another_string))