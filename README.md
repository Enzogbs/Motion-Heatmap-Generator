# Motion-Heatmap-Generator
This project allows you to generate heatmaps from motion in videos. 
---

https://github.com/user-attachments/assets/0475b42d-bd2c-4331-9a35-917c808dc41b


https://github.com/user-attachments/assets/26474652-bd4a-4518-ae8f-2750b96711ce


## Installation

Install all the pre-needed requirements using:

```pip install -r requirements.txt```

---

## Usage

```bash
video_heatmap.py [-h] -f VIDEO_FILE [-a VIDEO_ALPHA] [-d] [-o VIDEO_OUTPUT] [-s VIDEO_SKIP] [-t TAKE_EVERY]

optional arguments:
  -h, --help            show this help message and exit
  -f VIDEO_FILE, --file VIDEO_FILE
                        Video file path for which heatman will be created. Example: input.mp4
  -a VIDEO_ALPHA, --alpha VIDEO_ALPHA
                        Optional parameter to adjust alpha between heatmap and original video frames.
                        Value between 0.0-1.0 represent what part of original video heatmap gonna take. 
                        Default: 0.9
  -d, --disable         Disable live view of heatmap generation.
  -o VIDEO_OUTPUT, --output VIDEO_OUTPUT
                        Adjust name of output files. Script creates two files one video .mp4 and one image .png.
                        Default: output
  -c {TURBO,JET,HOT,COOL,SPRING,WINTER,RAINBOW,OCEAN,BONE,PLAID,HSV,PARULA}, --colormap {TURBO,JET,HOT,COOL,SPRING,WINTER,RAINBOW,OCEAN,BONE,PLAID,HSV,PARULA}
  -s VIDEO_SKIP, --skip VIDEO_SKIP
                        Skip first number of frames in order to warm up background substraction alghoritm.
                        Default: 200 frames
  -t TAKE_EVERY, --take-every TAKE_EVERY
                        In order to speed up process it is possible to skip frames and take every x frame.
                        Default: 1 (take all frames).
```

Example usage:

```bash
python video_heatmap.py -f input.mp4 -o output_name -a 0.7 -c HOT
```
