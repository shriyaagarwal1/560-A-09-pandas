# https://goheels.com/sports/mens-basketball/roster
#roster = ['Bacot', 'Davis', 'Cadeau']
#for player in roster:
    #print(player)
    
import pandas as pd
roster = ['Bacot', 'Davis', 'Cadeau']
player = {"Last Name": roster}
data =pd.DataFrame(player)
print(data)