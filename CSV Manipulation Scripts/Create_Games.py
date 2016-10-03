# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 19:34:31 2016

@author: James
"""
import numpy as np
import pandas
folder = "C:\Users\James\Documents\GitHub\Non Github NBA\Original_Scraped_CSV\\"
df0 = pandas.read_csv(folder + 'Post_Season_Scrape.csv')
df2 = pandas.read_csv(folder + 'Regular_Season_Scrape.csv')




def seperate_teams(df):
    
    WinningTeam = []
    LosingTeam = []
    df['WinningTeam']  = df['Matchup']
    df['LosingTeam']  = df['Matchup']
    
    HomeTeam = []
    AwayTeam = []
    df['HomeTeam']  = df['Matchup']
    df['AwayTeam']  = df['Matchup']
    
    """Date	Matchup	WL
26-May-91	POR @ LAL	L
"""
    
    for num,value in enumerate(df['Matchup']):
        
        
        playerTeam = value[:3]
        oppTeam = value[-3:]
        
       
        if "W" in str(df['WL'][num]):
            #print num
            WinningTeam += [playerTeam]
            LosingTeam += [oppTeam]
        elif "L" in str(df['WL'][num]):
            LosingTeam  += [playerTeam]
            WinningTeam += [oppTeam]
        else:
            LosingTeam  += ['unknown']
            WinningTeam += ['unknown']
            
        if "vs." in str(df['Matchup'][num]):
            HomeTeam += [playerTeam]
            AwayTeam += [oppTeam]
        else:
            AwayTeam  += [playerTeam]
            HomeTeam += [oppTeam]
    
    print len(LosingTeam)
    print len(WinningTeam )
    df['WinningTeam']  = np.transpose(np.array(WinningTeam))
    df['LosingTeam']  = np.transpose(np.array(LosingTeam))
    df['HomeTeam']  = np.transpose(np.array(HomeTeam))
    df['AwayTeam']  = np.transpose(np.array(AwayTeam))
    return df  
    
    
df0 = seperate_teams(df0)
df2 = seperate_teams(df2)
df0['PostReg'] = 'Post'
df2['PostReg'] = 'Reg'


gameDF = pandas.concat([df0[['GameID', 'SEASON_ID','Date', 'WinningTeam','LosingTeam','HomeTeam','AwayTeam', 'PostReg']],df2[['GameID', 'SEASON_ID','Date', 'WinningTeam','LosingTeam','HomeTeam','AwayTeam', 'PostReg']]])
gameDF = gameDF.drop_duplicates('GameID')
gameDF['Date']=gameDF['Date'].astype(str)
gameDF['Date']=pandas.to_datetime(gameDF['Date'])
fileName = 'C:\\Users\\James\\Documents\\GitHub\\Non Github NBA\\NBA Large CSV Files_Loadable\\GameLoad2.csv'
gameDF.replace({" DN": "DEN"}, inplace=True)
gameDF.replace({"UTH": "UTA"}, inplace=True)
gameDF.replace({"PHO": "PHX"}, inplace=True)
gameDF.replace({"PHL": "PHI"}, inplace=True)
gameDF.replace({"SAN": "SAS"}, inplace=True)
gameDF.replace({"GOS": "GSW"}, inplace=True)
gameDF.to_csv(fileName)
    