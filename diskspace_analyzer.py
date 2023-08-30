import argparse
import os

# Create an argument parser
parser = argparse.ArgumentParser(description='Analyze disk space usage.')

# Add arguments
parser.add_argument('directory', help='The directory to analyze')
parser.add_argument('--limit', type=int, default=10, help='Limit the number of results (default: 10)')

# Parse the arguments
args = parser.parse_args()

# Access the arguments
directory = args.directory
limit = args.limit

def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def analyze_disk_space(directory, limit):
    items = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            size = get_size(item_path)
            items.append((item, size))
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:limit]
def main():
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    results = analyze_disk_space(directory, limit)
    print(f"Top {limit} largest items in '{directory}':")
    for item, size in results:
        print(f"{item}: {size} bytes")

if __name__ == "__main__":
    main()

