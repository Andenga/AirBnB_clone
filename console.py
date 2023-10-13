#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            else:
                new_instance = classes[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """Show an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = class_name + "." + args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = class_name + "." + args[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if not arg:
            print([str(v) for v in storage.all().values()])
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            else:
                instances = [str(v) for k, v in storage.all().items() if k.split('.')[0] == class_name]
                print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = class_name + "." + args[1]
                if key not in storage.all():
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    instance = storage.all()[key]
                    attribute_name = args[2]
                    attribute_value = args[3]
                    setattr(instance, attribute_name, attribute_value)
                    instance.save()

    def do_count(self, arg):
        """Count the number of instances of a class"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in classes:
                print("** class doesn't exist **")
            else:
                instances = [v for k, v in storage.all().items() if k.split('.')[0] == class_name]
                print(len(instances)

    def do_<class>.show(self, arg):
        """Show an instance based on the class name and id"""
        if not arg:
            print(f"** {class_name} name missing **")
        else:
            args = arg.split()
            if len(args) < 1:
                print(f"** {class_name} id missing **")
            else:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + "." + instance_id
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print(f"** no {class_name} found **")

    def do_<class>.destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print(f"** {class_name} name missing **")
        else:
            args = arg.split()
            if len(args) < 1:
                print(f"** {class_name} id missing **")
            else:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + "." + instance_id
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print(f"** no {class_name} found **")

    def do_<class>.update(self, arg):
        """Updates an instance based on the class name and id with a dictionary"""
        if not arg:
            print(f"** {class_name} name missing **")
        else:
            args = arg.split()
            if len(args) < 1:
                print(f"** {class_name} id missing **")
            elif len(args) < 2:
                print(f"** dictionary missing **")
            else:
                class_name = args[0]
                instance_id = args[1]
                key = class_name + "." + instance_id
                if key not in storage.all():
                    print(f"** no {class_name} found **")
                else:
                    try:
                        # Parse the dictionary from the argument
                        data_dict = eval(args[2])
                        if not isinstance(data_dict, dict):
                            raise SyntaxError("Invalid dictionary")
                        instance = storage.all()[key]
                        for key, value in data_dict.items():
                            setattr(instance, key, value)
                        instance.save()
                    except Exception as e:
                        print(f"** {e} **")

if __name__ == "__main__":
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }
    HBNBCommand().cmdloop()
