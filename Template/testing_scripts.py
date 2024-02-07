import subprocess

# Path to the script files
script_sh_path = "/Users/rohanbanerjee/ICER/template/script.sh.erb"
before_sh_path = "/Users/rohanbanerjee/ICER/template/before.sh.erb"
after_sh_path = "/Users/rohanbanerjee/ICER/template/after.sh.erb"

# Function to execute the shell scripts
def execute_shell_script(script_path):
    try:
        # Read the content of the script file
        with open(script_path, 'r') as file:
            script_content = file.read()

        # Execute the script content using subprocess
        process = subprocess.Popen(['bash', '-c', script_content], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        # Print the output and errors
        print("Output:")
        print(stdout.decode())
        print("Errors:")
        print(stderr.decode())

    except FileNotFoundError:
        print(f"Script not found at {script_path}")

# Execute each script
print("Executing script.sh.erb...")
execute_shell_script(script_sh_path)

print("\nExecuting before.sh.erb...")
execute_shell_script(before_sh_path)

print("\nExecuting after.sh.erb...")
execute_shell_script(after_sh_path)
