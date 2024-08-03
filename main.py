# scripts/main.py
import os
from extract_frames import extract_frames
from process_frames import process_frames
from reconstruct_video import reconstruct_video

def main():
    input_video_path = '../input_video/input_sd_video.mp4'
    extracted_frames_folder = '../extracted_frames'
    processed_frames_folder = '../processed_frames'
    output_video_path = '../output_video/output_hd_video.mp4'

    print("Extracting frames...")
    extract_frames(input_video_path, extracted_frames_folder)

    print("Processing frames...")
    process_frames(extracted_frames_folder, processed_frames_folder, 'super_resolution_model', 'inpainting_model')

    print("Reconstructing video...")
    reconstruct_video(processed_frames_folder, output_video_path)

    print("All steps completed successfully.")

if __name__ == "__main__":
    main()
