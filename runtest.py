import argparse

parser = argparse.ArgumentParser(description='Do matrix calculations.')
parser.add_argument('action', choices=list(single_arg.keys())+list(multi_arg.keys()))
parser.add_argument('matrix', help="the matrix to do the operation on", nargs="+")

args = parser.parse_args()



