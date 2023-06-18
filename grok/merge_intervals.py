def merge_intervals(intervals):
    if len(intervals) == 0:
        return []
    results = [intervals.pop()]
    for s1, f1 in intervals:
        for i, r in enumerate(results):
            s2, f2 = r
            if (s1 >= s2 and s1 <= f2): # New one starts within the current frame
                if (f1 >= s2 and f1 <= f2): # Also ends within the current frame, no-op.
                    break
                # ends outside the frame, find where to insert it
                j = i + 1
                while j < len(results):
                    jstart, jfinish = results[j]
                    if f1 >= jstart and f1 <= jfinish: # insert here
                        break
                    j += 1
                if j == len(results):   # Reached the end
                    results[i][1] = f1  # Update current record
                    results = results[:i+1]  # Delete the rest of the results
                    break

                # It wasn't the end, merge all the records i->j
                results[i][1] = results[j][1]
                results = results[:i+1] + results[j+1:]
                break
            elif (f1 >= s2 and f1 <= f2): # ends within the current result but starts before
                #just extend the time
                results[i][0] = s1
                break
            elif f1 < s2: # New insert belongs before the current record
                results.insert(i, [s1, f1])
                break
            elif s2 > f1: # New insert starts after the current record
                continue
            else:   # If we hit this branch something was overlooked
                assert False
        else:   # It didn't belong anywhere so insert at the end
            results.append([s1, f1])

    return results

print(merge_intervals([[1, 5], [3, 7], [4, 6], [6, 8]]))
print(merge_intervals([[3, 7], [1, 5], [4, 6], [6, 8]]))
print(merge_intervals([[1, 5], [6, 8], [4, 6], [3, 7]]))
print(merge_intervals([[4, 6], [3, 7], [6, 8], [1, 5]]))

