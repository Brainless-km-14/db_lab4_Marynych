--кількість перемог  кожного з чемпіонів
-- SELECT Name , COUNT(ID) AS Wins
-- FROM Champion natural join year
-- GROUP BY Name
-- Order by Wins DESC

-- вивести місце проведення та кожного переможця і країни яку вони представляють 
-- SELECT City || ' / ' || Country AS Venue, Name AS ChampionName, represented_country AS RepresentedCountry
-- FROM Year natural join venue natural join champion

--Вивести загальну суму призових які отримав кожний переможець
SELECT Name AS Champion, SUM(Award$) AS TotalPrizeMoney
FROM Champion natural join year
GROUP BY Name
ORDER BY TotalPrizeMoney DESC;