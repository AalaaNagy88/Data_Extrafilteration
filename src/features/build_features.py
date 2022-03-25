from src.features import feature_extraction as extractFeatures


def build_features(df, test,csv):
    """
    returns a dataframe with all the columns created and populated

    Args:
        df: A dataframe
        test: A boolean. If True, the run extract feature functions from row data is 
        csv: A boolean. If True, the df data will be written to a csv file

    Returns:
        A dataframe.
    """
    if test:
        for url in df["domain"]:
            df["FQDN_count"] = df["domain"].map(lambda x:extractFeatures.get_character_count(x))
            df["subdomain_length"] = df["domain"].map(lambda x:extractFeatures.get_subdomain_len(x))
            df["upper"] = df["domain"].map(lambda x:extractFeatures.get_count_upper_case_letters(x))
            df["lower"] = df["domain"].map(lambda x:extractFeatures.get_count_lower_case_letters(x))
            df["numeric"] = df["domain"].map(lambda x:extractFeatures.get_count_numeric_letters(x))
            df["entropy"] = df["domain"].map(lambda x: extractFeatures.entropy(x))
            df["special"] = df["domain"].map(lambda x: extractFeatures.get_count_special_character(x))
            df["labels"] = df["domain"].map(lambda x: extractFeatures.get_num_labels(x))
            df["labels_max"] = df["domain"].map(lambda x: extractFeatures.get_max_label(x))
            df["labels_average"] = df["domain"].map(lambda x: extractFeatures.get_average_label(x))
            df["longest_word"] = df["domain"].map(lambda x: extractFeatures.get_longest_word(x))
            df["sld"] = df["domain"].map(lambda x: extractFeatures.get_sld(x))       
            df["len"] = df["domain"].map(lambda x: extractFeatures.get_len(x))
            df["subdomain"] = df["domain"].map(lambda x: extractFeatures.check_subdomain(x))
            break
    if csv:
        df.to_csv(r"C:\Users\alaa\Desktop\assignment2-AalaaNagy88\data\interim\features.csv",mode='a',header=False ,index=False)
    return df