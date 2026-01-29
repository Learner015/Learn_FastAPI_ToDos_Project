from Routers.Todo import get_db, get_current_user
from fastapi import status
from models import todos1 as Todos
from test.utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_read_all_authenticated(test_todo):
    response = client.get("/todo")
    assert response.status_code == status.HTTP_200_OK
    # assert response.json() == [{'completed': False, 'title': 'Learn to code!',
    #                             'description': 'Need to learn everyday!', 'id': 1,
    #                             'priority': 5, 'owner': 1}]


# def test_read_one_authenticated(test_todo):
#     response = client.get("/todo/1")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json() == [{'completed': False, 'title': 'Learn to code!',
#                                 'description': 'Need to learn everyday!', 'id': 1,
#                                 'priority': 3, 'owner': 1}]


# def test_read_one_authenticated_not_found():
#     response =client.get("/todo/999")
#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Todo not found.'}


# def test_create_todo(test_todo):
#     request_data={
#         'title': 'New Todo!',
#         'description':'New todo description',
#         'priority': 1,
#         'completed': False,
#     }

#     response = client.post('/todo/', json=request_data)
#     assert response.status_code == 201

#     db = TestingSessionLocal()
#     model = db.query(Todos).filter(Todos.id == 1).first()
#     assert model.title == request_data.get('title')
#     assert model.description == request_data.get('description')
#     assert model.priority == request_data.get('priority')
    # assert model.completed == request_data.get('completed')
# 

# def test_update_todo(test_todo):
#     request_data={
#         'title':'Change the title of the todo already saved!',
#         'description': 'Need to learn everyday!',
#         'priority': 1,
#         'completed': False,
#     }

#     response = client.put('/todo/2', json=request_data)
#     assert response.status_code == 204
#     db = TestingSessionLocal()
#     model = db.query(Todos).filter(Todos.id == 1).first()
#     assert model.title == 'Change the title of the todo already saved!'


# def test_update_todo_not_found(test_todo):
#     request_data={
#         'title':'Change the title of the todo already saved!',
#         'description': 'Need to learn everyday!',
#         'priority': 1,
#         'completed': False,
#     }

    # response = client.put('/todos/todo/999', json=request_data)
    # assert response.status_code == 404
    # assert response.json() == {'detail': 'Todo not found.'}


# def test_delete_todo(test_todo):
#     response = client.delete('/todo/2')
#     assert response.status_code == 204
#     db = TestingSessionLocal()
#     model = db.query(Todos).filter(Todos.id == 2).first()
#     assert model is None


# def test_delete_todo_not_found():
#     response = client.delete('/todo/999')
#     assert response.status_code == 404
#     assert response.json() == {'detail': 'Todo not found.'}













