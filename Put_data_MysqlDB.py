import pymysql.cursors
import pandas as pd

#


conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       charset='utf8mb4',
                       db ='test1'
                       )
# #
# Python을 사용해서 Mysql database 만들기
# try:
#     with conn.cursor() as cursor:
#         sql = 'CREATE DATABASE test1'
#         cursor.execute(sql)
#
#     conn.commit()
#
# finally:
#     conn.close()

# Python을 사용해서 Mysql table 만들기
# try:
#     with conn.cursor() as cursor:
#         sql = '''
#             CREATE TABLE Game_IF(
#                 Count int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
#                 game_name varchar(255) NOT NULL,
#                 game_owners int(255),
#                 game_all_tags varchar(255),
#                 game_languages varchar(255)
#                 ) ENGINE=InnoDB DEFAULT CHARSET=utf8
#         '''
#         cursor.execute(sql)
#     conn.commit()
# finally:
#     conn.close()

# Python 에서 MysqlDB에 Insert 하기

# try:
#     with conn.cursor() as cursor:
#         sql = 'INSERT INTO Game_IF (game_name,game_owners,game_all_tags,game_languages) VALUES (%s,%d,%s,%s)'
#         cursor.execcute(sql,())

Userinput = ['SINGLE',
             'MULTI',
             'COOP',
             'MMO',
             'ISFREE',
             'FREETOPLAY',
             'PURCHASEAVAIL',
             'CASUAL',
             'DARK',
             'CUTE',
             'MUSIC',
             'HUMOR',
             'COMEDY',
             'HORROR',
             'STORYRICH',
             'RELAXING',
             'GORE',
             'SURVIVE',
             'STRATGY',
             'PUZZLE',
             'SCI-FI',
             'FANTASY',
             'ACTION',
             'VIOLENT',
             'SHOOTER',
             'SPORT',
             'RACING',
             'FARM',
             'SIMULATION',
             'BUILDING'
             ]

for Read in range(0,len(Userinput)):
    df = pd.read_excel("C:/Users/user/Desktop/졸작/2019-03-16-Steam_API_코드수정/"+Userinput[Read]+".xlsx",sheet_name='Data')


    Game_name = df['game_name']
    # Game_owners = df['game_owners']
    Game_All_tags = df['game_All_tags']
    # Game_languages = df['game_languages']

    # -----------Excel 에서 불러온 데이터를 각각의 배열 주소값에 각각 넣어준다 .


    # Game_owners_array = []
    # 여기서 tag는 엑셀에 저장되어 있는 배열값이 저장되어 있는데 , 먼저 문자열 형태로 그대로 가져온다.
    # 문자열로 저장을 하고 , split으로 불필요한 문자들을 제거해 주기 위해서
    Game_All_tags_array = ""
    # Game_languages_array = ""


    # 필요없는 문자 제거 함수
    def character_removal_function(input):
        input =input.replace("'","")
        input =input.replace("[", "")
        input =input.replace("]", "")

        input = input.split(',')
        return input


    for col_index in range(0, len(Game_name.index)):

        # Game_name_array = []
        print(Game_name[col_index])
        # Game_name_array.insert(col_index,Game_name[col_index])
        # Game_owners_array.insert(col_index,Game_owners[col_index])
        # Game_All_tags_array.insert(col,Game_All_tags[col])
        # Game_languages_array.insert(col,Game_languages[col])

        # 엑셀에서 가져온 특정 칼럼의 값을 변수에 저장 , 이때 문자열로
        Game_All_tags_array = Game_All_tags[col_index]
        # Game_languages_array = Game_languages[col_index]

        #불필요한 문자 제거
        Remove_Tag_name = character_removal_function(Game_All_tags_array)
        # Remove_language = character_removal_function(Game_languages_array)


        # for count in range(0,len(Remove_Tag_name)):
        #     print(Remove_Tag_name[count])
        # for count in range(0, len(Remove_language)):
        #     print(Remove_language[count])




        # 태그가 존재하는 만큼
        for count in range(0, len(Remove_Tag_name)):

                with conn.cursor() as cursor:

                    sql = 'INSERT INTO Game_IF (game_name,game_all_tags) VALUES (%s,%s)'
                    cursor.execute(sql, (Game_name[col_index],Remove_Tag_name[count]))

                conn.commit()

        Game_All_tags_array = ""
        # Game_languages_array = ""

conn.close()