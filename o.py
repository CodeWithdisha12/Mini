""""
import numpy as np
data=np.array([12,69,87,15,])
avg,spread=data.mean(),data.std()
print("avg:", avg)
print("spreasd:",spread)
"""
"""""
import pandas as pd
data=pd.Series([12,65,87,29])
print("avg:",data.mean())
"""
import pandas as pd

df = pd.DataFrame({

'Department': ['CS', 'EE', 'ME', 'CS', 'EC'],

'Satisfaction': ['High', 'Low', 'Med', 'High', 'Low'],

'Study_Hours': [12.5, 8.0, 15.2, 9.5, 14.0],

'Marks': [88, 62, 91, 74, 85]

})

# Output: print(df.head())