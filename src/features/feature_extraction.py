import tldextract
import pandas as pd
from collections import Counter
import numpy as np

"""
    Args:
        str_obj: raw data

    Returns:
        number of uppercase character in the raw data.
"""
def get_count_upper_case_letters(str_obj):
    count = 0
    for elem in str_obj:
        if elem.isupper():
            count += 1
    return count
"""
    Args:
        str_obj: raw data

    Returns:
        number of lowercase character in the raw data.
"""
def get_count_lower_case_letters(str_obj):
    count = 0
    for elem in str_obj:
        if (elem.islower()==True) and (elem.isdigit()==False) :
            count += 1
    return count

"""
    Args:
        str_obj: raw data

    Returns:
        number of numeric character in the raw data.
"""
def get_count_numeric_letters(str_obj):
    count = 0
    for elem in str_obj:
        if elem.isnumeric():
            count += 1
    return count

"""
    Args:
        str_obj: raw data

    Returns:
        number of special character in the raw data.
"""
def get_count_special_character(str_obj): 
   count= 0
   for elem in str_obj:
        if (elem.isalpha()) or (elem.isdigit() or elem == "."):
            continue
        else: 
            count += 1
   return count

"""
    Args:
        str_obj: raw data

    Returns:
        subdomain,domain,suffix.
"""
def divide_url(str_obj):
  subdomain,domain,suffix=tldextract.extract(str_obj)
  return subdomain,domain,suffix

"""
    Args:
        str_obj: raw data

    Returns:
        count of all character expected '.'
"""
def get_character_count(str_obj):
  count= 0
  for elem in str_obj:
      if elem==".":  
          continue
      else: 
          count += 1
  return count

"""
    Args:
        str_obj: raw data

    Returns:
        number of character of subdomain
"""
def get_subdomain_len(str_obj):
  subdomain,_,__=divide_url(str_obj)
  return get_character_count(subdomain)

"""
    Args:
        str_obj: raw data

    Returns:
        value of the entropy
"""
def entropy(str_obj):
  p, lens = Counter(str_obj), np.float(len(str_obj))
  return -np.sum( count/lens * np.log2(count/lens) for count in p.values())

"""
    Args:
        str_obj: raw data

    Returns:
        divide the url into label by using '.' in split
"""
def get_num_labels(str_obj):
  N =len(str_obj.split('.'))
  return N

"""
    Args:
        str_obj: raw data

    Returns:
        number of the label
"""
def get_len_labels(str_obj):
  return  [len(l) for l in str_obj.split('.')]

"""
    Args:
        str_obj: raw data

    Returns:
        number of character in the label of longest label
"""
def get_max_label(str_obj):
  return max(get_len_labels(str_obj))
"""
    Args:
        str_obj: raw data

    Returns:
        average of all number of charachter/ the length of labels
"""
def get_average_label(str_obj):
  le=get_len_labels(str_obj)
  return sum(le)/len(le)
"""
    Args:
        str_obj: raw data

    Returns:
        longest label word
"""
def get_longest_word(str_obj):
    M = get_max_label(str_obj)
    lens = get_len_labels(str_obj)
    return str_obj.split('.')[lens.index(max(lens))]
"""
    Args:
        str_obj: raw data

    Returns:
        second level domain 
"""
def get_sld(str_obj):
  _,sld,__=divide_url(str_obj)
  return sld
"""
    Args:
        str_obj: raw data

    Returns:
        total length of subdomain and domain together
"""
def get_len(str_obj):
  subdomain,sld,__=divide_url(str_obj)
  return get_character_count(subdomain)+get_character_count(sld)
"""
    Args:
        str_obj: raw data

    Returns:
        A boolean value of if there is a subdomain of not.
"""
def check_subdomain(str_obj):
  subdomain,_,__=divide_url(str_obj)
  return 0 if subdomain==0 else 1