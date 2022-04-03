import argparse
import os 
import json
from pathlib import Path
import shutil

def get_image_ids(train_path, dev_path, test_path):
    path_list = [train_path, dev_path, test_path]
    ids = []
    for path in path_list:
        with open(path, 'r') as f:
            attr_dict = json.load(f)
            for k, _ in attr_dict.items():
                ids.append(k)
    return ids


def update_directory(data_path, ids, category):
    """
    Given an data path and image ids belong to one directory,
    create that directory and moves image corresponding to the ids to the created category directory.
    """
    dir_path = os.path.join(data_path, category)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    for id in ids:
        source = os.path.join(data_path, id+".png")
        destination = os.path.join(dir_path, id+".png")
        if os.path.isfile(source):
            shutil.move(source, destination)
        else:
            print(f"{source} does not exist!")
    print(f"moving {category} completed!")

def split_files(args):
    dress_train_path = os.path.join(args.data_split_path, "asin2attr.dress.train.json")
    dress_dev_path = os.path.join(args.data_split_path, "asin2attr.dress.val.json")
    dress_test_path = os.path.join(args.data_split_path, "asin2attr.dress.test.json")

    shirt_train_path = os.path.join(args.data_split_path, "asin2attr.shirt.train.json")
    shirt_dev_path = os.path.join(args.data_split_path, "asin2attr.shirt.val.json")
    shirt_test_path = os.path.join(args.data_split_path, "asin2attr.shirt.test.json")

    toptee_train_path = os.path.join(args.data_split_path, "asin2attr.toptee.train.json")
    toptee_dev_path = os.path.join(args.data_split_path, "asin2attr.toptee.val.json")
    toptee_test_path = os.path.join(args.data_split_path, "asin2attr.toptee.test.json")

    dress_ids = get_image_ids(dress_train_path, dress_dev_path, dress_test_path)
    shirt_ids = get_image_ids(shirt_train_path, shirt_dev_path, shirt_test_path)
    toptee_ids = get_image_ids(toptee_train_path, toptee_dev_path, toptee_test_path)

    update_directory(args.data_path, dress_ids, 'dress')
    update_directory(args.data_path, shirt_ids, 'shirt')
    update_directory(args.data_path, toptee_ids, 'toptee')
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, 
                        default='/home/deokhk/coursework/fashion-iq/transformer/resized_images/')
    parser.add_argument('--data_split_path', type=str, default='/home/deokhk/coursework/fashion-iq/data/')

    args = parser.parse_args()
    split_files(args)
