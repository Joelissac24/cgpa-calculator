import data
import gp_calculation as gc


def main():
    total = 0
    credit = 0
    reg_no = int(input("Enter your Registor Number  : "))

    for key, semester in data.cs_data.items():
        print(f"-----Enter your {key} grades-----")
        for sub in semester.keys():
            grades = input(sub + "  ").upper()
            semester[sub]["grade"] = grades
        total, credit = gc.semester_total(semester, total, credit)
    result = gc.cgpa(total, credit)

    print(f">>>>Your CGPA for {reg_no} is {result}<<<<<")


if __name__ == "__main__":
    main()
