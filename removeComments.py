__author__ = 'heiyanbin'

class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        inBlock = False
        ans = []
        for i in xrange(len(source)):
            line, newline, hasCommentStart, hasCommentEnd = source[i], [], False, False
            for j in xrange(len(line)):
                if inBlock:
                    if line[j] == '/' and j - 2 >= 0 and line[j - 1] == '*' and line[j - 2] != '/' :
                        inBlock, hasCommentEnd = False, True
                elif line[j] == '/' and j - 1 >= 0 and line[j - 1] == '/' and (j - 2 < 0 or line[j - 2] != '*'):
                    newline.pop()
                    break
                elif line[j] == '*' and j - 1 >= 0 and line[j - 1] == '/':
                    inBlock, hasCommentStart = True, True

                    newline.pop()
                else:
                    newline.append(line[j])
            content = ''.join(newline)
            if content != '':
                if hasCommentEnd and not hasCommentStart and len(ans) > 0:
                    ans[-1] += content
                else:
                    ans.append(content)
        return ans

input = ["a//*b//*c","blank","d*//e*//f"]
ans = Solution().removeComments(input)
print ans
for l in input: print l
for l in ans: print l