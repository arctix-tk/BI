import pandas as pd
import sweetviz as sv

df = pd.read_parquet('escooter_history.parquet')
report = sv.analyze(df)
report.show_html('escooter.html')