from which.inputs.joke import foo

doc_str = """\nReference dir structure
+-which/ (repo root directory)
  |- README.md
  |- which/
    |- __init__.py (empty)
    |- fun.py
    |- test_fun.py
    |- inputs/
        | -__init__.py (empty)
	    | -joke.py
        | -test_joke.py
"""

def main():
    spam = foo() 
    print ("\nwhich.fun module executed successfully")
    print ("which.inputs.joke.foo() accessed, value:", spam)
    print (doc_str)
    return spam
    
if __name__ == "__main__":
    main()