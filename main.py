
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request
from google.cloud import bigquery



logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'L', 'R', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', "T", 'T', "T", "T"]

is_set = False
throw = True
move_me = "L"
forward = True

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
@app.route("/", methods=['POST'])
def move():
    request_data = request.get_json()
    MY_X = None
    MY_Y = None
    MY_DIRECTION = None

    # logger.info(request.json)
    # players = request_data["arena"]["state"].keys()

    state = request_data["arena"]["state"]
    for player, info in state.items():
        if player == MY_SERVICE:
            MY_X = info.get('x')
            MY_Y = info.get('y')
            MY_DIRECTION = info.get('direction')

    for player, info in state.items():
        players_y = info.get('y')
        players_x = info.get('x')
        if info.get('wasHit') is True:
            continue
        else:
            if MY_X == players_x:
                if players_y < MY_Y and MY_DIRECTION == 'N' and abs(players_y - MY_Y) <= 3:
                    return "T"
                elif players_y < MY_Y and MY_DIRECTION == 'S':
                    return "L"
                elif players_y > MY_Y and MY_DIRECTION == 'S' and abs(players_y - MY_Y) <= 3:
                    return "T"
            if MY_Y == players_y:
                if players_x < MY_X and MY_DIRECTION == 'W' and abs(players_x - MY_X) <= 3:
                    return "T"
                elif players_x > MY_X and MY_DIRECTION == 'E' and abs(players_x - MY_X) <= 3:
                    return "T"
                elif players_x < MY_X and MY_DIRECTION == 'E':
                    return 'L'

    return moves[random.randrange(len(moves))]

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
