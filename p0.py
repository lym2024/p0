
var = {}
constantes = ["dim","myxpos","mypos"
            ,"mychips","myballoons","ballonshere"
            ,"chipshere","spaces",]
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
runDirs = [":front",":left",":right",":back"]
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
            print(line)
            line = line.strip()
            print(line)
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
    elif "def" in first or "def" in tokens[1]:
        if "def" in tokens[1]:
            tokens = Juntar_0_1(tokens)
        if check_parent(p_a,p_c):
            return  False
        return processDef(tokens)
    elif "=" in first or "=" in tokens[1]:
        if "(" == first:
            tokens = Juntar_0_1(tokens)
        if check_parent(p_a,p_c):
            return  False
        return  processAsign(tokens)
    elif "move-dir" in first or "move-dir" == tokens[1] or "move-face" in  first or "move-face" == tokens[1]:
        if tokens[1] == "move-dir" or tokens[1]=="move-face":
            tokens = Juntar_0_1(tokens)
        return process_movDir(tokens)
    elif "run-dirs" in first or "run-dirs" == tokens[1]:
        if "run-dirs" == tokens[1]:
            tokens = Juntar_0_1(tokens)
        return process_run(tokens)
    elif "move"in first  or "skip" in first  or "turn"  in first or "face" in first or "move"== tokens[1] or "skip"== tokens[1]  or "turn"== tokens[1]  or "face" == tokens[1] : 

        if ("move" or "skip"  or "turn"  or "face" ) == tokens[1]:
            tokens = Juntar_0_1(tokens)
            first=tokens[0]
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
        if tokens[1] not in var.keys() and tokens[1] not in constantes and noExiste:
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
    print("sagkhsahkjslhkjsddsklij")
    if len(tokens)==2:
        try:
                val = tokens[1]
                lst = posVal[key]

                val = val[0:len(val)-1]
                print(val)
                if val in lst:
                    return True
                if val in var.keys():
                    return True

                number = int(val)


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

def process_run(tokens):
    for i in tokens:
        if i == "(run-dirs" :
            pass
        elif ")" == i and tokens[len(tokens)-1] == i:
            return True
        elif ")" in i:
                val =i[0:len(i)-1]
                if val  not in runDirs:
                    return False
        else:
            if i not in runDirs:
                return False
    return True
            
def process_movDir(tokens):

    if len(tokens)<5:
        try:
            print(tokens)
            if not(tokens[1] in var.keys()):
                int(tokens[1])
            val = tokens[2]
            print(val)
            if ")" in val:
                    val =val[0:len(val)-1]
            if"dir" in tokens[0]:

                if not(val in runDirs):
                    return False
            else:
                
                if not(val in moveDir):
                    return False
        except:
            return False
        
        return True
    else:
        return False
def Juntar_0_1(tokens):
    pos = ""
    lst = []
    print(tokens)
    for i in range(0,len(tokens)):
        if i == 0:
            pos += tokens[i]
        elif i == 1:
            pos += tokens[i]
            lst.append(pos)
        elif i == len(tokens)-2 and ")" == tokens[i+1]:
            lst.append(tokens[i]+tokens[i+1])
            return lst
        else:
            lst.append(tokens[i])
    
    return lst
print(upload_txt("prueba.txt"))

