import argparse


def get_args():
    gendiff = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    gendiff.add_argument('first_file')
    gendiff.add_argument('second_file')

    args = gendiff.parse_args()
    return args
