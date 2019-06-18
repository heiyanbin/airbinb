vector<string> fullJustify(vector<string> &words, int maxWidth) {
    // write your code here
    vector<string> ans;
    int start = 0, curLen = 0, curLenNoSpace = 0;
    for (int i = 0; i <= words.size();) {
        int n = curLen == 0 ? words[i].size() : words[i].size() + 1;
        if (i < words.size() && curLen + n <= maxWidth) {
            curLen += n;
            curLenNoSpace += words[i].size();
            ++i;
        }
        else {
            if (i == words.size()) {
                if (start != i) {
                    string lastLine;
                    for (int j = start; j < words.size(); ++j) {
                        if (lastLine.size() > 0) {
                            lastLine.append(" ");
                        }
                        lastLine.append(words[j]);
                    }
                    while (lastLine.size() < maxWidth) {
                        lastLine.push_back(' ');
                    }
                    ans.push_back(lastLine);
                }
                break;
            }
            int divide = i - start == 1 ?  1 : i - start - 1;
            int totalSpace = maxWidth - curLenNoSpace;
            int numSpace =  totalSpace/ divide;
            string line(maxWidth, ' ');
            int k = maxWidth - 1;
            for (int j = i - 1; j > start; --j) {
                for (int p = words[j].size() - 1; p >= 0; ) {
                    line[k--] = words[j][p--];
                }
                k -= numSpace;
                if (numSpace * divide != totalSpace) {
                    totalSpace -= numSpace;
                    numSpace = totalSpace / (divide  - 1);
                }

            }
            for (int p = 0; p < words[start].size(); ++p) {
                line[p] = words[start][p];
            }

            ans.push_back(line);
            curLen = 0;
            curLenNoSpace = 0;
            start = i;
        }
    }
    return ans;
}
