# Comments:


def PrintItems(items=[]):  # 1. function should be in snake_case i.e. print_items():
    # 2. this comment should be more meaningful i.e. what this function and params does
    """
    :param items:
    :return:
    """

    if len(items) == 0:
        items = [1, 3, 5, 7]  # 3. not a good practice to have mutable object as default args, should be None
    i = 3  # 4. i should initialize to 0 since first item in items is 0
    while i < len(items):
        print("The " + i + " item is " + items[i])  # 6. variable i should convert to string before \
        # performing concat with str
        total += items[i]  # 7. total variable isn't defined in the function it may cause NameError
        print("The total is {}".format(total))  # 8. total variable should be incremented with current value in the list

    items[5] = total  # 9. why total is assigned to items index 5, doesn't make sense

    return total  # 10. why is this returning total


def RunQuery(query_param, t):   # func name should be n snake_case i.e. run_query():
    # this comment should be meaningful as what this function and param does
    """

    :return:
    """
    from db import *  # what is db model? specify the correct module and all the import statement should \
    # be on the top of file
    sql = "select * from " + t + "where " + query_param  # what is the table name here, where clause is not complete
    resutls = run_query(sql) # spell check on variable name should be results.
    if resutls[0] == "Monday":
        return True  # why is this returning True when results[0] is Monday? explain this

    import json  # always use import statement at the top of file
    file = open("query_results", "w")
    file.write(json.dumps(resutls))  # results variable is not in JSON-serializable so neet to convert \
    # this before writing to query_result
    return resutls