import json

class Util:
    def __init__(self) -> None:
        pass

    def make_response_json(self,products):
        '''
        db 조회결과를 응답에 맞는 형식으로 변환하기 위한 기능
        Args:
            products: products에 들어갈 데이터, db 조회 결과물
        '''
        try:
            assert products is not None, '검색 결과가 None'
            
        except Exception as e:
            raise e

        dict = {}
        dict['count'] = len(products)
        if dict['count'] ==0:
            dict['message'] ="Can't find any products."
        else:
            dict['products'] = products

        return dict