import psycopg2


username = 'Marynych_Mukola'
password = 'K30022161K'
database = 'db_lab3'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT Name AS ChampionName, Year, Award$
FROM Champion natural join year
ORDER BY Year;
'''
query_2 = '''
SELECT Name , COUNT(ID) AS Wins
FROM Champion natural join year
GROUP BY Name
Order by Wins DESC

'''
query_3 = '''
SELECT Name AS Champion, SUM(Award$) AS TotalPrizeMoney
FROM Champion natural join year
GROUP BY Name
ORDER BY TotalPrizeMoney DESC;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    cur.execute(query_1)

    print('Кількость призових  за рік для кожного представника')
    for row in cur:
        print(f'Представник: {row[0]},  рік: {row[1]}, призові:{row[2]}$')

    cur.execute(query_2)

    print('\nКількість перемог кожного з чемпіонів')
    for row in cur:
        print(f'Чемпіон: {row[0]}, Кількість перемог: {row[1]}')

    cur.execute(query_3)

    print('\nВивести загальну суму призових, які отримав кожний переможець')
    for row in cur:
        print(f'Переможець: {row[0]}, Призові: {row[1]}$')