import subprocess
import timeit

# Define the command to run the dictionary program
command = [
    'python',
    'dictionary_file_based.py',
    'trie',  # approach
    'sampleData.txt',  # data filename
    'test1.in',  # command filename
    'test1.out',  # output filename
]

# Function to execute the dictionary program and measure time
def run_dictionary_program():
    try:
        # Measure the execution time of the subprocess
        execution_time = timeit.timeit(
            lambda: subprocess.run(command, check=True),
            number = 1
        )
        print(f"Execution time: {execution_time} seconds")
    except subprocess.CalledProcessError as e:
        print("Error running the dictionary program:", e)

if __name__ == '__main__':
    run_dictionary_program()
