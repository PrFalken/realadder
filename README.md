La vraie Ligue 1
================

Attempt to reclaim equality in money-driven Soccer championships

Concept
-------

Soccer is a big deal here in France. Some people think Teams are too much ruled by money,
some think there is not enough money to compete with other European countries.

Recently Qatar bought the Paris team (Paris Saint Germain), doubling the budget of the team.
This should end up with Paris winning the championship.

Experiment
----------

I asked myself : What if the way of calculating points in the French Championship (called "Ligue 1")
was weighted by annual budget of each team ?

So I made this little web page : http://ligue1.clopo.net

Original Rankings on the left, and the rankings "weighted" by budget on the right : 

    "real" points = official points / annual budget.

Real-Time Rankings
------------------

"La vraie Ligue 1" uses YQL tables to get the rankings, as seen on https://github.com/ymainier/soccer_tables

To get updated rankings, just run generate-clubs.py periodically.
The script will add new Teams if they were promoted, remove them if they were eliminated.
You Need to manually edit Each team's annual budget each year, using django's admin page.

