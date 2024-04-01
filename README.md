# Cluster
 A compiled programming language targetted to C++

---

# Features
- **Speed**: Cluster is a compiled language, compiled to C++ - one of the fastest programming languages.
- **Static typing**: Cluster is statically typed, increasing type safety and performance. Cluster has type inference for variables, though you do have to explicitly say what type a function returns and it's parameters.
- **Simplicity**: Cluster's syntax is simple almost like a bridge between Python and C++.

---

# How to run

1. **Clone this repository**
    - With the git command line tool: `git clone https://github.com/LemurGamingYT/Cluster.git`
2. **Install Python**
    - You should install the latest version of Python
    - Make sure to add Python to PATH, install pip (the package manager) and run the pip install command: `pip install -r requirements.txt` in the directory you have downloaded this repository.
3. **Install a C++ compiler (g++ or clang++ are supported)**
    - MinGW (g++): https://sourceforge.net/projects/mingw/files/latest/download
    - LLVM (clang++): https://github.com/llvm/llvm-project/releases
4. **Run the compiler**
    - To initialize a new project use the command: `python main.py init [ProjectName]`
    - To build a file: `python main.py build [FileName]`
    - To build a project (omit the filename argument): `python main.py build` (in a cluster project)
    - To run a file (compiles then deletes the executable and .cpp): `python main.py run [FileName]`
    - To run a project (omit the filename argument): `python main.py run` (in a cluster project)

---

# Ideas

---

- **Dictionaries/Maps**: Maps are supported in C++, meaning it's possible for Cluster to have them.
```
// Create a new dictionary
dictionary = Dict[string: int] {
    "a": 1,
    "b": 2,
    "c": 3
}

print(dictionary)

// Use dictionary functions
print(dictionary.get("a")) // 1
print(dictionary.from_value(3)) // "c"
```
- **Function expressions**: Lambda function equivalent.
```
print((int x) => { return x - 20 }(20)) // 0
```
- **Reference parameters**: Pass parameters by reference, meaning anything that it changes with the parameter in the function will change outside the function too.
```
// 'ref' indicates it will be passed by reference
func test(ref int x) {
    x = x + 1000
}

// Define the 'x' variable
x = 50

// Call the function, 'x' is passed by reference
test(x)
print(x) // 1050, 'x' was changed in the function
```
- **String dollar**: String concatentation using the dollar ($) symbol
```
x = 50
print($"My luckiest number is {x}")

// Another reason I see this being useful is importing libraries
lib = input("What library do you want to import?\n> ")
use $"{lib}"
print($"Imported {lib}")
```
- **Structs**: Custom types in Cluster. Supported in C++ too meaning it can almost be directly translated into C++.
```
// Create a new struct
struct Vector3 {
    float x
    float y
    float z
}

// Make an attribute on the Vector3 struct
func Vector3.repr(Vector3 vec) { // Create a string representation of the struct
    return "Vector3(x=" + to_string(vec.x) + ", y=" + to_string(vec.y) + ", z=" + to_string(vec.z) + ")"
}

// Create a new property that is static
// Static means that it does not need an instance of the object to work
// Properties do not need to be called and take no parameters
static property Vector3.zero = Vector3{0, 0, 0}

// Create a new Vector3 object
vec_zero = Vector3.zero
vec = Vector3{70, 0, 120}
print(vec) // 'Vector3.repr' is called
```
- Compile time expressions: Expressions or functions evaluated at compile time instead of run time. This could make use of C++'s constexpr keyword, however this would mean that the feature would be limited to ints and floats.
```
comptime {
    func factorial(int n) -> int {
        if n == 0 || n == 1 {
            return 1
        } else {
            return n * factorial(n - 1)
        }
    }
}

print(factorial(5)) // This is evaluated at compile time and is replaced with the value of 120 in the generated assembly code.
```
