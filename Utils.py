def sort(arr, cur_uid):
    arr_before = []
    arr_after = []
    for user in arr:
        if user.uid < cur_uid:
            arr_before.append(user)
        if user.uid > cur_uid:
            arr_after.append(user)
    arr_before.reverse()
    arr_after.reverse()
    result = arr_before + arr_after

    return result
