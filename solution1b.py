import requests
import pandas as pd

my_header = {'app-id': '626a7e24178f712ce3f4cdbc'}
response = requests.get("https://dummyapi.io/data/v1/user", headers=my_header)
d = response.json()

id = []
for value in d['data']:
    id.append(value['id'])


users_id = []
users_image = []
users_likes = []
users_tags = []
users_text = []
users_publishDate = []

for user_id in id:
    response = requests.get("https://dummyapi.io/data/v1/user/"+user_id+"/post", headers=my_header)
    dic = response.json()
    for value in dic['data']:
        users_id.append(value['id'])
        users_image.append(value['image'])
        users_likes.append(value['likes'])
        users_tags.append(value['tags'])
        users_text.append(value['text'])
        users_publishDate.append(value['publishDate'])

df = pd.DataFrame({'Users Id': users_id, 'Users Image': users_image, 'Users Likes': users_likes, 'Users Tags': users_tags, 'Users Text': users_text, 'Users publishDate': users_publishDate})
df.to_csv('C:\\Users\\ganes\\OneDrive\\Desktop\\TalinodeINternAssgnmt\\assignment_1b.csv', index=False, encoding='utf-8')
