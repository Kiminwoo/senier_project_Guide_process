import urllib.parse
import requests
import pandas as pd

# Steamspy API Get
main_api = "http://steamspy.com/api.php?request=tag&tag"

Searching_tags = "http://steamspy.com/api.php?request=appdetails&appid="




# User input
# print("찾고자 하는 game 태그를 입력해 주세요.(영문)")

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

for count in range(0,len(Userinput)):
    # main_api 에다가 사용자가 입력한 값을 encode해서 덧 붙여준다
    url = main_api + urllib.parse.urlencode({'=':Userinput[count]})


    # url 요청을 json 형태로 받아온다 .
    json_data = requests.get(url).json()


    # 받아온 json 데이터가 이중 딕셔너리 형태이고 , 가져온 키값들이 규칙적인게 아니라
    # 특정 appid 를 가지고 있다 . 그렇기 때문에 , key값만 빼서 따로 keys라는 변수에 저장시켜준다.
    keys = [key for key in json_data]

    # 특정 태그에 해당하는 특정 appid를 기반으로 다시 api 사용해서 appid에 해당하는 language + tags를 가져온다.
    # decode 사용 필요 x , 숫자를 변수로 받기 때문에 , parse 필요없이 그냥 사용

    data_1 = []

    for Count in range(0,len(json_data)-4900):

        url2 = Searching_tags + str(keys[Count])
        json_data2 = requests.get(url2).json()
        # 태그에 해당하는 key 값을 따로 가져온다 .
        keys2 = [key for key in json_data2['tags']]

        print("==============="+Userinput[count]+"================")

        print("game_appid : " + keys[Count])
        print("================================")
        print("game_name : " + json_data[keys[Count]]['name'])
        # print("================================")
        # print("game_score_rank : " + str(json_data[keys[Count]]['score_rank']))
        # print("================================")
        # print("game_userscore : " + str(json_data[keys[Count]]['userscore']))
        print("================================")
        print("game_owners : " + str(json_data[keys[Count]]['owners']))
        print("================================")
        print("game_All_tags : "  + str(json_data2['tags']))
        print("================================")
        print("game_languages : " + str(json_data2['languages']))

        print(keys2)
        # data 집합
        #data =[['game_name','game_score_rank','game_userscore','game_owners','game_All_tags','game_languages'],
        #[json_data[keys[Count]]['name'],json_data[keys[Count]]['score_rank'],json_data[keys[Count]]['userscore'],
        # json_data[keys[Count]]['owners'],json_data2['tags'],json_data2['languages']]]

        data_1.insert(Count ,
                      [json_data[keys[Count]]['name'],
                       json_data[keys[Count]]['owners'],
                       # json_data2['tags'],
                       keys2,
                       json_data2['languages']])

    #     여기서 tags 는 딕셔너리 형태로 값이 넘어오게 된다 . 이 때 이 값들을 정제해줄 필요가 있다 .

    # Dataframe 생성 및 csv 파일 생성
    df = pd.DataFrame(data_1,columns=['game_name','game_owners','game_All_tags','game_languages'])
    df.to_excel("C:/Users/user/Desktop/졸작/2019-03-16-Steam_API_코드수정/"+Userinput[count]+".xlsx",sheet_name = 'Data')

    del data_1

