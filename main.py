import pandas as pd 
from scipy.spatial.distance import cdist

# find_lat = 40.765123
# find_lon = -73.965816


#print(df_metro)
def find_metro(find_lat,find_lon):
    df_metro = pd.read_csv('nyc_metro_coords.csv',sep=';') 

    find_coord = {'Lat': pd.Series([find_lat]),
            'Lon': pd.Series([find_lon])}
    df_find_coord = pd.DataFrame(find_coord)

    def closest_point(point, points):
        """ Find closest point from a list of points. """
        return points[cdist([point], points).argmin()]

    def match_value(df, col1, x, col2):
        """ Match value x from col1 row to value in col2. """
        return df[df[col1] == x][col2].values[0]


    df_metro['point'] = [(x, y) for x,y in zip(df_metro['Lat'], df_metro['Lon'])]
    df_find_coord['point'] = [(x, y) for x,y in zip(df_find_coord['Lat'], df_find_coord['Lon'])]

    df_find_coord['closest'] = [closest_point(x, list(df_metro['point'])) for x in df_find_coord['point']]
    df_find_coord['station'] = [match_value(df_metro, 'point', x, 'Station Name') for x in df_find_coord['closest']]

    return df_find_coord['station'].values[0]