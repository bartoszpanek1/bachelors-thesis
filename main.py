from semantic_memory import SemanticMemory
from input_vector_parser import InputVectorParser

def run_agent():
    agent_run = True
    while agent_run:
        print('Type: \'data\' to load external data into semantic memory \n'
              'Type: \'request\' to write a query for the cognitive agent \n'
              'Type: \'end\' to finish execution and save current semantic memory \n'
              '===============================================================')
        action = input('Action: ').lower()
        if action == 'data':
            path = input('Input path: ')
            file_name = input('Input file name: ')
            try:
                open(path + '\\' + file_name)
                parser = InputVectorParser(path, file_name)
                parser.read()

                input_vector_list = parser.return_vec_list()
                semantic_memory.update_from_list(input_vector_list)
            except IOError:
                print('No such file or directory')
        elif action == 'request':
            print('Type your request in format: <obj_name> <trait_1> <trait_2>')
            obj_name, trait_1, trait_2 = input('Query: ').split(' ')
            if obj_name in semantic_memory.object_names and \
                    trait_1 in semantic_memory.trait_names and \
                    trait_2 in semantic_memory.trait_names:
                semantic_memory.handle_user_request(obj_name, trait_1, trait_2)
            else:
                print('Wrong input')
        elif action == 'end':
            semantic_memory.save_to_file('D:\PyCharm\PyCharm Projects\\bachelors-thesis', 'memory_file')
            agent_run = False
            print('Memory has been saved and the execution has finished')
        else:
            print('ERROR! No such command')

trait_names = ['N', 'L', 'P']
semantic_memory = SemanticMemory([], trait_names)
# D:\PyCharm\PyCharm Projects\bachelors-thesis

run = True
while run:
    print('Type: \'new\' to create new semantic memory of an agent \n'
          'Type: \'load\' to load memory of an existing agent from an external file \n'
          'Type: \'end\' to finish execution \n'
          '===============================================================')

    action = input('Action: ').lower()
    # Selection of new agent creation
    if action == 'new':
        # Loop for operations on new agent
        run_agent()
                
    # Selection of loading existing agent into the system
    elif action == 'load':
        # Loading of the memory
        path = input('Input path: ')
        file_name = input('Input file name: ')
        try:
            open(path + '\\' + file_name)
            semantic_memory.load_from_file(path, file_name)
            print('Succesfully loaded agent\'s memory')
            print(semantic_memory.holons)
        except IOError:
            print('No such file or directory')

        old_agent_run = True
        # Loop for operations on existing agent
        run_agent()
    elif action == 'end':
        run = False
        print('Execution has finished')
    else:
        print('ERROR! No such command')

