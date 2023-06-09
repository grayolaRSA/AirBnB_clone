#!/usr/bin/python3
"""module to run The console"""
import cmd
import json
import models
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """The HBNB class with command line"""

    prompt = 'hbnb '

    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City",
                              "Amenity", "Place", "Review"]:
            print("***class doesn't exist ***")
            return
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City",
                              "Amenity", "Place", "Review"]:
            print("***class doesn't exist ***")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key_cmd = class_name + '.' + obj_id
        if key_cmd not in models.storage.all():
            print("**no instance found **")
        else:
            print(models.storage.all()[key_cmd])

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City",
                              "Amenity", "Place", "Review"]:
            print("***class doesn't exist ***")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key_cmd = class_name + '.' + obj_id
        if key_cmd not in models.storage.all():
            print("**no instance found **")
            return
        else:
            del models.storage.all()[key_cmd]
            models.storage.save()

    def do_all(self, line):
        if not line:
            print("** Class name missing **")
        args = line.split()
        class_name = args[0]
        if class_name not in ["BaseModel", "User", "State", "City",
                              "Amenity", "Place", "Review"]:
            print("***class doesn't exist ***")
        else:
            all_obj = storage.all()
            for obj_id, obj in all_obj.items():
                print(obj)

    def do_update(self, line):
        if not line:
            print("** Class name missing **")
        else:
            args = line.split()
            class_name = args[0]
            if class_name not in ["BaseModel", "User", "State", "City",
                                  "Amenity", "Place", "Review"]:
                print("***class doesn't exist ***")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                obj_id = args[1]
                key_cmd = class_name + '.' + obj_id
                if key_cmd not in models.storage.all():
                    print("**no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("**value missing **")
                else:
                    obj = models.storage.all()[key_cmd]
                    attr_name = args[2]
                    attr_val = args[3]
                    setattr(obj, attr_name, attr_val)
                    obj.save()

    def do_quit(self, args):
        return True

    def do_EOF(self, args):
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
