import os
from wand.image import Image

def convert_img_files(directory, input_ext, output_ext):
    # 지정된 디렉터리 내의 모든 파일을 확인
    for filename in os.listdir(directory):
        if filename.lower().endswith(input_ext):
            # 원본 파일의 전체 경로
            input_path = os.path.join(directory, filename)
            # 변환된 파일의 전체 경로
            output_filename = filename[:-len(input_ext)] + output_ext
            output_path = os.path.join(directory, output_filename)

            # 원본 파일의 확장자를 원하는 확장자로 변환
            with Image(filename=input_path) as img:
                img.format = output_ext.replace('.', '')  # 점을 제거
                img.save(filename=output_path)
                print(f'Converted {input_path} to {output_path}')

# 변환할 디렉터리 지정
directory_path = 'C:\\work-python\\Photos'
input_ext = '.heic'
output_ext = '.png'  # 여기서 점을 포함하지 않고 'png'라고 해도 됩니다.
convert_img_files(directory_path, input_ext, output_ext)