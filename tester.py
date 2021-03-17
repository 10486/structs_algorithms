lab_num = int(input("enter number of lab:"))
exercise = int(input("enter number of exercise:"))
variant = 12
module = __import__(f"{lab_num}.{exercise}_{variant}", fromlist = [None])
module.main(f"{lab_num}/tests/{exercise}_{variant}.test")
