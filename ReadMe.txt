# Face Recognition and Attendance System

This Python script uses the `face_recognition` library to recognize faces in images and keep track of attendance. The script defines a class `Attendence` with methods for encoding faces, saving encodings and names to CSV files, and checking attendance by comparing an unknown face encoding to the saved encodings.

## Dependencies

The script uses the following libraries:
- `face_recognition` for face detection and recognition
- `csv` for reading and writing CSV files
- `numpy` for numerical operations
- `os` for interacting with the operating system

## How it Works

1. The `encoding` method takes an image as input, detects the face in the image, and returns the face encoding.
2. The `saveencode` method takes a face encoding and a name as input, appends them to the respective lists, and saves the lists to CSV files.
3. The `checkattend` method takes an image as input, detects the face in the image, encodes the face, and compares the encoding to the saved encodings. If there's a match, it returns the corresponding name; otherwise, it returns `False`.

## Usage

To use the script, create an instance of the `Attendence` class and call its methods as needed. For example, to add a user, load an image file, encode the face in the image, and save the encoding and name. To check attendance, load an image file and call the `checkattend` method with the image as input.

Please note that this script is intended for educational purposes and may not be suitable for real-world attendance systems without further tuning and optimization. It's also important to note that the accuracy of the face recognition depends on the quality of the images and the performance of the `face_recognition` library.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).