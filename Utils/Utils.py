import numbers
import os
import datetime


class Utils:

    @classmethod
    def is_number(cls, value):
        '''
        Determines if value is number

        :param value: value for checking
        :return: boolean value of checking and number or value otherwise
        '''

        if isinstance(value, numbers.Number):
            return True, value
        else:
            try:
                int_cast = int(value, 0)
                return True, int_cast
            except:
                try:
                    float_cast = float(value)
                    return True, float_cast
                except:
                    return False, value

    @classmethod
    def is_bool(cls, value):
        '''
        Determines if value is bool

        :param value: value for checking
        :return: boolean value of checking and result or value otherwise
        '''

        if value in ["True", "False", True, False, 0, 1]:
            if isinstance(value, str):
                return True, value=="True"
            if isinstance(value,bool):
                return True,value
            return True, value==1
        else:
            return False, value

    @staticmethod
    def get_project_root_path():
        '''
        Get path of project root folder

        :return: path of project root folder
        '''

        return os.path.dirname(os.path.dirname(__file__))

    @staticmethod
    def is_file_exists(file_path):
        '''
        Check if file with path exists

        :param file_path: file path for checking
        :return: boolean value of existing file
        '''

        return os.path.exists(file_path)

    @staticmethod
    def get_file_name(path):
        '''
        Return only file name without extension

        :param path: file path
        :return: name file only
        '''
        return os.path.basename(path).split('.')[0]

    @staticmethod
    def get_current_date_with_format():
        '''
        :return: current date with format
        '''
        return datetime.datetime.today().strftime('%d-%m-%Y %H-%M-%S-%f')

    @staticmethod
    def create_folder_if_not_exists(folder_path):
        '''
        Create folder by path if it not exists
        '''
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        except:
            pass


    @staticmethod
    def is_int(value):
        '''
        Check if value is int by comparing value and value than cast to int

        :param value: value for checking
        :return: boolean value of checking
        '''
        return value == int(value)

    @staticmethod
    def remove_file_if_exists(path):
        try:
            if os.path.exists(path):
                os.remove(path)
        except:
            pass

    @staticmethod
    def get_abs_path_with_project_root_path(path):
        '''
        Get path of project root folder

        :return: path of project root folder
        '''
        print(path)
        print(os.path.join(os.path.dirname(os.path.dirname(__file__)), path))

        return os.path.join(os.path.dirname(os.path.dirname(__file__)), path)
