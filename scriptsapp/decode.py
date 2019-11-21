import requests
from ls8 import Ls8
import getopt, sys

all_command_args = sys.argv
arg_list = all_command_args[1:]
unixOptions = "k:d:h"
gnuOptions = ["key=", "destination=","help"]

destination = None

try:
    args, values = getopt.getopt(arg_list, unixOptions, gnuOptions)
except getopt.error as err:
    print(str(err))
    sys.exit(err)

for curr_arg, curr_val in args:
    if curr_arg in ("-k", "--key"):
        key = curr_val
    if curr_arg in ("-d", "--destination"):
        destination = int(curr_val)

base_url = "https://lambda-treasure-hunt.herokuapp.com/api/adv/"
auth_header = {"Authorization": f"Token {key}"}
response = requests.post(
    f"{base_url}examine/", json={"name": "WELL"}, headers=auth_header
)
result = response.json()

prayer = result["description"]
# print(prayer)

code = prayer.split("\n")[2:]
ls8 = Ls8(code)

ls8.run()
print(ls8.answer)
