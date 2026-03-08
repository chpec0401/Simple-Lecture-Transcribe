# Simple Video Transcibe Example
This is a simple script to demonstrate a setup using openai-whisper to transcribe contents of a .mp4 to a txt transcript. It should be simple enough to use as is. But note that there are several dependencies. Assuming you have pip and a python package management system (conda):
`conda create -n whisper_env python=3.11 -y
conda activate whisper_env`
1. Torch
[Official Website](pytorch.org)
2. openai-whisper
`pip install -U openai-whisper`
3. ffmpeg
`conda install -c conda-forge ffmpeg -y`
4.If you are using an nvidia gpu, Cuda also speeds the model up by alot, you can download CUDA toolkit from the nvidia website. Also make sure that your torch version aligns with your CUDA version. 
#Usage
Make sure the script and the videos you wish to transcribe are put into the same folder named "transcribe". Running the script by for example:
`conda activate whisper_env
python transcribe.py
`
This will result in all videos that have not been previously transcribed, determined by the existence of transcript in the same name in the "transripts" folder, to be transcribed by the "turbo" model of whisper. If you want to change the model, simply change turbo to something else.



