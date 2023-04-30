from django.test import TestCase

# Create your tests here.
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from apps.test_task.utils.tree import NLTKTreeParaphrase
from nltk.tree import Tree

from apps.test_task.views import paraphrase_list

TEST_SYNTAX_TREE = '(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars)) (, ,) (NP (NNS clubs)) (CC and) (NP (JJ Catalan) (NNS restaurants))))))))'
TEST_PARAPHRASES = [
    "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (NNS clubs)) (, ,) (NP (JJ trendy) (NNS bars)) (CC and) (NP (JJ Catalan) (NNS restaurants))))))))",
    "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars)) (, ,) (NP (JJ Catalan) (NNS restaurants)) (CC and) (NP (NNS clubs))))))))",
    "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (JJ Catalan) (NNS restaurants)) (, ,) (NP (NNS clubs)) (CC and) (NP (JJ trendy) (NNS bars))))))))",
    "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (NNS clubs)) (, ,) (NP (JJ Catalan) (NNS restaurants)) (CC and) (NP (JJ trendy) (NNS bars))))))))",
    "(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (JJ Catalan) (NNS restaurants)) (, ,) (NP (JJ trendy) (NNS bars)) (CC and) (NP (NNS clubs))))))))",
]


class TestNLTKTreeParaphrase(TestCase):

    def setUp(self) -> None:
        self.test_tree = NLTKTreeParaphrase(TEST_SYNTAX_TREE, 'np.np')

    def test_0_possible_cases(self):
        self.assertEqual(12, len(self.test_tree))

    def test_1_all(self):
        result = []

        for i, cs in enumerate(self.test_tree):
            with self.subTest(check_unique_i=i):
                rtree = Tree.fromstring(cs)
                self.assertNotIn(rtree, result)
                result.append(rtree)

        for i, pphrase in enumerate(TEST_PARAPHRASES):

            with self.subTest(test_in_test_paraphrases_i=i):
                rtree = Tree.fromstring(pphrase)
                self.assertIn(rtree, result)


class ParaphraseListViewCommonMixin:
    api_url = '/paraphrase/'

    def _error_tree_is_empty(self, response: Response):
        self.assertEqual(response.status_code, 200)
        tdata = {'errors': {'tree': [
            ErrorDetail('Parameter `tree` is empty:', code='invalid')
        ]}}
        self.assertDictEqual(response.data, tdata)

    def _error_tree_is_malformed(self, response: Response):
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.data.get('errors'))
        self.assertIsNotNone(response.data.get('errors').get('non_field_errors'))

    def _success_limit_default(self, response: Response):
        fact_result = response.data.get('paraphrases')
        self.assertIsNotNone(fact_result)

        fact_result_trees = [Tree.fromstring(rphrase.get('tree')) for rphrase in fact_result]

        for i, pphrase in enumerate(TEST_PARAPHRASES):
            with self.subTest(test_in_test_paraphrases_i=i):
                rtree = Tree.fromstring(pphrase)
                self.assertIn(rtree, fact_result_trees)

    def _success_limited(self, response: Response, limit):
        self.assertEqual(response.status_code, 200)

        fact_result = response.data.get('paraphrases')
        self.assertIsNotNone(fact_result)
        self.assertEqual(len(fact_result), limit)


class TestLocalParaphraseListView(ParaphraseListViewCommonMixin, APITestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = APIRequestFactory()

    def test_0_error_tree_is_empty(self):
        request = self.factory.get(self.api_url)
        response = paraphrase_list(request)
        self._error_tree_is_empty(response)

    def test_1_error_tree_is_malformed(self):
        request = self.factory.get(self.api_url, {'tree': '(S%20(NP%20(NP%20(DT%20The)%20(JJ%20ch'})
        response = paraphrase_list(request)
        self._error_tree_is_malformed(response)

    def test_2_success(self):
        request = self.factory.get(self.api_url, {'tree': TEST_SYNTAX_TREE})
        response = paraphrase_list(request)
        self._success_limit_default(response)

    def test_3_success_limited(self):
        limit = 5
        request = self.factory.get(self.api_url, {'tree': TEST_SYNTAX_TREE, 'limit': limit})
        response = paraphrase_list(request)
        self._success_limited(response, limit)


class TestRealParaphraseListView(ParaphraseListViewCommonMixin, APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.api_url = '/paraphrase/'

    def test_0_error_tree_is_empty(self):
        response = self.client.get(self.api_url, {}, format='json')
        self._error_tree_is_empty(response)

    def test_1_error_tree_is_malformed(self):
        response = self.client.get(self.api_url, {'tree': '(S%20(NP%20(NP%20(DT%20The)%20(JJ%20ch'}, format='json')
        self._error_tree_is_malformed(response)

    def test_2_success(self):
        response = self.client.get(self.api_url, {'tree': TEST_SYNTAX_TREE}, format='json')
        self._success_limit_default(response)

    def test_3_success_limited(self):
        limit = 5
        response = self.client.get(self.api_url, {'tree': TEST_SYNTAX_TREE, 'limit': limit}, format='json')
        self._success_limited(response, limit)
