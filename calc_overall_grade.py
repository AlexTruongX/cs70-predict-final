from statistics import NormalDist
import scipy.stats as st
import numpy as np

# From https://www.reddit.com/r/berkeley/comments/kbvxd2/calculating_your_grade_in_cs70_and_other_curved/

def grade(percentile):
    if 0.95 <= percentile <= 100:
        return 'A+'
    elif 0.78 <= percentile <= 0.95:
        return 'A'
    elif 0.66 <= percentile <= 0.78:
        return 'A-'
    elif 0.43 <= percentile <= 0.66:
        return 'B+'
    elif 0.26 <= percentile <= 0.43:
        return 'B'
    elif 0.16 <= percentile <= 0.26:
        return 'B-'
    elif 0.11 <= percentile <= 0.16:
        return 'C+'
    elif 0.07 <= percentile <= 0.11:
        return 'C'
    elif 0.04 <= percentile <= 0.07:
        return 'C-'
    else:
        return 'F'

def mt1_zscore(raw_score):
    # Updated 4/5/22
    mean = 132.72
    std = 39.01
    return (raw_score - mean)/std

def final_zscore(raw_score):
    # Updated 5/16/22
    mean = 139.56
    std = 51.47
    return (raw_score - mean)/std

def avg_std(score1, score2):
    return (score1 + score2)/2

def percentile_to_grade(percentile):
    # Percentiles pulled from Berkeley Time (historically accurate)
    grades_to_p = {'A+' : [0.95, 0.99], 'A' : [0.78, 0.95], 'A-' : [0.66, 0.78],
                'B+' : [0.43, 0.66], 'B' : [0.26, 0.43], 'B-' : [0.16, 0.26],
                'C+':[0.11, 0.16], 'C' : [0.07, 0.11], 'C-' : [0.04, 0.07],
                'F' : [0.01, 0.04]}
    
    count = 0
    for grade in grades_to_p:
        interval = grades_to_p[grade]
        if interval[0] == percentile or interval[1] == percentile:
            if count > 0:
                print(f"{grade}.")
                return
            print(f"You're on the border of a grade bin between {grade} and ", end="")
            count += 1
        elif percentile > interval[0]:
            print(f"Expected Grade: {grade}")
            return

def calc_overall_sd(mt_raw, final_raw):
    midterm_z = mt1_zscore(mt_raw)
    final_z = final_zscore(final_raw)
    clobber = avg_std(midterm_z, final_z)
    overall_std = np.sqrt(0.375**2 + 0.5**2 + 2 * 0.8 * 0.375 * 0.5)
    percentile = NormalDist(mu=0, sigma=overall_std).cdf(0.375 * max(midterm_z, clobber) + 0.5 * max(final_z, clobber))
    overall_z = NormalDist(mu=0, sigma=overall_std).inv_cdf(percentile)
    # print(f"Midterm z-score: { {clobber} if (midterm_z < clobber) else midterm_z } and a final z-score of { {clobber} "(CLOBBERED)" if (final_z < clobber) else midterm_z }}")
    print(f"Your overall z-score is: {round(overall_z, 2)} ")
    percentile_to_grade(round(percentile, 2))

if __name__ == "__main__":
    # calling the main function
    mt_raw = float(input("Enter your midterm raw score: "))
    final_raw = float(input("Enter your final raw score: "))
    calc_overall_sd(mt_raw, final_raw)
