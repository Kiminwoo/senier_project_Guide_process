# Try working with data in Python with R

Development journal 

I have detailed information on the following link.

--> https://dlsdn73.tistory.com/ 

//Author Kim In-woo 


2018.12.27 

- ( + Callaborative_Filtering_Practice1.py ) 

2018.12.30 

- ( + Collabarative Filtering2.py ) 

2019.01.01 

- ( + Collaborative_Filtering3.py ) 

2019.01.12 

- I have studied how to use Decision-tree based on iris and stagec data.( + Decision tree.R) 

2019.01.20 

- I studied with reference to the following address --> (https://github.com/Kiminwoo/steam-data ) 

( + Steam_Game_Analysis.ipynb)

2019.01.20 

- In Steam games, I compared the recommendations of Free Game and Pair games. 

The result was plotted, and as a result, it was found that Free Game was more satisfied. This result is a relative value.

I refer to the following address.

--> https://github.com/Kiminwoo/steam-data/blob/master/analysis/analysis-elh.ipynb

( + Steam_game_FreeVsPair_rating_Pergame.ipynb ) 


2019.01.24 

- I have compared Genre, Metacritic, and RecommendationCount in Steam games. I refer to the following site. 

--> https://github.com/Kiminwoo/steam-data/blob/master/analysis/analysis-elh.ipynb 

( + Steam_game_Analysis_GenreVsRecommendationCountVsMetacritic.ipynb ) 

Through study, I learned the following things.

1. It can be seen that Metacritic scores are higher than Pair_Game and Free_Game.

2. Comparing Metacritic scores with Recommendation Counts,

   Depending on Metacritic's score, you can see that there is a certain number of referrals.

   However, as Metacritic scores increased, we could see that the distribution of Recommendation Counts was higher.

3. When we look at the results according to genre, relatively early access genre was rated highest,

   Action, Strategy, and Racing genres were relatively similar, with the lowest rating.

4. I compared the initial price with the recommended number.

   According to the price, the recommendation number naturally exists, but it can be seen that the recommendation number is distributed    at a relatively low price.

5. There is a certain value of Metacritic depending on the price.

   Unlike the Recommendation Count, it can be seen that scores of the Metacritic score between 50 and 90 are clustered according to the    relatively low initial price.


6. "Increasing the value of Metacritic does not increase the number of users' recommendations"


7. When the initial price is low, we can see that the recommendation distribution is relatively unified.

   Again, the lower the price, the greater the likelihood that a recommendation will be present.

8. When the initial price was low, Metacritic scores were high in many places.

   Those with high Metacritic scores could be found at generally lower prices.


2019-02-10

- Based on the Steamspy API, I created an automated tool using tags.

--> https://steamspy.com/api.php

( + Tag retrieval automation tool.py ) 

( + Modified : add + Save CSV file in Python ) 

- Through the tags, you can get:

1.game_appid

2.game_name

3.game_score_rank

4.game_userscore

5.game_owners

6.game_all_tags

7.game_languages


2019-03-16

- Modify code ( + Tag retrieval automation tool.py ) 

When you import data from Steam_API and save it to Excel, only one column is output to Excel, the value is changed in one column, and 

only one column is output

I have solved this part.

2019-03-19

- Modify code ( + Tag retrieval automation tool.py ) 

Add multiple parts of tag information at once to save it in Excel

2019-03-19

- Mysql Python connection ( + Put_data_MysqlDB.py ) 

I have read an Excel file created using Automatic_API and added it to MysqlDB automatically.
