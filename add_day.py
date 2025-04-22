import os
import sys

def create_new_day(day_number):
    folder = f"Day{day_number:02d}"
    if os.path.exists(folder):
        print(f"{folder} already exists.")
        return
    
    os.makedirs(folder)
    
    with open("template.md", "r") as template_file:
        content = template_file.read().replace("Day XX", f"Day{day_number:02d}")
    
    with open(os.path.join(folder, "README.md"), "w") as new_file:
        new_file.write(content)
    
    print(f"✅ Created {folder}/README.md")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_day.py <day_number>")
    else:
        try:
            day_num = int(sys.argv[1])
            create_new_day(day_num)
        except ValueError:
            print("Please provide a valid number.")
