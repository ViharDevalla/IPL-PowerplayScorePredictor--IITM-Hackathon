### Custom definitions and classes if any ###
import pandas as pd
import numpy as np
import math
from sklearn.ensemble import RandomForestRegressor
import pickle

def predictRuns(testInput):
    venuedata = pd.read_csv('venuedata.csv')
    teamdata = pd.read_csv('teamdata.csv')
    batsmandata = pd.read_csv('batsmandata.csv')
    bowlerdata = pd.read_csv('bowlerdata.csv')

    prediction = 0
    batting_index=0
    batting_strike=0
    bowling_index=0

    inputdf = pd.read_csv(testInput)
    inputdf.is_copy = False
    inputdf['ppwickets'] = 0
    batsmen_list = inputdf['batsmen'].loc[0].split(',')
    bowler_list = inputdf['bowlers'].loc[0].split(',')

    if(inputdf['innings'].loc[0] == 1):
        inputdf['venue'].loc[0] = venuedata[venuedata['venue'] == inputdf['venue'].loc[0]]['index1'].unique()[0]
    else:
        inputdf['venue'].loc[0] = venuedata[venuedata['venue'] == inputdf['venue'].loc[0]]['index2'].unique()[0]
    
    
    if(inputdf['innings'].loc[0] == 1):
        inputdf['batting_team'].loc[0] = teamdata[teamdata['team'] == inputdf['batting_team'].loc[0]]['batindex_1'].unique()[0]
        inputdf['bowling_team'].loc[0] = teamdata[teamdata['team'] == inputdf['bowling_team'].loc[0]]['bowlindex_1'].unique()[0]

    else:
        inputdf['batting_team'].loc[0] = teamdata[teamdata['team'] == inputdf['batting_team'].loc[0]]['batindex_2'].unique()[0]
        inputdf['bowling_team'].loc[0] = teamdata[teamdata['team'] == inputdf['bowling_team'].loc[0]]['bowlindex_2'].unique()[0]
        
    for batsmen in batsmen_list:
        if(batsmandata[batsmandata['batsman']==batsmen]['index_1'].unique().size>0):
            if(inputdf['innings'].loc[0] == 1):
                batting_index = batting_index + batsmandata[batsmandata['batsman']==batsmen]['index_1'].unique()[0]
            else:
                batting_index = batting_index + batsmandata[batsmandata['batsman']==batsmen]['index_2'].unique()[0]
        else:
            batting_index = batting_index + 8

    for batsmen in batsmen_list:
        if(batsmandata[batsmandata['batsman']==batsmen]['index_1'].unique().size>0):
            if(inputdf['innings'].loc[0] == 1):
                batting_strike = batting_strike + batsmandata[batsmandata['batsman']==batsmen]['index_1'].unique()[0]
            else:
                batting_strike = batting_strike + batsmandata[batsmandata['batsman']==batsmen]['index_2'].unique()[0]
        else:
            batting_strike = batting_strike + 90

    for bowler in bowler_list:
        if(bowlerdata[bowlerdata['bowler']==bowler]['A1index'].unique().size>0):
            #print(bowlerdata[bowlerdata['bowler']==bowler]['A1index'].unique())
            bowling_index = bowling_index + bowlerdata[bowlerdata['bowler']==bowler]['A1index'].unique()[0]
            #print(bowler)
        else:
            bowling_index = bowling_index + 7
            

    inputdf['batsmen'].loc[0] = batting_index/len(batsmen_list)
    inputdf['bowlers'].loc[0] = bowling_index/len(bowler_list)
    inputdf['ppwickets'].loc[0] = len(batsmen_list) - 2

    inputdata = np.array(inputdf[['innings', 'venue', 'batting_team', 'bowling_team','batsmen','bowlers','ppwickets']])
    print(inputdata)

    regressor = pickle.load(open('model_11.xyz','rb'))
    prediction = regressor.predict(np.array(inputdata))[0]
    print(pickle.format_version)
    return math.ceil(prediction)