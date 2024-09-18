"""
Problem 7: Request Routing in a Web Server with a Trie

This module implements an HTTPRouter using a Trie data structure.

The HTTPRouter takes a URL path like "/", "/about", or 
"/blog/2019-01-15/my-awesome-blog-post" and determines the appropriate handler 
to return. The Trie is used to efficiently store and retrieve handlers based on 
the parts of the path separated by slashes ("/").

The RouteTrie stores handlers under path parts, and the Router delegates adding 
and looking up handlers to the RouteTrie. The Router also includes a not found 
handler for paths that are not found in the Trie and handles trailing slashes 
to ensure requests for '/about' and '/about/' are treated the same.

You sould implement the function bodies the function signatures. Use the test 
cases provided below to verify that your algorithm is correct. If necessary, 
add additional test cases to verify that your algorithm works correctly.
"""

from typing import Optional

class RouteTrieNode:
    """
    A node in the RouteTrie, representing a part of a route.

    Attributes:
    children (dict): A dictionary mapping part of the route to the corresponding RouteTrieNode.
    handler (Optional[str]): The handler associated with this node, if any.
    """
    def __init__(self):
        """
        Initialize a RouteTrieNode with an empty dictionary for children and no handler.
        """
        self.children = {}
        self.handler:str = None
        self.is_handler = False

class RouteTrie:
    """
    A trie (prefix tree) for storing routes and their handlers.

    Attributes:
    root (RouteTrieNode): The root node of the trie.
    """
    def __init__(self, root_handler: str):
        """
        Initialize the RouteTrie with a root handler.

        Args:
        root_handler (str): The handler for the root node.
        """
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path_parts: list[str], handler: str) -> None:
        """
        Insert a route and its handler into the trie.

        Args:
        path_parts (list[str]): A list of parts of the route.
        handler (str): The handler for the route.
        """
        current_node = self.root
        # root_handler = self.root.handler
        for part in path_parts:
            if part not in current_node.children.keys():
                current_node.children[part] = RouteTrieNode()
            current_node = current_node.children[part]
        current_node.handler = handler



    def find(self, path_parts: list[str]) ->  Optional[str]:
        """
        Find the handler for a given route.

        Args:
        path_parts (list[str]): A list of parts of the route.

        Returns:
        str or None: The handler for the route if found, otherwise None.
        """
        current_node = self.root
        # root_handler = self.root.handler
        for part in path_parts:
            if part not in current_node.children.keys():
                return None
            current_node = current_node.children[part]
        return current_node.handler
    

class Router:
    """
    A router to manage routes and their handlers using a RouteTrie.

    Attributes:
    route_trie (RouteTrie): The trie used to store routes and handlers.
    not_found_handler (str): The handler to return when a route is not found.
    """
    def __init__(self, root_handler: str, not_found_handler: str):
        """
        Initialize the Router with a root handler and a not-found handler.

        Args:
        root_handler (str): The handler for the root route.
        not_found_handler (str): The handler for routes that are not found.
        """
        self.root_handler = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler


    def add_handler(self, path: str, handler: str) -> None:
        """
        Add a handler for a route.

        Args:
        path (str): The route path.
        handler (str): The handler for the route.
        """
        list_paths = self.split_path(path)
        # if list_paths[0] == '':
        #     list_paths.remove('')
        
        self.root_handler.insert(list_paths,handler)

    def lookup(self, path: str) -> str:
        """
        Look up a route and return the associated handler.

        Args:
        path (str): The route path.

        Returns:
        str: The handler for the route if found, otherwise the not-found handler.
        """
        if path == '/':
            return self.root_handler.root.handler
        elif path == '':
            return self.not_found_handler
        
        list_paths = self.split_path(path)
        if list_paths[-1] == '':
            list_paths.pop()

        handler = self.root_handler.find(list_paths)
        return handler if handler else self.not_found_handler

    def split_path(self, path: str) -> list[str]:
        """
        Split the path into parts and remove empty parts to handle trailing slashes.

        Args:
            path (str): The path to split.

        Returns:
            List[str]: A list of parts of the path.
        """
        list_path = path.split('/')
        # print(list_path[-1])

        # print(list_path)
        return list_path

if __name__ == '__main__':
    # create the router and add a route
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    # Edge case: Empty path
    print("''")
    print(router.lookup(""))
    # Expected output: 'not found handler'

    # Normal case: Path not found
    print("/home/contact")
    print(router.lookup("/home/contact"))
    # Expected output: 'not found handler'

    # Normal case: Path with multiple segments
    print("/home/about/me")
    print(router.lookup("/home/about/me"))
    # Expected output: 'not found handler'

    # Normal case: Path with exact match
    print("/home/about")
    print(router.lookup("/home/about"))
    # Expected output: 'about handler'

    # some lookups with the expected output
    print("/")
    print(router.lookup("/")) # should print 'root handler'
    print("/home")
    print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
    print("/home/about")
    print(router.lookup("/home/about")) # should print 'about handler'
    print("/home/about/")
    print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
    print("/home/about/me")
    print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one