import json


class Util:
    @staticmethod
    def make_response_json(products):
        """
        db 조회결과를 응답에 맞는 형식으로 변환하기 위한 기능
        Args:
            products: products에 들어갈 데이터, db 조회 결과물
        """
        try:
            assert products is not None, "검색 결과가 None"

        except Exception as e:
            raise e

        dict = {}
        dict["count"] = len(products)
        if dict["count"] == 0:
            dict["message"] = "Can't find any products."
        else:
            dict["products"] = products

        return dict
    
    def remove_none_img(data):
        """
        db 조회 결과에서 img가 없어서 'None'인 경우 아예 제거하여 반환
        Args:
            data(list(dict)) : db 조회 결과가 dict 타입으로 들어있는 list 
        """
        for item in data:
            if item['img'] == 'None':
                del(item['img'])
        return data
