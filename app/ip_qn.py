import datefinder
import json
from df import find_dates_in_sentence
from ordinal_no import extract_ordinals

def keyword_identifier(qn):

    stadium_list=[['wankhede', 'stadium'], ['brabourne', 'stadium'], ['dr.dy', 'patil', 'sports', 'academy'], ['maharashtra', 'cricket', 'assosciation', 'stadium'], ['eden', 'gardens'], ['narendra', 'modi', 'stadium']]
    teams_list_sf= ['csk','dc','gt','kkr','lsg','mi','pbks','rcb','rr','srh']
    teams_list_ff=[['chennai', 'super', 'kings'], ['delhi', 'capitals'], ['gujarat', 'titans'], ['kolkata', 'knight', 'riders'], ['lucknow', 'super', 'giants'], ['mumbai', 'indians'], ['punjab', 'kings'], ['royal', 'challengers', 'bangalore'], ['rajasthan', 'royals'], ['sunrisers', 'hyderabad']]

    word_list = qn.split()
    lowercase_list = [word.lower() for word in word_list]

    ord_num_list=extract_ordinals(qn)

    dates_list = find_dates_in_sentence(qn)
    date_str=''
    f_date_list=[]
    for i in dates_list:
        split_list=i.split("-")
        dd,mm,yyyy=split_list[2],split_list[1],split_list[0]
        h="-"
        date_str=dd + h + mm + h+ yyyy
        f_date_list.append(date_str)


    t_matching_words = [word for word in lowercase_list if word in teams_list_sf]

    for i in range(len(lowercase_list)):
        for j in range(len(teams_list_ff)):
            if lowercase_list[i]==teams_list_ff[j][0]:
                if len(teams_list_ff[j])==3:
                    if lowercase_list[i+1]==teams_list_ff[j][1] and lowercase_list[i+2]==teams_list_ff[j][2]:
                        t_matching_words.append(teams_list_sf[j])
                elif len(teams_list_ff[j])==2:
                    if lowercase_list[i+1]==teams_list_ff[j][1]:
                        t_matching_words.append(teams_list_sf[j])

    sta_matching_words=[]
    for i in range(len(lowercase_list)):
        for j in range(len(stadium_list)):
            if lowercase_list[i]==stadium_list[j][0]:
                if len(stadium_list[j])==4:
                    if lowercase_list[i+1]==stadium_list[j][1] and lowercase_list[i+2]==stadium_list[j][2] and lowercase_list[i+3]==stadium_list[j][3]:
                        sta_matching_words.append(stadium_list[j])
                if len(stadium_list[j])==3:
                    if lowercase_list[i+1]==stadium_list[j][1] and lowercase_list[i+2]==stadium_list[j][2]:
                        sta_matching_words.append(stadium_list[j])
                elif len(stadium_list[j])==2:
                    if lowercase_list[i+1]==stadium_list[j][1]:
                        sta_matching_words.append(stadium_list[j])
    stadium_str=''
    for i in sta_matching_words:
        for j in range(len(i)):
            stadium_str=stadium_str+i[j]
            if j!=(len(i)-1):
                stadium_str=stadium_str+" "
        sta_matching_words.remove(i)
        sta_matching_words.append(stadium_str)

    player_name_list=[]
    json_teams_list=['CSK.json','DC.json','GT.json','KKR.json','LSG.json','MI.json','PBKS.json','RCB.json','RR.json']
    for i in json_teams_list:
        with open(i) as team_file:
            teams_json = json.load(team_file)
        for key,value in (teams_json["Players"]).items():
            single_player_l=(key.lower()).split()
            for word in lowercase_list:
                if word in single_player_l:
                    player_name_list.append(key)

    return f_date_list,t_matching_words,sta_matching_words,player_name_list,ord_num_list,lowercase_list

print(keyword_identifier("Winner of IPL 22"))