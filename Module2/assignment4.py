import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
url ='http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2'
df = pd.read_html(url,match='.+',header=1)[0]



# TODO: Rename the columns so that they match the
# column definitions provided to you on the website
#
# .. your code here ..
columns=['RK', 'PLAYER', 'TEAM', 'GAMES_PLAYED', 'GOALS', 'ASSISTS', 'POINTS',
         'PLUS_MINUS_RATING', 'PENALTY_MINUTES', 'POINTS_PER_GAME',
         'SHOTS_ON_GOAL', 'SHOOTING_PERCENT', 'GAME-WINNING_GOALS',
         'POWER PLAY_GOALS', 'POWER_PLAY_ASSISTS', 'SHORT_HANDED_GOALS',
         'SHORT_HANDED_ASSISTS']

df.columns = columns

# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
df = df.dropna(axis=0, thresh=4)


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
df = df[df.GOALS != 'G']


# TODO: Get rid of the 'RK' column
#
# .. your code here ..
df = df.drop(axis=1,labels ='RK')
print df

# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
df = df.reset_index(drop=True)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric

numeric = ['GAMES_PLAYED', 'GOALS', 'ASSISTS', 'POINTS',
         'PLUS_MINUS_RATING', 'PENALTY_MINUTES', 'POINTS_PER_GAME',
         'SHOTS_ON_GOAL', 'SHOOTING_PERCENT', 'GAME-WINNING_GOALS',
         'POWER PLAY_GOALS', 'POWER_PLAY_ASSISTS', 'SHORT_HANDED_GOALS',
         'SHORT_HANDED_ASSISTS']
         
df[numeric] = df[numeric].apply(pd.to_numeric)
print df.dtypes

# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.
print df.count(axis=0)

print df.SHOOTING_PERCENT.unique().size

print df.loc[15,'GAMES_PLAYED'] + df.loc[16,'GAMES_PLAYED']
