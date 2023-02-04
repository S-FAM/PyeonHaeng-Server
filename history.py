from flask import request, Response, jsonify, make_response
from flask_restx import Resource, Api, Namespace
import json
from pandas.io.json import json_normalize
from sql import SQL, SQLRequest
from util import Util

HISTORY = Namespace("products/history")


@HISTORY.route("")
class History(Resource):
    def get(self):
        connection = SQL()
        error_msg = {}
        data = SQLRequest()
        try:
            name = request.args.get("name")
            cvs = request.args.get("cvs")

            
            if name is None:
                error_msg["message"] = "name is empty"
            else:
                data.add("history_name", name)

            if cvs is None:
                error_msg["message"] = "cvs is empty"
            else:
                data.add("cvs", cvs)


            if len(error_msg) == 0:
                connection.check_connection()
                res = connection.processDB(data,True)
                code = 200
                if len(res)==0:
                    code = 400
                return make_response(jsonify(Util.make_response_json(res)),code)
            else:
                return make_response(jsonify(error_msg), 400)

        except Exception as e:
            print(f"error {e}")
            raise e
