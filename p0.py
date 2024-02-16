
var = {}
constantes = ["dim","myXpos","myYpos"
            ,"myChips","myBalloons","ballonsHere"
            ,"ChipsHere","Spaces",]
posVal = {
    "(move":constantes,
    "(skip":constantes,
    "(turn":["left","right","around"],
    "(face":["north", "east", "south", "west"], #face
    "(put":["balloons","chips"],#put
    "(pick":["balloons","chips"],#pick
    "(move-dir":["front", "back", "left", "right"],#move-dir
    "(runs-dir":["front", "back", "left", "right"],#runs-dir
    "(move-face":["north", "east", "south", "west"], #move-face                
    }
moveDir = [":north",":south",":east",":west"]
dir = ["north)","south)","east)","west)","north","south","east","west"]
condicionales = ["(facing?","facing?",
                 "(blocked?)","blocked?","blocked?)","(blocked?",
                 "(can-put?","can-put?"
                 "(can-pick?", "can-pick?"
                 "(can-move?", "can-move"
                 "(not","not"]

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

            estado = processTokens(tokens[0],tokens,p_a,p_c)
            if estado == False:
                break

    return estado
def processTokens(first,tokens,p_a,p_c):
    
    if "(" not in first:
        return False
    elif "(null)" == first:
        return True
    elif "def" in first:
        if check_parent(p_a,p_c):
            return  False
        return processDef(tokens)
    elif "=" in first:
        if check_parent(p_a,p_c):
            return  False
        return  processAsign(tokens)
    elif "move-dir" in first:
        pass
    elif "move" in first or "skip" in first or "turn" in first or "face" in first:
        return process2(first,tokens)
    elif len(tokens) == 1 and "(" == first:
        return True
    elif "(if" in first:
        return processConditional() 
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
    for x in posVal.keys():
        if tokens[1] in posVal[x] :
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
def process2(key,tokens):
    if len(tokens)==2:
        try:
                val = tokens[1]
                lst = posVal[key]

                val = val[0:len(val)-1]
                if val in lst:
                    return True
                if val in var.keys():
                    return True
                number = int(number)
                return True
        except:
                return False
            
    return False

def processConditional(tokens):
    inst = tokens[1]
    if inst in condicionales:
        if "facing?" in inst:
            if tokens[2] in dir:
                return True
            else:
                return False
        elif "(blocked?)" in inst:
            return True    
        elif "can-p" in inst:
            print("LOL")            
        else:
            print("Feliz cumpleaños Jimmy")
    else:
        return False
print(upload_txt("prueba.txt"))
