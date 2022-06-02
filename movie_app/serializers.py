from rest_framework import serializers
from . import models


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Director
        fields = "__all__"


class MovieSerializersList(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "id title director".split()


class MovieSerializersDetail(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "__all__"


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = "__all__"


class MovieSerializerList(serializers.ModelSerializer):
    reviews = ReviewSerializers(many=True)
    filtered_reviews = serializers.SerializerMethodField()

    class Meta:
        model = models.Movie
        field = "id title director reviews filtered_rewiews".split()

    def get_filtered_rewiews(self, product):
        reviews = product.reviews.filter(stars_gt=2)

        return [{"id": reviews.id,
                 "text": reviews.text,
                 "reviews": reviews.stars} for review in reviews]
