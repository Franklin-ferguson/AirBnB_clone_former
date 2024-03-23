#!/usr/bin/python3
from models.base_models import BaseModel
from models import storage
import cmd
import shlex


"""
command line interface for testing Airbnb clone application
"""
class HBNBCommand(cmd.Cmd):
    """
    Represents a class called HBNBCommand
    """
    all_classes = ["BaseModel"]

    def do_quit(self, arg):
        """
        Quits the program
        """
        return (True)

    def do_EOF(self, arg):
        """
        end of file and quits the program
        """
        print()
        return (True)

    def do_help(self, arg):
        """
        gives you more info about a command
        """
        print("Quit command to exit the program")

    prompt = "(hbnb)"

    
    def do_create(self):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        command_passed  = shlex.split(arg)

        if len(command_passed) ==  0:
            print("** class name missing **")

        elif command_passed[0] not in self.all_classes:
            print("** class doesn't exist **")

        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)


    def do_show(self):
        """
        Prints the string representation of an instance based on the class name and id
        """
        command_passed  = shlex.split(arg)

        if len(command_passed) ==  0:
            print("** class name missing **")

        elif command_passed[0] not in self.all_classes:
            print("** class doesn't exist **")

        elif len(command_passed) < 2:
            print("** instance id missing **")

        else:
            all_objects = storage.all()

            key = "{}{.{}".format(command_passed[0], command_passed[1])

            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_destroy(arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file)
        """

        command_passed = shlex.split(arg)

        if len(command_passed) == 0:
            print("** class name missing **")

        elif command_passed[0] not in self.all_classes:
            print("** class doesn't exist **")

        elif len(command_passed) < 2:
            print("** instance id missing **")

        else:
            all_objects = storage.all()
            key = "{}.{}".format(command_passed[0], command_passed[1])
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")


    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name
        """

        command_passed = shlex.split(arg)
        all_objects = storage.all()

        if len(command_passed) == 0:
            for key, value in all_objects.items():
                print(str(value))
        elif command_passed[0] not in self.all_classes:
            print("** class doesn't exist **")
        else:
            for key, value in all_objects.items():
                if key.split('.')[0] == command_passed[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        
        command_passed = shlex.split(arg)

        if len(command_passed) == 0:
            print("** class name missing **")

        elif command_passed[0] not in self.all_classes:
            print("** class doesn't exist **")

        if len(command_passed) < 2:
            print("** instance id missing **")

        else:
            all_objects = storage.all()

            key = "{}.{}".format(command_passed[0], command_passed[1])

            if key not in all_objects:
                print("** no instance found **")

            elif len(command_passed) < 3:
                print("** attribute name missing **")

            elif len(command_passed) <4:
                print("** value missing **")

            else:

                inst_object = all_objects [key]

                attribute_one = command_passed[2]

                attribute_two = command_passed[3]

                try:
                    attribute_two = eval(attribute_two)

                except Exception:
                    pass

                setattr(inst_object, attribute_one, attribute_two)

                inst_object.save()
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
