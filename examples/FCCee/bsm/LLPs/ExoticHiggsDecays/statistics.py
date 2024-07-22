import re
import pandas as pd
import numpy as np

latex_table = r"""
\begin{table}[H]
    \centering
    \resizebox{\textwidth}{!}{
        \begin{tabular}{|l||c|c|c|c|c|} \hline
          & Before selection & Exactly 2 oppositely charged leptons & 70 < $m_{ll}$ < 110 GeV & n DVs $\geq$ 1 & n DVs $\geq$ 1 (merged) \\
        \hline
        wzp6_ee_ssH_Hbb_ecm240 & 125640.000 $\pm$ 222.670 & 16.961 $\pm$ 3.264 & $\leq$ 3.264 & $\leq$ 3.264 & $\leq$ 3.264 \\
        wzp6_ee_ssH_Hcc_ecm240 & 6235.920 $\pm$ 1.641 & 0.021 $\pm$ 0.021 & $\leq$ 0.021 & $\leq$ 0.021 & $\leq$ 0.021 \\
        wzp6_ee_ssH_Hgg_ecm240 & 23548.800 $\pm$ 9.034 & 0.235 $\pm$ 0.118 & $\leq$ 0.118 & $\leq$ 0.118 & $\leq$ 0.118 \\
        wzp6_ee_ssH_Hmumu_ecm240 & 46.937 $\pm$ 0.001 & 37.569 $\pm$ 0.066 & 0.697 $\pm$ 0.009 & $\leq$ 0.009 & $\leq$ 0.009 \\
        wzp6_ee_ssH_Hss_ecm240 & 51.768 $\pm$ 0.001 & 0.000 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6_ee_ssH_Htautau_ecm240 & 13528.800 $\pm$ 3.934 & 522.719 $\pm$ 4.205 & 60.102 $\pm$ 1.426 & $\leq$ 1.426 & $\leq$ 1.426 \\
        wzp6_ee_bbH_Hbb_ecm240 & 125640.000 $\pm$ 445.340 & 42.718 $\pm$ 7.326 & $\leq$ 7.326 & $\leq$ 7.326 & $\leq$ 7.326 \\
        wzp6_ee_bbH_Hcc_ecm240 & 6238.080 $\pm$ 1.232 & 1.388 $\pm$ 0.147 & $\leq$ 0.147 & $\leq$ 0.147 & $\leq$ 0.147 \\
        wzp6_ee_bbH_Hgg_ecm240 & 17668.800 $\pm$ 11.743 & 2.915 $\pm$ 0.507 & $\leq$ 0.507 & $\leq$ 0.507 & $\leq$ 0.507 \\
        wzp6_ee_bbH_Hmumu_ecm240 & 46.951 $\pm$ 0.001 & 37.126 $\pm$ 0.076 & 0.747 $\pm$ 0.011 & $\leq$ 0.011 & $\leq$ 0.011 \\
        wzp6_ee_bbH_Hss_ecm240 & 51.790 $\pm$ 0.001 & 0.013 $\pm$ 0.001 & $\leq$ 0.001 & $\leq$ 0.001 & $\leq$ 0.001 \\
        wzp6_ee_bbH_Htautau_ecm240 & 13536.000 $\pm$ 3.937 & 548.817 $\pm$ 4.310 & 58.577 $\pm$ 1.408 & $\leq$ 1.408 & $\leq$ 1.408 \\
        wzp6_ee_ccH_Hbb_ecm240 & 97848.000 $\pm$ 153.038 & 13.699 $\pm$ 2.589 & $\leq$ 2.589 & $\leq$ 2.589 & $\leq$ 2.589 \\
        wzp6_ee_ccH_Hcc_ecm240 & 4857.840 $\pm$ 0.846 & 0.024 $\pm$ 0.017 & $\leq$ 0.017 & $\leq$ 0.017 & $\leq$ 0.017 \\
        wzp6_ee_ccH_Hmumu_ecm240 & 36.569 $\pm$ 0.001 & 29.316 $\pm$ 0.052 & 0.548 $\pm$ 0.007 & $\leq$ 0.007 & $\leq$ 0.007 \\
        wzp6_ee_ccH_Hss_ecm240 & 40.370 $\pm$ 0.001 & 0.000 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6_ee_ccH_Htautau_ecm240 & 10540.800 $\pm$ 2.706 & 406.242 $\pm$ 3.272 & 46.590 $\pm$ 1.108 & $\leq$ 1.108 & $\leq$ 1.108 \\
        wzp6_ee_eeH_Hbb_ecm240 & 30031.200 $\pm$ 13.011 & 19775.846 $\pm$ 38.532 & 18974.238 $\pm$ 37.743 & $\leq$ 37.743 & 0.075 $\pm$ 0.075 \\
        wzp6_ee_eeH_Hcc_ecm240 & 1490.400 $\pm$ 0.144 & 1004.764 $\pm$ 1.935 & 960.920 $\pm$ 1.892 & $\leq$ 1.892 & $\leq$ 1.892 \\
        wzp6_ee_eeH_Hgg_ecm240 & 4221.360 $\pm$ 0.686 & 2660.333 $\pm$ 5.299 & 2552.034 $\pm$ 5.190 & $\leq$ 5.190 & $\leq$ 5.190 \\
        wzp6_ee_eeH_Hmumu_ecm240 & 11.218 $\pm$ 0.000 & 9.859 $\pm$ 0.017 & 8.050 $\pm$ 0.015 & $\leq$ 0.015 & $\leq$ 0.015 \\
        wzp6_ee_eeH_Hss_ecm240 & 12.370 $\pm$ 0.000 & 8.379 $\pm$ 0.017 & 8.020 $\pm$ 0.017 & $\leq$ 0.017 & $\leq$ 0.017 \\
        wzp6_ee_eeH_Htautau_ecm240 & 3233.520 $\pm$ 0.460 & 1846.615 $\pm$ 3.864 & 2248.824 $\pm$ 4.264 & $\leq$ 4.264 & $\leq$ 4.264 \\
        wzp6_ee_mumuH_Hbb_ecm240 & 28368.000 $\pm$ 15.927 & 21415.760 $\pm$ 45.001 & 21025.511 $\pm$ 44.589 & $\leq$ 44.589 & $\leq$ 44.589 \\
        wzp6_ee_mumuH_Hcc_ecm240 & 1408.320 $\pm$ 0.132 & 1083.354 $\pm$ 1.953 & 1056.553 $\pm$ 1.929 & $\leq$ 1.929 & $\leq$ 1.929 \\
        wzp6_ee_mumuH_Hgg_ecm240 & 3987.360 $\pm$ 0.629 & 2999.222 $\pm$ 5.468 & 2933.690 $\pm$ 5.408 & $\leq$ 5.408 & $\leq$ 5.408 \\
        wzp6_ee_mumuH_Hmumu_ecm240 & 10.598 $\pm$ 0.000 & 0.754 $\pm$ 0.004 & 1.384 $\pm$ 0.006 & $\leq$ 0.006 & $\leq$ 0.006 \\
        wzp6_ee_mumuH_Hss_ecm240 & 11.693 $\pm$ 0.000 & 9.046 $\pm$ 0.016 & 8.836 $\pm$ 0.016 & $\leq$ 0.016 & 0.000 $\pm$ 0.000 \\
        wzp6_ee_mumuH_Htautau_ecm240 & 3054.960 $\pm$ 0.422 & 1861.586 $\pm$ 3.771 & 2333.501 $\pm$ 4.222 & $\leq$ 4.222 & $\leq$ 4.222 \\
        wzp6_ee_tautauH_Hbb_ecm240 & 28310.400 $\pm$ 11.909 & 986.264 $\pm$ 8.355 & 10.900 $\pm$ 0.878 & $\leq$ 0.878 & $\leq$ 0.878 \\
        wzp6_ee_tautauH_Hcc_ecm240 & 1405.440 $\pm$ 0.132 & 50.125 $\pm$ 0.420 & 0.573 $\pm$ 0.045 & $\leq$ 0.045 & $\leq$ 0.045 \\
        wzp6_ee_tautauH_Hgg_ecm240 & 3980.160 $\pm$ 0.628 & 122.708 $\pm$ 1.105 & 1.403 $\pm$ 0.118 & $\leq$ 0.118 & $\leq$ 0.118 \\
        wzp6_ee_tautauH_Hmumu_ecm240 & 10.577 $\pm$ 0.000 & 6.677 $\pm$ 0.013 & 0.302 $\pm$ 0.003 & $\leq$ 0.003 & $\leq$ 0.003 \\
        wzp6_ee_tautauH_Hss_ecm240 & 11.664 $\pm$ 0.000 & 0.416 $\pm$ 0.003 & 0.005 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6_ee_tautauH_Htautau_ecm240 & 3049.200 $\pm$ 0.421 & 389.665 $\pm$ 1.723 & 25.133 $\pm$ 0.438 & $\leq$ 0.438 & $\leq$ 0.438 \\
        wzp6_ee_nunuH_Hbb_ecm240 & 193680.000 $\pm$ 71.031 & 27.922 $\pm$ 2.123 & $\leq$ 2.123 & $\leq$ 2.123 & $\leq$ 2.123 \\
        wzp6_ee_nunuH_Hcc_ecm240 & 9612.000 $\pm$ 0.857 & 0.009 $\pm$ 0.009 & $\leq$ 0.009 & $\leq$ 0.009 & $\leq$ 0.009 \\
        wzp6_ee_nunuH_Hdd_ecm240 & 0.070 $\pm$ 0.000 & 0.000 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6_ee_nunuH_Hgg_ecm240 & 27230.400 $\pm$ 4.256 & 0.696 $\pm$ 0.134 & $\leq$ 0.134 & $\leq$ 0.134 & $\leq$ 0.134 \\
        wzp6_ee_nunuH_Hmumu_ecm240 & 72.360 $\pm$ 0.002 & 66.308 $\pm$ 0.110 & 1.250 $\pm$ 0.015 & $\leq$ 0.015 & $\leq$ 0.015 \\
        wzp6_ee_nunuH_Hss_ecm240 & 79.848 $\pm$ 0.001 & 0.000 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6_ee_nunuH_Htautau_ecm240 & 20858.400 $\pm$ 2.510 & 1077.058 $\pm$ 4.327 & 111.645 $\pm$ 1.393 & $\leq$ 1.393 & $\leq$ 1.393 \\
        wzp6_ee_nunuH_Huu_ecm240 & 0.030 $\pm$ 0.000 & 0.000 $\pm$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 & $\leq$ 0.000 \\
        wzp6_ee_eeH_HZZ_ecm240 & 1361.520 $\pm$ 0.126 & 856.920 $\pm$ 1.708 & 864.943 $\pm$ 1.716 & $\leq$ 1.716 & $\leq$ 1.716 \\
        wzp6_ee_mumuH_HZZ_ecm240 & 1285.920 $\pm$ 0.115 & 932.642 $\pm$ 1.732 & 966.784 $\pm$ 1.763 & $\leq$ 1.763 & $\leq$ 1.763 \\
        wzp6_ee_qqH_HZZ_ecm240 & 10144.800 $\pm$ 0.851 & 789.511 $\pm$ 2.584 & 388.918 $\pm$ 1.813 & $\leq$ 1.813 & $\leq$ 1.813 \\
        wzp6_ee_tautauH_HZZ_ecm240 & 1283.760 $\pm$ 0.139 & 133.105 $\pm$ 0.719 & 54.752 $\pm$ 0.461 & $\leq$ 0.461 & $\leq$ 0.461 \\
        wzp6_ee_eeH_HWW_ecm240 & 11095.200 $\pm$ 2.922 & 6065.247 $\pm$ 12.971 & 6676.093 $\pm$ 13.608 & $\leq$ 13.608 & $\leq$ 13.608 \\
        wzp6_ee_mumuH_HWW_ecm240 & 10483.200 $\pm$ 2.683 & 6525.451 $\pm$ 13.077 & 7421.581 $\pm$ 13.946 & $\leq$ 13.946 & $\leq$ 13.946 \\
        wzp6_ee_qqH_HWW_ecm240 & 82656.000 $\pm$ 21.603 & 1673.709 $\pm$ 11.215 & 29.005 $\pm$ 1.476 & $\leq$ 1.476 & $\leq$ 1.476 \\
        wzp6_ee_tautauH_HWW_ecm240 & 10461.600 $\pm$ 2.675 & 891.485 $\pm$ 4.829 & 38.813 $\pm$ 1.008 & $\leq$ 1.008 & $\leq$ 1.008 \\
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
        combined_values.append(f'{combined_events:.3f} $\pm$ {combined_uncertainty:.3f}')
    return combined_values

table_data = extract_table_data(latex_table)

df = pd.DataFrame(table_data[1:], columns=table_data[0])

combined_row = ' & '.join(['ZH, H$\to$SM'] + combine_columns(df)) + ' \\\\ \\hline'

print("\nCombined LaTeX Row:")
print(combined_row)