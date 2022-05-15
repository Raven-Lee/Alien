import shelve

with shelve.open('score.txt') as d:
    d['score'] = 100

    print(d['score'])