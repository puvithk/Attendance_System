import face_recognition as fr
import csv
import numpy as np
import os

class Attendence:
    faceencode = []
    searchdic = []
    my_dict = []
    namelist = []

    def __init__(self):
        pass

    def encoding(self, img):
        my_face_encoding = fr.face_encodings(img)[0]
        return my_face_encoding

    def saveencode(self, encode, name):
        self.namelist.append(name)
        key = len(self.namelist) - 1
        self.faceencode.append(encode.tolist())  # convert numpy array to list

        # Write names to CSV file
        with open('/namer.csv', "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.namelist)

        # Write encodings to CSV file
        with open('/data.csv', "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for encoding in self.faceencode:
                writer.writerow(encoding)

        return True

    def checkattend(self, img):
        unknown_face_encoding = fr.face_encodings(img)[ 0 ]

        # Load names from CSV file
        with open('/namer.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                self.namelist = list(row)

        # Load encodings from CSV file
        with open('/data.csv', "r") as csvfile:
            reader = csv.reader(csvfile)
            self.faceencode = [ np.array(eval(','.join(row))) for row in reader ]  # join the row elements before converting to a numpy array

        # Compare faces
        for i in range(len(self.namelist)):
            result = fr.compare_faces([ self.faceencode[ i ]] , unknown_face_encoding)
            if result[ 0 ]:
                return self.namelist[ i ]

        return False

if '__name__' == '__main__':
    model = Attendence()

    a = input("Want to add user (Y/N)")
    if a.lower() == "y":
        print("Enter the file path :")
        img = fr.load_image_file("/img/base/OIP jeff.jpeg")
        encode = model.encoding(img)
        key = model.saveencode(encode=encode, name='jeff')

    a = input("do You want to check")
    if a.lower() == "y":
        img1 = fr.load_image_file("/img/elon/download.jpg")
        print(model.checkattend(img=img1))
