import sender_stand_request
def test_check_get_order_code_200():
    response = sender_stand_request.get_order_by_track()
    code_for_assert = response.status_code
    assert code_for_assert == 200
