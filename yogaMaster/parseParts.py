import argparse
import glob
import json
import os
from blog.poseParts import Pose, Part, PoseSequence


def main():
    parser = argparse.ArgumentParser(description='Pose Trainer Parser')
    parser.add_argument('--input_folder', type=str, default='poses_compressed', help='input folder for json files')
    parser.add_argument('--output_folder', type=str, default='poses_npy', help='output folder for npy files')

    args = parser.parse_args()

    image_paths = glob.glob(os.path.join(args.input_folder, '*.json'))
    image_paths = sorted(image_paths)
    # print(image_paths)

    # Get all the json sequences for each video
    for image_path in image_paths:
        all_keypoints=parse_sequence(image_path, args.output_folder)
        return PoseSequence(all_keypoints)


def parse_sequence(json_folder):
    """extract body parts from a json file
       and return a poseSequence for evaluation

       json_folder means a specified json file
    """

    json_files=json_folder

    with open(json_files) as f:
        json_obj = json.load(f)
        keypoints_json = json_obj['person_info'][0]['body_parts']
        return PoseSequence(keypoints_json)


if __name__ == '__main__':
    main()
