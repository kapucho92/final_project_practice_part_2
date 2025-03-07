#Олег Осадчук, 27-я когорта - Финальный проект. Инженер по тестированию плюс.
import requests
import configuration
import data
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=body,
                         headers=data.headers)
response = post_new_order(data.order_body)
order_track = response.json().get('track')
#print (response.status_code)
#print (response.json())

def get_order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_FROM_TRACKER + str(order_track),
                        headers=data.headers)
response = get_order_by_track()
code_for_assert = response.status_code
#print (response.status_code)

def test_check_get_order_code_200():
    assert code_for_assert == 200
    

