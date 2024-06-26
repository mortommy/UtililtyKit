import datetime as dt
import os
import shutil
import zipfile


def move_file_to_zip_archive(file_name: str, sub_folder: str):
    """
    Move a file from the current working directory to a zip archive in a subfolder

    param: file_name the file name to move
    param: sub_folder the folder where the zip archive will be created
    """
    file_path = os.path.join(os.getcwd(), file_name)

    if os.path.exists(file_path):
        downloads_folder = os.path.join(os.getcwd(), sub_folder)
        if not os.path.exists(downloads_folder):
            os.makedirs(downloads_folder)

        current_date = dt.datetime.now().strftime("%Y-%m-%d")
        csv_file_name = os.path.basename(file_name)
        csv_file_name_with_date = f'{os.path.splitext(csv_file_name)[0]}_{current_date}.csv'
        csv_file_path = os.path.join(os.path.dirname(file_path), csv_file_name_with_date)
        os.rename(file_path, csv_file_path)

        zip_file_name = os.path.splitext(os.path.basename(file_name))[0] + '.zip'
        zip_file_path = os.path.join(downloads_folder, zip_file_name)

        if not os.path.exists(zip_file_path):
            with zipfile.ZipFile(zip_file_path, 'w') as zipf:
                pass

        with zipfile.ZipFile(zip_file_path, 'a') as zipf:
            zipf.write(csv_file_path, os.path.basename(csv_file_path))

        os.remove(csv_file_path)

    else:
        raise Exception('File ' + file_path + ' does not exist.')
