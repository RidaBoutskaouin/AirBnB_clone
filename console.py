#!/usr/bin/python3
""" import cmd module, BaseModel and storage """
import cmd, sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

list_classes = ["BaseModel",
                "User",
                "State",
                "City",
                "Amenity",
                "Review",
                "Place"]

class HBNBCommand(cmd.Cmd):
    """ the entry point of the command interpreter """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
    def help_quit(self):
        """Quit command to exit the program."""
        print("Quit command to exit the program.")
        print("")
    
    def help_help(self):
        """Display help message for the help command."""
        print("List available commands or provide help for a specific command.")

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        and prints the id. Example:(hbnb) create BaseModel\n """
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] in list_classes:
            print(eval(args[0])().id)
            models.storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation
        of an instance based on the class name and id"""
        args = arg.split(" ")
        objects = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] in list_classes:
            if len(args) == 2:
                inst_id = args[0] + "." + args[1]
                if inst_id in objects.keys():
                    print(objects[inst_id])
                else :
                    print("** no instance found **")
            else:
               print("** instance id missing **")
        else:
            print("** class doesn't exist **")
        
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        objects = models.storage.all()
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] in list_classes:
            if len(args) >= 2:
                inst_id = args[0] + "." + args[1]
                if inst_id in objects.keys():
                    del(objects[inst_id])
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name."""
        args = arg.split(" ")
        objects = models.storage.all()
        if len(arg) == 0:
            list_p = []
            for key in objects.keys():
                string = str(objects[key])
                list_p.append(string)
            print(list_p)
        elif args[0] in list_classes:
            """ to revieeewwwwweeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee """          
            list_p = []
            for key in objects.keys():
                string = str(objects[key])
                if args[0] == key[: len(args[0])]:
                    
                    list_p.append(string)
            print(list_p)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name 
        and id by adding or updating attribute. """
        objects = models.storage.all()
        args = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif args[0] in list_classes:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                inst_id = args[0] + "." + args[1]
                if inst_id in objects.keys():
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        try:
                            objects[inst_id].__dict__[args[2]] = eval(args[3])
                            models.storage.save()
                        except:
                            objects[inst_id].__dict__[args[2]] = args[3]
                            models.storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")
	

    def default(self, args):
        words = args.split(".")
        class_name = words[0]
        if class_name in list_classes:
            command = words[1]
            if command in ['all()', 'count()']:
                if command == "all()":
                    self.do_all(class_name)
                elif command == "count()":
                    self.count(class_name)
            else:
                if "show" in command :
                    my_id = command.split("(")[1].strip(")")
                    para = class_name + " " + my_id
                    self.do_show(para)
                elif "destroy" in command :
                    my_id = command.split("(")[1].strip(")")
                    para = class_name + " " + my_id
                    self.do_destroy(para)
                elif "update" in command :
                    cn = class_name
                    if "{" not in command.split("(")[1]:
                        my_id_splited = command.split("(")[1].strip(")")
                        my_id_splited2 = my_id_splited.replace('"', '').replace(',', '')
                        my_id_splited3 = my_id_splited2.split(" ")[0]
                        my_id = cn + " " + my_id_splited3
                        my_att = my_id_splited2.split(" ")[1]
                        my_val = my_id_splited2.split(" ")[2]
                        arg = my_id + " " + my_att + " " + my_val
                        self.do_update(arg)
                    elif len(command.split("(")[1].split(", {")) == 2:
                        my_id = command.split("(")[1].split(", {")[0].strip(')"')
                        my_dict = command.split("(")[1].split(", {")[1].strip(')')
                        dic = eval("{" + my_dict)
                        for att, val in dic.items():
                            arg = cn + " " + my_id + " " + att + " " + str(val)
                            self.do_update(arg)

    def count(self, class_name):
        objects = models.storage.all()
        num_objs = 0
        for name_id in objects.keys():
            if name_id.split(".")[0] == class_name:
                num_objs += 1
        print(num_objs)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
