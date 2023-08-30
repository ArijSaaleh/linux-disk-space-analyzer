# Linux Disk Space Analyzer

The Linux Disk Space Analyzer is a command-line utility written in Python that allows you to analyze and visualize disk space usage within a specified directory. With this tool, you can identify the largest directories and files that are consuming disk space, helping you to manage your data effectively.

## Features

- Analyze disk space usage for a specified directory.
- Display the top N largest items (directories and files) based on size.
- User-friendly output with human-readable sizes.

## Getting Started

1. Clone this repository:
   ```sh
   git clone https://github.com/ArijSaaleh/linux-disk-space-analyzer.git
2. Navigate to the project directory:
    ```sh
    cd linux-disk-space-analyzer
3. Run the script:

    ```sh

    python diskspace_analyzer.py /path/to/directory --limit N

Replace /path/to/directory with the directory you want to analyze and N with the number of largest items to display.

## Usage 

    ```sh
    usage: diskspace_analyzer.py [-h] [--limit LIMIT] directory

    Analyze disk space usage.

    positional arguments:
    directory        The directory to analyze

    optional arguments:
    -h, --help       show this help message and exit
    --limit LIMIT    Limit the number of results (default: 10)