import pandas as pd


def sen(fname):
    fi = pd.read_excel(fname)
    print("outpput runn"+fname)
    print(fi.head())
    subset_df = fi[fi["Unnamed: 2"] == 1]

    """
    subset_df = fi[fi["Unnamed: 2"] == 2]
    print("2  : " + str(subset_df.count()))
    subset_df = fi[fi["Unnamed: 2"] == 3]
    print("3  : " + str(subset_df.count()))
    subset_df = fi[fi["Unnamed: 2"] == 4]
    print("4  : " + str(subset_df.count()))
    subset_df = fi[fi["Unnamed: 2"] == 5]
    print("5  : " + str(subset_df.count()))"""