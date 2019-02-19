import pandas as pd
import azure_helper

def load_data_from_blob(file_name,retain_file=True):
    azure_helper.download_from_blob(file_name,file_name)
    data = pd.read_csv(file_name)
    if retain_file == False:
        os.remove(file_name)
    return data

def hand_label(df):
    """
    Asks an end user to hand label each comment as
    * syntax
    OR
    * semantics
    """
    if len(df) < 200:
        sample = df.copy()
    else:
        sample = df.sample(frac=0.3)
    
    # df["labels"] = ''
    # for index in df.index:
    #     dicter = df.loc[index].to_dict()
    #     for key in dicter:
    #         print(key, ":", dicter[key])
    #     label = input("what label should this have?")
    #     df.loc[index, ["labels"]] = label
    # return df, index

def ask_for_labels(local=True):
    if local:
        df = pd.read_csv("predicted_labels.csv")
    else:
        df = load_data_from_blob("predicted_labels.csv")
    df, index = hand_label(df)
    df = auto_label(df, index)
    

if __name__ == '__main__':
    ask_for_labels("wikipedia", "comments.csv")
