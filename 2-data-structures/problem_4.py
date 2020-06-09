def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    for g in group.get_groups():
        if is_user_in_group(user, g):
            return True
    return False


class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users


if __name__ == '__main__':
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    sub_parent_user = "sub_parent_user"
    sub_baby_user = "sub_baby_user"
    sub_baby = Group("Baby")
    sub_baby.add_user(sub_baby_user)
    sub_child.add_group(sub_baby)
    no_user = ""

    child.add_group(sub_child)
    parent.add_group(child)

    # Tests
    print(is_user_in_group(sub_child_user, parent))
    print(is_user_in_group(sub_parent_user, parent))
    print(is_user_in_group(sub_baby_user, parent))
    print(is_user_in_group(no_user, parent))
