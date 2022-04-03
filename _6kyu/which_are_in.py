def in_array(array1, array2):
    result = set()
    a1 = ["live", "arp", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    for line1 in a1:
        for line2 in a2:
            if line1 in line2:
                result.add(line1)
    return [*sorted(result)]



