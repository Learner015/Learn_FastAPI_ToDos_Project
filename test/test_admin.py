from test.utils import *
from Routers.Admin import get_current_user,get_db
from fastapi import status
# from models import todos1 as Todos
app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_read_all_authenticated_admin(test_todo):
    resp = client.get("/admin/todo")
    assert resp.status_code==status.HTTP_200_OK
    assert resp.json() == {
    'username':"anjali",
    'user_id': 1,
    'user_role':'admin',   
  }
    
# def test_admin_delete_todo(test_todo):
#     response = client.delete("/admin/todo/1")
#     assert response.status_code == 204, "Not Found"
#     db = TestingSessionLocal()
#     model = db.query(Todos).filter(Todos.id == 1).first()
#     assert model is None


# def test_admin_delete_todo_not_found():
#     response = client.delete("/admin/todo/9999")
#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Not Found'}

