3D Interactive Analysis Stress Viewer

I am sharing the 3D Analysis Stress Viewer I developed to easily explore and visualize analysis results from any CSV file containing X, Y, Z, and stress (e.g., Von Mises) values.

Note: I used PrePoMax 2.4.0 for development. However, the viewer will work with CSV files exported from any analysis software (e.g., Nastran, Ansys, Altair, etc.).

I am not an expert analyst, just a mechanical designer. I only perform simple, amateur static analyses when needed for my own work.

Initially, I started this project because I needed a CSV file with X, Y, Z, and stress values from Analysis-1.frd (v2.4.0), but couldn’t find a working Python script for it. Existing scripts I found didn’t work correctly.

Now, the viewer can load any CSV file with X, Y, Z, and stress values and display an interactive 3D visualization.

Required files to run the viewer:

v05.py

Analysis-1.csv (or any CSV file with the same format)

How to Use

Open v05.py in Python (requires standard Python libraries like pandas and plotly).

Place your CSV file in the same folder as v05.py.

Run the script; it will generate an interactive 3D HTML viewer.

Open the output file Prepromax_interactive_stress_plot.html in any web browser.

Example Output

PDF user guide: Standalone 3D Interactive Stress viewer.pdf

HTML viewer: Prepromax_interactive_stress_plot.html
