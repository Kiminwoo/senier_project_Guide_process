# Try working with data in Python with R

<ins>Development journal</ins>

<ins>I have detailed information on the following link.</ins>

--> https://dlsdn73.tistory.com/ 

//Author Kim In-woo 

</br>
<h1>2018.12.27</h1>

- ( + Callaborative_Filtering_Practice1.py ) 
</br>
<h1>2018.12.30</h1>
   
- ( + Collabarative Filtering2.py ) 
</br>
<h1>2019.01.01</h1>

- ( + Collaborative_Filtering3.py ) 
</br>
<h1>2019.01.12</h1>
<blockquote>
- I have studied how to use Decision-tree based on iris and stagec data.( + Decision tree.R) 
</blockquote>
<h1>2019.01.20</h1> 
<blockquote>
- I studied with reference to the following address --> (https://github.com/Kiminwoo/steam-data ) 
</blockquote>
( + Steam_Game_Analysis.ipynb)
</br>
<h1>2019.01.20</h1>
<blockquote>
- In Steam games, I compared the recommendations of Free Game and Pair games. 

The result was plotted, and as a result, it was found that Free Game was more satisfied. This result is a relative value.

I refer to the following address.

--> https://github.com/Kiminwoo/steam-data/blob/master/analysis/analysis-elh.ipynb
</blockquote>
( + Steam_game_FreeVsPair_rating_Pergame.ipynb ) 

</br>
<h1>2019.01.24</h1> 
<blockquote>
- I have compared Genre, Metacritic, and RecommendationCount in Steam games. I refer to the following site. 
</blockquote>
--> https://github.com/Kiminwoo/steam-data/blob/master/analysis/analysis-elh.ipynb 

( + Steam_game_Analysis_GenreVsRecommendationCountVsMetacritic.ipynb ) 
<blockquote>
Through study, I learned the following things.
</blockquote>
<blockquote>
1. It can be seen that Metacritic scores are higher than Pair_Game and Free_Game.
</blockquote>
<blockquote>
2. Comparing Metacritic scores with Recommendation Counts,

   Depending on Metacritic's score, you can see that there is a certain number of referrals.

   However, as Metacritic scores increased, we could see that the distribution of Recommendation Counts was higher.
</blockquote>
<blockquote>
3. When we look at the results according to genre, relatively early access genre was rated highest,

   Action, Strategy, and Racing genres were relatively similar, with the lowest rating.
</blockquote>
<blockquote>
4. I compared the initial price with the recommended number.

   According to the price, the recommendation number naturally exists, but it can be seen that the recommendation number is distributed    at a relatively low price.
</blockquote>
<blockquote>
5. There is a certain value of Metacritic depending on the price.

   Unlike the Recommendation Count, it can be seen that scores of the Metacritic score between 50 and 90 are clustered according to the    relatively low initial price.
</blockquote>
<blockquote>
6. "Increasing the value of Metacritic does not increase the number of users' recommendations"
</blockquote>
<blockquote>
7. When the initial price is low, we can see that the recommendation distribution is relatively unified.

   Again, the lower the price, the greater the likelihood that a recommendation will be present.
</blockquote>
<blockquote>
8. When the initial price was low, Metacritic scores were high in many places.

   Those with high Metacritic scores could be found at generally lower prices.
</blockquote>
</br>
<h1>2019.02.10</h1>
<blockquote>
- Based on the Steamspy API, I created an automated tool using tags.

--> https://steamspy.com/api.php
</blockquote>
( + Tag retrieval automation tool.py ) 

( + Modified : add + Save CSV file in Python ) 


<h2>- Through the tags, you can get:</h2>
<blockquote>
1.game_appid

2.game_name

3.game_score_rank

4.game_userscore

5.game_owners

6.game_all_tags

7.game_languages
</blockquote>
</br>
<h1>2019.03.16</h1>

- Modify code ( + Tag retrieval automation tool.py ) 
<blockquote>
When you import data from Steam_API and save it to Excel, only one column is output to Excel, the value is changed in one column, and 

only one column is output

I have solved this part.
</blockquote>
<h1>2019.03.19</h1>

- Modify code ( + Tag retrieval automation tool.py ) 
<blockquote>
Add multiple parts of tag information at once to save it in Excel
</blockquote>
<h1>2019.03.19</h1>

- Mysql Python connection ( + Put_data_MysqlDB.py ) 
<blockquote>
I have read an Excel file created using Automatic_API and added it to MysqlDB automatically.
</blockquote>
