class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        '''
    
            ['root/a', '1.txt(abcd)', '2.txt(efgh)']
            ['root/c', '3.txt(abcd)']
            ['root/c/d', '4.txt(efgh)']
            ['root', '4.txt(efgh)']

        
        
        
        '''
        
        fileSystem = {}
        output = []

        for path in paths:
            currentPath = path.split(" ")
            for i in range(1,len(currentPath)):
                (prefix, content) = currentPath[i].split("(")
                if content not in fileSystem:
                    fileSystem[content] = [currentPath[0]+'/'+prefix]
                else:
                    fileSystem[content].append(currentPath[0]+'/'+prefix)

        for val in fileSystem.values():
            if len(val) > 1:
                output.append(val)

        return output 

