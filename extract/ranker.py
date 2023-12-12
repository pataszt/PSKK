import re

def parse_professor_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    professors = []
    for block in content.split('\n\n'):
        if block.strip():
            professor = {}
            lines = block.split('\n')
            professor['name'] = lines[0].split(': ')[1]
            professor['email'] = lines[1].split(': ')[1]
            professor['url'] = lines[2].split(': ')[1]
            professor['interests'] = lines[4:]
            professors.append(professor)
    return professors

def rank_professors(professors, student_interests):
    rankings = []
    for prof in professors:
        score = sum(interest in prof['interests'] for interest in student_interests)
        rankings.append((prof['name'], score))

    rankings.sort(key=lambda x: x[1], reverse=True)
    return rankings

def write_rankings_to_file(rankings, file_path):
    with open(file_path, 'w') as file:
        file.write("Professor Rankings based on your interests:\n")
        for rank, (name, score) in enumerate(rankings, start=1):
            file.write(f"{rank}. {name} - Score: {score}\n")


def main():
    file_path = 'combined_output.txt'  # Path to the text file containing professor data
    professors = parse_professor_data(file_path)

    student_interests = input("Enter your research interests (separated by commas): ").split(',')
    student_interests = [interest.strip() for interest in student_interests]

    rankings = rank_professors(professors, student_interests)

    output_file_path = 'rankings.txt'
    write_rankings_to_file(rankings, output_file_path)
    print(f"Rankings have been written to {output_file_path}")

if __name__ == "__main__":
    main()
