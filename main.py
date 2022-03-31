from mlforkids import MLforKidsImageProject
import glob
import shutil
import os

# treat this key like a password and keep it secret!
key = "eb03c1c0-ae88-11ec-9154-550abd8452cd77d36526-a99e-44f1-b49d-026f46f4e44e"

# this will train your model and might take a little while
myproject = MLforKidsImageProject(key)
myproject.load_exisiting_model()
for f in glob.glob("./Pictures/output_rad/*.jpg"):
    os.remove(f)
for f in glob.glob("./Pictures/output_fuss/*.jpg"):
    os.remove(f)
for f in glob.glob("./Pictures/output_auto/*.jpg"):
    os.remove(f)

for img_path in glob.glob("./Pictures/input/*.jpg"):
    img_name = img_path.replace("./Pictures/input\\", "")
    print(img_name)
    demo = myproject.prediction(img_path)

    label = demo["class_name"]
    confidence = demo["confidence"]
    confidence_file = str(int(confidence))


    # CHANGE THIS to do something different with the result
    print("result: '%s' with %d%% confidence" % (label, confidence))
    if label == "Fusganger":
        shutil.copyfile(img_path, "./Pictures/output_fuss/" + confidence_file + "%_" + img_name)
    elif label == "Fahrrad":
        shutil.copyfile(img_path, "./Pictures/output_rad/" + confidence_file + "%_" + img_name)
    else:
        shutil.copyfile(img_path, "./Pictures/output_auto/" + confidence_file + "%_" + img_name)