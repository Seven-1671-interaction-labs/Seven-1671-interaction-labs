import re
def split_my_info(my_info):
    search_result = re.split(":", my_info)
    
    seven = search_result[1]
    seven = re.split("My ID is", seven)
    print (f"My name is {seven[0]}")
    
    sevenza = seven[1]
    print (f"My ID is {sevenza}")

if __name__=="__main__":
    my_info = "My name:chakkapat Waenmook My ID is 6530401671"
    split_my_info(my_info)