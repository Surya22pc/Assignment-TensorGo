# scripts/reconstruct_video.py
import cv2
import os

def reconstruct_video(frames_folder, output_video):
    frame_array = []
    files = sorted([f for f in os.listdir(frames_folder) if f.endswith('.jpg')])
    
    for i in range(len(files)):
        img = cv2.imread(os.path.join(frames_folder, files[i]))
        height, width, layers = img.shape
        size = (width, height)
        frame_array.append(img)

    out = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
    
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
    print(f"Video saved as {output_video}")

if __name__ == "__main__":
    reconstruct_video('../processed_frames', '../output_video/output_hd_video.mp4')
