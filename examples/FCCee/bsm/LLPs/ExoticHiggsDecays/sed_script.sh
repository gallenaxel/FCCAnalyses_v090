#! /bin/bash
# Create array 'process_array' which contains all processes from the 'list_w23_bkgs.py' skimming script
readarray -t process_array < test_processes.txt

# You can also define your processes manually (don't forget to comment the 'readarray' line above):
# declare -a process_array=("process1" "process2" "etc")

# Keep this fixed. It defines the process name _to replace_
toReplace='custom_process'

# For every process in the 'arr', 
for process in "${process_array[@]}"
do

    part1='s/'
    part2=${toReplace}
    part3='/'
    part4=${process}
    part5='/g'

    # Combining the parts
    sed_input_1=${part1}${part2}${part3}${part4}${part5}

    # Edit the processList process
    sed -i ${sed_input_1} Reco_analysis_stage1.py
    sleep 1

    # Run the condor submission
    fccanalysis run Reco_analysis_stage1.py

    # Change the processName back to the 'toReplace' variable
    sed_input_2=${part1}${part4}${part3}${part2}${part5}
    sed -i ${sed_input_2} Reco_analysis_stage1.py
    sleep 1

done

