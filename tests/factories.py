from django.contrib.auth.models import User
from django.utils import timezone

from core import models as core_models
from entries import models as entries_models

import factory


class UserFactory(factory.Factory):
    FACTORY_FOR = User
    first_name = factory.Sequence(lambda n: 'Firstname {0}'.format(n))
    last_name = factory.Sequence(lambda n: 'Lastname {0}'.format(n))
    username = factory.Sequence(lambda n: 'user-{0}'.format(n).lower())
    email = factory.LazyAttribute(lambda a: '{0}@example.com'.format(a.username).lower())

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', 'password')
        user = super(UserFactory, cls)._prepare(create=False, **kwargs)
        user.set_password(password)
        user.raw_password = password
        if create:
            user.save()
        return user


class BowstyleFactory(factory.Factory):
    FACTORY_FOR = core_models.Bowstyle
    name = factory.Sequence(lambda n: 'Bowstyle %s' % n)


class ClubFactory(factory.Factory):
    FACTORY_FOR = core_models.Club
    name = factory.Sequence(lambda n: 'Name %s' % n)
    short_name = factory.Sequence(lambda n: 'Short Name %s' % n)
    slug = factory.Sequence(lambda n: 'name-%s' % n)


class ArcherFactory(factory.Factory):
    FACTORY_FOR = core_models.Archer
    club = factory.SubFactory(ClubFactory)
    bowstyle = factory.SubFactory(BowstyleFactory)


class TournamentFactory(factory.Factory):
    FACTORY_FOR = entries_models.Tournament
    short_name = factory.Sequence(lambda n: 'Tournament %s' % n)
    host_club = factory.SubFactory(ClubFactory)


class CompetitionFactory(factory.Factory):
    FACTORY_FOR = entries_models.Competition
    tournament = factory.SubFactory(TournamentFactory)
    date = timezone.now().date()
    slug = factory.Sequence(lambda n: 'comeptition-%s' % n)


class SessionFactory(factory.Factory):
    FACTORY_FOR = entries_models.Session
    competition = factory.SubFactory(CompetitionFactory)
    start = timezone.now()
    archers_per_target = 4


class RoundFactory(factory.Factory):
    FACTORY_FOR = core_models.Round
    name = factory.Sequence(lambda n: 'Name-%s' % n)


class SessionRoundFactory(factory.Factory):
    FACTORY_FOR = entries_models.SessionRound
    session = factory.SubFactory(SessionFactory)
    shot_round = factory.SubFactory(RoundFactory)


class CompetitionEntryFactory(factory.Factory):
    FACTORY_FOR = entries_models.CompetitionEntry
    competition = factory.SubFactory(CompetitionFactory)
    archer = factory.SubFactory(ArcherFactory)
    club = factory.SubFactory(ClubFactory)
    bowstyle = factory.SubFactory(BowstyleFactory)
    age = 'S'
    novice = 'E'


class SessionEntryFactory(factory.Factory):
    FACTORY_FOR = entries_models.SessionEntry
    competition_entry = factory.SubFactory(CompetitionEntryFactory)
    session_round = factory.SubFactory(SessionRoundFactory)
