import pandas as pd

Data =[

    {'name':'Komal', 'age':26, 'city':'navi mumbai'},
    {'name':'Komi', 'age':25, 'city':'mumbai'},
    {'name':'Patra', 'age':26, 'city':'Airoli'},
]

Data = pd.DataFrame(Data)
Data.to_csv('data/data.csv', index=False)

