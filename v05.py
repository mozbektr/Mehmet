# -*- coding: utf-8 -*-
"""VON-MISES STRESS VIEWER -Mehmet Ozbek
"""

# -*- coding: utf-8 -*-
"""input csv x,y,z,stress formatı olmalıdır.

"""

# -*- coding: utf-8 -*-
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import sys
import os
import base64
import time

# Input and output file names
INPUT_FILE = 'Analysis-1.csv'
OUTPUT_HTML_FILE = 'Prepromax_interactive_stress_plot.html'
ARROW_OFFSET_PIXELS = 80

if __name__ == '__main__':
    print(f"--- Starting: Reading data from '{INPUT_FILE}' ---")

    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: File '{INPUT_FILE}' not found.")
        sys.exit(1)

    # Load CSV data
    df = pd.read_csv(INPUT_FILE, header=None, names=['x', 'y', 'z', 'value'])
    df = df.apply(pd.to_numeric, errors='coerce').dropna()

    if len(df) == 0:
        print("ERROR: No valid data found after cleaning.")
        sys.exit(1)

    print(f"Loaded {len(df)} data rows.")

    # Determine max/min stress points
    max_i = df['value'].idxmax()
    min_i = df['value'].idxmin()

    pmax = df.loc[max_i]
    pmin = df.loc[min_i]

    max_val = pmax['value']
    min_val = pmin['value']

    print(f"Max Stress: {max_val:.3f} MPa at ({pmax['x']:.2f}, {pmax['y']:.2f}, {pmax['z']:.2f})")
    print(f"Min Stress: {min_val:.3f} MPa at ({pmin['x']:.2f}, {pmin['y']:.2f}, {pmin['z']:.2f})")

    # Create main scatter plot
    main_scatter = go.Scatter3d(
    x=df['x'], y=df['y'], z=df['z'],
    mode='markers',
    marker=dict(
        size=6,
        color=df['value'],
        colorscale='Turbo',
        colorbar=dict(title='Stress (MPa)'),
        cmin=df['value'].min(),
        cmax=df['value'].max()
    ),
    hovertemplate=
        "X: %{x:.2f} mm<br>" +
        "Y: %{y:.2f} mm<br>" +
        "Z: %{z:.2f} mm<br>" +
        "Stress Value: %{marker.color:.3f} MPa<extra></extra>"
)

    fig = go.Figure([main_scatter])

    # Add max stress marker
    fig.add_trace(go.Scatter3d(
        x=[pmax['x']], y=[pmax['y']], z=[pmax['z']],
        mode='markers',
        marker=dict(size=10, color='red', symbol='diamond', line=dict(width=1, color='darkred')),
        name='MAX Stress'
    ))

    # Add min stress marker
    fig.add_trace(go.Scatter3d(
        x=[pmin['x']], y=[pmin['y']], z=[pmin['z']],
        mode='markers',
        marker=dict(size=10, color='blue', symbol='square', line=dict(width=1, color='darkblue')),
        name='MIN Stress'
    ))

    # Create annotations
    annotations = [
        dict(
            x=pmax['x'], y=pmax['y'], z=pmax['z'],
            text=f"MAX: {max_val:.3f} MPa",
            ax=-ARROW_OFFSET_PIXELS, ay=0,
            font=dict(color='red', size=14),
            bgcolor='rgba(255,255,255,0.7)',
            bordercolor='red', arrowcolor='red',
            arrowhead=1, arrowside='start', arrowsize=1.5, arrowwidth=2
        ),
        dict(
            x=pmin['x'], y=pmin['y'], z=pmin['z'],
            text=f"MIN: {min_val:.3f} MPa",
            ax=-ARROW_OFFSET_PIXELS, ay=0,
            font=dict(color='blue', size=14),
            bgcolor='rgba(255,255,255,0.7)',
            bordercolor='blue', arrowcolor='blue',
            arrowhead=1, arrowside='start', arrowsize=1.5, arrowwidth=2
        )
    ]

    fig.update_layout(
        title=f'Stress Point Cloud - Max/Min Indicators ({len(df)} Points)',
        scene=dict(
            xaxis_title='X (mm)', yaxis_title='Y (mm)', zaxis_title='Z (mm)',
            aspectmode='data', annotations=annotations
        ),
        showlegend=False
    )

    # Save HTML
    fig.write_html(OUTPUT_HTML_FILE, auto_open=False, include_plotlyjs='full')

    # ---------------- CSV EXPORT BUTTON INJECTION ----------------
    csv_string = df.to_csv(index=False, header=False)
    encoded = base64.b64encode(csv_string.encode()).decode()
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    export_name = f"exported_stress_data_{timestamp}.csv"

    inject = """
    <div style='text-align:right;padding:10px;background:#f7f7f7;border-bottom:1px solid #ddd;position:sticky;top:0;z-index:100;'>
        <button onclick=\"downloadCSV()\" style='padding:8px 15px;background:#007BFF;color:white;border:none;border-radius:4px;cursor:pointer;font-weight:bold;'>Export CSV</button>
    </div>
    <script>
        const b64 = '%s';
        const fname = '%s';
        function downloadCSV(){
            const s = atob(b64);
            const blob = new Blob([s], {type:'text/csv;charset=utf-8;'});
            const link = document.createElement('a');
            const url = URL.createObjectURL(blob);
            link.setAttribute('href', url);
            link.setAttribute('download', fname);
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    </script>
    """ % (encoded, export_name)

    with open(OUTPUT_HTML_FILE, 'r', encoding='utf-8') as f:
        html = f.read()
    body = html.find('<body>') + len('<body>')
    html = html[:body] + inject + html[body:]
    with open(OUTPUT_HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(html)

    # ---------------- FINAL CONSOLE REPORT ----------------
    print("\n================ PROCESS COMPLETED SUCCESSFULLY ================")
    print(f"Total Node Count       : {len(df)} points")
    print(f"Maximum Stress Value   : {max_val:.3f} MPa")
    print(f"Minimum Stress Value   : {min_val:.3f} MPa")
    print(f"Output HTML File       : {OUTPUT_HTML_FILE}")
    print("HTML file generated successfully with Max/Min annotations and CSV export button.")