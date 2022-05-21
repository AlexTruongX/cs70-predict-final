from statistics import NormalDist
import scipy.stats as st
import numpy as np

"""
@author Alex Truong
Calculates predicted letter grade given midterm and final raw scores.
"""

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


def key_at_index(mydict, index_to_find):
  for index, key in enumerate(mydict.keys()):
    if index == index_to_find:
      return key
  return None  # the index doesn't exist

def calc_overall_sd(mt_raw, final_raw):

    def percentile_to_grade(percentile):
        # Percentiles pulled from Berkeley Time (historically accurate) - Fa'21 Semester
        grades_to_p = {'A+' : [0.95, 0.99], 'A' : [0.78, 0.95], 'A-' : [0.66, 0.78],
                    'B+' : [0.43, 0.66], 'B' : [0.26, 0.43], 'B-' : [0.16, 0.26],
                    'C+':[0.11, 0.16], 'C' : [0.07, 0.11], 'C-' : [0.04, 0.07],
                    'F' : [0.01, 0.04]}

        count = 0
        for index, grade in enumerate(grades_to_p):
            interval = grades_to_p[grade]
            if interval[0] == percentile or interval[1] == percentile:
                if grade == "A+":
                    print(f"Expected Grade: {grade}")
                    return    
                elif count > 0:
                    print(f"{grade}.")
                    return
                else:
                    print(f"You're on the border of a grade bin between {grade} and ", end="")
                    count += 1
            elif percentile > interval[0]: # above lower bound -> then in!
                if grade == "A+":
                    print(f"Expected Grade: {grade}")
                    return None
                else:
                    next_grade = key_at_index(grades_to_p, index - 1)
                    return [(grade, grades_to_p[grade]), (next_grade, grades_to_p[next_grade])]
    
    def reach_next_bin(curr_bin, next_bin):
        curr_grade = curr_bin[0]
        curr_interval = curr_bin[1]
        next_grade = next_bin[0]
        next_interval = next_bin[1]

        sim_final_raw = final_raw + 1
        sim_p = percentile
        

        while sim_p <= next_interval[0]:
            sim_final_z = final_zscore(sim_final_raw)
            clobber = avg_std(midterm_z, sim_final_z)
            sim_p = norm_dist.cdf(0.375 * max(midterm_z, clobber) + 0.5 * max(sim_final_z, clobber))
            sim_final_raw += 1
        
        pt_diff = abs(sim_final_raw - final_raw - 1)
        print(f"Your expected grade is a {curr_grade}. To get an {next_grade}, you needed to score {int(pt_diff)} more points on the final.")
        

    # Calculate z-scores (and relative changes)
    midterm_z = mt1_zscore(mt_raw)
    final_z = final_zscore(final_raw)
    clobber = avg_std(midterm_z, final_z)

    # Setup normal distribution
    overall_std = np.sqrt(0.375**2 + 0.5**2 + 2 * 0.8 * 0.375 * 0.5)
    norm_dist = NormalDist(mu=0, sigma=overall_std)
    percentile = norm_dist.cdf(0.375 * max(midterm_z, clobber) + 0.5 * max(final_z, clobber))

    # Overall z-score and grade calcualtion
    overall_z = norm_dist.inv_cdf(percentile)
    print(f"Your overall z-score is: {round(overall_z, 2)} ")
    curr_and_next = percentile_to_grade(round(percentile, 2))

    # Compute pts needed to hit next bin (unless in A+ bin)
    if curr_and_next is None:
        return
    else:
        reach_next_bin(curr_and_next[0], curr_and_next[1])

    
if __name__ == "__main__":
    # calling the main function
    mt_raw = float(input("Enter your midterm raw score: "))
    final_raw = float(input("Enter your final raw score: "))
    calc_overall_sd(mt_raw, final_raw)
