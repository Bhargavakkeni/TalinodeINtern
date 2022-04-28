import requests
import pandas as pd

my_header = {'app-id': '626a7e24178f712ce3f4cdbc'}
response = requests.get("https://dummyapi.io/data/v1/user", headers=my_header)
d = response.json()

id = []
title = []
firstName = []
lastName = []
picture = []

for value in d['data']:
    id.append(value['id'])
    title.append(value['title'])
    firstName.append(value['firstName'])
    lastName.append(value['lastName'])
    picture.append(value['picture'])

df = pd.DataFrame({'id': id, 'title': title, 'firstName': firstName, 'lastName': lastName, 'picture': picture})
df.to_csv('C:\\Users\\ganes\\OneDrive\\Desktop\\TalinodeINternAssgnmt\\assignment_1.csv', index=False, encoding='utf-8')