


from_pc = input("What is the old PC: ")
to_pc = input("What is the new PC: ")
username = input("What is the Username: ")


first = ("\\\\%s\c$\\Users\%s" % (from_pc, username))
second = ("\\\\%s\c$\\Users\%s" % (to_pc, username))





