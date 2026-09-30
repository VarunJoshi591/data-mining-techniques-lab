


import pandas as pd 

year = 2026

sundays = pd.date_range(start=f'{year}-01-01',
                       end=f'{year}-12-31',
                       freq='W-SUN')

print(sundays)

