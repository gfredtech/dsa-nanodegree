# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.handler = root_handler

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        # Setting node to the root of the RouteTrie
        node = self.root

        # Adding blocks to root node
        for block in path:
            node.insert(block)
            node = node.children[block]

        # Setting the handler to the inputted hanlder
        node.handler = handler


    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        # Setting node to the root of the RouteTrie
        node = self.root

        # Searching for path in RouteTrie
        for block in path:
            if block not in node.children:
                return None
            node = node.children[block]

        # Returning hanndler when match is found
        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = None

    def insert(self, block):
        # Insert the node as before
        if block not in self.children:
            self.children[block] = RouteTrieNode()
        else:
            pass

# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router = RouteTrie(root_handler = root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, raw_path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie

        # Splitting up the raw path
        path = self.split_path(raw_path)

        # Adding path and handler to RouteTrie
        self.router.insert(path = path, handler = handler)

    def lookup(self, raw_path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        # Splitting up the raw path
        path = self.split_path(raw_path)

        # Returning hits if found using the inputted path
        hits = self.router.find(path = path)

        # Returning results appropriately
        if hits is None:
            return self.not_found_handler
        else:
            return hits


    def split_path(self, raw_path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        # Splitting raw path
        results = raw_path.split(sep = '/')

        # Returning non-blank results
        return [i for i in results if i != '']

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
#
