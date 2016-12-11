from django.test import TestCase
from challenges.models import CHALLENGES, TorChallenge, ButtonStep, Step, TextStep, InputStep
from challenges.tests.factories import IdentityLeakCheckerChallengeFactory, TorChallengeFactory
from unittest.mock import patch, Mock, PropertyMock


class TestChallenge(TestCase):
    def test_challenges_list_unique(self):
        challenges_list = list(CHALLENGES)
        challenges_dict = dict(CHALLENGES)

        self.assertEqual(len(challenges_list), len(challenges_dict.keys()),
                         msg='Two challenges are violating the unique identifier constraint')

    def test_challenge_metas(self):
        for challenge_tuple in CHALLENGES:
            challenge = challenge_tuple[1]
            self.assertIsNotNone(challenge.ChallengeMeta.title,
                                 msg='{0} is missing a title'.format(challenge))
            self.assertIsNotNone(challenge.ChallengeMeta.description,
                                 msg='{0} is missing a description'.format(challenge))
            for step in challenge.ChallengeMeta.steps:
                self.assertEqual(type(step[0]), str)
                self.assertIn(type(step[1]), [ButtonStep, InputStep, TextStep],
                              msg='Steps in {0} needs have a given type'.format(challenge))


class TestIdentityLeakCheckerChallenge(TestCase):
    def test_check_email(self):
        challenge = IdentityLeakCheckerChallengeFactory()
        url = 'https://sec.hpi.uni-potsdam.de/leak-checker/search'

        with patch('requests.post') as patched_post:
            type(patched_post.return_value).ok = PropertyMock(return_value=True)

            self.assertTrue(challenge.check_email())
            patched_post.assert_called_once_with(url, data={'email': challenge.user.email})


class TestTorChallenge(TestCase):
    def test_check_tor_connection(self):
        challenge = TorChallengeFactory()
        mocked_ip = '192.168.178.22'
        url = 'https://check.torproject.org/exit-addresses'

        request_mock = Mock()
        request_mock.META.get.return_value = mocked_ip

        with patch('requests.get') as patched_get:
            type(patched_get.return_value).text = PropertyMock(return_value=mocked_ip)

            self.assertTrue(challenge.check_tor_connection(request_mock))
            request_mock.META.get.assert_called_once_with('REMOTE_ADDR')
            patched_get.assert_called_once_with(url)


class TestStep(TestCase):
    def test_to_json(self):
        title = 'a random title'
        text = 'a random text'
        step = Step(title=title, text=text)

        self.assertEqual(step.to_json(), {'title': title, 'text': text})


class TestButtonStep(TestCase):
    def test_to_json(self):
        button_title = 'Click me'
        title = 'a random title'
        text = 'a random text'
        step = ButtonStep(button_title=button_title, title=title, text=text)

        self.assertEqual(step.to_json(),
                         {'title': title, 'text': text, 'button_title': button_title})


class TestTextStep(TestCase):
    def test_to_json(self):
        title = 'a random title'
        text = 'a random text'
        step = TextStep(title=title, text=text)

        self.assertEqual(step.to_json(), {'title': title, 'text': text})


class TestInputStep(TestCase):
    def test_to_json(self):
        button_title = 'Click me'
        input_title = 'this is a text field'
        title = 'a random title'
        text = 'a random text'
        step = InputStep(input_title=input_title, button_title=button_title, title=title, text=text)

        self.assertEqual(step.to_json(),
                         {'title': title, 'text': text, 'button_title': button_title,
                          'input_title': input_title})