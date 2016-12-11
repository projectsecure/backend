import factory
from challenges.models import Challenge, TorChallenge, IdentityLeakCheckerChallenge
from faker import Factory as FakeFactory
from users.tests.factories import UserFactory

fake = FakeFactory.create()


class ChallengeFactory(factory.DjangoModelFactory):
    class Meta:
        model = Challenge

    user = factory.SubFactory(UserFactory)


class TorChallengeFactory(ChallengeFactory):
    class Meta:
        model = TorChallenge


class IdentityLeakCheckerChallengeFactory(ChallengeFactory):
    class Meta:
        model = IdentityLeakCheckerChallenge