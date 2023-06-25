import json


def genDiff(path_to_file1, path_to_file2):
    res = []

    with open(path_to_file1) as file1, open(path_to_file2) as file2:
        file1_data = json.load(file1)
        file2_data = json.load(file2)

        for k, v in file1_data.items():
            if k in file2_data:
                if v == file2_data[k]:
                    res.append(f"     {k}: {v}")
                else:
                    res.append(f"   - {k}: {v}")
                    res.append(f"   + {k}: {file2_data[k]}")
                del file2_data[k]
            else:
                res.append(f"   - {k}: {v}")

        for k, v in file2_data.items():
            res.append(f"   + {k}: {v}")

        res.insert(0, "{")
        res.append("}")

    return "\n".join(res)

