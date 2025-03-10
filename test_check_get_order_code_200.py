#Олег Осадчук, 27-я когорта - Финальный проект. Инженер по тестированию плюс.
import sender_stand_request
import data
def test_check_get_order_code_200():
    response_create = sender_stand_request.post_new_order(data.order_body)
    order_track = response_create.json().get('track')  
    response_get = sender_stand_request.get_order_by_track(order_track)  
    assert response_get.status_code == 200