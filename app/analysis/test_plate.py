from app.analysis.plate_detector import detect_plate

images = [

    "app/storage/uploads/image1.jpeg",
    "app/storage/uploads/image2.jpeg",
    "app/storage/uploads/image3.jpeg"

]

for image in images:

    number, valid = detect_plate(image)

    print("=" * 50)
    print(image)
    print("Vehicle Number:", number)
    print("Valid:", valid)