#!/usr/bin/env python3
import sys
import os

def pad(n):
    return f"{int(n):02d}"

def main():
    if len(sys.argv) != 2:
        print("Usage: generate_day.py DAY_NUMBER")
        sys.exit(1)
    day = pad(sys.argv[1])
    base_dir = os.path.dirname(os.path.abspath(__file__))
    day_dir = os.path.join(base_dir, f"Day{day}")
    if os.path.exists(day_dir):
        print(f"Day {day} already exists.")
        sys.exit(1)
    os.makedirs(day_dir)
    template_path = os.path.join(base_dir, "template.md")
    with open(template_path) as t:
        content = t.read().replace("DD", day)
    with open(os.path.join(day_dir, "README.md"), "w") as out:
        out.write(content)
    print(f"Created {day_dir}/README.md")

if __name__ == "__main__":
    main()
