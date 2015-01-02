import re
# first read the file
def read(file):
	f = open(file).read()
	return f

# check the name and create dictionary
def checkname(final):
        result = {}
        for k, v in final:
                if int(v) > result.get(k, 0):
                        result[k] = v
        return result
                       

def eachname (entries):
        final = [[x[1],x[0]]for x in entries] + [[y[2],y[0]]for y in entries]
        result = checkname(final)
        return result

def save(result, year):
        lst = []
        lst.append(year)
        for key in sorted(result):
                lst.append([key, result[key]])
        return lst
              
        
def saveinfile (lst):
        lstsave = list()
        for lines in lst:
                lstsave.append(' '.join(lines)+ '\n')
        lstsave= ''.join(lstsave)
        print (lstsave)   # possible  to use this and don't use function printdic more quick
        file = open (lst[0][0], 'w')
        file.write(lstsave)
        file.close()
        
def extractnames(filename):
        try:
                f = read(filename)
        except FileNotFoundError:
                "Called File do not exist"                              
        entries = re.findall(r'<td>(\d+)</td> <td>(\w+)</td> \<td>(\w+)</td>', f)
        year = re.findall(r'Popularity\sin\s(\d\d\d\d)', f)
        dic = eachname(entries)
        lst = save(dic, year)
        saveinfile(lst)


extractnames('baby2013.html')
        
        
