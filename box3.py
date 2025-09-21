def bereken_box3(spaargeld, beleggingen, schulden, vrijstelling):
    vermogen = spaargeld + beleggingen - schulden
    belastbaar = max(0, vermogen - vrijstelling)
    belasting = belastbaar * 0.0135  # fictief tarief
    return {"vermogen": vermogen, "belastbaar": belastbaar, "belasting": belasting}

def genereer_matrix():
    import plotly.graph_objects as go
    fig = go.Figure(data=go.Heatmap(
        z=[[1.2, 2.1], [2.5, 3.0]],
        x=["Laag risico", "Hoog risico"],
        y=["Laag rendement", "Hoog rendement"]
    ))
    fig.update_layout(title="Risico vs. Rendement")
    return fig

def genereer_profieladvies(profiel):
    if profiel == "Defensief":
        return "U kiest voor zekerheid. Overweeg meer spaargeld en minder aandelen."
    elif profiel == "Neutraal":
        return "U balanceert risico en rendement. Houd uw mix in de gaten."
    else:
        return "U zoekt groei. Let op volatiliteit en spreiding."

