Interactive 3D Viewer for X, Y, Z, and Von Mises Stress Results

I am sharing a 3D interactive viewer that visualizes X, Y, Z, and Von Mises stress data from any CSV file. The output is a single standalone HTML file that can be opened in any web browser.

Note: I used PrePoMax 2.4.0 for development, but the viewer works with CSV files exported from any analysis software (e.g., Nastran, Ansys, Altair, etc.).

I am not an expert analyst, just a mechanical designer. I only perform simple, amateur static analyses when needed for my own work.

Initially, I started this project because I needed a CSV file with X, Y, Z, and stress values, but couldn’t find a working Python script. Existing scripts I found didn’t work correctly.

Now, the viewer can load any CSV file with X, Y, Z, and stress values and generate a standalone interactive HTML file (Prepromax_interactive_stress_plot.html).

Required Files

v05.py

Analysis-1.csv (or any CSV file with the same format)

How to Use
PDF user guide: Standalone 3D Interactive Stress viewer.pdf

Open v05.py in Python (requires standard Python libraries like pandas and plotly).

Place your CSV file in the same folder as v05.py.

Run the script; it will generate the interactive HTML viewer.

Open Prepromax_interactive_stress_plot.html in any web browser.

Note: The script has been successfully run on Google Colab, so you can also execute it online without installing Python locally.

Example Output

HTML viewer: Prepromax_interactive_stress_plot.html

⚡ Upcoming Other Phyton script

I am currently working on Python scripts to convert PrePoMax .frd analysis outputs to CSV files containing X, Y, Z, and stress values.

The scripts are ready but need further testing before being shared.
