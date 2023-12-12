import re
import glob

file_pattern = 'faculty*.txt'
output_file = 'combined_output.txt'

with open(output_file, 'a') as output:
    for filename in glob.glob(file_pattern):
        with open(filename, 'r') as file:
            text = file.read()

            full_name_pattern = '^(.*)\n'
            full_name_match = re.search(full_name_pattern, text)

            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            email_match = re.search(email_pattern, text)

            url_pattern = r'https?://[^\s]+'
            url_match = re.search(url_pattern, text)

            interests_pattern = 'Research Interests\n(.*?)(?=\n\n|\Z)'
            interests_match = re.search(interests_pattern, text, re.DOTALL)

            if full_name_match:
                full_name = full_name_match.group(1)
                output.write("Name: " + full_name + "\n")
            else:
                output.write("Name: Not found\n")

            if email_match:
                email = email_match.group(0)
                output.write("Email: " + email + "\n")
            else:
                output.write("Email: Not found\n")

            if url_match:
                url = url_match.group(0)
                output.write("URL: " + url + "\n")
            else:
                output.write("URL: Not found\n")

            if interests_match:
                research_interests = interests_match.group(1).strip().split('\n')
                output.write("Research Interests:\n")
                for interest in research_interests:
                    output.write(interest.strip() + "\n")
            else:
                output.write("Research Interests: Not found\n")

            output.write("\n") #Adds newline as separator

print("Extraction complete. Check " + output_file + " for the combined output.")
