# Project 1: Basic School Administration tool
import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer =csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "E-Mail ID"])

        writer.writerow(info_list)

if __name__ =='__main__':
    condition = True
    student_num = 1
    while(condition):
        student_info = input("Enter student information for student #{} in the following format(Name Age Contact_no Email_id) : ".format(student_num))

        #split
        student_info_list = student_info.split(' ')

        print("\nThe Entered Information is: \nName: {} \nAge: {}\nContact_no: {}\nEmail_id: {}\n"
              .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice = input("Is the entered information correct? (yes/no): ")

        if choice == "yes":
            write_into_csv(student_info_list)
            cond_check= input("Enter (yes/no) if you want to enter another student info: ")
            if cond_check == "yes":
                condition = True
                student_num = student_num + 1
            elif cond_check == "no":
                condition = False
        elif choice == "no":
            print("\nPlease re-enter the values!")