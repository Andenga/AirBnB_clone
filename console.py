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
            valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
            if class_name not in valid_classes:
                print("** class doesn't exist **")
            else:
                new_instance = eval(class_name)()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """Show an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if len(args) < 2:
                print("** instance id missing **")
            else:
                class_name = args[0]
                valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
                if class_name not in valid_classes:
                    print("** class doesn't exist **")
                else:
                    key = f"{class_name}.{args[1]}"
                    all_instances = storage.all()
                    if key in all_instances:
                        print(all_instances[key])
                    else:
                        print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if len(args) < 2:
                print("** instance id missing **")
            else:
                class_name = args[0]
                valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
                if class_name not in valid_classes:
                    print("** class doesn't exist **")
                else:
                    key = f"{class_name}.{args[1]}"
                    all_instances = storage.all()
                    if key in all_instances:
                        del all_instances[key]
                        storage.save()
                    else:
                        print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        if not arg:
            print([str(v) for k, v in storage.all().items() if k.split('.')[0] in valid_classes])
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in valid_classes:
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
            if len(args) < 2:
                print("** instance id missing **")
            else:
                class_name = args[0]
                valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
                if class_name not in valid_classes:
                    print("** class doesn't exist **")
                else:
                    key = f"{class_name}.{args[1]}"
                    all_instances = storage.all()
                    if key not in all_instances:
                        print("** no instance found **")
                    elif len(args) < 3:
                        print("** attribute name missing **")
                    elif len(args) < 4:
                        print("** value missing **")
                    else:
                        instance = all_instances[key]
                        attribute_name = args[2]
                        attribute_value = args[3]
                        try:
                            setattr(instance, attribute_name, eval(attribute_value))
                            instance.save()
                        except Exception:
                            print("Invalid attribute value")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
