from data import DataSeq

def InsertionSort(ds, time_interval=1):
    assert isinstance(ds, DataSeq), "Type Error"

    Length = ds.length
    for i in range(Length):
        tmp = ds.data[i]
        j=i
        while j>=1 and ds.data[j-1]>tmp:
            ds.SetVal(j, ds.data[j-1])
            j-=1
        ds.SetVal(j, tmp)


if __name__ == "__main__":
    ds=DataSeq(64)
    ds.Visualize()

    InsertionSort(ds)

    ds.SetTimeInterval(0)
    ds.Visualize()