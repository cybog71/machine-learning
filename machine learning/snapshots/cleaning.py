import janitor
import pandas as pd

df_clean = df.clean_names() \
             .remove_empty() \
             .dropna(subset=['profession'])

print(df_clean.columns)