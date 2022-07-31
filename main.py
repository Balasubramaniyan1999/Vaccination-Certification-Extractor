import pdfplumber
import os


def conversion(path):
    extracted_data = 'extracted.txt'
    with pdfplumber.open(path) as pdf:
        first_page = pdf.pages[0]
        data = (first_page.extract_text())
        text_data = open(extracted_data, 'w',encoding="utf-8")
        text_data.writelines(data)

def extraction():
    file_name = "extracted.txt"

    try:

        file_read = open(file_name, "r", encoding="utf-8")
        Name_text = "Beneﬁciary Name"
        Age = "Age"
        Gender = "Gender"
        Vaccine_name = "Vaccine Name"


        lines = file_read.readlines()

        new_list = []
        count = 0

        # looping through each line in the file
        for line in lines:
            if Name_text in line:
                new_list.insert(count, line)
            elif Age in line:
                new_list.insert(count, line)
            elif Gender in line:
                new_list.insert(count, line)
            elif Vaccine_name in line:
                new_list.insert(count, line)
                count += 1
        file_read.close()

        if len(new_list) == 0:
            print("Text is not found")
        else:
            lineLen = len(new_list)
            for i in range(lineLen):
                print(end=new_list[i])
    except:
        print("\nThe file doesn't exist!")
    print(new_list)
def file_remover():
    os.remove('extracted.txt')

if __name__ == '__main__':
    path_way = input("Enter the path:")
    conversion(path=path_way)
    extraction()
    file_remover()




