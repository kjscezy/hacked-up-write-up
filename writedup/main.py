import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file',
                    help='Path of the docx file.')

def main():
    args = parser.parse_args()
    file_path = os.path.abspath(args.file)
    assert os.path.exists(os.path.abspath(file_path)), "file doesn't exist"


if __name__ == '__main__':
    main()
