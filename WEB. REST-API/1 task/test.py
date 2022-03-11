from requests import get, post, delete

print(get('http://localhost:5000/api/jobs').json())
print(get('http://localhost:5000/api/jobs/1').json())
print(get('http://localhost:5000/api/jobs/876557').json())
print(get('http://localhost:5000/api/jobs/try').json())

print(post('http://localhost:5000/api/jobs',
           json={'id': 67,
                 'team_leader': 45,
                 'job': 'Engineer',
                 'work_size': 8,
                 'collaborators': 'Collaborators',
                 'is_finished': False}).json())  # aright

print(post('http://localhost:5000/api/jobs').json())  # empty
print(post('http://localhost:5000/api/jobs', json={'id': 98}).json())  # not all
print(post('http://localhost:5000/api/jobs',
           json={'id': 1,
                 'team_leader': 45,
                 'job': 'Engineer',
                 'work_size': 8,
                 'collaborators': 'Collaborators',
                 'is_finished': False}).json())  # exists

print(get('http://localhost:5000/api/jobs').json())  # get all

print(delete('http://localhost:5000/api/news/1').json())  # aright
print(delete('http://localhost:5000/api/news/999').json())  # wrong id
print(delete('http://localhost:5000/api/news/0').json())  # wrong id
print(delete('http://localhost:5000/api/news/try').json())  # wrong id
print(get('http://localhost:5000/api/jobs').json())  # get all
