
import readline, os, subprocess, tempfile

def history(history_id=None):
    if history_id is None:
        for i in range(readline.get_current_history_length()):
            print( str(i+1) + ': ' + readline.get_history_item(i+1) ) 
    else:
        print( str(history_id ) + ': ' + readline.get_history_item(history_id) ) 

def templist():
    (fd, path) = tempfile.mkstemp()

    editor = os.getenv('EDITOR', 'vi')
    subprocess.call('%s %s' % (editor, path), shell=True)

    f = open(path, 'r')
    temp_data = list(f)
    f.close()

    os.unlink(path)

    for i in range(len(temp_data)):
        temp_data[i] = temp_data[i].strip().replace('\n', '')
        
    return temp_data
