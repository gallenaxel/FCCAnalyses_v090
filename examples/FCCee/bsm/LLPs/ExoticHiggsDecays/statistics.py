import re
import pandas as pd
import numpy as np

latex_table = r"""
\begin{table}[H]
    \centering
    \resizebox{\textwidth}{!}{
        \begin{tabular}{|l||c|c|c|c|c|c|} \hline
          & Before selection & Exactly 2 oppositely charged leptons & $70<m_{ll}<110$ GeV & $r<2000$ & $n_{trk} < 2$ & $m_{DV} < 2$ \\
        \hline
        wzp6\_ee\_ssH\_Hbb\_ecm240 & 188460.000 $\pm$ 409.071 & 25.442 $\pm$ 4.896 & $\leq$ 4.896 & $\leq$ 4.896 & $\leq$ 4.896 & $\leq$ 4.896 \\
        wzp6\_ee\_ssH\_Hcc\_ecm240 & 9353.880 $\pm$ 3.016 & 0.031 $\pm$ 0.031 & $\leq$ 0.031 & $\leq$ 0.031 & $\leq$ 0.031 & $\leq$ 0.031 \\
        wzp6\_ee\_ssH\_Hgg\_ecm240 & 26492.400 $\pm$ 10.780 & 0.265 $\pm$ 0.132 & $\leq$ 0.132 & $\leq$ 0.132 & $\leq$ 0.132 & $\leq$ 0.132 \\
        wzp6\_ee\_ssH\_Hmumu\_ecm240 & 70.405 $\pm$ 0.001 & 56.354 $\pm$ 0.100 & 1.046 $\pm$ 0.014 & $\leq$ 0.014 & $\leq$ 0.014 & $\leq$ 0.014 \\
        wzp6\_ee\_ssH\_Hss\_ecm240 & 77.652 $\pm$ 0.002 & 0.001 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6\_ee\_ssH\_Htautau\_ecm240 & 20293.200 $\pm$ 7.227 & 784.079 $\pm$ 6.307 & 90.153 $\pm$ 2.139 & $\leq$ 2.139 & $\leq$ 2.139 & $\leq$ 2.139 \\
        wzp6\_ee\_bbH\_Hbb\_ecm240 & 188460.000 $\pm$ 818.142 & 64.076 $\pm$ 10.989 & $\leq$ 10.989 & $\leq$ 10.989 & $\leq$ 10.989 & $\leq$ 10.989 \\
        wzp6\_ee\_bbH\_Hcc\_ecm240 & 9357.120 $\pm$ 2.263 & 2.082 $\pm$ 0.221 & $\leq$ 0.221 & $\leq$ 0.221 & $\leq$ 0.221 & $\leq$ 0.221 \\
        wzp6\_ee\_bbH\_Hgg\_ecm240 & 26503.200 $\pm$ 21.573 & 4.373 $\pm$ 0.761 & $\leq$ 0.761 & $\leq$ 0.761 & $\leq$ 0.761 & $\leq$ 0.761 \\
        wzp6\_ee\_bbH\_Hmumu\_ecm240 & 70.427 $\pm$ 0.002 & 55.689 $\pm$ 0.114 & 1.015 $\pm$ 0.015 & $\leq$ 0.015 & $\leq$ 0.015 & $\leq$ 0.015 \\
        wzp6\_ee\_bbH\_Hss\_ecm240 & 77.684 $\pm$ 0.002 & 0.019 $\pm$ 0.002 & $\leq$ 0.002 & $\leq$ 0.002 & $\leq$ 0.002 & $\leq$ 0.002 \\
        wzp6\_ee\_bbH\_Htautau\_ecm240 & 20304.000 $\pm$ 7.233 & 823.226 $\pm$ 6.464 & 85.987 $\pm$ 2.089 & $\leq$ 2.089 & $\leq$ 2.089 & $\leq$ 2.089 \\
        wzp6\_ee\_ccH\_Hbb\_ecm240 & 146772.000 $\pm$ 281.148 & 20.548 $\pm$ 3.883 & $\leq$ 3.883 & $\leq$ 3.883 & $\leq$ 3.883 & $\leq$ 3.883 \\
        wzp6\_ee\_ccH\_Hcc\_ecm240 & 7286.760 $\pm$ 1.555 & 0.036 $\pm$ 0.026 & $\leq$ 0.026 & $\leq$ 0.026 & $\leq$ 0.026 & $\leq$ 0.026 \\
        wzp6\_ee\_ccH\_Hmumu\_ecm240 & 54.853 $\pm$ 0.001 & 43.974 $\pm$ 0.078 & 0.813 $\pm$ 0.011 & $\leq$ 0.011 & $\leq$ 0.011 & $\leq$ 0.011 \\
        wzp6\_ee\_ccH\_Hss\_ecm240 & 60.556 $\pm$ 0.002 & 0.001 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6\_ee\_ccH\_Htautau\_ecm240 & 15811.200 $\pm$ 4.970 & 609.364 $\pm$ 4.908 & 69.767 $\pm$ 1.661 & $\leq$ 1.661 & $\leq$ 1.661 & $\leq$ 1.661 \\
        wzp6\_ee\_eeH\_Hbb\_ecm240 & 45046.800 $\pm$ 23.902 & 29663.768 $\pm$ 57.798 & 28354.258 $\pm$ 56.508 & 5.068 $\pm$ 0.755 & $\leq$ 0.755 & $\leq$ 0.755 \\
        wzp6\_ee\_eeH\_Hcc\_ecm240 & 2235.600 $\pm$ 0.264 & 1507.147 $\pm$ 2.902 & 1443.505 $\pm$ 2.840 & 0.017 $\pm$ 0.010 & $\leq$ 0.010 & $\leq$ 0.010 \\
        wzp6\_ee\_eeH\_Hgg\_ecm240 & 6332.040 $\pm$ 1.260 & 3990.499 $\pm$ 7.948 & 3822.937 $\pm$ 7.779 & 0.032 $\pm$ 0.022 & $\leq$ 0.022 & $\leq$ 0.022 \\
        wzp6\_ee\_eeH\_Hmumu\_ecm240 & 16.826 $\pm$ 0.000 & 14.789 $\pm$ 0.025 & 12.076 $\pm$ 0.023 & $\leq$ 0.023 & $\leq$ 0.023 & $\leq$ 0.023 \\
        wzp6\_ee\_eeH\_Hss\_ecm240 & 18.554 $\pm$ 0.000 & 12.569 $\pm$ 0.026 & 12.030 $\pm$ 0.025 & 0.001 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6\_ee\_eeH\_Htautau\_ecm240 & 4850.280 $\pm$ 0.844 & 2769.922 $\pm$ 5.795 & 2476.771 $\pm$ 5.480 & $\leq$ 5.480 & $\leq$ 5.480 & $\leq$ 5.480 \\
        wzp6\_ee\_mumuH\_Hbb\_ecm240 & 42552.000 $\pm$ 29.259 & 32123.640 $\pm$ 67.501 & 31340.966 $\pm$ 66.674 & 6.383 $\pm$ 0.951 & $\leq$ 0.951 & $\leq$ 0.951 \\
        wzp6\_ee\_mumuH\_Hcc\_ecm240 & 2112.480 $\pm$ 0.243 & 1625.031 $\pm$ 2.930 & 1586.525 $\pm$ 2.895 & 0.042 $\pm$ 0.015 & $\leq$ 0.015 & $\leq$ 0.015 \\
        wzp6\_ee\_mumuH\_Hgg\_ecm240 & 5981.040 $\pm$ 1.156 & 4498.834 $\pm$ 8.202 & 4392.775 $\pm$ 8.105 & 0.120 $\pm$ 0.042 & $\leq$ 0.042 & $\leq$ 0.042 \\
        wzp6\_ee\_mumuH\_Hmumu\_ecm240 & 15.898 $\pm$ 0.000 & 1.131 $\pm$ 0.007 & 0.300 $\pm$ 0.003 & $\leq$ 0.003 & $\leq$ 0.003 & $\leq$ 0.003 \\
        wzp6\_ee\_mumuH\_Hss\_ecm240 & 17.539 $\pm$ 0.000 & 13.569 $\pm$ 0.024 & 13.252 $\pm$ 0.024 & 0.001 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6\_ee\_mumuH\_Htautau\_ecm240 & 4582.440 $\pm$ 0.776 & 2792.379 $\pm$ 5.656 & 2615.897 $\pm$ 5.474 & $\leq$ 5.474 & $\leq$ 5.474 & $\leq$ 5.474 \\
        wzp6\_ee\_tautauH\_Hbb\_ecm240 & 42465.600 $\pm$ 21.877 & 1479.395 $\pm$ 12.532 & 14.863 $\pm$ 1.256 & $\leq$ 1.256 & $\leq$ 1.256 & $\leq$ 1.256 \\
        wzp6\_ee\_tautauH\_Hcc\_ecm240 & 2108.160 $\pm$ 0.242 & 75.188 $\pm$ 0.629 & 0.864 $\pm$ 0.067 & $\leq$ 0.067 & $\leq$ 0.067 & $\leq$ 0.067 \\
        wzp6\_ee\_tautauH\_Hgg\_ecm240 & 5970.240 $\pm$ 1.153 & 184.062 $\pm$ 1.657 & 2.090 $\pm$ 0.177 & $\leq$ 0.177 & $\leq$ 0.177 & $\leq$ 0.177 \\
        wzp6\_ee\_tautauH\_Hmumu\_ecm240 & 15.865 $\pm$ 0.000 & 10.016 $\pm$ 0.020 & 0.217 $\pm$ 0.003 & $\leq$ 0.003 & $\leq$ 0.003 & $\leq$ 0.003 \\
        wzp6\_ee\_tautauH\_Hss\_ecm240 & 17.496 $\pm$ 0.000 & 0.625 $\pm$ 0.005 & 0.007 $\pm$ 0.001 & $\leq$ 0.001 & $\leq$ 0.001 & $\leq$ 0.001 \\
        wzp6\_ee\_tautauH\_Htautau\_ecm240 & 4573.800 $\pm$ 0.773 & 584.497 $\pm$ 2.585 & 28.232 $\pm$ 0.568 & $\leq$ 0.568 & $\leq$ 0.568 & $\leq$ 0.568 \\
        wzp6\_ee\_nunuH\_Hbb\_ecm240 & 290520.000 $\pm$ 130.492 & 41.883 $\pm$ 3.184 & $\leq$ 3.184 & $\leq$ 3.184 & $\leq$ 3.184 & $\leq$ 3.184 \\
        wzp6\_ee\_nunuH\_Hcc\_ecm240 & 14418.000 $\pm$ 1.574 & 0.013 $\pm$ 0.013 & $\leq$ 0.013 & $\leq$ 0.013 & $\leq$ 0.013 & $\leq$ 0.013 \\
        wzp6\_ee\_nunuH\_Hdd\_ecm240 & 0.105 $\pm$ 0.000 & 0.000 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6\_ee\_nunuH\_Hgg\_ecm240 & 40845.600 $\pm$ 7.818 & 1.045 $\pm$ 0.201 & $\leq$ 0.201 & $\leq$ 0.201 & $\leq$ 0.201 & $\leq$ 0.201 \\
        wzp6\_ee\_nunuH\_Hmumu\_ecm240 & 108.540 $\pm$ 0.003 & 99.462 $\pm$ 0.164 & 1.875 $\pm$ 0.023 & $\leq$ 0.023 & $\leq$ 0.023 & $\leq$ 0.023 \\
        wzp6\_ee\_nunuH\_Hss\_ecm240 & 119.772 $\pm$ 0.001 & 0.000 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6\_ee\_nunuH\_Htautau\_ecm240 & 31287.600 $\pm$ 4.612 & 1615.587 $\pm$ 6.490 & 167.467 $\pm$ 2.090 & $\leq$ 2.090 & $\leq$ 2.090 & $\leq$ 2.090 \\
        wzp6\_ee\_nunuH\_Huu\_ecm240 & 0.045 $\pm$ 0.000 & 0.000 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6\_ee\_eeH\_HZZ\_ecm240 & 2042.280 $\pm$ 0.231 & 1285.380 $\pm$ 2.562 & 1197.389 $\pm$ 2.473 & 0.026 $\pm$ 0.011 & $\leq$ 0.011 & $\leq$ 0.011 \\
        wzp6\_ee\_mumuH\_HZZ\_ecm240 & 1928.880 $\pm$ 0.212 & 1398.964 $\pm$ 2.597 & 1343.436 $\pm$ 2.545 & 0.068 $\pm$ 0.018 & $\leq$ 0.018 & $\leq$ 0.018 \\
        wzp6\_ee\_qqH\_HZZ\_ecm240 & 15217.200 $\pm$ 1.564 & 1184.266 $\pm$ 3.875 & 553.741 $\pm$ 2.650 & 0.038 $\pm$ 0.022 & $\leq$ 0.022 & $\leq$ 0.022 \\
        wzp6\_ee\_tautauH\_HZZ\_ecm240 & 1925.640 $\pm$ 0.255 & 199.658 $\pm$ 1.078 & 56.705 $\pm$ 0.574 & $\leq$ 0.574 & $\leq$ 0.574 & $\leq$ 0.574 \\
        wzp6\_ee\_eeH\_HWW\_ecm240 & 16642.800 $\pm$ 5.368 & 9097.870 $\pm$ 19.456 & 8255.536 $\pm$ 18.533 & 0.083 $\pm$ 0.059 & $\leq$ 0.059 & $\leq$ 0.059 \\
        wzp6\_ee\_mumuH\_HWW\_ecm240 & 15724.800 $\pm$ 4.930 & 9788.177 $\pm$ 19.616 & 9258.762 $\pm$ 19.078 & 0.157 $\pm$ 0.079 & $\leq$ 0.079 & $\leq$ 0.079 \\
        wzp6\_ee\_qqH\_HWW\_ecm240 & 123984.000 $\pm$ 39.688 & 2510.563 $\pm$ 16.822 & 43.507 $\pm$ 2.214 & $\leq$ 2.214 & $\leq$ 2.214 & $\leq$ 2.214 \\
        wzp6\_ee\_tautauH\_HWW\_ecm240 & 15692.400 $\pm$ 4.914 & 1337.228 $\pm$ 7.243 & 45.822 $\pm$ 1.341 & $\leq$ 1.341 & $\leq$ 1.341 & $\leq$ 1.341 \\
        \hline 
    \end{tabular}} 
    \caption{Caption} 
    \label{tab:my_label} 
\end{table}
"""

