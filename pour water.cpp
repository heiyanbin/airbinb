vector<int> pourWater(vector<int> &heights, int V, int K) {
    // Write your code here
    for (int i = 0; i < V; ++i) {
        for (auto x : heights) {
            cout << x << ", ";
        }
        cout << endl;
        int settle = -1, h = -1;
        for (int j = K - 1; j >= 0; --j) {
            if (heights[j] < heights[K]) {
                if (h == -1 || heights[j] < h) {
                    h = heights[j];
                    settle = j;
                }
            }
            if (h != -1 && heights[j] > h || heights[j] > heights[K]) break;
        }

        if (settle != -1) {
            heights[settle] += 1;
            continue;
        }

        for (int j = K + 1; j < heights.size(); ++j) {
            if (heights[j] < heights[K]) {
                if (h == -1 || heights[j] < h) {
                    h = heights[j];
                    settle = j;
                }
            }
            if (h != -1 && heights[j] > h || heights[j] > heights[K]) break;
        }
        if (settle != -1) {
            heights[settle] += 1;
            continue;
        }
        heights[K] += 1;
    }
    return heights;
}