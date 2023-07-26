"""
In-class revision
 At the end of this class, you should be able to answer the following questions:

 What is a module in Python? How do you create one?
    A module is a block of code that has been defined with the def keyword
 What is the purpose of the import statement in Python? Can you provide a code example of its usage?
    import joins python files together. Example in week2/main.py
 How can you import only a specific function or class from a module in Python? What is the syntax for this?
    use the from a python file, then import function name
 How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference?
    If immutable more similar to pass-by-value if mutable pass-by-reference
 Given the following Python code, what will be the output and why?
 def modify_list(lst):
    lst.append("new")
    lst = ["completely", "new"]

 items = ["original"]
 modify_list(items)
 print(items)
 If Python uses pass-by-reference, why does not reassigning a variable inside a function change the original variable
 outside the function? How is this related to the mutability of Python objects?
 """