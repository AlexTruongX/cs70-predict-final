import predict_70_final as pt
import argparse

def main():
    parser = argparse.ArgumentParser(description = "Predicts final score while factoring in 50% two-way clobber policy for CS70")

    parser.add_argument("mt_score", nargs = 1, metavar = "score", type = float,
                         help = "Your midterm score")

    parser.add_argument("-g", "--grade", type = str, nargs = 1,
                            metavar = "desired grade", default = None,
                            help = "Predicts the specified grade")
    parser.add_argument("-s", "--std", type = float, nargs = 1,
                            metavar = "desired std", default = None,
                            help = "Predicts the specified standard deviation")

    args = parser.parse_args()
    if args.grade != None:
        print()
        pt.predict_final_std_range(args.grade[0], args.mt_score[0])
    elif args.std != None:
        print()
        pt.predict_final_std_exact(args.std[0], args.mt_score[0])
    else:
        print()
        print("You're actually clowning rn, choose -g or -s.")

if __name__ == "__main__":
    # calling the main function
    main()


