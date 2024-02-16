
var = {}
constantes = ["dim","myXpos","myYpos"
            ,"myChips","myBalloons","ballonsHere"
            ,"ChipsHere","Spaces"]
directions = {"(turn":["left","right","around"],
              "(face":["north", "east", "south", "west"], #face y move-face
              "(dir" or "s":["front", "back", "left", "right"], #move y run dirs
              
              }


def upload_txt(txt_direction):
    estado = True
    with open(txt_direction) as txt:
        for line in txt:
            print(line)
            p_a =line.count("(")
            p_c = line.count(")")
            line = line.lower() 
            line = line.strip()
            if not line:
                continue
            tokens = line.split()

            estado = processTokens(tokens,p_a,p_c)
            if estado == False:
                break

    return estado
def processTokens(tokens,p_a,p_c):
    
    if "(" not in tokens[0]:
        return False
    elif "(null)" == tokens[0]:
        return True
    elif "def" in tokens[0]:
        if check_parent(p_a,p_c):
            return  False
        return processDef(tokens)
    elif "=" in tokens[0]:
        if check_parent(p_a,p_c):
            return  False
        return  processAsign(tokens)
    elif "move-dir" in tokens[0]:
        pass
    elif "move" in tokens[0] or "skip" in tokens[0] or "turn" in tokens[0] or "face" in tokens[0]:
        return process2(tokens)
    elif len(tokens) == 1 and "(" == tokens[0]:
        return True
    else:
        return False
def check_parent(p_a,p_c):
    return  p_a != p_c or p_a != 1
def processDef(tokens):
    if"defvar" in  tokens[0]:
        return procDefVar(tokens)
def processAsign(tokens):
    if len(tokens)<4:
        if tokens[1] in var:
            try:
                val = tokens[2]
                print(val)
                number = int(val[0:len(val)-1])
                var[tokens[1]] = number
                return True
            except:
                return False
    return False
def procDefVar(tokens):
    noExiste = True
    for x in directions.keys():
        if tokens[1] in directions[x] :
            noExiste = False
            
    if len(tokens)<=3:
        if tokens[1] not in var and tokens[1] not in constantes and noExiste:
            try:
                val = tokens[2]
                val =val[0:len(val)-1]
                if val in constantes:
                    var[tokens[1]] = val
                    return True
                number = int(val[0:len(val)-1])
                var[tokens[1]] = number
                return True
            except:
                return False
        
    return False
def process2(tokens,key):
    if len(tokens)==2:
        try:
                val = tokens[1]
                if val in directions[key]:
                    return True
                number = val[0:len(val)-1]
               
                if not (number in var.keys()):
                    number = int(number)
                return True
        except:
                return False
            
    return False
print(upload_txt("prueba.txt"))