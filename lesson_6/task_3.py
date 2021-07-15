import json

user_hobbies = {}

with open("users.csv", 'r', encoding="utf-8") as users, open("hobby.csv", 'r', encoding="utf-8") as hobbies:
    count_of_users = sum(1 for line in users)
    count_of_hobbies = sum(1 for line in hobbies)

    users.seek(0)
    hobbies.seek(0)

    if count_of_hobbies > count_of_users:
        exit(1)

    for user in users:
        hobby = hobbies.readline().strip()

        if hobby == '':
            hobby = None
        if user not in user_hobbies:
            user_hobbies[user.strip().replace(',', ' ')] = hobby


with open('dictionary.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(user_hobbies, ensure_ascii=False))

