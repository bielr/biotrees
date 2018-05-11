from phylotree import shape_to_phylotree
import phylotree.yule as phyloyule


def yule_from_t(sh, prob):
    """
    Returns a list of tuples containing each shape obtained from `Shape` sh (assuming sh has probability prob) with
    their associate probability under the Yule model.
    :param sh: `Shape` instance.
    :param prob: `function` instance.
    :return: `list` instance.
    """
    t = shape_to_phylotree(sh)
    tps = [(ti.shape(), p) for ti, p in phyloyule.yule_from_t(t, prob)]
    return phyloyule.collapse_tree_prob_list(tps)


def yule(n):
    """
    Returns a list of tuples containing all the shapes of n leaves that can be obtained under the Yule model and their
    corresponding probability.
    :param n: `int` instance.
    :return: `list` instance.
    """
    tps = [(ti.shape(), p) for ti, p in phyloyule.pseudo_yule(n)]
    return phyloyule.collapse_tree_prob_list(tps)
