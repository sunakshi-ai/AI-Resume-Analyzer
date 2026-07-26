import plotly.express as px

def skills_chart(found, missing):

    labels = ["Found Skills", "Missing Skills"]

    values = [len(found), len(missing)]

    fig = px.pie(
        names=labels,
        values=values,
        title="Skills Analysis"
    )

    return fig