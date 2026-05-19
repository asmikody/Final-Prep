'''with open("student.txt", 'r') as f:
    score = []
    sum1 = 0
    
    for line in f:
        word = line.split()
        num = [int(i) for i in word if i.isdigit()]  # Handling numbers correctly
        score.extend(num)  # Append numbers directly instead of lists
        print("Extracted numbers:", num)

    for i in score:
        sum1 += i  # Summing individual numbers correctly
        print("Current sum:", sum1)
    
    avg = sum1 / len(score) if score else 0  # Avoid division by zero
    print("Average:", avg)'''


def calculate_average(filename):
    total_score = 0
    student_count = 0
    
    try:
        with open("student.txt", 'r') as f:
            for line in f:
                data = line.strip().split(',')
                
                # Ensure correct formatting (should contain exactly 2 values)
                if len(data) == 1 and data.isdigit() or data.isalpha():

                    print(f"Skipping malformed line: {line.strip()}")
                    continue
                
                name, score = data
                
                # Validate score (must be numeric)
                try:
                    score = float(score)
                    total_score += score
                    student_count += 1
                except ValueError:
                    print(f"Skipping invalid score for {name}: {score}")

        # Calculate and print average score
        if student_count > 0:
            avg_score = total_score / student_count
            print(f"Average Score: {avg_score:.2f}")
        else:
            print("No valid scores found.")

    except FileNotFoundError:
        print(f"Error: {filename} not found.")

# Example Usage
calculate_average("student.txt")
