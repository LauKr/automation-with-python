import os
import shutil


def sort_files_in_a_folder(directory_path='/home/lau/Downloads/', create_new_dir=False):
    '''
    A function to sort the files in a download folder
    into their respective categories
    '''
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    file_type_variation_list = ['zip', 'iso', 'pdf']
    filetype_folder_dict = {'zip': directory_path+'zip_folder', 'iso': directory_path+'iso_folder',
                            'pdf': directory_path+'pdf_folder', 'png': directory_path+'png_folder', }
    if not files:
        print('No files. Skipped.')
        exit()
    for file in files:
        if create_new_dir:
            filetype = file.split('.')[-1]
            if filetype not in file_type_variation_list:
                file_type_variation_list.append(filetype)
                new_folder_name = directory_path + filetype + '_folder'
                filetype_folder_dict[str(filetype)] = str(new_folder_name)
                if os.path.isdir(new_folder_name):  # folder exists
                    continue
                else:
                    os.mkdir(new_folder_name)
        src_path = directory_path + file
        filetype = file.split('.')[-1]
        if filetype in filetype_folder_dict.keys():
            dest_path = filetype_folder_dict[str(filetype)]
            shutil.move(src_path, dest_path)
        else:
            dest_path = directory_path + 'misc/'
            shutil.move(src_path, dest_path)
        print(src_path + '>>>' + dest_path)
    return 0


if __name__ == "__main__":
    dir_path = '/home/lau/Downloads/'
    sort_files_in_a_folder(dir_path)
