import os
import platform
import csv
import glob
import datetime



def creation_date(path_to_file):
    stat = os.stat(path_to_file)
    try:
        return stat.st_birthtime

    except AttributeError as e:
        print('Error in getting creation date')
        print("Error: " + str(e))




def write_to_csv(csv_line):
    try:
        with open('files-and-meta-deta' + '.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(csv_line)

    except Exception as e:
        print('Error in generating csv')
        print("Error: " + str(e))


def get_all_files(directory):
    try:
        filesAndDirs = glob.glob(directory+'/**', recursive=True)
        onlyfiles=[]
        for f in filesAndDirs:
            if os.path.isfile(f):
                onlyfiles.append(f)
        return onlyfiles

    except Exception as e:
        print('Error in listing all files in a directory')
        print("Error: " + str(e))





def main():
    try:
        directory='~/Documents'
        onlyfiles=get_all_files(directory)
        for f in onlyfiles:
            c_date=creation_date(f)
            # csv_line=f+','+datetime.datetime.utcfromtimestamp(c_date).strftime("%m/%d/%Y %H:%M:%S")
            csv_line=f+','+str(datetime.datetime.utcfromtimestamp(c_date))
            print(csv_line)
            write_to_csv(csv_line)

    except Exception as e:
        print("Error: " + str(e))





if __name__ == '__main__':
    main()