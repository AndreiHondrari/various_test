from rest_framework import serializers, exceptions

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'price',)
        read_only_fields = ('id',)

    def validate(self, data):
        # throw exception for batman with price 0
        if "batman" in data['title'].lower() and data['price'] < 100:
            raise exceptions.APIException("How dare you underestimate BATMAN ?!?!", code="invaluable")

        if "php" in data['title'] and data['price'] > 0:
            raise exceptions.APIException("Why would you even learn it?")

        if "bieber" in data['title'].lower() and data['price'] > 0:
            raise serializers.ValidationError("You could spend money on something else", code="unworthy")

        if "bogota" in data['title'] and "snoop" not in data['title']:
            raise serializers.ValidationError("A person not in the right location")

        if "answer" in data['title'] and data['price'] == 42:
            raise serializers.ValidationError({
                "answer": "The answer is 42",
                "binary_number": "101010"
            })

        return data

    def validate_price(self, value):

        if value < 0:
            raise serializers.ValidationError("Can't have negative numbers")

        if value > 1000:
            raise serializers.ValidationError("Can't spend more than 1000 on a book", code="too_much")

        if value == 666:
            raise exceptions.APIException("Are you one of those?")

        if value == 123:
            raise exceptions.APIException("Do you use this number for a password too?", code="bad_password")

        return value

    def validate_title(self, value):
        if "vader" in value:
            raise exceptions.ValidationError([
                "I am your father",
                "NOOOOOOOOOOOOOO!!!"
            ])
        return value