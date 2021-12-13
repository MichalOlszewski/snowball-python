
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
moves = ['F', 'L', 'R', 'T']

is_set = False
throw = True
move_me = "L"
forward = True

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    global is_set
    global throw
    global forward
    global move_me
    request.get_data()
    logger.info(request.json)
    if throw:
        throw = False
        return 'T'
    throw = True
    me = request.json["_links"]["self"]["href"]
    x = request.json['arena']["state"][me]['x']
    if x == 0:
        is_set = True
    y = request.json['arena']["state"][me]['y']
    direction = request.json['arena']["state"][me]['direction']
    size = request.json["arena"]["dims"]
    size_y = size[1]
    return moves[random.randint(0,len(moves))]



    return "T"

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
