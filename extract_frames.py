# scripts/extract_frames.py
import cv2
import os

def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(f"{output_folder}/frame_{count:04d}.jpg", image)
        success, image = vidcap.read()
        count += 1
    print(f"Extracted {count} frames.")

if __name__ == "__main__":
    extract_frames('../input_video/input_sd_video.mp4', '../extracted_frames')
