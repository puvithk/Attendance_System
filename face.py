import face_recognition as fr
import csv
import numpy as np

class Attendence:
    faceencode={}
    searchdic = {}
    my_dict = {}
    namelist = []


    def __init__(self):
        pass

    def encoding(self, img):
        my_face_encoding = fr.face_encodings(img)[0]
        return my_face_encoding

    def saveencode(self, encode, name):
        self.namelist.append(name)
        list_name=[]
        with open('/namer.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                for r in row :
                    list_name.append(r)
                print(row)
        key = len(list_name)
        self.faceencode[ f'{key}' ] = encode.tolist()  # convert numpy array to list
        print(key)


        with open('/namer.csv', "a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.namelist)
        with open('/data.csv', "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.searchdic = {k: np.array(eval(v)) for k, v in dict(row).items()}  # convert list to numpy array

        with open('/data.csv', "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.faceencode.keys())
            writer.writeheader()
            writer.writerow(self.faceencode)
        with open('/data.csv', "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.my_dict = dict(row)

        return True

    def checkattend(self, img):
        unknown_face_encoding = fr.face_encodings(img)[0]
        with open('/data.csv', "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row)
                searchdic = {k: np.array(eval(v)) for k, v in dict(row).items()}  # convert list to numpy array
            print(searchdic)
            for i in range(len(self.namelist)):
                result = fr.compare_faces([searchdic[f'{i+1}']], unknown_face_encoding)
                if result[0]:
                    with open('/namer.csv', 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            list_name = list(row)
                        try:
                            return list_name[ i ]
                        except:
                            return False
                else:
                    return False




model = Attendence()
a=input("Want to add user (Y/N)")
if(a=="Y" or a=="y"):
    print("Enter the file path :")
    img = fr.load_image_file("/img/base/OIP.jpeg")
    encode = model.encoding(img)
    key = False
    key = model.saveencode(encode=encode, name='elon')
a=input("do YOu want to check")
if(a=="Y"):
    img1 = fr.load_image_file("/img/elon/download.jpg")
    print(model.checkattend(img=img1))
