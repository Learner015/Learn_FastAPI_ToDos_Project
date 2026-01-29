# from fastapi import status
# from Routers.Users import get_current_user,get_db
# from test.utils import *


# app.dependency_overrides[get_db] = override_get_db
# app.dependency_overrides[get_current_user] = override_get_current_user

# def test_return_user(test_user):
#     response = client.get("/users")
#     # assert response.status_code == status.HTTP_200_OK
#     # assert response.json()['username'] == 'anjali'
#     # assert response.json()['email'] == 'a@gmail.com'
#     # assert response.json()['f_name'] == 'anjali'
#     # assert response.json()['l_name'] == 'shah'
#     # assert response.json()['role'] == 'admin'

# # def test_change_password_success(test_user):
# #     response = client.put("/users/password", json={"password": "testpassword",
# #                                                   "new_password": "123456"})
# #     assert response.status_code == status.HTTP_204_NO_CONTENT


# # def test_change_password_invalid_current_password(test_user):
# #     response = client.put("/users/password", json={"password": "wrong_password",
# #                                                   "new_password": "newpassword"})
# #     assert response.status_code == status.HTTP_401_UNAUTHORIZED
# #     assert response.json() == {'detail': 'Error on password change'}
