#!/usr/bin/python3
"""This module defines the HBnB console"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBnBCommand(cmd.Cmd):
    """HBnBCommand class that defines the console"""

    prompt = "(hbnb) "
    __classes = [
        "BaseModel", "User", "State", "City",
        "Amenity", "Place", "Review"
    ]

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

    def do_create(self, line):
        """Create a new instance of a class and print its id
Usage: create <class>"""
        if not line:
            print("** class name missing **")
            return
        if line not in HBnBCommand.__classes:
            print("** class doesn't exist **")
            return
        obj = eval(line)()
        obj.save()
        print(obj.id)

    def do_show(self, line):
        """Print the string representation of an instance
Usage: show <class> <id>"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBnBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, line):
        """Delete an instance based on the class name and id
Usage: destroy <class> <id>"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBnBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, line):
        """Print all string representations of instances
Usage: all [class]"""
        objects = storage.all()
        if not line:
            print([str(v) for v in objects.values()])
            return
        if line not in HBnBCommand.__classes:
            print("** class doesn't exist **")
            return
        print([str(v) for v in objects.values()
               if type(v).__name__ == line])

    def do_update(self, line):
        """Update an instance based on the class name and id
Usage: update <class> <id> <attribute name> <attribute value>"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBnBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = objects[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            setattr(obj, attr_name, attr_type(attr_value))
        else:
            setattr(obj, attr_name, attr_value)
        obj.save()

    def default(self, line):
        """Handle alternative syntax: <class>.<command>(<args>)"""
        methods = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        if "." not in line:
            print("*** Unknown syntax: {}".format(line))
            return
        parts = line.split(".", 1)
        class_name = parts[0]
        rest = parts[1]
        if "(" not in rest or not rest.endswith(")"):
            print("*** Unknown syntax: {}".format(line))
            return
        method_name = rest.split("(", 1)[0]
        args = rest.split("(", 1)[1][:-1]
        if method_name not in methods:
            print("*** Unknown syntax: {}".format(line))
            return
        if args:
            call = "{} {}".format(class_name, args)
        else:
            call = class_name
        methods[method_name](call)

    def do_count(self, line):
        """Count the number of instances of a class
Usage: count <class>"""
        objects = storage.all()
        count = sum(1 for v in objects.values()
                    if type(v).__name__ == line)
        print(count)


if __name__ == "__main__":
    HBnBCommand().cmdloop()
