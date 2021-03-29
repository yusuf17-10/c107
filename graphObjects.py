import csv
import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv("data.csv")

print("for_all_the_students")

print(df.groupby("level")["attempt"].mean())
print("for_student :TRL_imb")

student_df=df.loc[df["student_id"]=="TRL_imb"]

print(student_df.groupby("level")["attempt"].mean())

fig=go.Figure(go.Bar(
    x=student_df.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation="h"

))
fig.show()