from rest_framework import serializers

from movies.models import Filmwork, Role  # isort:skip


class FilmworkSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()
    directors = serializers.SerializerMethodField()
    writers = serializers.SerializerMethodField()

    class Meta(object):
        model = Filmwork
        fields = [
            'id',
            'title',
            'description',
            'creation_date',
            'rating',
            'type',
            'genres',
            'actors',
            'directors',
            'writers',
        ]

    def get_genres(self, filmwork):
        return [
            film_work_genre.genre.name
            for film_work_genre in filmwork.film_work_genres.prefetch_related(
                'genre',
            ).all()
        ]

    def get_actors(self, filmwork):
        return [
            filmwork_person.person.full_name
            for filmwork_person in filmwork.film_work_persons.prefetch_related(
                'person',
            ).filter(role=Role.ACTOR)
        ]

    def get_directors(self, filmwork):
        return [
            filmwork_person.person.full_name
            for filmwork_person in filmwork.film_work_persons.prefetch_related(
                'person',
            ).filter(role=Role.DIRECTOR)
        ]

    def get_writers(self, filmwork):
        return [
            filmwork_person.person.full_name
            for filmwork_person in filmwork.film_work_persons.prefetch_related(
                'person',
            ).filter(role=Role.WRITER)
        ]
