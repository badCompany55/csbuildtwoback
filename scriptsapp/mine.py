import hashlib
import requests
import json
# import os
import getopt, sys
# from dotenv import load_dotenv

all_command_args = sys.argv
arg_list = all_command_args[1:]
unixOptions = "k:d:h"
gnuOptions = ["key=", "destination=","help"]

destination = None

try:
    args, values = getopt.getopt(arg_list, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    sys.exit(x)

for curr_arg, curr_val in args:
    if curr_arg in ("-k", "--key"):
        key = curr_val
    if curr_arg in ("-d", "--destination"):
        destination = int(curr_val)


def proof_of_work(last_proof, difficulty):
    proof = 0
    while valid_proof(last_proof, proof, difficulty) is False:
        proof += 1
    return proof


def valid_proof(last_proof, proof, difficulty):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    return guess_hash[:difficulty] == '0'*difficulty


if __name__ == '__main__':
    if len(sys.argv) > 1:
        token = key
    else:
        token = input("Enter your Auth Token: ")
    node = "https://lambda-treasure-hunt.herokuapp.com/api/bc"

    coins_mined = 0

    while True:
        res = requests.get(node + '/last_proof',
                           headers={'Authorization': f'Token {token}'}).json()
        last_proof = res['proof']
        difficulty = res['difficulty']

        print('last_proof: ', last_proof)

        print('difficulty: ', difficulty)

        new_proof = proof_of_work(last_proof, difficulty)
        print('proof: ', new_proof)

        mined = requests.post(node + '/mine',
                              headers={'Authorization': f'Token {token}'},
                              json={"proof": new_proof})

        print('mined: ', mined.json())

        balance = requests.get(node + '/get_balance',
                               headers={'Authorization': f'Token {token}'}).json()

        print('balance: ', balance)

