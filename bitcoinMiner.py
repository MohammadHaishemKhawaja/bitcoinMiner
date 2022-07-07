# IMPORTING MODULES
import hashlib
import random
import string
numberLimit = 100000000000
zeros = 4

# RANDOMLY GENERATED FOR TRANSACTION, AND HASH
def random_char(words):
    return ''.join(random.choice(string.ascii_letters) for x in range(words))


def mine(blockNumber, transaction, hash):
    for number in range(numberLimit):
        base_text = str(blockNumber) + transaction + hash + str(number)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeros):
            print (f"Found number: {number}")
            return hash_try

    return -1

blockNumber = 24
transaction = (random_char(12))
hash = (random_char(16))

mine(blockNumber, transaction, hash)
