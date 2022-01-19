# Importing Pandas as pd
import pandas as pd

# Importing numpy as np
import numpy as np

# Creating a dataframe
# Setting the seed value to re-generate the result.
np.random.seed(25)

df = pd.DataFrame(np.random.rand(10, 3), columns =['A', 'B', 'C'])

# np.random.rand(10, 3) has generated a
# random 2-Dimensional array of shape 10 * 3
# which is then converted to a dataframe

# We want NaN values in dataframe.
# so let's fill the last row with NaN value
df.iloc[-1] = np.nan
# add 1 to all the elements
# of the data frame
df.add(1)

# We have given a default value
# of '10' for all the nan cells
df.add(1, fill_value = 10)

print(df)
