"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.
The canonical path should have the following format:
The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')
Return the simplified canonical path.
#----------------------------------------------
Example 1:
Input: path = "/home/"
Output: "/home"
#----------------------------------------------
Example 2:
Input: path = "/../"
Output: "/"
#----------------------------------------------
#Approach:
Initialize an empty stack to hold the directories in the simplified path.
Split the input path string into individual directories using the forward slash ("/") as a separator.
For each directory:
If the directory is a parent directory reference ("..") and the stack is non-empty, pop the last directory off the stack to remove the preceding directory.
If the directory is not a special directory reference (i.e. neither ".", "" nor ".."), append it to the stack.
Construct the simplified path by joining the directories in the stack with forward slashes ("/") and adding a leading forward slash ("/").
"""


class Solution:
    def simplifyPath(self, path):
        dir_stack = []
        path = path.split("/")
        for elem in path:
            if dir_stack and elem == "..":
                dir_stack.pop()
            elif elem not in [".", "", ".."]:
                dir_stack.append(elem)

        return "/" + "/".join(dir_stack)
