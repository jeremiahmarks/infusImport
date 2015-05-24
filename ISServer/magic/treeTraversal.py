def traverseTree(TreeStructure,depth=0,covered=[]):
    brkStr="\t"*(depth+1)
    retStr=""
    if TreeStructure not in covered:
        covered.append(TreeStructure)
        for eachItem in TreeStructure.keys():
            retStr=retStr+'\n'+brkStr
            if type(TreeStructure[eachItem]) is not type({}):
                retStr += eachItem + ":\t" + TreeStructure[eachItem] 
            else:
                retStr += eachItem + ":" +"\t"+ traverseTree(TreeStructure[eachItem],depth+1,covered)
    else:
        retStr="AlreadyCovered"
    return retStr

allExisting={}
allExisting['Category']={}
allExisting['Category']['awesome']={}
allExisting['Category']['awesome']['cool']={}
allExisting['Category']['awesome']['cool']['sweet']={}
allExisting['Category']['pollo']={}
allExisting['Category']['pollo']['fundido']={}
allExisting['Category']['pollo']['fundido']['yum']={}
allExisting['Category']['pollo']['tacos']={}
allExisting['Category']['pollo']['tacos']['great']={}
allExisting['Category']['pollo']['tacos']['ok']={}
allExisting['Product']={}
allExisting['Product']['5']={}
allExisting['Product']['5']['categoryPaths']={}
allExisting['Product']['5']['categoryPaths']['awesome']=allExisting['Category']['awesome']
allExisting['Product']['5']['categoryPaths']['awesome']['actualPath']='awesome'
allExisting['Product']['5']['categoryPaths']['awesome']['parent']=allExisting['Category']
allExisting['Product']['5']['categoryPaths']['awesome']['children']={}
allExisting['Product']['5']['categoryPaths']['awesome']['children']['cool']=allExisting['Category']['awesome']['cool']
allExisting['Product']['5']['categoryPaths']['awesome']['children']['cool']['actualPath']='awesome/cool'
allExisting['Product']['5']['categoryPaths']['awesome']['children']['cool']['parent']=allExisting['Category']['awesome']
allExisting['Product']['5']['categoryPaths']['awesome']['children']['cool']['children']={}
allExisting['Product']['5']['categoryPaths']['awesome']['children']['cool']['children']['sweet']=allExisting['Category']['awesome']['cool']['sweet']
allExisting['Product']['5']['categoryPaths']['awesome']['children']['cool']['children']['sweet']['actualPath']='awesome/cool/sweet'
allExisting['Product']['5']['categoryPaths']['awesome']['children']['cool']['children']['sweet']['parent']=allExisting['Product']['5']['categoryPaths']['awesome']['children']['cool']
allExisting['Product']['5']['categoryPaths']['awesome']['children']['cool']['children']['sweet']['children']={}
allExisting['Product']['5']['categoryPaths']['pollo']=allExisting['Category']['pollo']
allExisting['Product']['5']['categoryPaths']['pollo']['actualPath']='pollo'
allExisting['Product']['5']['categoryPaths']['pollo']['parent']=allExisting['Category']
allExisting['Product']['5']['categoryPaths']['pollo']['children']={}
allExisting['Product']['5']['categoryPaths']['pollo']['children']['fundido']=allExisting['Category']['pollo']['fundido']
allExisting['Product']['5']['categoryPaths']['pollo']['children']['fundido']['actualPath']='pollo/fundido'
allExisting['Product']['5']['categoryPaths']['pollo']['children']['fundido']['parent']=allExisting['Product']['5']['categoryPaths']['pollo']
allExisting['Product']['5']['categoryPaths']['pollo']['children']['fundido']['children']={}
allExisting['Product']['5']['categoryPaths']['pollo']['children']['fundido']['children']['yum']=allExisting['Category']['pollo']['fundido']['yum']
allExisting['Product']['5']['categoryPaths']['pollo']['children']['fundido']['children']['yum']['actualPath']='pollo/fundido/yum'
allExisting['Product']['5']['categoryPaths']['pollo']['children']['fundido']['children']['yum']['parent']=allExisting['Category']['pollo']['fundido']
allExisting['Product']['5']['categoryPaths']['pollo']['children']['fundido']['children']['yum']['children']={}
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']=allExisting['Category']['pollo']['tacos']
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']['actualPath']='pollo/tacos'
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']['parent']=allExisting['Category']['pollo']
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']['children']={}
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']['children']['great']=allExisting['Category']['pollo']['tacos']['great']
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']['children']['great']['actualPath']='pollo/tacos/great'
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']['children']['great']['parent']=allExisting['Category']['pollo']['tacos']
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']['children']['great']['children']={}
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']['children']={}
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']['children']['ok']=allExisting['Category']['pollo']['tacos']['ok']
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']['children']['ok']['actualPath']='pollo/tacos/ok'
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']['children']['ok']['parent']=allExisting['Category']['pollo']['tacos']
allExisting['Product']['5']['categoryPaths']['pollo']['children']['tacos']['children']['ok']['children']={}

def main():
    print traverseTree(allExisting)

if __name__ == '__main__':
    main()