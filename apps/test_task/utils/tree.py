# IDE: PyCharm
# Project: maklai-internship
# Path: apps/test_task/utils
# File: tree.py
# Contact: Semyon Mamonov <semyon.mamonov@gmail.com>
# Created by ox23 at 2023-04-28 (y-m-d) 9:02 PM
from math import factorial
from itertools import permutations, product
from functools import partial, reduce
from typing import Collection

from nltk.tree import ParentedTree


class HashableParentedTree(ParentedTree):

    def __hash__(self) -> int:
        return id(self)


PATH_SEPARATOR = '.'


def _filter(tree: ParentedTree, path: str):
    lbls = path.upper().split(PATH_SEPARATOR)
    if not lbls:
        raise ValueError('path is `%s` should have string like `NP` or `NP%sNP` etc' % (path, PATH_SEPARATOR))
    ctree = tree
    for lbl in reversed(lbls):
        if not isinstance(ctree, ParentedTree):
            raise ValueError('tree %s is not instance of ParentedTree' % ctree)
        if ctree.label() != lbl:
            return False
        ctree = ctree.parent()

    return True


class NLTKTreeParaphrase(Collection):

    def __init__(self, stree: str, path: str, last_children_gt=1):
        self.root: HashableParentedTree = HashableParentedTree.fromstring(stree)
        self.last_children_gt = last_children_gt
        self.path = path

    def get_subtrees(self, path='') -> dict[HashableParentedTree, list[HashableParentedTree]]:
        result = {}
        for pt in self.root.subtrees(partial(_filter, path=path)):
            prnt = pt.parent()
            result.setdefault(prnt, []).append(pt)
        return {k: v for k, v in result.items() if len(v) > self.last_children_gt}

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._subtrees = self.get_subtrees(path)
        self._path = path

    def __contains__(self, __x: object) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        lens = [factorial(len(v)) for k, v in self._subtrees.items() if len(v) > 0]
        if not lens:
            return 0
        trees_len = reduce((lambda x, y: x * y), lens)

        return trees_len

    def _get_packed_cases(self):
        rset = []
        for pt, trees in self._subtrees.items():
            rset.append([*permutations((t.parent_index(), t.parent(), i, t) for i, t in enumerate(trees))])

        result = []
        for cs in product(*rset):
            result.append(tuple(reduce(lambda x, y: x+y, (itm for itm in cs))))
        return result

    def __iter__(self):
        cases = self._get_packed_cases()
        for i, case in enumerate(cases):
            if i == 0:
                main_case = tuple((parent_index, cparent) for parent_index, cparent, trsh, trsh in case)
            for casei, (parent_index, cparent, _subtrees_idx_for_prnt, tree) in enumerate(case):
                repl_parent_index, repl_parent = main_case[casei]

                # # this is a more right implementation (no deep copy, that was the original idea,
                # # just move the tree to a different location)
                # # but a bit tricky
                # list.pop(repl_parent, repl_parent_index)
                # tree._parent = None
                # repl_parent.insert(repl_parent_index, tree)

                # the next one is even shorter
                tree._parent = repl_parent
                list.__setitem__(repl_parent, repl_parent_index, tree)

                # # It was the first edition
                # # Looks like a bug.
                # # Only in this form (next two lines) allows to make a tree replacement
                # # so that there are no errors or assertions
                # del repl_parent[repl_parent_index]
                # repl_parent.insert(repl_parent_index, tree.copy(True))

            yield str(self.root)


if __name__ == '__main__':
    test_stree = '''
    (S
    (NP
    (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))
    (, ,)
    (CC or)
    (NP (NNP Barri) (NNP Gòtic)))
    (, ,)
    (VP
    (VBZ has)
    (NP
    (NP (JJ narrow) (JJ medieval) (NNS streets))
    (VP
    (VBN filled)
    (PP
    (IN with)
    (NP
    (NP (JJ trendy) (NNS bars))
    (, ,)
    (NP (NNS clubs))
    (CC and)
    (NP (JJ Catalan) (NNS restaurants))))))))
    '''

    def get_trees(stree: str, path='NP.NP') -> dict[HashableParentedTree, list[HashableParentedTree]]:
        result = {}
        ptree = HashableParentedTree.fromstring(stree)
        ptree.pretty_print()
        for pt in ptree.subtrees(partial(_filter, path=path)):
            result.setdefault(pt.parent(), []).append(pt)
        return result

    def print_result(result: dict[HashableParentedTree, list[HashableParentedTree]]):
        for rt, pt in filter(lambda itm: len(itm[1]) > 1, result.items()):
            print('@', rt)
            for t in pt:
                print('@@', t)

    res = get_trees(test_stree, 'VP.np.NP.JJ')
    print_result(res)
    # @ (NP (JJ narrow) (JJ medieval) (NNS streets))
    # @@ (JJ narrow)
    # @@ (JJ medieval)

    res = get_trees(test_stree, 'PP.NP.NP.NNS')
    print_result(res)
    # Empty

    res = get_trees(test_stree, 'NP.NP')
    print_result(res)
    # @ (NP
    #   (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))
    #   (, ,)
    #   (CC or)
    #   (NP (NNP Barri) (NNP Gòtic)))
    # @@ (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))
    # @@ (NP (NNP Barri) (NNP Gòtic))
    # @ (NP
    #   (NP (JJ trendy) (NNS bars))
    #   (, ,)
    #   (NP (NNS clubs))
    #   (CC and)
    #   (NP (JJ Catalan) (NNS restaurants)))
    # @@ (NP (JJ trendy) (NNS bars))
    # @@ (NP (NNS clubs))
    # @@ (NP (JJ Catalan) (NNS restaurants))
