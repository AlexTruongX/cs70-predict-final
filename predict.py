import predict_70_final as pt
import predict_with_corr as cr
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
    parser.add_argument("-a", "--all", action = "store_true",
                            help = "Displays all possible grades")
    parser.add_argument("-c", "--corr", action = "store_true",
            help = "Use the correlation based prediction (more accurate) Note: you must use the -a flag with this option. Use of -s and -g are experimental and may be inaccurate.")

    args = parser.parse_args()
    predictor = cr if args.corr else pt
    process = cr.mt1_zscore if args.corr else lambda x: x
    if args.grade != None:
        print()
        predictor.predict_final_std_range(args.grade[0], process(args.mt_score[0]))
    elif args.std != None:
        print()
        predictor.predict_final_std_exact(args.std[0], process(args.mt_score[0]))
    elif args.all:
        print()
        predictor.predict_final_std_all(process(args.mt_score[0]))
    else:
        print("You're actually clowning rn, choose -g or -s.")

if __name__ == "__main__":
    # calling the main function
    main()


