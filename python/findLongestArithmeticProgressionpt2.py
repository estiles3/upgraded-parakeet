class Solution:
    def longestSubsequence(self, arr: List[int], k: int) -> int:
        total = 0
        if len(arr) < 2:
            return len(arr)
        if k == 0:
            arr.sort()
            dicts = {}
            total = 1
            for x in range(len(arr)):
                if arr[x] in dicts:
                    dicts[arr[x]] += 1
                    if dicts[arr[x]] > total:
                        total = dicts[arr[x]]
                else:
                    dicts[arr[x]] = 1
            return total
        # arr.sort()
        # if k < 0:
        #     arr.reverse()
        prev = {}
        for x in range(len(arr)):
            if (len(arr[x:]) <= total):
                break
            if (arr[x] in prev):
                continue
            running = 1
            checked = False
            nextVal = arr[x] + k
            for y in range(x+1,len(arr)):
                current = arr[y]
                # print(current,nextVal,running)
                if current == nextVal:
                    running+=1
                    nextVal = current + k
                    prev[current] = 1
                    if nextVal not in arr[y:]:
                        break
            if not checked:
                if total < running:
                    total = running
                checked = True
        if not checked:
            if total < running:
                total = running
        # print("--- %s seconds ---" % (time.time() - start_time))
        return total