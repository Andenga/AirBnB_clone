#!/usr/bin/python3
"""Defines the Custom Console for Holberton BnB."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse_arguments(argument_string):
    curly_braces = re.search(r"\{(.*?)\}", argument_string)
    brackets = re.search(r"\[(.*?)\]", argument_string)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(argument_string)]
        else:
            lexer = split(argument_string[:brackets.span()[0]])
            result_list = [i.strip(",") for i in lexer]
            result_list.append(brackets.group())
            return result_list
    else:
        lexer = split(argument_string[:curly_braces.span()[0]])
        result_list = [i.strip(",") for i in lexer]
        result_list.append(curly_braces.group())
        return result_list


class CustomConsole(cmd.Cmd):
    """Custom console for the Holberton BnB project.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def default(self, argument):
        """Default behavior for cmd module when input is invalid."""
        argument_dict = {
            "all": self.do_show_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", argument)
        if match is not None:
            argument_list = [argument[:match.span()[0]], argument[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argument_list[1])
            if match is not None:
                command = [argument_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argument_dict.keys():
                    call = "{} {}".format(argument_list[0], command[1])
                    return argument_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(argument))
        return False

    def do_quit(self, argument):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, argument):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, argument):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argument_list = parse_arguments(argument)
        if len(argument_list) == 0:
            print("** class name missing **")
        elif argument_list[0] not in CustomConsole.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(argument_list[0])()
            print(new_instance.id)
            storage.save()

    def do_show(self, argument):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argument_list = parse_arguments(argument)
        obj_dict = storage.all()
        if len(argument_list) == 0:
            print("** class name missing **")
        elif argument_list[0] not in CustomConsole.__classes:
            print("** class doesn't exist **")
        elif len(argument_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument_list[0], argument_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(argument_list[0], argument_list[1])])

    def do_destroy(self, argument):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argument_list = parse_arguments(argument)
        obj_dict = storage.all()
        if len(argument_list) == 0:
            print("** class name missing **")
        elif argument_list[0] not in CustomConsole.__classes:
            print("** class doesn't exist **")
        elif len(argument_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument_list[0], argument_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(argument_list[0], argument_list[1])]
            storage.save()

    def do_show_all(self, argument):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        argument_list = parse_arguments(argument)
        if len(argument_list) > 0 and argument_list[0] not in CustomConsole.__classes:
            print("** class doesn't exist **")
        else:
            object_list = []
            for obj in storage.all().values():
                if len(argument_list) > 0 and argument_list[0] == obj.__class__.__name__:
                    object_list.append(obj.__str__())
                elif len(argument_list) == 0:
                    object_list.append(obj.__str__)
            print(object_list)

    def do_count(self, argument):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class.
        """
        argument_list = parse_arguments(argument)
        count = 0
        for obj in storage.all().values():
            if argument_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, argument):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        """
        argument_list = parse_arguments(argument)
        obj_dict = storage.all()

        if len(argument_list) == 0:
            print("** class name missing **")
            return False
        if argument_list[0] not in CustomConsole.__classes:
            print("** class doesn't exist **")
            return False
        if len(argument_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argument_list[0], argument_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(argument_list) == 2:
            print("** attribute name missing **")
            return False
        if len(argument_list) == 3:
            try:
                type(eval(argument_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argument_list) == 4:
            obj = obj_dict["{}.{}".format(argument_list[0], argument_list[1])]
            if argument_list[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[argument_list[2]])
                obj.__dict__[argument_list[2]] = val_type(argument_list[3])
            else:
                obj.__dict__[argument_list[2]] = argument_list[3]
        elif type(eval(argument_list[2])) == dict:
            obj = obj_dict["{}.{}".format(argument_list[0], argument_list[1])]
            for key, value in eval(argument_list[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    val_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = val_type(value)
                else:
                    obj.__dict__[key] = value
            storage.save()


if __name__ == "__main__":
    CustomConsole().cmdloop()
