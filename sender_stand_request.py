#Олег Осадчук, 27-я когорта - Финальный проект. Инженер по тестированию плюс.
import requests
import configuration
import data
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=body,
                         headers=data.headers)
def get_order_by_track(order_track):
    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_FROM_TRACKER + str(order_track),
                        headers=data.headers)
    

