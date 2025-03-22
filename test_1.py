import requests
import pytest

base_url = "https://yougile.com/api-v2"
key='LOJ7QbE6Q7ZTIbh0dxNeLkeQd2Ul8Xc1Y9SSNtQ79ZviNfymluKmlbTCyafvDsuD'
Authorization=f'Bearer {key}'
my_headers={'Content-Type': 'application/json',
            'Authorization':Authorization
}

# Тест. Создать проект.
def test_project():
    body ={
	'title':'Срочно надо сдать'
	}
    resp = requests.post(base_url + '/projects', json=body, headers=my_headers)
	#new_project	= resp.json()
    new_project_id = new_project['id']

    assert resp.headers['Content-Type'] == 'application/json; charset=utf-8'
    assert body ['title'] == 'Срочно надо сдать'
    assert resp.status_code == 201

# Тест.
def test_create_projects_len():
#	получить список проектов
    len_projects = requests.get(base_url + '/projects', headers=my_headers)
    #len_projects_data = len_projects.json()
    len_projects_data = len_projects.json().get("content", [])
    assert len_projects.json().status_code == 200
#	создать проект
    body = {
    'title': 'Срочно надо сдать и срочно изменить',
    'users':{'c7c50038-290a-4ca3-816f-d13f9a7380e6': 'admin'}
      }
    resp = requests.post(base_url + '/projects', json=body, headers=my_headers)
    assert resp.status_code == 201
#	повторно получить список проектов
    full_len_projects = requests.get(base_url + '/projects', headers=my_headers)
    #full_len_projects_data = full_len_projects.json()
    full_len_projects_data = full_len_projects.json().get("content", [])
    #assert full_len_projects.status_code == 200
#	сравнить первый и второй списки
    assert len(len_projects_data) < len(full_len_projects_data)


