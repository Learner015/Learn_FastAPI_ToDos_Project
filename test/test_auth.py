from fastapi import HTTPException,status
from Routers.Auth import get_db,authenticate_user,SECRET_KEY,ALGORITHM,create_access_token,get_current_user
from jose import jwt
from datetime import timedelta
from test.utils import *
import pytest

app.dependency_overrides[get_db] = override_get_db

# def test_authenticate_user(test_user):
#     db = TestingSessionLocal()
#     authenticate = authenticate_user(test_user.username, "testpassword",db)
#     assert authenticate is not None
#     assert authenticate.username == test_user.username

#     non_existent_user = authenticate_user("Invalid username","testpassword",db)
#     assert non_existent_user is False

#     non_existent_password = authenticate_user(test_user.username,"setpassword123",db)
#     assert non_existent_password is False


def test_create_access_token():
    username = "testuser"
    id = 1
    role = "user"
    expires_delta= timedelta(days=1)
    token = create_access_token(username, id,role,expires_delta)
    decoded_token = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM],options={'verify_signature': False})
    assert decoded_token['sub'] == username
    assert decoded_token['id'] == id
    assert decoded_token['role'] == role

@pytest.mark.asyncio
async def test_get_current_user():
    encode = {'sub': 'testuser','id': 1,'role': 'admin'}
    token = jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)
    user = await get_current_user(token=token)
    assert user == {'username': 'testuser','id': 1,'user_role': 'admin'}


@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
    encode = {'role': 'user'}
    token = jwt.encode(encode,SECRET_KEY,algorithm=ALGORITHM)
    with pytest.raises(HTTPException) as exc:
        await get_current_user(token=token)
    assert exc.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert exc.value.detail == "Could not validate user."
