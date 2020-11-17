from semantic_memory import SemanticMemory
from input_vector_parser import InputVectorParser

trait_names = ['N', 'L', 'P']
semantic_memory = SemanticMemory([], trait_names)
action = input().lower()

run = True
while run:
    print("Type: 'data' to load external data into semantic memory \n "
          "Type: 'request' to write a query for the cognitive agent \n"
          "Type: 'load memory' to load memory from an external file \n"
          "Type: 'end' to finish execution and save current semantic memory \n"
          "===============================================================\n")
    if action == "data":
        path = input("Input path: ")
        file_name = input("Input file name: ")
        try:
            open(path + "/" + file_name)
            parser = InputVectorParser(path, file_name)
            parser.read()

            input_vector_list = parser.return_vec_list()
            semantic_memory.update_from_list(input_vector_list)
        except IOError:
            print("No such file or directory")
    elif action == "request":
        print("Type your request in format: <obj_name> <trait_1> <trait_2>")
        obj_name, trait_1, trait_2 = input("Query: ").split(" ")
        if obj_name in semantic_memory.object_names and \
                trait_1 in semantic_memory.trait_names and \
                trait_2 in semantic_memory.trait_names:
            semantic_memory.save_user_request(obj_name, trait_1, trait_2)

        else:
            print("Wrong input")

    elif action == "load memory":
        path = input("Input path: ")
        file_name = input("Input file name: ")
        try:
            open(path + "/" + file_name)
            semantic_memory.load_from_file(path, file_name)
        except IOError:
            print("No such file or directory")
    elif action == "end":
        run = False
        print("Execution has finished")
    else:
        pass

# memory = SemanticMemory(["o1","o2","o3","o4"],["N","L","P"])
# vec1=InputVector("o1",3,[1,0,2],0)
# vec2=InputVector("o2",3,[1,2,0],1)
# vec3=InputVector("o3",3,[0,0,1],2)
# vec4=InputVector("o4",3,[2,0,2],3)
# vec5=InputVector("o4",3,[1,1,2],4)
# memory.update(vec1)
# memory.update(vec2)
# memory.update(vec3)
# memory.update(vec4)
# memory.update(vec5)
# memory.save_to_file("/home/bartosz/PycharmProjects/inzynierka","data.json")

# memory = SemanticMemory([],[])
# memory.load_from_file("/home/bartosz/PycharmProjects/inzynierka","data.json")
# memory.expand("o5")
# print(memory.obj_names)
# print(memory.trait_names)
# print(memory.obj_traits)
#

# input = InputVectorParser('/home/bartosz/PycharmProjects/inzynierka', 'dane', '')
# input.read()
#
# for vec in input.input_vectors_list:
#     print(vec.obj_name,vec.list)
