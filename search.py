from flask import request, Response, jsonify, make_response
from flask_restx import Resource, Api, Namespace
import json
from pandas.io.json import json_normalize
from sql import SQL, SQLRequest
from util import Util

SEARCH = Namespace("products/search")


@SEARCH.route("")
class Search(Resource):
    def get(self):
        connection = SQL()
        error_msg = {}
        data = SQLRequest()
        try:
            name = request.args.get("name")
            cvs = request.args.get("cvs")
            event = request.args.get("event")
            offset = request.args.get("offset")
            limit = request.args.get("limit")
            order = request.args.get("order-by")

            if name is not None:
                data.add("name", name)
                
            if cvs is None:
                error_msg["message"] = "cvs is empty"
            else:
                data.add("cvs", cvs)

            if event is None:
                error_msg["message"] = "event is empty"
            else:
                data.add("event", event)


            if offset is not None:
                if not offset.isdecimal():
                    error_msg["message"] = f"offset must be a integer : {offset}"
                else:
                    data.set_offset(offset)

            if limit is not None:
                if not limit.isdecimal():
                    error_msg["message"] = f"limit must be a integer : {limit}"
                else:
                    data.set_limit(limit)

            if order is not None:
                order = order.lower()
                if order != "asc" and order != "desc" and order !='none':
                    error_msg["message"] = f"order must be asc or desc or None: {order}"
                else:
                    data.set_order_by(order)

            if len(error_msg) == 0:
                res = connection.processDB(data)
                code = 200
                if len(res)==0:
                    code = 400
                return make_response(jsonify(Util.make_response_json(res)),code)
            else:
                return make_response(jsonify(error_msg), 400)

        except Exception as e:
            print(f"error {e}")
            raise e
