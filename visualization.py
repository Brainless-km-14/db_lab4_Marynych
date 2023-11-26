import psycopg2
import matplotlib.pyplot as plt

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
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3, figsize=(12, 12))
    plt.subplots_adjust(wspace=1)
    cur = conn.cursor()

    cur.execute(query_1)

    champion = []
    year = []
    prize = []
    for row in cur:
        champion.append(row[0])
        year.append(row[1])
        prize.append(row[2])

    x_range = range(len(champion))

    bar = bar_ax.bar(x_range, prize)
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(champion, rotation=45, ha='right')

    for i, value in enumerate(year):
        bar_ax.text(i, 0, str(value),rotation=90, ha='center',va ='bottom')
    bar_ax.set_xlabel('Чемпіон')
    bar_ax.set_ylabel('Призові')
    bar_ax.set_title('Кількость призових  за рік для кожного представника')

    cur.execute(query_2)

    champion = []
    wins = []
    for row in cur:
        champion.append(row[0])
        wins.append(row[1])

    pie_ax.pie(wins, labels=champion, autopct='%1.2f%%')
    pie_ax.set_title('Кількість перемог  кожного з чемпіонів')

    cur.execute(query_3)

    champion = []
    total_awards = []

    for row in cur:
        champion.append(row[0])
        total_awards.append(row[1])

    graph_ax.plot(champion, total_awards , marker='o', linestyle='-', color='b')
    for champ, total_award in zip(champion, total_awards):
        graph_ax.text(champ, total_award, f'{total_award}', ha='right', va='bottom')
    graph_ax.set_xticks(range(len(champion)))
    graph_ax.set_xticklabels(champion, rotation=45, ha='right')
    graph_ax.set_xlabel('Переможець')
    graph_ax.set_ylabel('Призові')
    graph_ax.set_title('Вивести загальну суму призових які отримав \nкожний переможець')

mng = plt.get_current_fig_manager()
mng.resize(1400, 600)

plt.show()