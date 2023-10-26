dummy_data = ["John Doe", 725, 5.8, "Alice Smith", 370, 5.6, "Bob Johnson", 528, 6.0, "Eve Williams", 363, 5.9]


def filterData(datas):
    integerData = list(filter(lambda x: isinstance(x, int), datas))
    floatData = list(filter(lambda x: isinstance(x, float), datas))
    stringData = list(filter(lambda x: isinstance(x, str), datas))

    return {"integer": integerData, "float": floatData, "string": stringData}

def mapData(datas):
    data = []
    allData = list(map(lambda num: str(num) , datas))
    satuan = list(map(lambda num: int(num[len(num) - 1]) , allData))
    puluhan = list(map(lambda num: int(num[len(num) - 2]) , allData))
    ratusan = list(map(lambda num: int(num[len(num) - 3]) , allData))
    
    for x, y in enumerate(datas):
        data.append({"Ratusam": ratusan[x], "Puluhan": puluhan[x], "Satuan":satuan[x]})
    # for i in len(datas):
    
    return data


def main():
    data = filterData(dummy_data)

    print(f"Data Integer {data['integer']}")
    print(f"Data Float {data['float']}")
    print(f"Data String {data['string']}")


    print(mapData(data['integer']))

if __name__ == "__main__":
    main()

