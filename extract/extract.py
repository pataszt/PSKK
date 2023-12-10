import re
import glob

file_pattern = 'faculty*.txt'
output_file = 'output.txt'

with open(output_file, 'w') as output:
    for filename in glob.glob(file_pattern):
        with open(filename, 'r') as file:
            text = file.read()

            full_name_pattern = '^(.*)\n'
            full_name_match = re.search(full_name_pattern, text)

            interests_pattern = 'Research Interests\n(.*?)(?=\n\n|\Z)'
            interests_match = re.search(interests_pattern, text, re.DOTALL)

            output.write("\nProcessing file: " + filename + "\n")

            if full_name_match:
                full_name = full_name_match.group(1)
                output.write("Full Name: " + full_name + "\n")
            else:
                output.write("No full name found.\n")

            if interests_match:
                research_interests = interests_match.group(1).strip().split('\n')
                output.write("\nResearch Interests:\n")
                for interest in research_interests:
                    output.write(interest.strip() + "\n") 
            else:
                output.write("No research interests found.\n")

print("Extraction complete. Check " + output_file + " for the output.")
