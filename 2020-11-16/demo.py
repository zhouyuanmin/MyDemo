"""
argparse的用法
"""
import oj
if __name__ == '__main__':
    import argparse
    import base64
    parser = argparse.ArgumentParser(description='wordCloud oj for python')
    parser.add_argument('--answer', help='give the answer of wordCloud', default="{'ddcmaker':'1'}")
    parser.add_argument('--data', help='give the user code', default='')
    parser.add_argument('--match', default=0.9)
    parser.add_argument('--debug', default="False")
    args = parser.parse_args()
    answer = eval(base64.b64decode(base64.b64decode(base64.b64encode(args.answer.encode()))))
    match = float(args.match)
    debug = args.debug
    data = base64.b64encode(args.data.encode())
    o0 = oj.OJ(answer, data, match, debug)
    dd = o0.evaluating()
    print(dd)