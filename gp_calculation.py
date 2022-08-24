import data


def semester_total(semester1_grades: dict, total_score: int, total_credits: int):
    for each_sub in semester1_grades.values():
        sub_total = each_sub["cd"] * data.gp[each_sub["grade"]]
        total_credits = total_credits + each_sub["cd"]
        total_score = total_score + sub_total

    return total_score, total_credits


def cgpa(total: int, credit: int):
    final_cgpa = total / credit
    return final_cgpa
