
import readline

def history(history_id=None):
    if history_id is None:
        for i in range(readline.get_current_history_length()):
            print( str(i+1) + ': ' + readline.get_history_item(i+1) ) 
    else:
        print( str(history_id ) + ': ' + readline.get_history_item(history_id) ) 



