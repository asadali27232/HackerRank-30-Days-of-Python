n = int(input())

phonebook = dict()
for _ in range(n):
    name, number = tuple(input().strip().split())
    phonebook[name] = number

queries = []
while True:
    try:
        query = input().strip()
        if not query:
            break
        queries.append(query)
    except EOFError:
        break

for query in queries:
    if query in phonebook:
        print("{}={}".format(query, phonebook[query]))
    else:
        print("Not found")
