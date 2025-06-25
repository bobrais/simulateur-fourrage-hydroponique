
# visualization_3d.py

import plotly.graph_objects as go
import streamlit as st

def afficher_plan_3d(racks, niveaux, plateaux_par_niveau):
    x, y, z = [], [], []

    for r in range(racks):
        for n in range(niveaux):
            for p in range(plateaux_par_niveau):
                x.append(p)
                y.append(r)
                z.append(n)

    fig = go.Figure(data=[go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(size=5, color=z, colorscale='Viridis'),
        text=[f'Rack {r+1} | Niveau {n+1}' for r, n in zip(y, z)]
    )])

    fig.update_layout(
        title='Visualisation 3D des plateaux',
        scene=dict(
            xaxis_title='Plateaux par niveau',
            yaxis_title='Racks',
            zaxis_title='Niveaux'
        ),
        margin=dict(l=0, r=0, b=0, t=30)
    )

    st.plotly_chart(fig, use_container_width=True)