def extract_table_data(latex_str):
    # Find the tabular environment
    tabular_match = re.search(r'\\begin\{tabular\}\{[^\}]*\}([\s\S]*?)\\end\{tabular\}', latex_str)
    if not tabular_match:
        raise ValueError("No tabular environment found in the given LaTeX string.")
    
    tabular_content = tabular_match.group(1)
    
    tabular_content = tabular_content.replace('\\hline', '').strip()
    
    rows = tabular_content.split('\\\\')
    
    table_data = []
    for row in rows:
        row = row.strip()
        if row:  # Ignore empty rows
            columns = [col.strip() for col in row.split('&')]
            table_data.append(columns)
    
    return table_data

def parse_value_with_uncertainty(value_str):
    if ' $\pm$ ' in value_str:
        value, uncertainty = value_str.split(' $\pm$ ')
        return float(value), float(uncertainty)
    elif '$\leq$' in value_str:
        # Handling the "$\leq$" case, treating it as zero with the upper limit as uncertainty
        limit_value = value_str.split('$\leq$ ')[1]
        return 0.0, float(limit_value)
    else:
        return float(value_str), 0.0

def combine_columns(dataframe):
    combined_values = []
    for column in dataframe.columns[1:]:  # Skip the first column as it is the identifier
        total_events = 0.0
        total_uncertainty_squared = 0.0
        for value_str in dataframe[column]:
            value, uncertainty = parse_value_with_uncertainty(value_str)
            total_events += value
            total_uncertainty_squared += uncertainty ** 2
        combined_events = total_events
        combined_uncertainty = np.sqrt(total_uncertainty_squared)
        combined_values.append(f'{combined_events:.0f} $\pm$ {combined_uncertainty:.0f}')
    return combined_values

table_data = extract_table_data(latex_table)

df = pd.DataFrame(table_data[1:], columns=table_data[0])

combined_row = ' & '.join(['ZH, H$\to$SM'] + combine_columns(df)) + ' \\\\ \\hline'

print("\nCombined LaTeX Row:")
print(combined_row)