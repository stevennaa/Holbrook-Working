import numpy as np
import wbdata
from plotly.offline import iplot
import cufflinks as cf

cf.go_offline()

variable_labels = {"SN.ITK.DEFC.ZS": "Malnutrition"}

countries = {"WLD": "World",
             "UGA": "Uganda",
             "IND": "India",
            }

# Adjust the start year as per your desired timeframe
start_year = 2002

# Fetch data
df = wbdata.get_dataframe(variable_labels, country=countries)

# Reset the index to move the date index level to a column
df = df.reset_index()

# Convert the 'date' column to integer type
df['date'] = df['date'].astype(int)

# Filter dataframe to include data from 2003 onwards
df = df[df['date'] >= start_year]

# Unstack the dataframe
df = df.set_index(['date', 'country'])['Malnutrition'].unstack()

# Plot the data
df.iplot(title="Malnutrition (%)",
          yTitle="Percent of Undernourishment",
          xTitle='Year')
