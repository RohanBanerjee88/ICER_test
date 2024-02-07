#!/bin/bash

# Define paths to your script files
SCRIPT="./script.sh.erb"
BEFORE="./before.sh.erb"
AFTER="./after.sh.erb"

# Function to execute scripts
execute_script() {
    local script_path=$1
    echo "Executing $script_path"
    bash "$script_path"
    echo "Finished executing $script_path"
    echo "==================================="
}

# Execute the three scripts one by one
execute_script "$BEFORE"
execute_script "$SCRIPT"
execute_script "$AFTER"
