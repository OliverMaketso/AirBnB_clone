#!/usr/bin/python3
import json

class FileStorage:
    """
    A class to handle serialization and deserialization of objects to and from a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file where objects are stored.
        __objects (dict): Dictionary to store objectsby <class name>.id.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all objects stored in the FileStorage.

        Returns:
            dict: A dictionary containing all objects stored in the FileStorage.
            """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the FileStorage.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes objects stored in the FileStorage to a JSON file.
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """
        deserializes the JSON file to objects stored in the FileStorage.
        If the JSON file doesn't exist, no action is taken.
        """

        try:
            with open(self.__file_path, 'r') as file:
                self.__objects = json.load(file)
        except FileNotFoundError:
            pass

